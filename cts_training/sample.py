# n = int(input())
# if n%9 == 0:
#     print(9)
# else:
#     print(n%9)    

# import math
# n = 100
# n1 = int(math.sqrt(n))
# sq = n1**2
# cb = int((n-1) ** (1/3))
# cb = cb ** 3
# print(sq + cb)


# tasks = list(map(int,input().split()))
# tasks = sorted(tasks)
# l,r = 0,len(tasks)-1
# max_d = 0
# while l<=r:
#     res = tasks[l] + tasks[r]
#     if res > max_d:
#         max_d = res
#     l+=1
#     r-=1
# print(max_d)        


# n = int(input())
# max_weight = int(input())
# weights = list(map(int,input().split()))
# weights = sorted(weights)

# for i in range(len(weights)):
#     # print(max_weight)
#     max_weight-= weights[i]
#     # print(max_weight)
#     if max_weight < 0:
#         break
# print(i)    


# n = int(input())
# a = list(map(int,input().split()))
# total = 0
# for i in range(len(a)):
#     if i%2 == 0:
#         total+= a[i] ** 2
#     else:
#         total-= a[i] ** 2

# print(total)      
     
    
n = int(input())
ids = list(map(int,input().split()))
e_count, o_count = 0,0
for i in ids:
    if i%2 == 0:
        e_count+=1
    else:
        o_count+=1
print(min(e_count,o_count))        
