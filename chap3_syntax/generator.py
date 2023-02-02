"""
제네레이터(Generator)
루프의 반복 동작을 제어할 수 있는 루틴 형태
"""

'''
yield: 제네레이터가 여기까지 실행 중이던 값을 내보낸다는 의미
중간값을 리턴한 다음 함수는 종료되지 않고 계속해서 맨 끝에 도달할 때까지 실행됨
'''

# 종료 조건이 없어서 계속 값을 내보내는 함수
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

# 함수의 리턴값은 제네레이터가 됨
get_natural_number()

# 다음 값을 생성하려면 next()를 이용하면 됨
g = get_natural_number()
for _ in range(0, 100):     # 100 개의 값을 생성
    print(next(g))

# 여러 타입의 값을 하나의 함수에서 생성할 수도 있음
def generator():
    yield 1
    yield 'string'
    yield True

g = generator()

g

next(g) # 1

next(g) # 'string'

next(g) # True

