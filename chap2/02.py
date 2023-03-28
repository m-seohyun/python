#0328

'''
var = "python"
ch1 = var[0]
#str
print(var[0], " ", var[2], " ")
#p
print(var[0], " : ", var[-6])
print("length of var : ", len(var))

print("PYTHON"[0], "PYTHON"[2])
'''

'''
print("python"[1:5])
print("python"[2:4])
print("python"[0:3])
print("python"[0:6])
print("python"[0:len("python")])

#시험X
print("python"[-5:-1])
print("python"[-4:-1])
print("python"[-6:-3])
print("python"[-6:-1])
print("python"[-len("python"):-1])
'''

'''
print("python"[:3])
print("python"[:4])
print("python"[1:])
print("python"[3:])
print("python"[:])
'''


'''
str = "Monty Python"
print (len(str))

print(str[0:5], str[6:], str[6:12])
#start 첨자는 end 첨자보다 문자열 범위 내에서 왼쪽에 위치한 첨자여야 반환문자열 존재
#그렇지 않으면 공백 문자열 반환(오류는 발생하지 않음)
print(str[-12:-7], str[-6:], str[-6:0])
print(str[-12:-7], str[-6:], str[-6:])

print(str[1:5:3])
print(str[::-1])
print(str[5:0:-1])
print(str[-1:-7:-1])
'''


'''
print("ab" + "\b" + "c")
print(" \"hello \n\v\t world\" ")
#\\ : 역슬래시
#\' : 작은 따옴표
#\" : 큰 따옴표
#\n : 새 줄
#\t : 수평 탭
#\v : 수직 탭
#\b : Backspace, 지우기
'''


'''
#string method
str_var = "하하하"
#type(str_var) => str
print(str_var.replace("하", "호"))

str_var2 = "안녕하세요, 파이썬. 파이썬 파이썬. 파이썬 파이썬. 파이썬 파이썬. 파이썬 수업입니다."
print(str_var2.replace("파이썬", "자바"))
str_var3 = str_var2.replace("파이썬", "자바")
str_var4 = str_var2.replace("파이썬", "자바", 3)

print("str_var2" , str_var2)
print("str_var3", str_var3)
print("str_var4", str_var4)
'''



num_str = input("실수를 하나 입력하세요.")
num_str.replace('.', '')

sum = 0
sum += int(num_str[0])
sum += int(num_str[1])
sum += int(num_str[2])
sum += int(num_str[3])
sum += int(num_str[4])
sum += int(num_str[5])

print("입력값 : ", num_str)
print("모든 자리수 합 : ", sum)