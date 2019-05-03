# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:23:48 2019

Script that Compares Pylint and PyFlakes (Too Long Lines Smell)

@author: YJ
"""

from subprocess import run, PIPE

with open(r'sourcecode\flask_pylint.txt', encoding='UTF8') as fp:  
   line = fp.readline()
   cnt = 0
   while line:
       line = fp.readline()
       if 'C0301' in line:
           cnt += 1
        
print('flask-master: Pylint detects {} lines that are too long'.format(cnt))
       
with open(r'sourcecode\flask_flake.txt', encoding='UTF8') as fp:  
   line = fp.readline()
   cnt = 0
   while line:
       line = fp.readline()
       if 'E501' in line:
           cnt += 1
        
print('flask-master: Pyflakes detects {} lines that are too long'.format(cnt))
       
with open(r'sourcecode\keras_pylint.txt', encoding='UTF8') as fp:  
   line = fp.readline()
   cnt = 0
   while line:
       line = fp.readline()
       if 'C0301' in line:
           cnt += 1
        
print('keras-master: Pylint detects {} lines that are too long'.format(cnt))
       
with open(r'sourcecode\keras_flake.txt', encoding='UTF8') as fp:  
   line = fp.readline()
   cnt = 0
   while line:
       line = fp.readline()
       if 'E501' in line:
           cnt += 1
        
print('keras-master: Pyflakes detects {} lines that are too long'.format(cnt))
       
with open(r'sourcecode\scikit_pylint.txt', encoding='UTF8') as fp:  
   line = fp.readline()
   cnt = 0
   while line:
       line = fp.readline()
       if 'C0301' in line:
           cnt += 1
        
print('scikit-learn-master: Pylint detects {} lines that are too long'.format(cnt))
       
with open(r'sourcecode\scikit_flake.txt', encoding='UTF8') as fp:  
   line = fp.readline()
   cnt = 0
   while line:
       line = fp.readline()
       if 'E501' in line:
           cnt += 1
        
print('scikit-learn-master: Pyflakes detects {} lines that are too long'.format(cnt))

with open(r'sourcecode\scrapy_pylint.txt') as fp:  
   line = fp.readline()
   cnt = 0
   while line:
       line = fp.readline()
       if 'C0301' in line:
           cnt += 1
        
print('scrapy-master: Pylint detects {} lines that are too long'.format(cnt))
       
with open(r'sourcecode\scrapy_flake.txt', encoding='UTF8') as fp:  
   line = fp.readline()
   cnt = 0
   while line:
       line = fp.readline()
       if 'E501' in line:
           cnt += 1
        
print('scrapy-master: Pyflakes detects {} lines that are too long'.format(cnt))