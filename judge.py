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

judge = "0"
if (output == answer and output_image == answer_image):
  judge = "1"
elif (output == answer and output_image != answer_image):
  judge = "2"
elif (output != answer and output_image == answer_image):
  judge = "3"
else:
  judge = "4"
print(judge)

f = open('../debug.txt', 'w', encoding='UTF-8')
f.write('output: '+output.replace("\n","<newline>")+'\n')
f.write('answer: '+answer.replace("\n","<newline>")+'\n')
f.write('output_len: '+str(len(output)))
f.write('answer_len: '+str(len(answer)))
f.write('output_image: '+output_image+'\n')
f.write('answer_image: '+answer_image+'\n')
f.write('judge: '+judge+'\n')
f.close()
