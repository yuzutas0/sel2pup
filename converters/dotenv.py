# coding:utf-8

import argparse
import re

# e.g. python dotenv.py -i xxx.yaml
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="input file name like foobar.yaml", required=True)
args = parser.parse_args()
input_file_name = args.input

# create dotenv file
with open('./' + input_file_name) as f:
  s = f.read()
  parsed = re.findall('(?<="{)\w+(?=}")', s)
  parsed = list(set(parsed)) # make list-item unique
  consts = []
  for item in parsed:
    consts.append(item + '=')
  const_text = '\n'.join(consts)
  with open('.env', mode='w') as f:
    f.write(const_text)

