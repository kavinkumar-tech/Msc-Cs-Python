print("----- Conditional Branches-----")
a=int(input("Enter A : "))
print(a)
b=int(input("Enter B : "))
print(b)
c=int(input("Enter C : "))
print(c)
small=a
if b<a and b<c:
    small=b
if c<a and c<b:
    small=c
print(small,"is the smallest value")
