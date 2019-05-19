spam = [[1,2,3,4,5,6], ['a','b','c','d']]

print(spam[1][-3])
print(spam[0][0:2])

spam[0].append('1')

print(spam)

spam[1][2:5] = ['1','3','1']
print(spam[1])

spam = ['cat', 'mouse', 'dog', 'rat']
del spam[1]
print(spam)
newList = list('Heya')
print(newList)
if 'dog'  not in spam:
    print('No dogs here')
else:
    print('You got a dog in there')

