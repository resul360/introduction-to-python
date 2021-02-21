# homework2
# Global Ai HUB homework2 18/02/2021
# import random
# # num_of_student=int(input("how many student in the class? :  "))
             
midterm_list=[40,30,60,90,70]

final_list=[50,60,80,30,90]

homework_list=[60,80,90,20,80]

student_name=["Yaşar pala", "Yusuf küçük","Ahsen yılmaz","Bahar çetin","Efecan şavaş"]
num_of_student=len(midterm_list)
Dict1={}     

for i in range(num_of_student):
    avg_note=(midterm_list[i]+final_list[i]+homework_list[i])/3
    Dict1[student_name[i]]=avg_note

print(Dict1)