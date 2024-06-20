# 중복 순열 
# 중복 허용, 순서가 다르면 다른 경우의 수

# 4장의 카드 중에서 3장 뽑기 
card = ['A', 'B', 'C', 'D']
path = [0]*3

def dfs(level):
		# 3장 모두 뽑았으면 출력하고 리턴
    if level == 3:
        print(*path)
        return
    for i in range(4):
        path[level] = card[i]  # 카드 뽑고
        dfs(level+1)  # 다음 카드 뽑으러 가기
        path[level] = 0  # 리턴 이후 뽑은 카드 초기화

dfs(0)