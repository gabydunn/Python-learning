# def hello():
#     print('Howdy')
#     print('Howdy!!!')
#     print('Hello there')

# hello()
# hello()
# hello()
# def plusOne(number):
#     return number+1
# print(plusOne(5))
# #None = null?

# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)
# def bacon():
#     ham = 101
#     eggs =0
# spam()
# def spam():
#     print(eggs)

# eggs = 42
# spam()
#manipulating global variables
def spam():
    global eggs
    eggs = 'Hello'

eggs = 42
spam()
print(eggs)