print ("How old are you?",)
age = input()
print ("How tall are you?",)
height = input()
print ("How much do you weight?",)
weight = input()

print ("So, you're %r old, %r tall and %r heavy." %(age, height, weight))

# Fix python 2.x
try: input = raw_input
except NameError: pass
print("Hi " + input("Say something: "))