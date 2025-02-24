
CREATE TABLE Semester (
Sem_Id  INT PRIMARY KEY ,
Sem SMALLINT 
    
);

CREATE TABLE Student (
    Student_Id  BIGSERIAL PRIMARY key ,
    Usn varchar UNIQUE,
    Name varchar,
    Branch varchar,
    Current_sem smallint
    
    );

CREATE TABLE Subject(
Sub_Id BIGINT PRIMARY KEY,
sub_name VARCHAR
);

CREATE TABLE Marks(
Student_Id BIGINT,
Sub_Id BIGINT,
Marks FLOAT,
Sem_Id INT,
FOREIGN KEY (Student_Id) REFERENCES Student(Student_Id),
FOREIGN KEY (Sub_Id) REFERENCES Subject(Sub_Id),
FOREIGN KEY (Sem_Id) REFERENCES Semester(Sem_Id)


);
  

-- Get all distinct sem of student
select  DISTINCT current_sem  
from student;

-- list all student belonging to sem 1
select name 
from student 
where current_sem='1';


-- get all marks of a student given usn for a particular subject
select student.usn ,student.name,subject.sub_name ,marks.marks 
from student ,marks ,subject 
where student.student_id=marks.student_id 
and marks.sub_id=subject.sub_id 
and student.usn='vv003' 
and subject.sub_name='DS';


-- get all marks of a student given usn for the latest seem
select student.name,marks.marks,semester.sem as latest_sem
 from student,marks ,semester 
 where student.student_id=marks.student_id 
 and semester.sem_id=marks.sem_id 
 and semester.sem=student.current_sem ;



-- get all marks of a student given usn for the latest seem
select student.name,marks.marks,semester.sem as latest_sem
 from student,marks ,semester 
 where student.student_id=marks.student_id 
 and semester.sem_id=marks.sem_id 
 and semester.sem=student.current_sem  and student.usn ='vv003';

-- get the aggregarate or percentange of marks for a student in a sem
select student.name ,AVG (marks.marks)
 from student,marks ,semester 
 where student.student_id=marks.student_id 
 and semester.sem_id=marks.sem_id 
 and student.usn ='vv003' AND marks.sem_id = 1 
 GROUP BY student.name;



-- get total percentage of student of all sem

select marks.student_id ,AVG (marks.marks)
 from student,marks ,semester 
 where student.student_id=marks.student_id 
 and semester.sem_id=marks.sem_id  
 GROUP BY marks.student_id;


