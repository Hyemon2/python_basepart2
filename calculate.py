def n_polygon(n, length):
    for i in range(n):
        t.forward(length)
        t.left(360//n) # 정수 나눗셈은 //으로 한다.

for i in range(18):
    t.right(20)
    n_polygon(4,100)