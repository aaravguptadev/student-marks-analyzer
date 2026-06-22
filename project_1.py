print("enter your marks")
maths = int(input("Enter your marks of Maths",))
science = int(input("Enter your marks of Science",))
SST = int(input("Enter your marks of SST",))
English = int(input("Enter your marks of English",))
AI = int(input("Enter your marks of AI",))
Hindi = int(input("Enter your marks of Hindi",))
n = maths + science + SST + English + AI + Hindi
percent = n /600*100
if percent >= 90 :
    grade = "A"
elif percent >= 70 :
    grade = "B"
elif percent >= 50 :
    grade = "c"
else :
    grade = "Fail"
print("Total Marks :", n )
print("Percentage : :", percent)
print("grade :",grade )




