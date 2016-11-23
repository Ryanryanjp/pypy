#素数を出力するプログラムの改善版だよ

import time
st = int(input('入力した数までの素数を調べます : '))

start = time.time()

if (st < 2):

  pricount = 0

elif (st == 2):

  print (2)
  pricount = 1

else:

  print (2)
  pricount = 1 

  for prime in range(1, st + 1):

    count = 0

    if (prime % 2 == 1):

      for i in range(1, prime + 1):

        if (prime % i == 0) and (count <= 2):

          count += 1

        else:

         continue 
      
    if (count == 2):

      print (prime)
      pricount += 1
   
print ('{0}に含まれている素数は{1}こでした。'.format(st, pricount))

elapsed_time = time.time() -start
print ('かかった時間 : {0}'.format(elapsed_time))
