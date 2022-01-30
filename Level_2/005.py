while True:
    H, M = map(int, input().split())

    if 0 <= H <= 23 and 0 <= M <= 59:
        break

if M >= 45:
    M -= 45
    print(H, M, sep=" ")
else:
    if H == 0:
        H = 24
    H -= 1
    M += 15 # 60분 더하고 45분 빼면 최종적으로 +15분. 
    print(H, M, sep=" ")
