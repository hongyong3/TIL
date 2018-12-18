# python 과거 // 저 %s를 자주 바꿔야 할 때 'one', 'two'만 바꾸면 됨 
#'일은 영어로 %s, 이는 영어로 %s' % ('one', 'two')

#pyformat // .format은 매소드
#'{} {}'.format('one', 'two') // name과 e_name의 순서를 바꾸고 싶으면 {1}, {0}으로 입력하면 위치가 바뀐다.

#name = '최홍용'
#e_name = 'Choi'
#print('안녕하세요. {}입니다. My name is {}'.format(name, e_name))

# f-string python 3.6
#print(f'안녕하세요. {name}입니다. My name is {e_name}')

#Lotto
#import random
#x = range(1, 46)
#Lotto = random.sample(x, 6)
#Lotto.sort()
#numbers = Lotto
#print(f'오늘의 행운의 번호는 {numbers}')

#Lotto
#import random
#x = list(range(1, 46))
#Lotto = random.sample(x, 6)
#Lotto.sort()
#numbers = Lotto
#print(f'오늘의 행운의 번호는 {numbers}')

#name = "최홍용"
#print("안녕하세요." + name + "입니다.")

