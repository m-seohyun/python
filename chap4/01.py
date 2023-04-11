list1=[]
print(list1)
list1.append("python")
list1.append("python")
list1.append("python")
list1.append("python")
list1.append("python")
list1.append("java")
list1.append("C++")
print(list1)
print(list1[0])

for i in range(len(list1)): #range(3) 0,1,2
    print(list1[i])

print("=====for 2=====")
for i in list1:  #for i in {pyton, java, c++}
    print(i)

print(list1)
print ("count : " , list1.count("python"))
print("index : " , list1.index("python"))
#"hahaha".index("a")


#list 수정
list1[0]="AI"
list1[2]="IoT"
print(list1)
#['python', 'python', 'python', 'python', 'python', 'java', 'C++']
list2 = list1[1:0:3] #
print(list2)
list2 = list1[1:5:1] #['python', 'IoT', 'python', 'python']
print(list2)
list2 = list1[1:len(list1):2] #['python', 'python', 'java']
print(list2)
list2 = list1[2:6:3] #['IoT', 'java']
print(list2)
list2 = list1[::-1] #['C++', 'java', 'python', 'python', 'IoT', 'python', 'AI'] 
print(list2)





#수정 불가 : append, insert, 값 변경 X
#[1,2,3,4]
#(1,2,3,4)  t1+t2 => t3
#t1 +1 => t1




list2 = list1[2:6:3] # 2~5, 2, 5 'IoT', 'python'
['IoT', 'python']
print(list2)
list3 = [1,2,3,4,5,6,7,8]

list3[1] = list2
print(list3)

list3[1:2] = list2
print(list3)





#List insert
food = []
food.append("짜장면")
food.append("샌드위치")
print(food)
food.insert (0,"파스타")
print(food)
food.insert(2,"제육볶음")
print(food)

'''
food.remove("제육볶음")
print(food)


print("food.pop : " , food.pop())
print(food)
print("food.pop : " , food.pop())
print(food)
'''

#extend
print(food)
dessert = ['커피', '케이크', '와플']

food_list = food + dessert
print(food_list)

food.extend(dessert) #food + dessert
print(food)

food.reverse()


#sort()
#sorted()
l1 = ['apple', 'banana', 'orange','mango']
print(l1)
print("sorted(l1): ", sorted(l1))
print("l1        : ", l1)

l1.sort()
print(l1)


'''
a = "1"
print(type(a))
print(int(a) + 5)
print(type(a))
'''

'''
#food.clear()
#del food
print(food)
'''



#리스트 컴프리헨션
#리스트 변수명 = [i for i in range() ]


#0 ~ 10 까지 있는 List를 만들자


#1
l3 = {0,1,2,3,4,5,6,7,8,9,10}
print(l3)

#2
l3 = []
for i in range(11) :
    l3.append(i)
print(l3)

#3
l3 = [ i for i in range(11)]
print(l3)

#0 ~ 10 까지의 숫자의 제곱을 원소로 가지는 리스트를 작성
#l ** 2
#[0,1,4,9,16,...,64,81,100]

l4 = []
for i in range(11) :
    l4.append(i**2)
print(l4)

l5 = [ i**2 for i in range(11) ]
print (l5)

l6 = [ i*3 for i in range(11) ]
print (l6)

#"hello"를 10개 가지는 리스트 작성
l7 = ["hello" for i in range(10)]
print(l7)

l8 = []
for i in range(10) :
    l8.append("hello")
print(l8)

#짝수의 제곱
#[0,1,4,9, ... ,100]
#[0,4,16  ,...,100]

l10 = []
for i in range(11):
    if i%2 == 0: #짝수
        l10.append(i**2)    
print(l10)

l11 = [ i**2 for i in range(11) if i%2 == 0]
print(l11)




#shallow copy
whishlist = food[:]
print("food : ", food)
print ("whishlist : ", wishlist)

food.pop()
print("after food.pop()")
print("food :      ", food)
print("whishlist : ", wishlist)

print(food is wishlist)


#deep copy
food2 = food[:]
food3 = list(food)



food2 = food[:]
print("deep copy")
print("food :      ", food)
print("food2 :     ", food2)
print(food is food2)

food2.append('김밥')
print("food :      ", food)
print("food2 :     ", food2)

food.append("라볶이")
print("food :       ", food)
print("food2 :      ", food2)
print ("whishlist : ", wishlist)