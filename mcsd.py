#q-1
# name=input("enter a string:")
# print("positve  index")
# for i in range(len(name)):
#     print(name[i])

# print("negtive idx")
# for i in range(len(name)-1,-1,-1):
#      print(name[i])


#q-2  

# s = "  hello Python programming  "

# # i) len()
# print("len:", len(s))

# # ii) strip()
# print("strip:", s.strip())

# # iii) rstrip()
# print("rstrip:", s.rstrip())

# # iv) lstrip()
# print("lstrip:", s.lstrip())

# # v) find()
# print("find:", s.find("Python"))

# # vi) rfind()
# print("rfind:", s.rfind("o"))

# # vii) index()
# print("index:", s.index("Python"))

# # viii) rindex()
# print("rindex:", s.rindex("o"))

# # ix) count()
# print("count:", s.count("o"))

# # x) replace()
# print("replace:", s.replace("hello", "Hi"))

# # xi) split()
# print("split:", s.split())

# # xii) join()
# print("join:", "-".join(["Hello", "Python"]))

# xiii) upper()
# print("upper:", s.upper())

# # xiv) lower()
# print("lower:", s.lower())

# # xv) swapcase()
# print("swapcase:", s.swapcase())

# # xvi) title()
# print("title:", s.title())

# # xvii) capitalize()
# print("capitalize:", s.capitalize())

# # xviii) startswith()
# print("startswith:", s.startswith("  hello"))

# # xix) endswith()
# print("endswith:", s.endswith("  ")) 


# #q-3
# s=input("enter a string:")
# i=0
# while i<len(s):
#      print(s[i])
#      i+=1

# s=input("enter a string:")
# i=len(s)-1
# while i>=0:
#      print(s[i])
#      i=i-1

#q-4

# a = [10, 20, 30, 20, 40]

# # i) list()
# print("list:", list((1, 2, 3)))

# # ii) len()
# print("len:", len(a))

# # iii) count()
# print("count:", a.count(20))

# # iv) index()
# print("index:", a.index(30))

# # v) append()
# a.append(50)
# print("append:", a)

# # vi) insert()
# a.insert(1, 15)
# print("insert:", a)

# # vii) extend()
# a.extend([60, 70])
# print("extend:", a)

# # viii) remove()
# a.remove(20)
# print("remove:", a)

# # ix) pop()
# a.pop()
# print("pop:", a)

# # x) reverse()
# a.reverse()
# print("reverse:", a)

# # xi) sort()
# a.sort()
# print("sort:", a)

# # xii) copy()
# b = a.copy()
# print("copy:", b)

# # xiii) clear()
# b.clear()
# print("clear:", b)



# l=[1,2,3,4,5]
# l.append(6)
# print(l)

#q-5
# def remove_duplicate(a):
#     b=[]
#     for i in a :
#         if i not in b:
#             b.append(i)
#     return b

# a=[]
# n=int(input("enter no of ele:"))
# for i in range(n):
#     x=int(input("enter ele:"))
#     a.append(x)
# print("original list:",a)
# print("removed list:",remove_duplicate(a))

#q-6
# a=[]
# n=int(input("enter size of list:"))

# for i in range(n):
#     x=int(input("enter ele:"))
#     a.append(x)

# print("list:",(a))
# print("max:",max(a))

#q-7
# import random
# a=[]
# n=int(input("enter size of list:"))

# for i in range(n):
#     x=random.randint(1,100)
#     a.append(x)
# print("list:",a)

# sum=0
# for i in a:
#     sum = sum + i

# avg= sum/n
# print("sum:",sum)
# print("avg:",avg)


#q-8
# a=[10,20,30,40,50]
# x=int(input("enter a no to search:"))

# count=0

# for i in a:
#     if i==x:
#         count+=1

# if count>0:
#     print("found")
#     #print("count:",count)
# else:
#     print("not found")

#q-10

# n = int(input("Enter number of students: "))

# d = {}

# for i in range(n):
#     name = input("Enter student name: ")
#     marks = float(input("Enter percentage marks: "))
#     d[name] = marks

# print("Student Information:")
# print(d)


#q-11

# d = {}

# n = int(input("Enter number of students: "))

# for i in range(n):
#     name = input("Enter student name: ")
#     marks = int(input("Enter marks: "))
#     d[name] = marks

# x = input("Enter student name to search: ")

# if x in d:
#     print("Student marks:", d[x])
# else:
#     print("Student not found")

#  #q-12

# f = open("data.txt", "w")
# f.write("Hello Python")
# f.close()


# f = open("data.txt", "r")
# print(f.read())
# f.close()       

#q-13
# f = open("data.txt", "w")
# f.write("Hello Python")
# f.close()

# #n = int(input("Enter n: "))

# f = open("data.txt", "r")
# dat = f.read()
# f.close()

# result = dat[::-1]

# print("Result:", result)

#q-14
# f = open("data.txt", "w")
# f.write("Hello Python")
# f.close()


# f = open("data.txt", "r")
# data = f.read()
# words = data.split()

# print("Number of words:", len(words))

# f.close()

#q-15
# f = open("data.txt", "w")
# f.write("Hello Python \n efiufbfn")
# f.close()

# f = open("data.txt", "r")
# lines = f.readlines()

# print("Number of lines:", len(lines))

# f.close()

#-------------------------------------------------------------------------------------------
# post lab

#q--1
# s = input("Enter a string: ")

# if s[0].lower() in "aeiou":
#     print("String starts with a vowel")
# else:
#     print("String does not start with a vowel")


#q--2
# a = [10, 20, 30, 10]

# if a[0] == a[-1]:
#     print("First and last numbers are same")
# else:
#     print("First and last numbers are not same")

#q--3
f = open('PYTHON.txt', 'w')

description = ['we either choose the pain of discipline \n',
               'or\n',
               'the pain of regret\n']

f.writelines(description)
f.close()

f = open('PYTHON.txt', 'r')
print(f.read())
f.close()
