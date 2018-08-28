# coding:utf-8

import argparse
import yaml
import re

# e.g. python parser.py -i xxx.yaml
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="input file name like foobar.yaml", required=True)
args = parser.parse_args()
input_file_name = args.input

# convert: {XXX} -> env.XXX
def dotenv(str):
  converted = re.sub(r'{(\w+)}', "env.\\1", str)
  if not converted.startswith('env.'):
    converted = '"' + converted + '"'
  return converted

def convert_target(commands):
  # print(commands);
  target = commands['target'].split('=', 1)
  if target[0] == 'id':
    return '(await page.$("#' + target[1] + '"))'
  elif target[0] == 'css':
    return '(await page.$("' + target[1] + '"))'
  elif target[0] == 'name':
    return '(await page.$("[name=' + target[1] + ']"))'
  elif target[0] == 'xpath':
    return '(await page.$x("' + target[1] + '"))[0]'
  elif target[0] == 'linkText':
    return '(await page.$x("//a[contains(text(), \'' + target[1] + '\')]"))[0]'
  return None # for debugging by raising execption

def convert_window_target(commands):
  target = commands['target'].split('win_ser_')[1]
  if target == 'local':
    target = '0'
  return target

# each command converter
def convert_command(scripts, commands):
  if commands['command'] == 'open':
    command = 'await page.goto("' + commands['target'] + '");'
    scripts.append(command)
    scripts.append('await page.waitFor(5000);')
    scripts.append('await page.screenshot({path: screenShotPath(), fullPage: true});')
  elif commands['command'] == 'type':
    command_target = convert_target(commands)
    command = 'await ' + command_target + '.type(' + dotenv(commands['value']) + ');'
    scripts.append(command)
    scripts.append('await page.waitFor(1000);')
    scripts.append('await page.screenshot({path: screenShotPath(), fullPage: true});')
  elif commands['command'] == 'clickAt' or commands['command'] == 'click':
    command_target = convert_target(commands)
    command = 'await ' + command_target + '.click();'
    scripts.append(command)
    scripts.append('await page.waitFor(5000);')
    scripts.append('await page.screenshot({path: screenShotPath(), fullPage: true});')
  elif commands['command'] == 'mouseOver':
    command_target = convert_target(commands)
    command = 'await ' + command_target + '.focus();'
    scripts.append(command)
    scripts.append('await page.waitFor(1000);')
    scripts.append('await page.screenshot({path: screenShotPath(), fullPage: true});')
  elif commands['command'] == 'selectWindow':
    scripts.append('pages = await browser.pages();')
    command_target = convert_window_target(commands)
    command = 'page = await pages[' + command_target + '];'
    scripts.append(command)
    scripts.append('await page.bringToFront();')
    scripts.append('await page.waitFor(1000);')
    scripts.append('await page.screenshot({path: screenShotPath(), fullPage: true});')
  elif commands['command'] == 'close':
    scripts.append('pages = await browser.pages();')
    command_target = convert_window_target(commands)
    command = 'page = await pages[' + command_target + '];'
    scripts.append(command)
    scripts.append('await page.bringToFront();')
    scripts.append('await page.waitFor(1000);')
    scripts.append('await page.close();')
  return scripts

with open('./' + input_file_name, 'rt') as f:
  text = f.read()
data = yaml.safe_load(text)

scripts = []
for k, v in data.items():
  scripts.append('// command: ' + str(k))
  scripts = convert_command(scripts, v)
  scripts.append('')

prefix = ''
with open('./templates/template_prefix.js') as f:
  prefix = f.read()

suffix = ''
with open('./templates/template_suffix.js') as f:
  suffix = f.read()

output_file_name = input_file_name.split('.')[0]
output = "const projectName = '" + output_file_name + "'\n\n" + prefix + '\n'.join(scripts) + suffix
with open('./' + output_file_name + '.js', mode='w') as f:
  f.write(output)

