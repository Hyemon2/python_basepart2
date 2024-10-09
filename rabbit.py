def pascal_n(n):
    row = [1]
    for i in range(n-1):
        row = [1] + [row[j]+row[j+1] for j in range(len(row)-1)] + [1]
    return row

n = int(input("n의 값 : "))
row_n = pascal_n(n)
print(row_n)

