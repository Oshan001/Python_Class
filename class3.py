# def sum(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
# lst = []
# for i in range(1, 5):
#     b = int(input("Enter a number for the list: "))
#     lst.append(b)



"""  STUDENT DATABASE """
# def add_student(dis):
#     name = input("Enter your name: ")
#     student_class = int(input("Enter your class: "))
#     roll = int(input("Enter your roll: "))
#     dis[name] = {"name": name, "class": student_class, "roll": roll}
#     print(f"Name: {dis[name]['name']}\nClass: {dis[name]['class']}\nRoll: {dis[name]['roll']}")

# def display_students(dis):
#     if not dis:  # Check if dis is empty
#         print("No students found.")
#     else:
#         for i in dis.values():
#             print(f"Name: {i['name']}, Class: {i['class']}, Roll: {i['roll']}")

# def search_student(dis):
#     a = input("Enter the name you want to search: ")
#     if a in dis:
#         print("Found")
#         print(f"Name: {dis[a]['name']}, Class: {dis[a]['class']}, Roll: {dis[a]['roll']}")
#     else:
#         print("Not found")

# def update_student(dis):
#     name = input("Enter the name of the student to update: ")
#     if name in dis:
#         field = ["name", "class", "roll"]
#         for f in field:
#             new_value = input(f"Enter new {f}: ")
#             if f == "class" or f == "roll":
#                 dis[name][f] = int(new_value)
#             else:
#                 dis[name][f] = new_value
#         print("Student info updated successfully!")
#     else:
#         print("Student not found.")

# def delete_student(dis):
#     name = input("Enter the name of the student to delete: ")
#     if name in dis:
#         del dis[name]
#         print("Student deleted successfully!")
#     else:
#         print("Student not found.")

# dis = {}

# while True:
#     print("""1. ADD STUDENT INFO
# 2. DISPLAY ALL STUDENTS
# 3. SEARCH STUDENT
# 4. UPDATE STUDENT
# 5. DELETE STUDENT
# Any number to exit""")
    
#     c = input("Enter your option: ").strip()
    
#     match c:
#         case '1':
#             add_student(dis)
        
#         case '2':
#             display_students(dis)
        
#         case '3':
#             search_student(dis)
        
#         case '4':
#             update_student(dis)
        
#         case '5':
#             delete_student(dis)
        
#         case _:
#             break




'''RANDOM'''

# result = sum(*lst)
# print(f"The sum of the list is: {result}")


# import random import randint as r:
# print(r(1,2))


# import random  
# print(random.randint(1,2))
# import random  as r
# print(r(1,2))
# from random import randint as r
# print(r(1,2))


# '''ROCK SCISSOR GAME'''
# from random import randint as r
# list = ['ROCK', 'SCISSOR', 'PAPER']
# index = r(0, 2)
# print(list[index])
# temp=list[index]
# A=str(input("enter the choice ROCK PAPER SICISSOR"))
# user = A.upper()
# if(temp=="SCISSOR" and user =="PAPER"):
#     print("you lose")
# elif(temp=="SCISSOR" and user =="ROCK"):
#     print("you WIN")


# elif(temp=="PAPER" and user =="SICISSOR"):
#     print("you WIN")
# elif(temp=="PAPER" and user =="ROCK"):
#     print("you LOSE")


# elif(temp=="ROCK" and user =="PAPER"):
#     print("you WIN")
# elif(temp=="ROCK" and user =="PAPER"):
#     print("you LOSE")
# else :
#     print("DRAW")


#----->STUDENT DATABASE
# def add_student(dis):
#     name = input("Enter your name: ")
#     student_class = int(input("Enter your class: "))
#     roll = int(input("Enter your roll: "))
#     dis[name] = {"name": name, "class": student_class, "roll": roll}
#     print(f"Name: {dis[name]['name']}\nClass: {dis[name]['class']}\nRoll: {dis[name]['roll']}")

# def display_students(dis):
#     if not dis:  # Check if dis is empty
#         print("No students found.")
#     else:
#         for i in dis.values():
#             print(f"Name: {i['name']}, Class: {i['class']}, Roll: {i['roll']}")

# def search_student(dis):
    #   a = input("Enter the name you want to search: ")
   
    #   if a in dis:
    #     print("Found")
    #     print(f"Name: {dis[a]['name']}, Class: {dis[a]['class']}, Roll: {dis[a]['roll']}")
    # else:
    #     print("Not found")

# def update_student(dis):
#     name = input("Enter the name of the student to update: ")
#     if name in dis:
#         field = ["name", "class", "roll"]
#         for f in field:
#             new_value = input(f"Enter new {f}: ")
#             if f == "class" or f == "roll":
#                 dis[name][f] = int(new_value)
#             else:
#                 dis[name][f] = new_value
#         print("Student info updated successfully!")
#     else:
#         print("Student not found.")

# def delete_student(dis):
#     name = input("Enter the name of the student to delete: ")
#     if name in dis:
#         del dis[name]
#         print("Student deleted successfully!")
#     else:
#         print("Student not found.")

# dis = {}
# while True:
#     print("""1. ADD STUDENT INFO
# 2. DISPLAY ALL STUDENTS
# 3. SEARCH STUDENT
# 4. UPDATE STUDENT
# 5. DELETE STUDENT
# Any number to exit""")
    
#     c = input("Enter your option: ")
    
#     match c:
#         case '1':
#             add_student(dis)
        
#         case '2':
#             display_students(dis)
        
#         case '3':
#             search_student(dis)
        
#         case '4':
#             update_student(dis)
        
#         case '5':
#             delete_student(dis)
        
#         case _:
#             break








# #try and except to overcome crash on program or to overcome

# try:
#     num1=int(input("Enter the first number:"))
#     num2=int(input("Enter the second number:"))
#     result=num1/num2
#     print("Result:",result)
# except ValueError:
#     print("Invalid input. Please enter number only.")
# except ZeroDivisionError:
#     print("cannot divide by zero.")
# except Exception as e:
#     print(e)


