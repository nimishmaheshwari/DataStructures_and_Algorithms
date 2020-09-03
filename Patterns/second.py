"""
1
22
333
4444
55555
"""
a=int(input("Enter the number of rows"))
for i in range(a):
    for j in range(i+1):
        print(i+1,end="")
    print()