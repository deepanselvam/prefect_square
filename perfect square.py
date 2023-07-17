a=int(input("give a number "))
def square(a):
    m=a
    for i in range(1,a):
        if i*i==m:
         return True
    else:
         return False
print(square(a))
