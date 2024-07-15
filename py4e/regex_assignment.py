import re

hand = open('regex_sum_2051606.txt')
numlist = list()

for line in hand:
  line = line.rstrip()
  num = re.findall('[0-9]+', line)
  if len(num) < 1:
    continue
  for n in num:
    numlist.append(int(n))

print(sum(numlist))