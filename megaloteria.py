# coding: utf-8
import itertools
from random import choice
def lotery(min_numb,max_num,n):
    all_numbers = range(min_numb,max_num + 1)
    selection = []
    for i in xrange(n):
      r = choice(all_numbers)
      selection.append(r)
      all_numbers.remove(r)
    dict_lot = {p:selection}
    return dict_lot
p = 1
while p <= 100:
  print lotery(1,75,5)
  p = p+1


comb1 = list(itertools.combinations(range(1,5),3))
comb2 = []
i = 0
while i < len(comb1):
  if len(set(comb1[i]) & set(comb1[i+1])) == 3:
    comb2 = comb2 + comb1[i]
    i = i+1

