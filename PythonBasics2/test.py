def count_threes(n):
    d = dict()
    d['3'] = 0
    d['6'] = 0
    d['9'] = 0
    for i in n:
      if i not in d:
        d[i] = 1
      else:
        d[i] = d[i] + 1
    if d['3'] > d['6'] and d['3'] > d['9']:
        return d['3']
    elif d['6'] > d['3'] and d['6'] > d['9']:
        return d['6']
    else:
        return d['9']


myWord = '03393'
letterCount = count_threes(myWord)
print(letterCount)
