# def create_matrix(rows: int, columns:int, data_matrix:list):
#     matrix = [[]]

n = int(input())
m = int(input())
matrix = [[input() for i in range(n)] for j in range(m)]
for i in matrix:
    print(*i)
