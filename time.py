#とりあえず時間を表示させるプログラムです。
#ライブラリ探せば普通にありそう。

import time

count = 0
sec = 0
man = 0
hor = 0

while (count < 1):
  
  print ('{0}:{1}:{2}'.format(hor, man, sec), '\r', end="")
  time.sleep(1)
  sec += 1

  if (sec == 60):
    man += 1
    sec = 0

  if (man == 60):
    hor += 1
    man = 0
