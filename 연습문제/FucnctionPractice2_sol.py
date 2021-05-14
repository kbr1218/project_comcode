#함수 연습문제 2 답
# 1. 아래 함수를 호출했을 때 에러가 발생하는 이유는?
def function1(a, b) :
    print(a + b)
# function1("Hello", 3)

#function1은 같은 타입의 값을 두 개 입력받아 덧셈을 하는 함수이다.
#함수를 호출할 때 (function1("Hello", 3)에서 문자열과 숫자를 입력했으므로 더할 수 없다.






# 2. 입력된 문자열을 역순으로 출력하는 print_reverse 함수 정의
def print_reverse(string) :
    print(string[::-1])

print_reverse("Hello")




# 3. 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수 정의
def print_even(my_list) :
    for i in my_list :
        if i % 2 == 0 :
            print(i)






# 4. ,(콤마)가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수 정의
def convert_int(string) :
    return int(string.replace(',', ''))







# 5. 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수 정의
# (회사는 연봉을 12개월로 나누어 분할 지급하며, 1원 미만은 버린다.)
def calc_monthly_salary(annual_salary) :
    monthly_pay = int(annual_salary / 12)
    return monthly_pay







# 6. 아래 코드의 실행 결과 예측하기
def my_print(a, b):
    print("왼쪽 : ", a)
    print("오른쪽 : ", b)

my_print(b = 100, a = 200) 
