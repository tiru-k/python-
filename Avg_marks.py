# Average of student marks
stu_marks = [38,43,56,68,72,84,56,54,86,48]
stu_all = sum(stu_marks)
a = len(stu_marks)
stu_avg = stu_all/a
print(stu_avg)

#Take student marks dynamically and find the average of the student marks
stu_marks = []

i = 1
while i <= 6:
    print("enter marks of subjetc",i,":")
    a = int(input())
    stu_marks.append(a)
    i  += 1
stu_tot_marks = sum(stu_marks)
no_sub = len(stu_marks)
print(no_sub)
stu_avg = stu_tot_marks/no_sub
print("average marks of students:",stu_avg)

# Take number of subjects dynamically to the above requirement

stu_marks = []
stu_sub = int(input("how many subjetcs:"))
i = 1
while i <= stu_sub:
    print("enter marks of subjetc",i,":")
    a = int(input())
    stu_marks.append(a)
    i  += 1
stu_tot_marks = sum(stu_marks)
no_sub = len(stu_marks)
print(no_sub)
stu_avg = stu_tot_marks/no_sub
print("average marks of students:",stu_avg)