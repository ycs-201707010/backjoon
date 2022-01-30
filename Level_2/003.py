while True:
    year = int(input())

    if 1 <= year <= 4000:
        break
    else:
        print("다시 입력하세요.")

div_4 = year % 4
div_100 = year % 100
div_400 = year % 400

if div_4 == 0 and div_100 != 0:
    print('1')
elif div_4 == 0 and div_400 == 0:
    print('1')
else:
    print('0')