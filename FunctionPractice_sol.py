#Function 연습문제 답
print("Q1")
#Q1. 다음 코드의 실행 결과 예측하기
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()





print("\n\nQ2")
#Q2. 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수 정의하기
def print_with_smile (string) :
    print (string + ":D")
print_with_smile("Python")





print('\n\nQ3')
#Q3. 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수 정의
def print_upper_price(price) :
    print(price * 1.3)
print_upper_price(3000)





print('\n\nQ4')
#Q4. 주어진 자연수가 홀수인지 짝수인지 판별하는 함수(is_odd) 만들기
def is_odd(num) :
    if num % 2 == 1:
        return True
    else :
        return False
print(is_odd(3))
print(is_odd(4))

#lambda 사용하기
is_odd2 = lambda x : True if x % 2 == 1 else False
print(is_odd2(3))






print("\n\nQ5")
#Q5. 입력으로 들어오는 모든 수의 평균값을 계산하는 함수 작성하기(입력값의 수는 정해져있지 않음)
def avg_numbers(*args):   # 입력 개수에 상관없이 사용하기 위해 *args를 사용
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1, 2))
print(avg_numbers(1,2,3,4,5))






print("\n\nQ6")
#Q6. 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의(if 문을 사용해서 수 비교)
def print_max(a, b, c) :
    max_val = 0
    if a > max_val :
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    print(max_val)
print_max(40, 32, 54)






print("\n\nQ7")
#Q7. 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5(string) 함수 작성
def print_5(line):
    num = int(len(line) / 5)
    for x in range(num + 1) :
        print (line[x * 5: x * 5 + 5])
print_5("영화를통해본바이러스감염증특강ㅎㅎ")







print("\n\nQ8")
#Q8. 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수 작성
def print_mxn(line, num):
    chunk_num = int(len(line) / num)
    for x in range(chunk_num + 1) :
        print(line[x * num: x * num + num])

print_mxn("영화를통해본바이러스감염증특강", 7)








print("\n\nQ9")
#Q9. 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수 정의
def make_url(string) :
    url = "www." + string + ".com"
    return url

print(make_url("gmail"))





print("\n\nQ10")
#Q10. 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수 정의
def make_list (string) :
    my_list = []
    for i in string :
        my_list.append(i)
    return my_list
print(make_list("Hello"))





print("\n\nQ11")
#Q11. 아래 코드의 실행 결과 예측하기
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)