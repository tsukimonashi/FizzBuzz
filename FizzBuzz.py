__author__ = 'tsukinashi'

a = int(input()) #目標値設定
for i in range(a):  #iから目標値まで
    if (i+1)%15 == 0:
        print('FizzBuzz')
    elif (i+1)%3 == 0:
        print('Fizz')
    elif (i+1)%5 == 0:
        print('Buzz')
    else:
        print(i+1)
