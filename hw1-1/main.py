#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import numpy as np
import sys

pi = np.zeros((1, 37))
f = np.zeros((37, 37))
p = np.zeros((37, 37))

# Bigram language model
def bigram():
   _file = open('bigram.txt', 'r')
   while True:
      _line = _file.readline()
      if not _line: break
      argv = _line.split(' ')
      a = _line[0]
      b = _line[2]
      f = 0.0
      if len(_line) > 5:
         try:
            _str = argv[len(argv) - 1]
            f = float(_str)
         except ValueError:
            f = 0.0
      else:
         f = 0.0
      #print ord(a), 
      #print ord(b),
      #print f
   _file.close

# Encoding Table
def encoding():
   _file = open('encode.txt', 'r')
   while True:
      _line = _file.readline()
      if not _line: break
      argv = _line.split(' ')
      x = _line[0]
      y = _line[2]
      p = 0.0
      if len(_line) > 5:
         try:
            _str = argv[len(argv) - 1]
            p = float(_str)
         except ValueError:
            p = 0.0
      else:
         p = 0.0
      #print ord(x),
      #print ord(y),
      #print p

   _file.close

def test():
   _file = open('tmp.txt', 'r')
   _text = _file.read()
   
   _words = _text.split(' ')
   _word_num = len(_words)
   
   for _word in _words:
      length = len(_word)
      test_str(_word, length)

   _file.close

def test_str(_word, length):
   arr = np.zeros((1, length))
   for i in range(0, length):
      arr[0][i] = index(_word[i])
      print arr[0][i]

def index(_ch):
   if ord(_ch) >= 48 and ord(_ch) <= 57: #index('9') = 9
      return ord(_ch) - 48 
   elif ord(_ch) >= 97 and ord(_ch) <= 122: # index('a') = 10 
      return ord(_ch) - 87
   elif ord(_ch) == 32:
      return 36;
   else:
      return -1

def char(_index):
   if _index >= 0 and _index <= 9:
      return chr(_index + 48)
   elif _index >= 10 and _index <= 35:
      return chr(_index + 87)
   elif _index == 36:
      return '?'
   else:
      return '?'


# Main function
def main():
   bigram()
   encoding()
   test()
   #print ord('a'), #97, chr(97) = 'a'
   #print ord('z'), #122
   #print ord('0'), #48
   #print ord('9')  #57
   #print ord(' ')  #32
   #print index('0'), # = 0
   #print index('9'), # = 9
   #print index('a'), # = 10
   #print index('z'), # = 35
   #print index(' ')  # = 36
   #print char(0),
   #print char(9),
   #print char(10),
   #print char(35)


if __name__ == '__main__':
   main()

