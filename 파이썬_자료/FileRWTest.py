#파일 읽고 쓰기 : 파일을 새로 만든 후 프로그램이 만든 결괏값을 새 파일에 write && 파일 read 후 새로운 내용 추가

'''
파일 생성하기 (open)
파일 객체 = open("파일 이름", "파일 열기 모드")

파일 열기 모드 :
r - 읽기 모드 (파일을 읽을 때만 사용)
w - 쓰기 모드 (파일에 내용을 쓸 때)
a - 추가 모드 (파일의 마지막에 새로운 내용 추가)

***쓰기 모드(w)는 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 사라짐***
'''
print('파일 생성하기', '-'*30)
#생성한 후 주석처리
# f = open("test1.txt", 'w')
# f.close()








# 새 파일을 원하는 디렉터리에 생성하는 경우
print('\n\n새 파일을 원하는 디렉터리에 생성하기', '-'*30)
# f = open("C:\Users\kbr_u\source\Pycharm2021_comcode3/test3.txt", "w")
# f.close()




'''
f.close()
생략 가능, 프로그램을 종료할 때 파이썬 프로그램이 열려 있는 파일의 객체를 자동으로 닫음
***쓰기모드로 열었던 파일을 닫지 않고 다시 사용하려고 하면 오류 발생***
'''














#파일을 쓰기 모드로 열어 출력값 적기
# print('\n\n파일을 쓰기 모드로 열어 출력값 적기', '-'*30)
# #파일 생성하고 주석처리
# f = open("test2.txt", 'w')
#for문을 써서 1~10까지 출력
# for i in range(1, 11) :
#     data = "%d번째 줄입니다. \n" %i
#     f.write(data)
# f.close()
#
# f = open("test3.txt", 'w')
#for문을 써서 1~10까지 출력
# for i in range(1, 11) :
#     data = "%d번째 줄입니다. \n" %i
#     f.write(data)
# f.close()







#프롬프트 창에서 실행하기










#프로그램의 외부에 저장된 파일을 읽는 방법
# 1. readline() 함수 사용하기
print('\n\n1. readline() 함수 사용하기 - 한 줄 출력', '-'*30)
f = open("test2.txt", 'r')
line = f.readline()
print(line)
f.close()





print('\n\n1. readline() 함수 사용하기 - 모든 줄 출력', '-'*30)
f1 = open("test2.txt", 'r')
while True :                    #무한루프
    line = f1.readline()
    if not line :
        break
    print(line)
f1.close()








# 2. readlines 함수 사용하기 : list로 리턴
print('\n\n2. readlines 함수 사용하기', '-'*30)
f2 = open("test2.txt", 'r')
lines = f2.readlines()
print(type(lines))
for line in lines :
    print(line)
print(type(line))
f2.close()












# 3. read 함수 사용하기 : 파일 전체를 문자열로 return
print('\n\n3. read 함수 사용하기', '-'*30)
f3 = open("test2.txt", 'r')
data = f3.read()
print(data)
print(type(data))
f3.close()














# 파일에 새로운 내용 추가하기 (추가모드 a)
print('\n\n파일에 새로운 내용 추가하기', '-'*30)
#추가한 후 주석처리
# f3 = open("test2.txt", 'a')
# for i in range(11, 21) :
#     data = "%d번째 줄입니다. \n" % i
# #     f3.write(data)
# # f3.close()
#
#
#
#
#
#
#
#
# # with문과 함께 사용 : 자동으로 close
# print('\n\nwith문 사용하기', '-'*30)
#
#
# f4 = open("test3.txt", 'w')
# f4.write("with문과 함께 사용하기")
# f4.close()
#
# with open("test4.txt", 'w') as f5 :
#     f5.write("with문과 함께 사용하기 _ 2")
#



print(max(3, 1, 4))