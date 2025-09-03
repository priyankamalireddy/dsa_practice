# word = input()
# for i in word:
#     # asci = ord(i)
#     # if asci >= 65 and asci < 91:
#     if i >= 'A' and i <= 'Z':
#         print(chr(ord(i) + 32),end="")
#     elif i >= 'a' and i <= 'z':
#         print(chr(ord(i) - 32),end="")    



# statement = input()
# count = 0
# for i in range(len(statement)-1):
#     if statement[i] == " "and statement[i+1] != " ":
#         count+=1  
#     elif statement[i] == " " and statement[i+1] == " ":
#         while statement[i] != " ":
#             i = i+1
       
    
# print(count+1)   

# s = input()
# # dict1 = {}
# # for i in s:
# #     dict1[i] = dict1.get(i,0)+1
# # for i in dict1:
# #     print(i,dict1[i],end = " ")     
# for i in s:
#     if s.count(i) > 1:
#         print(i, s.count(i), end=" ")
#         s = s.replace(i, "")  # Remove the character to avoid duplicates in output



#anagram checker

# s1 = input()
# s2 = input()
# print(len(set(s1)) == len(set(s2)))


s = input()

for i in range(len(s)):
    print(s[len(s)-1 - i],end= " ")
    
    