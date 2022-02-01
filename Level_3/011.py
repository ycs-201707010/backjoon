N, X = map(int, input().split())

list_A = list(map(int, input().split()))

for i in list_A:
    if i < X:
        print(i, end=" ")