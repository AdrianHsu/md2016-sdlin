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
      f = float(sys.maxsize)
      if len(_line) > 5:
         try:
            _str = argv[len(argv) - 1]
            f = float(_str)
         except ValueError:
            f = float(sys.maxsize)
      else:
         f = float(sys.maxsize)
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
      p = float(sys.maxsize)
      if len(_line) > 5:
         try:
            _str = argv[len(argv) - 1]
            p = float(_str)
         except ValueError:
            p = float(sys.maxsize)
      else:
         p = float(sys.maxsize)
      print(x + " " + y + " ", end="")
      print(p)

   _file.close

# Main function
def main():
   bigram()
   encoding()

if __name__ == '__main__':
   main()

