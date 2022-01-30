A = int(input())
B = input()

for i in B[::-1]:
    print(A * int(i))

B = int(B)

print(A * B)