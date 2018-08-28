# coding:utf-8

import argparse
import json
import yaml

# e.g. python parser.py -i xxx.side
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="input file name like foobar.side", required=True)
args = parser.parse_args()

input_file_name = args.input

f = open('./' + input_file_name, 'r')
side = json.load(f)

command_options = [
  'click',
  'clickAt',
  'close',
  'open',
  'selectWindow',
  'type',
  'mouseOver'
]

converted = {}
for command in side['tests'][0]['commands']:
  # command
  if not command['command'] in command_options:
    continue
  item = {}
  item['command'] = command['command']
  # target
  item['target'] = side['url'] + command['target'] if item['command'] == 'open' else command['target']
  if item['target'].startswith('//'):
    item['target'] = 'xpath=' + item['target']
  # command
  if item['command'] == 'type':
    item['value'] = command['value']
  index = len(converted)
  converted[index] = item

output_file_name = input_file_name.split('.')[0] + '.yml'
with open('./' + output_file_name, 'w') as f:
  yaml.dump(converted, f, default_flow_style=False, allow_unicode=True)

