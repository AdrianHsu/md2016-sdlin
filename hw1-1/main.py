#!/usr/bin/env python3

import sys

# Bigram language model
def bigram():
   _file = open('bigram.txt', 'r', encoding='utf-8')
   while True:
      _line = _file.readline()
      argv = _line.split(' ')
      if not _line: break
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
      print(a + " " + b + " ", end="")
      print(f)
   _file.close

# Encoding Table
def encoding():
   _file = open('encode.txt', 'r', encoding='utf-8')
   while True:
      _line = _file.readline()
      argv = _line.split(' ')
      if not _line: break
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
      print(x + " " + y + " ", end="")
      print(p)

   _file.close

# Main function
def main():
   bigram()
   encoding()

if __name__ == '__main__':
   main()

