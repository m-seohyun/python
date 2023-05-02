# 함수
# input을 주면 output이 나오는것
'''
input - 숫자 - num1
output - 숫자 - output_num
이런 기능을 하는 function - multi
'''

# 3을 곱하는 함수
# 함수 정의
def multi(num1) :
    output_num = num1 * 3
    print("여기는 multi 함수 안 입니다.")
    return output_num

# 정의한 함수 호출
print(multi(10)) # return 30


# funtion - hello
# paraneter - input - 사람이름 2개 입력 
# output - 안녕 1번 사람, 안녕 2번 사람
# 함수 내에서 출력


def hello(name1 = "김", name2 = "이") :
    print("안녕,", name1)
    print("안녕,", name2)

print("기본값")
print(hello())
print("사용자값")
print(hello("박", "최"))



# 두 개의 숫자를 입력받아, 두 개의 합을 함수 내에서 출력

'''
def mysum(num1, num2) :
    print("두 숫자의 합은 :", num1 + num2)

mysum(100,1000)

def mysum2(num1, num2) :
    return num1 + num2

result = mysum2(100,1000)
print(result)
print(mysum2(100,1000))
'''


'''
# 지역 변수, 전역 변수

num = 100 # 전역 변수 global variable
print("*** num : ", num) #100

def addone() :
    num = 10
    print( "addone() : " , num + 1) # num + \=> 11
    print( "addone() num : " , num) # num = 10
    num + num * 8 + 20
    return num

result1 = addone()
print("*** num : ", num) #100
print("*** num : ", result1) #100
'''


'''
num = 100 # 전역 변수 global variable
print("*** num : ", num) #100

def addone() :
    # 내부 function 에서 num을 수정 하지 않을 때
    print( "addone() : " , num + 1) # num + 1
    print( "addone() num : " , num) # num = 

addone()
print("*** num : ", num) #100
'''

'''
# 3) 내부 function에서 번역변수를 사용하면 좋겠고 수정도 하고 싶고, function이 끝나도 그 값이 반영 되었으면 좋겠음

num = 100 # 전역 변수 global variable
print("*** num : ", num) #100

def addone() :
    global num # 전역변수를 사용. 변수에 새로운 값 대입 가능
    num = 3
    num = num + 1
    #print( "addone() : " , num + 1) # num + 1
    #print( "addone() num : " , num) # num = 

addone()
print("*** num : ", num) # 101
'''

print()
print(1,2,3,4,5,6,7,8,9)
print()

def hello2(*names) :
    # 안녕 찍기
    for i in names :
        print("hello ", i) # hello 홍길동

hello2("홍길동", "김", "이", "박")



# 합을 구하는 function

def mysum2(*nums) :
    result = 0
    for num in nums :
        result = result + num        
    return result

print("합: ", mysum2(1,2,3,4,5,6,7,8,9,0))

list1 = [1,2,3,4,5,6,7,8,9,0]
print("합: ", mysum2(*list1))

# dictionary = {key1:value1, key2:value2}
# **

coffee = {"아메리카노":2000, "라떼":3000, "티":2500}

def printmenu(**keyvalue) :
    for key in keyvalue : 
        print(key, keyvalue[key])

printmenu(**coffee)
printmenu(아메리카노 = 2000, 라떼 = 3000, 티 = 2500, 핫초코 = 4000)


def func1 (*num, **menu) :
    # num 합
    result = 0
    for n in num :
        result = result + n
    print(result)

    # menu 출력
    for key in menu :
        print(key, menu[key])

coffee = {"아메리카노":2000, "라떼":3000, "티":2500}
list1 = [1,2,3,4,5,6,7,8,9,0]

func1(1,2,3,4,5,6,7,8,9,0,아메리카노 = 2000, 라떼 = 3000, 티 = 25000, 핫초코 = 4000)
func1(*list1, **coffee)
func1(1,2,3,4,5,6,7,8,9,0,**coffee)

# lambda function
# function을 만드는데 이름짓기 귀찮다. 실행문이 1개밖에 없음.

def addone(x) :
    return x + 1

print(addone(100))

# lambda parameter_name : parameter로 실행하는 문

print((lambda x : x + 1)(100))

def mysum3(num1, num2) :
    return num1 + num2

print(mysum3(100,1000))

print((lambda num1, num2 : num1 + num2)(100, 1000))

'''
map, filter
list가 존재할 때,
list1 = [1,2,3,4,5,6,7]
addone()
list2 = [2,3,4,5,6,7,8]

map(함수, input 리스트)
map(lambda 함수, input 리스트)
map(addone, list1) => list2
map(lambda x : x + 1)(100)
'''

lst1 = [1,2,3,4,5,6,7]
print(list(map(lambda x : x + 1, lst1)))

#lambda num1, num2 : num1 + num2
lst1 = [1,2,3,4,5,6,7]
lst2 = [1,2,3,4,5,6,7]
# result = [2,4,6,8,10, 12, 14]
# map(함수, input 리스트, inputlist2)

print(list(map(lambda num1, num2 : num1 + num2, lst1, lst2)))
#map(lambda num1, num2 : num1 + num2, [1,2,3,4,5,6,7], [1,2,3,4,5,6,7]))