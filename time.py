#とりあえず時間を表示させるプログラムです。
#ライブラリ探せば普通にありそう。

import time

count = 0
sec = 0
miu = 0
hor = 0

while (count < 1):
  
  print ('{0}:{1}:{2}'.format(hor, miu, sec), '\r', end="")
  time.sleep(1)
  sec += 1

  if (sec == 60):
    miu += 1
    sec = 0

  if (miu == 60):
    hor += 1
    miu = 0
