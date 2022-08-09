import sys
input = sys.stdin.readline

n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_lst = sorted([(i, a_) for i, a_ in enumerate(a)], key=lambda x:x[-1], reverse=True)
b_lst = sorted([(i, b_) for i, b_ in enumerate(b)], key=lambda x:x[-1], reverse=True)
c_lst = sorted([(i, a_+b_) for i, (a_, b_) in enumerate(zip(a,b))], key=lambda x:x[-1], reverse=True)

passed = []
# math
for i in range(x): passed.append(a_lst[i][0])

# english
cnt = 0
for num, score in b_lst:
    if cnt==y: break
    if not num in passed:
        passed.append(num)
        cnt+=1

# math + english
cnt = 0
for num, score in c_lst:
    if cnt==z: break
    if not num in passed:
        passed.append(num)
        cnt+=1

passed.sort()
for i in passed: print(i+1)


