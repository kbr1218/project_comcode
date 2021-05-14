# 함수 : 반복되는 일을 한줄에 여러번 표현하기 귀찮으니까 사용하는것

# def 함수(매개변수) : 수행할 문장

def add_fun(a,b) :
    return a + b

c = add_fun(3, 4)
print(c)

#매개변수와 인수
#매개변수는 함수를 정의할때
#인수는 함수를 call 할때

#입력값이 없는 함수
def say() :
    return "hi"
print(say())

#결과값이 없는 함수
def add_fun(a,b) :
    print("%d, %d 의 합은 %d 입니다" %(a, b, (a+b)))
print(add_fun(5,6))

#둘다 없는 함수
def say() :
    print("hi")

a = say()
print(a)

#매개변수 지정하여 호출하기
def add_fun(a, b) :
    c = a + b
    return c

result = add_fun(a = 3, b = 4)
print(result)

#매개변수 몇 개 인지 모를 때 * 매개변수
def add_many(*args) :
    result = 0
    for i in args :
        result = result + i
    return result

result = add_many(1, 3, 7)
print(result)

#입력값이 여러 개인 경우 2
def add_mul(choice, *args) :
    if choice == "add" :
        result = 0
        for i in args :
            result = result + i

    elif choice == "mul" :
        result = 1
        for i in args :
            result = result * i
    return result

b = add_mul("add", 3, 4, 5)
print(b)
d = add_mul("mul", 1, 3, 4)
print(d)

#함수의 리턴값
def add_and_mul (a,b) :