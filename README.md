#ex01.py
str = input('文字列を入力してください:')
print(len(str))


#ex03.py
mail = input('メールアドレスを入力してください:')

a = '@'

def slicemail():
	findmail = mail.find(a)
	cutmail = mail[findmail + 1:]
	print('メールアドレス' + mail + 'のドメイン:' + cutmail)

slicemail()


#ex04.py
username1 = "yoshino"
password1 = "yt1974"

username = input()
password = input()

if username == username1 and password == password1:
	print('OKです')
else:
	print('IDかパスワードが違います')
  
#ex05.py
  def listreplace():
	list = [13,17,31,57,' ',41,83]
	list.remove(' ')
	print(list)

listreplace()
def listave():
	list = [13,17,31,57,41,83]
	ave = sum(list)/len(list)

	print(ave)

listave()
