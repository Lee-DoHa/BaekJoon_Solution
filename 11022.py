a = int(input())
sum = []
i1 = []
i2 = []
for i in range(0,a):
    j, k = map(int, input().split())
    i1.append(j)
    i2.append(k)
    sum.append(j+k)
i = 1
for j in sum:
    print("Case #%d: %d + %d = %d"%(i, i1[i-1], i2[i-1], j))
    i += 1