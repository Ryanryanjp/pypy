#約数を出力するプログラム

st = int(input('入力した整数の約数を出力します : '))

count = 0
for i in range(1, st + 1):

  if (st % i == 0):
    print (i)
    count += 1

print ('{0}の約数は{1}こありました'.format(st, count))
