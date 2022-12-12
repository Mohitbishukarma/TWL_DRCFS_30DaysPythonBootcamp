# defining a fucntiom
def sum(x,y):
    result = x+y
    print(f"The sum is {result}.")

sum(2,3)


# returning value in func
def cube(x):
    result = x**3
    return result

cub = cube(3)
print("The cube of 3 is",cub)



def times_three(x:int) -> int:
    res = x*3
    return res

r = times_three(2)
print(r)