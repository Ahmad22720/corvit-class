id=[1,2,3,4]
eng=[70,80,90,60]
math=[90,90,80,80]
cump=[80,80,90,90]
for i in range(len(id)):
    total=eng[i]+math[i]+cump[i]
    average=total/3
    print(f"the id of student is: {id[i]}")
    print(f"total numbers are: {total}")
    print(f"Average is: {average}")