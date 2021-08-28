#_____________Day 10____________!
#__________i/o,if-else___________!

name=str(input("Enter your Name: "))   #Must Clear data type while getting input....
print("My Name is: " , name)
total_marks=550
marks=int(input("Enter Your Marks: "))
print(marks)                               
per=marks*100/total_marks
if(per>50):
    print("Passed")                      #Space matters in Python code
else:
    print("Failed")

 