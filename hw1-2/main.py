#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import numpy as np
import sys


probs = np.zeros((37, 37))
chars = [''] * 37;

def read_in():
   _file = open('./valid/encode.bin', 'r')
   while True:
      _line = _file.readline()
      if not _line: break
      argv = _line.split(" ")
      _char = int(argv[0])
      _trans_char = int(argv[1])
      _prob = int(argv[2])

      probs[ _char ][ _trans_char ] = _prob;
   _file.close

def symbolToNum():
   _file = open('./valid/symbolToNum.dict', 'r')
   while True:
      _line = _file.readline()
      if not _line: break
      argv = _line.split("\t")
      _char = argv[0]
      _encode = int(argv[1])

      chars[ _encode ] = _char
   _file.close


# Main function
def main():

   read_in()
   symbolToNum()
   #print ord('0'), #48
   #print ord('9')  #57
   #print ord('a'), #97, chr(97) = 'a'
   #print ord('z'), #122
   #print ord(' ')  #32
   #print index('0'), # = 0
   #print index('9'), # = 9
   #print index('a'), # = 10
   #print index('z'), # = 35
   #print index(' ')  # = 36


if __name__ == '__main__':
   main()

