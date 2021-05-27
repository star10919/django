# *****************
# --- Data Type ---
# *****************
'''
Python has Five standard types
scalar
    Numbers : int, float, complex
    String : str
vector : List, Tuple, Dictionary, Set
hello = 'hello'
print(hello)
print(hello[0])
print(hello[2:5])
print(hello[2:])
'''
# List CRUD Example
ls = ['abcd', 786, 2.23, 'john', 70.2]
tinyls = [123, 'john']
# Create: ls 에 '100'을 추가 Create
ls.append(100)
print(f'Create:{ls}')
# Read: ls 의 목록을 출력
print(f'Read:{ls}')
# Update: ls와 tinyls 의 결합
print(f'Uqdate:{ls + tinyls}')
# Delete: ls 에서 786을 제거
del ls[1]
print(f'Delete:{ls}')


# Tuple CRUD Example
tp = ('abcd', 786, 2.23, 'john', 70.2)
tinytp = (123, 'john')
# Create: tp 에 '100'을 추가 Create
tp.append[100]
print(f'create:{tp}')
# Read: tp 의 목록을 출력
print(f'read:{tp}')
# Update: tp와 tinytp 의 결합
print(f'update:{tp+tinytp}')
# Delete: tp 에서 786을 제거
del tp[1]


# dictionary CRUD Example
dt = {'abcd' : 786, 'john': 70.2}
tinydt = {'홍' : '30세'}
# Create: dt 에 키값으로 'tom', 밸류로 '100'을 추가 Create
dt['tom'] = 100
# Read: dt 의 목록을 출력
print(f'Read:{dt}')
# Update: dt와 tinydt 의 결합
print(f'Update:{dt+tinydt}')
# Delete: dt 에서 'abcd' 제거
#del (f'Delete:{dt[abcd]}')