c = input('請問您式哪國人:')
a = input('請輸入年齡: ')
a = int(a)
if c == '台灣':
	if a >= 18:
		print('你可以考駕照')
	else:
		print('你不能考駕照')
if c == '美國':
	if a >= 16:
		print('你可以考駕照')
	else:
		print('你不能考駕照')