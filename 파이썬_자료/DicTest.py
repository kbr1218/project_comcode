#Dictionary 딕셔너리
print("-" * 10, "dictionary 생성, type 확인", "-" * 10)
d1 = {"사과" : [100, 200], "바나나" : 500}
print(type(d1))
#"사과" = key, 1000 = value

#딕셔너리 쌍 추가하기 dic[x] = 'x'
print("\n", "-" * 10, "딕셔너리 쌍 추가하기", "-" * 10)
d1["망고"] = 400                      #key = "망고", value = 400
print(d1)

#딕셔너리 요소 삭제하기 del dic[x]
print("\n", "-" * 10, "딕셔너리 요소 삭제하기", "-" * 10)
del d1["바나나"]                       #key값을 입력해서 key-value 쌍 삭제
print(d1)

#딕셔너리 key value 얻기 dic[key]
print("\n", "-" * 10, "딕셔너리 key value 얻기", "-" * 10)
v1 = d1["사과"]                       #딕셔너리 d1의 "사과"의 value 값을 v1에 저장
print(v1)

#주의해야 할 사항 : 딕셔너리는 key값이 중복되면 안됨
# d2 = {"money" : 1000, "card" : 3000, "money" : 500}
# v2 = d2["money"]
# print(v2)

#key 리스트 만들기, value 리스트 만들기
print("\n", "-" * 10, "key/value 리스트 만들기", "-" * 10)
print(d1)                           #딕셔너리 요소 확인
print(d1.keys())                    #key 값만 모아서 리스트로 출력
print(d1.values())                  #value 값만 모아서 리스트로 출력


#dic.items()
print("\n", "-" * 10, "items 함수", "-" * 10)
print(d1.items())                   #key-value 쌍을 튜플로 만들어서 리스트에 저장

#dic.clear()
print("\n", "-" * 10, "clear 함수", "-" * 10)
d3 = {"name" : "김말이", "age" : 7}
d3.clear()                          #딕셔너리에 있는 모든 요소 삭제 : {} 빈 딕셔너리 출력
print(d3)

#dic.get('key')
print("\n", "-" * 10, "get 함수", "-" * 10)
v2 = d1.get("사과")                   #딕셔너리 d1의 "사과" value를 v2에 저장
print(v2)

#해당 key가 딕셔너리 안에 있는지 조사하기 (in)
print("\n", "-" * 10, "key값 조사(in)", "-" * 10)
print("호랑이" in d1)                  #"호랑이" key가 없으므로 False
print("사과" in d1)                   #"사과" key가 있으므로 True


