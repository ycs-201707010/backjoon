while True:
    H, M = map(int, input().split())

    if 0 <= H <= 23 and 0 <= M <= 59:
        break

if H == 0:
    H = 24

minus_45 = (H * 60) + M
minus_45 -= 45

print(int(minus_45/60), (minus_45%60), sep=" ")