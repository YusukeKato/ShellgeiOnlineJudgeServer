#!/usr/bin/env python3
import sys
import re

args = sys.argv
output = args[1]
output_image = args[2]
answer = args[3]
answer_image = args[4]

output = re.sub('\r', '', output)
answer = re.sub('\r', '', answer)

if ((output == answer or output+"\n" == answer or output+"\n\n" == answer) and output_image == answer_image):
  print("true")
else:
  print("false")

f = open('debug.txt', 'w', encoding='UTF-8')
f.write('output: '+output+'\n')
f.write('answer: '+answer+'\n')
f.write('output_image: '+output_image+'\n')
f.write('answer_image: '+answer_image+'\n')
f.close()
