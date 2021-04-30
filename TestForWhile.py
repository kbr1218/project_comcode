#while문 / for문 연습문제

#1. while문을 사용해서 1부터 1000까지의 자연수 중 3의 배수의 합 구하기
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print(result)


print("\n", "-" * 80)
#2. while문을 사용해서 아래와 같이 별(*)을 표시하는 프로그램을 작성하기
'''
*
**
***
****
*****
'''
i = 0
while True:
    i += 1
    if i > 5: break
    print ('*' * i)


print("\n", "-" * 80)
#3. for문을 사용해서 1부터 100까지 숫자 출력하기
for i in range(1, 101):
    print(i)


print("\n", "-" * 80)
#4. A 학급에 총 10명의 학생이 있다. 리스트 grade는 이 학생들의 중간고사 점수이다. for문을 사용해서 A 학급의 평균 점수 구하기
grade = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for score in grade:
    total += score
average = total / len(grade)
print(average)