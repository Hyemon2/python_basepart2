a=[1, 2, 3, 'a', 'b', ['a','b','c']] #리스트 a를 생성하고, 총 6개의 원소를 가진다.
print(a[-1]) #리스트 a의 인덱스 -1번에 해당되는 원소를 출력한다 -> [‘a’,’b’,’c’] 출력
print(a[5]) #리스트 a에서 인덱스 5번의 원소를 출력한다.  ->[‘a’,’b’,’c’] 출력
print(a[-1][1]) #리스트의 인덱스 -1번의 원소에서 인덱스 2번까지에 해당되는 원소를 출력한다.  -> b 출력
print(a[:2]) #리스트의 인덱스 0번부터 1번까지의 원소를 출력한다. -> [1,2] 출력
print(a[2:]) #리스트의 인덱스 2번부터 마지막까지의 원소를 출력한다. ->[3,’a’,’b’,[‘a’,’b’,’c’]] 출력
a=[1, 2, ['a','b',['life','is']]] #리스트 a를 생성하고, 총 3개의 원소를 가진다.
print(a[2][2][0]) #리스트의 인덱스 2번의 원소를 선택하고, 다시 그 리스트의 인덱스 2번에 해당되는 원소를 선택한 후, 인덱스 1에 해당되는 ‘life’를 출력한다.
