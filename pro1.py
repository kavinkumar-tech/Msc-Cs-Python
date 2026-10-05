print("******LISTS, DICTIONARIES AND TUPLES*******")
print("----LIST----")
a=["apple","banana","cherry"]
print(a)
print("----List Items----")
print(a[1])
print("---- TUPLES----")
b=("apple","banana","cherry")
if "apple" in b:
    print("Yes, Apple is in the fruits tuple")
print("----DICTIONARY----")
employee={"name":"john",
"age":29,
"salary":25000,
"company":"Google"}
for x in employee.items():
    print(x)
