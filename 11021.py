a = int(input())
sum = []
for i in range(0,a):
    j, k = map(int, input().split())
    sum.append(j+k)
i = 1
for j in sum:
    print("Case #%d: %d"%(i, j))
    i += 1