# fizz buzz
for i in range(1,50):
    if i%3==0 and i%5==0:
        print("Fizz Buzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)


# List

lst = ["mohit","syam","hari"]
lst.append("ram")  #>>> interior mutability
print(lst)
lst.pop(2)   # removes item at index 2
print(lst)


# Tuples

tp = ("mohit","ram","hari")
for i in tp:
    print(i)

print(tp.index("mohit"))