#素数を求めるプログラム

for prime in range(1, 10000 + 1):

  count = 0
  for i in range(1, prime + 1):

    if (prime % i == 0):
      count += 1

  if (count == 2):
    print (prime)
