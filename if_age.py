# if...elif...else
age = int(input('請輸入年齡：'))
if age < 6:
	print('學齡前')
elif age >= 6 and age < 13:
	print('國小')
elif age >= 13 and age < 15:
	print('國中')
elif age >= 15 and age < 19:
	print('高中')
else:
	print('社會')