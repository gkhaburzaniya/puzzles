#!/usr/bin/env python3
import time, importlib

i = input('\nSolve which problem?\n')
while i[0] != 'q':
  start_time = time.time()
  module = importlib.import_module('euler'+i)
  finish = time.time() - start_time
  print('Answer: ', module.answer, '\nTook: ', finish, ' seconds')
  i = input('\nSolve which problem?\n')
