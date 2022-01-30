while True:
    A = int(input())

    if 0 <= A <= 100:
        break
    else:
        print("다시 입력하세요.")

if A >= 90:
    print('A')    
elif A >= 80:
    print('B')
elif A >= 70:
    print('C')
elif A >= 60:
    print('D')
else:
    print('F')