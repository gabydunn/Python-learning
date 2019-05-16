#While loop intro 
# spam = 0
# while spam < 5:
#     print("hello world " + str(spam))
#     spam+=1

# name = ''
# while name != 'your name':
#     print("Please enter your name: ")
#     name = input().lower()
# print("gotcha")

# name = ''
# while True:
#     print("Please enter your name: ")
#     name = input().lower()
#     if name == 'your name':
#         break
# print("gotcha")

# spam =0
# while spam<5:
#     spam = spam+1
#     if spam == 3:
#         #this continue will cause the print line to be skipped for the spam ==3 condition
#         continue
#     print('spam is '+ str(spam))

#for loop intro

# print('My name is ')
# for i in range(5):
#     print('Jimmy 5 times ' + str(i))

#for loops non-inclusive of last number
#Syntax:
#for index in range(start range, end range, step amount)
sum =0 

for i in range (100):
    sum = sum+(i+1)
print(str(sum))
