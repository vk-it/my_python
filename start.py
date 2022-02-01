print('hello')
print('world')
print('all')
print('Проверка')

#for i in 'hello world':
#    if i == 'o':
#        continue
#    print(i *2, end ='')
print(4+5)
#import this
small = False
green = True
if small:
    if green:
        print("pea")
    else:
        print("cherry")
else:
    if green:
#Ты попадаешь в else, потому что small - False, далее там встречается if green, который True и отдает тебе арбуз, \\потому что труе выпало на арбуз
        print("watermelon")
    else:
        print("pumpkin")