"""
리스트 컴프리헨션이란?
기존 리스트를 기반으로 새로운 리스트를 만들어내는 구문
"""

'''
파이썬은 map, filter와 같은 함수형 기능을 지원하고
Lambda Expression도 지원함
'''
list(map(lambda x: x + 10, [1, 2, 3]))

list(filter(lambda x: x == 10, [1, 2, 10]))

'''
리스트 컴프리헨션
map과 filter 대신에 리스트 컴프리헨션을 쓰는 것이 좋음 (from Effective Python)
가독성이 훨씬 높다
'''
# 짝수인 경우 2를 곱해 출력하는 예제
[n * 2 for n in range(1, 10 + 1) if n % 2 == 1]

# 리스트 컴프리헨션을 사용하지 않는 경우
a = []
for n in range(1, 10 + 1):
    if n % 2 == 1:
        a.append(n * 2)

a

'''
딕셔너리 컴프리헨션
'''

original = {1: 1, 2: 1, 3: 3}

# 원래 딕셔너리 매핑
a = {}
for key, value in original.items():
    a[key] = value

a

# 컴프리헨션을 이용한 매핑
{key: value for key, value in original.items()}
