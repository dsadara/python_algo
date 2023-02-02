"""
PEP8의 인덴트 기준
- 기본은 공백 4개
"""

'''
첫 번째 줄에 파라미터가 있으면 파라미터가 시작되는 부분에 인덴트 맞추기
'''


def long_function_name1(var_one, var_two,
                        var_three, var_four):
    print(var_one)


hello = long_function_name1('hello1', 1, 1, 1)

'''
첫번째 줄에 파라미터가 없으면 공백 4칸 인덴트를 한 번 더 추가해서 다른 행과 구분
'''


def long_function_name2(
        var_one, var_two, var_three,
        var_four):
    print(var_one)


hello = long_function_name2('hello2', 1, 1, 1)

'''
여러 줄로 나눠쓸 경우 다음 행과 구분되도록 인덴트를 추가
'''


def long_function_name3(
        var_one, var_two,
        var_three, var_four):
    print(var_one)


hello = long_function_name3('hello3', 1, 1, 1)
