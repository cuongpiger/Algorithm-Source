'''
https://www.hackerrank.com/challenges/camelcase/problem
Comment
'''
import sys
import queue

def FILE_IO():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

'''____________________________________________________________________________________________'''

#_____main_____
#FILE_IO()

s = input()
res = 1

for char in s:
    if char.isupper():
        res += 1

print(res)
