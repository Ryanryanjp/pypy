#Fizz Buzz問題に挑戦するょ
#千葉県松戸市六甲台
for count in range(1, 101):
	
	if (count % 3 == 0) and (count % 5 == 0):
		print ('fizz buzz')

	elif (count % 3 == 0):
		print ('fizz')

	elif (count % 5 == 0):
		print ('buzz')

	else:
		print (count)
