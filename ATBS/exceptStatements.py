# def div42by(divideBy):
#     try:
#         return 42/divideBy
#     except ZeroDivisionError:
#         print('Error: You tried to divide by zero')

# print(div42by(2))
# print(div42by(12))
# print(div42by(0))
# print(div42by(1))

#Most built in errors (ex: ValueError) derived from exception class
#Error will just be used here for custom user errors
#The pass statement is a null operation, it's here because the custom error classes 
#need to be here syntactically but no code needs to be executed currently
class Error(Exception):
    pass
class ValueTooSmallError(Error):
    pass
print('How many cats do you have?')
numcats = input()
try:
    if int(numcats)<0:
        raise ValueTooSmallError
    elif int(numcats)>=4:
        print('Thats a lot of cats')
    else:
        print('That is not very many cats.')
except ValueError:
    print('You did not enter a number')
except ValueTooSmallError:
    print('This value is too small')

