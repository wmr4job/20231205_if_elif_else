#if_driving license
driving = input('你有開過車嗎？')
if driving != '有' and driving != '沒有':
	print('只能輸入有或沒有！')
	raise SystemExit #讓程式在這邊中止

age = int(input('請輸入年齡：'))

if driving == '有':
	if age >= 18:
		print('合格駕駛！')
	else:
		print('嗶嗶！無照駕駛！')
else:
	if age >= 18:
		print('符合考照資格囉~')
	else:
		print('年輕真好，再等等就能考照了！')

