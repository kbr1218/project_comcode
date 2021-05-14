#리스트 List[]
print("-" * 10, "리스트 생성", "-" * 10)
a = ["사과", "바나나", "호랑이", 1, 2, 3]               #문자와 숫자가 들어있는 리스트 a
print(type(a))                                       #리스트 a의 타입 확인

c = []                                               #비어있는 리스트
d = [1, 2, 3, [4, 5, 6]]                             #리스트가 중첩된 리스트 안의 리스트


# 리스트 인덱싱 list[], 슬라이싱list[:]
print("\n", "-" * 10, "리스트 인덱싱과 슬라이싱", "-" * 10)
print(a[2])                          #리스트 a의 3번째 값 인덱싱 : '호랑이' 출력
print(a[2:5])                        #리스트 a의 2번째 ~ 4번째 값 슬라이싱 : ['호랑이', 1, 2]

print(d[3][1])                       #리스트 안의 4번째 값(리스트)의 2번째 요소 출력 : 5
print(a[-1])                         #리스트 a의 마지막 요소 출력 : 3

#리스트 더하기(+)
print("\n", "-" * 10, "리스트 더하기", "-" * 10)
a = [1, 2, 3]
b = ["사과", "바나나", "호랑이", 1, 2, 3]
print(a + b)

#리스트 반복하기(*)
print("\n", "-" * 10, "리스트 반복하기(곱하기)", "-" * 10)
e = b * 3                           #리스트 e에 리스트 b를 3번 곱한 결과를 저장
print(e)                            #리스트 e 출력

#리스트 길이구하기(len(a))
print("\n", "-" * 10, "리스트 길이 구하기", "-" * 10)
print(len(e))

#리스트 수정 a[0] = x
print("\n", "-" * 10, "리스트 수정(인덱싱 사용)", "-" * 10)
a[0] = 5                            #리스트 a의 첫번째 자리 값(1)을 5로 교환
print(a)

# #리스트 삭제 del a[x], a[:]
print("\n", "-" * 10, "리스트 삭제", "-" * 10)
del b[0]                            #인덱싱으로 삭제
del a[1:]                           #슬라이싱으로 삭제
print(b)
print(a)

#리스트 관련 함수(append, sort, reverse, index, insert, remove, pop, count, extend)
#a.append(x)
print("\n", "-" * 10, "append 함수", "-" * 10)
f = ["고구마", "돌", "호랑이"]
f.append("감자")          #"감자"라는 요소 추가
print(f)

#a.sort()
print("\n", "-" * 10, "sort 함수", "-" * 10)
g = [3, 4, 1, 69, 34, 2]
g.sort()                #작은 순으로 정렬 (문자는 abc순)
print(g)

#a.reverse()
print("\n", "-" * 10, "reverse 함수", "-" * 10)
g.reverse()             #리스트의 순서를 거꾸로
print(g)

#a.index(x)
print("\n", "-" * 10, "index 함수", "-" * 10)
print(g.index(69))      #괄호 안의 값의 위치 반환

#a.insert(x, y)
print("\n", "-" * 10, "insert 함수", "-" * 10)
g.insert(3, 2)          #3번째 자리에 2 추가
print(g)

#a.remove(x)
print("\n", "-" * 10, "remove 함수", "-" * 10)
g.remove(2)             #첫번째로 나오는 2 삭제
print(g)

#a.pop()
print("\n", "-" * 10, "pop 함수", "-" * 10)
g.pop()                 #리스트의 마지막 요소 뽑아내고 삭제
print(g)

#a.count(x)
print("\n", "-" * 10, "count 함수", "-" * 10)
g.insert(0, 1)
#g = [1, 4, 1, 69, 34]
print(g.count(1))       #리스트에 포함된 요소 1의 개수 세기


#a.extend([x])
print("\n", "-" * 10, "extend 함수", "-" * 10)
g.extend([1, 2, 3, 4])              #리스트 g에 괄호 안의 리스트 더하기
print(g)


#리스트로 바꾸기, 튜플로 바꾸기
print("\n", "-" * 10, "리스트로 바꾸기, 튜플로 바꾸기", "-" * 10)
test = [3, 4, 5]
make_tuple = tuple(test)
print(type(make_tuple))

make_list = list(make_tuple)
print(type(make_list))