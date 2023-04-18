#수정이 불가한 항목들 -> 튜플
t1 = (1, 2, 3, 4)
print(t1)
t2 = tuple()
print(t2)
t3 = 1, 2, 4, 5, 5
print(type(t3))


#print(t3.index(3))
print(t3.count(3))

t4 = 1, 2, 3, 7, 5, 6
t5 = 100, 200, 300
print("t4 + t5 : ", t4 + t5)
print("t4 : ", t4)
print("t5 : ", t5)

print("t4 : ", t4)
print(sorted(t4)) # 원본은 안바뀜
print("t4 : ", t4)

#Lst.sort() #원본이 바뀜



#dictionary
#key : value
#1001:"홍길동", 1002:"김길동"

d1 = {1001:"홍길동", 1002:"김길동", 1003:"박길동", 1004:"고길동"}
print(d1[1001])
#print(d1[key])

#d2 = {}
#강좌에 대한 dictionary
d2 = dict()
d2['강좌명'] = '파이썬'
d2['개설 요일'] = '화요일'
d2['년도'] = 2003
d2['수강생'] = ['김', '이', '박', '최']
print("d2 : ", d2)
print(d2['수강생'])
print(len(d2))

'''
dictionary key:value 1:월, 2:2월 ... 12:12월
for문을 돌려서 각각의 value값 찍기
'''

#1) key값이 숫자인것을 활용

month = {1:'1월', 2:'2월',3:'3월', 4:'4월', 5:'5월', 6:'6월', 7:'7월', 8:'8월', 9:'9월', 10:'10월', 11:'11월', 12:'12월'}
#for i in range(1,13) :   #1, 2, 3, 4, ... ,12
#    print(month[i])


#dictionary method
print("month.keys :", month.keys())
print("month.values : ", month.values())
print("month.items : ", month.items())

for i in range(10,3,10)   :
    print(month[i])

#2) month.keys() 활용

for i in month.keys() :
    #print("i : ", i)
    print(month[i])

#3) month.values() 활용

print("month.values() 활용")
for i in month.values() :
    print(i)

#4) month.items() 활용

print(month.items())
print("month.items()")
for item in month.items() :
    #print(item)
    print(item[1])


#5) month.items() 활용

print("month.items() 2")
for k, v in month.items() :
    #print(item)
    #print(item[1])
    print(k)
    print(v)

#6) month.keys() month
for i in month : 
    print(i) #key
    print(month[i]) #value


print("month.pop(10) :",month.pop(10)) # index에 있는 item 제거
print(month)
print("month.popitem() :",month.popitem()) #제일 마지막 item 제거
print(month)


month.update({3: 'March'})
print("month.update() :", month)
month.update({5:'15월'})
print(month)
month.update({3: '300월'})
print(month)


# dictionary-tuple-list 변환
# tuple - 변경불가 수정불가  (아메리카노, 핫초코, 라떼)
# tuple -> list 유자차 추가 -> tuple변경
# list -> tuple 수강신청 전 수강생 변경 -> tuple
# tuple, list -> dictionary (1,2,3,4), (홍,김,박,고)

seql = ['a', 'b', 'c', 'd']
seqt = tuple(seql)
print(seqt)
print(type(seqt))

seql2 = list(seqt)
print(seql2)
print(type(seql2))

seqd = dict(enumerate(seql))
print(seqd)
print(type(seqd))

# zip
# list, tuple 여러개 -> 하나의 튜플의 조합으로 된 리스트
l1 = ['1조', '2조', '3조']
YA = ['홍', '김', '이']
YB = ['최', '한', 'James,']

z = zip(l1, YA, YB)
print(type(z))
print(z)
print(list(z))

print(tuple(zip(l1, YA, YB)))

l10 = ['한식', '양식', '일식', '중식']
l11 = ['김가네', '아웃백', '미소야', '영화루']
l12 = ['김밥', '스테이크', '우동', '짬뽕']

print(list(zip(l10, l11, l12)))

for i in range(4) :
    print(l10[i], l11[i], l12[i])

l100 = list(zip(l10, l11, l12))
for i in l100 :
    print(i[0], i[1], i[2])

l100 = list(zip('ABCD', l10, l11, l12))
for i in l100 :
    print(i[0], i[1], i[2], i[3])

l10 = ['한식', '양식', '일식', '중식']
l11 = ['김가네', '아웃백', '미소야', '영화루']
l12 = ['김밥', '스테이크', '우동', '짬뽕']

#dictionary
print(list(zip(l10, l11)))
print(dict(zip(l10, l11)))

print(dict(zip(l10, zip(l11, l12))))


l11 = ['김가네', '아웃백', '미소야', '영화루']
print(list(enumerate(l11)))
print(dict(enumerate(l11)))


lec = ['파이썬', '자바', '알고리즘', 'IoT', 'C']
sp = [101, 102, 103, 104, 105]
f = dict(zip(lec, sp))

while True :
    c = input("강의명 : ")
    if c == "quit" :
        print("종료합니다.")
        break
    else :
        if c in f.keys() :
            print(f[c])
        else :
            print("컴퓨터과 과목만")
            continue