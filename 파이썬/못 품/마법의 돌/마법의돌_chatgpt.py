from itertools import product

def generate_strings(k):
    # I와 X로 이루어진 문자열 생성
    characters = ['I', 'X']
    
    # 모든 가능한 조합 생성
    combinations = product(characters, repeat=k)
    
    # 조합을 사전순으로 정렬하고 문자열로 변환
    sorted_strings = [''.join(combination) for combination in sorted(combinations)]
    
    return sorted_strings

# 예시: 3개의 문자열 생성
k = int(input('정수 입력 : '))
result = generate_strings(k)
print(result)
