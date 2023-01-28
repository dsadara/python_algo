"""
파이썬의 타입 힌트 사용하기
- typing.py에 타입이 명시되어 있음
"""

'''
변수에 타입 선언하기
'''

a: str = "1"
b: int = 1

'''
타입 힌트를 사용하지 않는 함수
'''


def fn(a):
    print(a)


fn(1)

'''
매개변수와 반환값의 타입이 명시된 함수
'''


def fn2(a: int) -> bool:
    print(a)
    return False


print(fn2(1))

print(fn2('1'))  # 여전히 동적 타입이므로 문자열이 들어갈 수 있음

'''
지양해야될 사용법: 문자열에 정수 할당하기
'''

a2: str = 1
print(type(a2))

'''
타입 힌트에 오류가 있는지 확인하는 법: mypy 이용하기
pip install mypy

mypy typehint.py

실행하면 line 36과 42가 Incompatible types를 가지고 있음 
'''