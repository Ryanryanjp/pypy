a = []
for i in range(3):
  a.append(input())
          
k = a[0].split()

num1 = int(k[0])
num2 = int(k[1])

word1 = list(a[1])
word2 = list(a[2])

if(num1 > num2):
  tip = num1
  for d in range(num1 - num2):
    word2.append('fuck')

elif(num1 < num2):
  tip = num2
  for d in range(num2 - num1):
    word1.append('fuck')

elif(num1 == num2):
  tip = num1

count = tip

for x in range(tip):
  for f in range(tip):
    if(word1[f] == word2[x]):
      count -= 1
      word1[f] = 'non'
      break

print(count)
