num = int(input("Enter a number :"))

# for i in range(2, num // 2 + 1):
#     if num % i == 0:
#         print(i, end=' ')


i = 2
while i <= num//2:
    if num % i == 0:
        print(i)

    i = i + 1
