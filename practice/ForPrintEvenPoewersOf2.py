"""Print the even powers of 2 until 2^n: 2^0, 2^2, 2^4, 2^8, …, 2^n. For example,
if n = 10, then the output would be 1, 4, 16, 64, 256, 1024."""

n = int(input("enter n"))
for i in range(0, n+1):
    if i%2 == 0:
        print(2**i)