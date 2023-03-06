#When using a function you will need to start of with def
#You can also add parameters within the (), another way to think of it is a variable.
#At the def part you add the key and at the execution of the function you give it the value you want it to use.

def sayhi(name, age):
    print("Hello " + name + ", you are " + age + ".")
#this is the command to execute function
sayhi("Leon", "31")

#you can also use the return information back from a function.
#Also you can't add anything any code under the return function
def cube(num):
    return num*num*num
print(cube(4))