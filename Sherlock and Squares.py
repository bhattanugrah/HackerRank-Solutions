#Problem Link: https://www.hackerrank.com/challenges/sherlock-and-squares/problem?h_r=next-challenge&h_v=zen
from math import *

def squares(a, b):
    return floor(sqrt(b)) - ceil(sqrt(a)) + 1
