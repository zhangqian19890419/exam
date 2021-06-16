mail = input('メールアドレスを入力してください:')

a = '@'

def slicemail():
	findmail = mail.find(a)
	cutmail = mail[findmail + 1:]
	print('メールアドレス' + mail + 'のドメイン:' + cutmail)

slicemail()