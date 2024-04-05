"""Write a program that prints the numbers from 1 to n with a step of 3. For example, if n = 100,
then the output would be: 1, 4, 7, 10, …, 94, 97, 100."""
n = int(input("enter number for n"))
for i in range(1, n+1,3):
    print(i)