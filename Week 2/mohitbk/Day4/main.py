# error handling
try:
    age = int(input("ENter your age: "))
    print(age)
# except Exception:
#     print("Conversion error, Please integer")

# except Exception as exp:
#     # print("Conversion error, Please integer")
#     print(exp)

except ValueError:
    print("Type error has occured.")



# list comprehension
a = [2,3,4,5,6,7,8,9]
b = [number for number in a if number%2==0]
print(a)
print(b)


# 
