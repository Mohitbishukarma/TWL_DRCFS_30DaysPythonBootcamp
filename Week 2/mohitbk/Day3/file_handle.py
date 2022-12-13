# f = open('names.txt','r')
# print(f)
# file_data = f.read()
# print(file_data)
# f.close()


# opening in write mode
# f = open('file.txt','w')
# data = f.write("Hello Mohit")
# f.close()

# opening in append mode
# f = open('file.txt','a')
# f.write("\nHow are you?")
# f.close()

# with statement
# with open('names.txt','r') as f:
#     content = f.read()
#     print(content)

# with open('names.txt','r') as f:
#     content = f.read().split('\n')
#     print(content)
#     print("\n\n",content[0])
    # print("\n\n",content[0].split(',')[0])


print("Student Details".center(40,'*'))
print("Name".center(20),"age".center(20))
print("-----".center(20),"-----".center(20))
with open('names.txt','r') as f:
    content = f.read().split('\n')
    for data in content:
        name , age = data.split(',')
        print(f"{name.center(20)}{age.center(20)}")
