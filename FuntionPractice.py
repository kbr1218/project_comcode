#Function 연습문제
#Q1. 다음 코드의 실행 결과 예측하기
'''
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()
'''



#Q2. 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수 정의하기





#Q3. 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수 정의





#Q4. 주어진 자연수가 홀수인지 짝수인지 판별하는 함수(is_odd) 만들기






#Q5. 입력으로 들어오는 모든 수의 평균값을 계산하는 함수 작성하기(입력값의 수는 정해져있지 않음)






#Q6. 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의(if 문을 사용해서 수 비교)





#Q7. 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5(string) 함수 작성






#Q8. 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수 작성





#Q9. 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수 정의




#Q10. 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수 정의






#Q11. 아래 코드의 실행 결과 예측하기
'''
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)
'''