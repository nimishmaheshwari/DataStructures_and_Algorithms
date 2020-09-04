"""
   *
  **
 ***
****
"""
a=int(input("Enter the number of rows"))
k=a-1
for i in range(0,a):
    for j in range(0,k):
        print(end=" ")
    k-=1
    for n in range(0,i+1):
        print("*",end="")
    print()