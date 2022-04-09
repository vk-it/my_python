# print(47)
#print("Winter came for " + "the House of Frey.")
#a = 4
# print(a)
#b = a
# print(b)
#type(7) == int
#a = 4
# type(a)
#y = 5
#x = 12 - y
# print(x)
#a = b = c = 3
# print(a,b,c)
#a = a + 3
# print(a)
#a += 2
# print(a)
#a = 10
#print(5 < a > 8)
#a = 8
#b  = 3 + 5
#print(a == b)
#print(a is b)
x = [1, 2, 3, 4, 5]
print(5 in x)
print(5 not in x)

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

