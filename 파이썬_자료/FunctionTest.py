#함수
'''
함수 : 입력값을 가지고 어떤 일을 수행한 다음에 그 결과물을 내어놓는 것
입력 -----> 함수 -----> 출력

함수를 사용하는 이유  : 반복적인 프로그래밍을 피하기 위해
                   : 유지보수가 쉽다

함수의 구조
def 함수명(매개변수) :
    <수행할 문장 1>
    <수행할 문장 2>
    ...
    return
'''

#가장 간단한 함수 예시
print('파이썬 함수의 구조', '-'*30)
#이 함수의 이름은 add이고, 입력으로 두 개의 값을 받으며 결괏값은 2개의 입력값을 더한 값이다.
def add(a, b) :
    return a + b

c = add(3, 4)
print(c)








#매개변수(parameter)와 인수(argument)
print('\n\n매개변수와 인수', '-'*30)
def add(a, b) :         #매개변수
    return a + b


print(add(4, 5))        #인수





#입력값과 결괏값에 따른 함수의 형태
print('\n\n함수 예시 1 : 입력값과 결괏값이 모두 있는 함수', '-'*30)
#함수 예시 1 : 입력값과 결괏값이 모두 있는 함수
def add(a, b) :
    result = a + b
    return result

c = add(3, 4)
print(c)





#함수 예시 2 : 입력값이 없는 함수
print('\n\n함수 예시 2 : 입력값이 없는 함수', '-'*30)
def say() :
    return "Hi"

c = say()
print(c)






#함수 예시 3 : 결괏값이 없는 함수
print('\n\n함수 예시 3 : 결괏값이 없는 함수', '-'*30)
def add(a, b) :
    print("%d, %d의 합은 %d입니다. " %(a, b, a+b))


c = add(3, 4)







#함수 예시 4 : 입력값과 결과값이 없는 함수
print('\n\n함수 예시 4 : 입력값과 결괏값이 없는 함수', '-'*30)
def say() :
    print("hi")

say()
print(say())




#매개변수 지정하여 호출하기
print('\n\n매개변수 지정하여 호출하기', '-'*30)
def add(a, b) :         #매개변수
    return a + b

print(add(3, 4))

#매개변수 지정 1
c = add(a = 3, b = 4)
print(c)


#매개변수 지정 2 (순서 관계없이)
c = add(b = 3, a = 4)
print(c)


#입력값이 몇 개인지 모를 때
'''
def 함수 이름(*매개변수) :
    <수행할 문장>
    ...
 - 매개변수 앞에 *을 붙이면 입력값을 모두 튜플로 만듦 
 - *arg는 임의로 정한 변수 이름
'''
print('\n\n입력값이 몇 개인지 모를 때 예시 1', '-'*30)
def add_many(*hi) :
    result = 0
    for i in hi :
        result = result + i
    return result

result = add_many(1, 2, 3)
print(result)



print('\n\n입력값이 몇 개인지 모를 때 예시 2', '-'*30)
def add_mul(choice, *args) :
    if choice == "add" :
        result = 0
        for i in args:
            result = result + i
        return result
    elif choice == "mul" :
        result = 1
        for i in args :
            result = result * i
        return result

result = add_mul("add", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)
result = add_mul("mul", 1, 2, 3, 4, 5)
print(result)







'''
키워드 파라미터 kwargs (keword arguments)
키워드 파라미터를 사용할 때는 매개변수 앞에 별 두개(**)를 붙인다. 

매개변수 앞에 **을 붙이면 kwargs는 딕셔너리가 되고 모든 key=value 형태의 결괏값이 딕셔너리에 저장
'''
print('\n\n키워드 파라미터 예시', '-'*30)
def print_kwargs(**kwargs) :
    print(kwargs)

print_kwargs(a = 1)
print_kwargs(name = "Kim", age = 33)








#함수의 결괏값은 언제나 하나 == return은 한 번만
print('\n\n함수의 결괏값은 언제나 하나', '-'*30)
def add_and_mul(a, b) :
    return a+b, a*b

result = add_and_mul(3, 4)
print(result)





#return을 두 번 사용해보면
def add_and_mul(a, b) :
    return a+b
    # return a*b

result = add_and_mul(3, 4)
print(result)
# print(add_and_mul(3))





#return문의 또 다른 쓰임새
print('\n\nreturn문의 또 다른 쓰임새', '-'*30)
def say_nick(nick) :
    if nick == "바보" :
        return
    print("나의 별명은 %s입니다. " %nick)

say_nick("바보")
say_nick("호떡")




#매개변수에 초깃값 미리 설정하기
# ***초기화시키고 싶은 매개변수는 항상 뒤쪽에***
print('\n\n매개변수에 초깃값 미리 설정하기', '-'*30)
def say_myself(name, old, man=True) :
    print("나의 이름은 %s입니다. " %name)
    print("나이는 %d입니다. " %old)
    if man :
        print("남자입니다. ")
    else :
        print("여자입니다. ")

say_myself("mal", 4, False)
print("-"*30)
say_myself("mal", 4)







#함수 안에서 선언한 변수의 효력 범위
print('\n\n함수 안에서 선언한 변수의 효력 범위', '-'*30)
#예시 1
a = 1
def vartest(f) :
    f = f + 1
    print(f)
    return f

print(a)
f = vartest(a)
print(f)




#예시 2 (error)
def vartest2(e) :
    e = e + 1
    print (e)

vartest2(3)
a = vartest2(3)
print(a)
# print(e)


#함수 안에서 함수 밖의 변수를 변경하는 방법
print('\n\n방법1 : return 사용하기', '-'*30)
a = 1
def vartest3 (a) :
    a = a + 1
    return a
print(a)
a = vartest3(a)
print(a)








print('\n\n방법2 : global 변수 사용하기', '-'*30)
#global a = 함수 밖의 변수 a를 직접 사용하겠다는 뜻, 사용하지 않는 것이 좋음
g = 1

def vartest4():
    global g
    g = g + 1
    print(g)
    return g

vartest4()
#g = 2
print(vartest4())
# g = 3
print(g)




#lambda 함수 : 함수를 간결하게 만들 때 사용 (def를 사용하지 않아도 될 함수)
#lambda 예약어로 만든 함수는 return 명령어가 없어도 결괏값을 돌려줌
print('\n\n lambda 함수', '-'*30)

def add(a, b) :
    return a + b

c = add(3, 4)
print(c)

add1 = lambda a, b : a+b
d = add1(3, 4)
print(d)
