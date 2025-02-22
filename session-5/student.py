class Marks:
    def __init__(self,marks):
        self.marks=marks

class Subject:
    def __init__(self,s_name,marks):
        self.s_name=s_name
        self.marks=marks
        

class Semester:
    def __init__(self,sem,subject):
        self.sem=sem
        self.subject=subject
        



class Student:
    def __init__(self,name,id,branch,current_sem,all_sem):
        self.name=name
        self.id=id
        self.branch=branch
        self.current_sem=current_sem
        self.all_sem=all_sem
    def display(self):
        print(f"Name: {self.name}\nId: {self.id}\nBranch: {self.branch}\n")


def get_details(id,sem,students):
    b=[]
    for student in students:

        for i in student.all_sem:
            b.append(student.all_sem)
        print(type(student.all_sem))
    print(b)
        # if(student.id==id and sem==student.all_sem):






#student 1   
s1_ds=Subject("DS",90)
s1_cn=Subject("CN",80)
s1_os=Subject("OS",70)
s1_python=Subject("python",60)
s1_cpp=Subject("cpp",100)

s1_sem1=Semester(1,[s1_cpp,s1_ds])
s1_sem2=Semester(2,[s1_python,s1_os])
s1_sem3=Semester(3,[s1_cn])

s1=Student('student1',10,'cs',3,[s1_sem1,s1_sem2,s1_sem3])

#student2
s2_ds=Subject("DS",50)
s2_cn=Subject("CN",60)
s2_os=Subject("OS",60)
s2_python=Subject("python",80)
s2_cpp=Subject("cpp",70)

s2_sem1=Semester(1,[s2_cpp,s2_ds])
s2_sem2=Semester(2,[s2_python,s2_os])

s2=Student('student2',20,'aiml',2,[s2_sem1,s2_sem2])

# s1.display()
get_details(10,2,[s1,s2])