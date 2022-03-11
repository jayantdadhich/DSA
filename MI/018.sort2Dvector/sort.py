class solution:
    def diagonalsort(self, matrix, n, m):
        lower_triangle = [[] for i in range(n)]
        upper_triangle = [[] for i in range (m)]
        major_diagonal = []
        for i in range(n):
            for j in range(m):
                if j < i:
                    lower_triangle[i-j].append(matrix[i][j])
                elif i < j:
                    upper_triangle[i-j].append(matrix[i][j])
                else:
                    major_diagonal.append(matrix[i][j])
        for i in range(n):
            lower_triangle[i].sort()
            lower_triangle[i] = lower_triangle[i][::-1]
        for i in range(m):
            upper_triangle.sort()
        for i in range(0,n):
            for j in range(0,m):
                if j<i:
                    d = i - j
                    l = len(lower_triangle[d])-1
                    matrix[i][j] = lower_triangle[d][l]
                    lower_triangle[d].pop()
                elif i<j:
                    d = j-i
                    l = len(upper_triangle[d])-1
                    matrix[i][j] = upper_triangle[d][l]
                    upper_triangle[d].pop()

m = int(input("Enter number of rows"))
n = int(input("Enter number of columns"))
out = []
print("Enter elements")
for i in range(0,m):
    row = []
    for j in range(0,n):
        a = int(input(""))
        row.append(a)
    out.append(row)
print(out)
x = solution(out,m, n)
print(x)