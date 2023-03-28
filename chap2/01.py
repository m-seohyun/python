#0328
'''
print ("hello")
print (3)
print (10.5)

print(type("hello"))
print(type(3))
print(type(10.5))

i = 3
print (i)


i, j, k = 3, 5, "hi"
print(i, j, k)
'''


'''
a = 100
b = 5
a += b
print("a +=b : a = ", a)

a = 100
b = 5
a -= b
print("a -=b : a = ", a)

a = 100
b = 5
a *= b
print("a *=b : a = ", a)

a = 100
b = 5
a /= b
print("a /=b : a = ", a)

a = 100
b = 5
a %= b
print("a %=b : a = ", a)

a = 100
b = 5
a //= b
print("a //=b : a = ", a)

a = 100
b = 5
a **= b
print("a **=b : a = ", a)
'''

'''
name = input("너의 이름은?")
print("저의 이름은 ",name, "입니다.")

year2class = input("2학년 몇반?")
print("저는 ", year2class , "반 입니다.")
print(type(year2class))

age = input("몇살?")
print("저는 ", age , "살 입니다.")
print(type(age))

print("우리 아빠는 저보다 30살 많은 ", int(age)+30 ,"이에요.")
#int()
#float()
#str()
'''

a = 10
str_a = str(a)
print("type(a): ", type(a))
print("type(str_a :", type(str_a))

planet = input("원하는 행성은?")
strRadius = input(planet + "반지름은?")
radius = int(strRadius)

length = 2 * 3.14 * radius
print (planet, "반지름 : ", radius)
print (planet, "둘레길이 : ", length)