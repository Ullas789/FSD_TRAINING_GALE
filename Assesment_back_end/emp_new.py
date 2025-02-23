
# contact_details belongs to an employee

d={}
def dict(contact,person):
    for key in d:
        if(key==contact.number):
            print("Validation Err")
            return
        
    d.update({contact.number:person.name})
    print(d)
   

    
class Contact:
   
   def __init__(self,employee_details,number,address):
       self.number=number
       self.address=address
       self.employee_details=employee_details
   def display(self):
        print(f"\nName:{self.employee_details.name}\nId:{self.employee_details.identifier} \nEmail:{self.employee_details.email}\nDesignation:{self.employee_details.designation} \ncontact:{self.number} \nAddress:{self.address}")
     

class Person:
    def __init__(self,name,identifier,email):
        self.name=name
        self.identifier=identifier
        self.email=email
       


class Employee(Person):

    def __init__(self,name,identifier,email,designation,salary):
        super().__init__(name,identifier,email)
        self.designation=designation
        self.salary=salary
    def display(self):
        print(f"\nName:{self.name}\nId:{self.identifier} \nEmail:{self.email}\nDesignation:{self.designation} \ncontact:{self.contact_detail.number} \nAddress:{self.contact_detail.address}")
     


def get_details(contact,contacts):
    
    for cont in contacts:
       
        if contact==cont.number:
            print(cont.display())
   
def get_contact(id,contacts):
    for contact in contacts:
        if contact.employee_details.identifier==id:
            print(contact.number)
    




p1 = Person('p1', 100, 'p1.email')
e1=Employee(p1.name,p1.identifier,p1.email,'jnr',10000) 
c1 = Contact(e1,1111111111, 'abc')
c11=Contact(e1,121,'cdc')


p2 = Person('p2', 200, 'email')
e2=Employee(p2.name,p2.identifier,p2.email,'snr',20000)
c2 = Contact(e2,2222222222, 'abc')


p3 = Person('p3', 300, 'email')
e3=Employee(p3.name,p3.identifier,p3.email,'Tc',30000)
c3 = Contact(e3,3333333333, 'abc')


p4 = Person('p4', 400, 'email')
e4=Employee(p4.name,p4.identifier,p4.email,'snr',40000) 
c4 = Contact(e4,1111111111, 'abc')

dict(c1,p1) 
dict(c11,p1)
dict(c2,p2)
dict(c3,p3) 
dict(c4,p4)
    


get_details(c2.number,[c1,c11,c2,c3,c4])  #get details by giving number
get_contact(p1.identifier,[c1,c11,c2,c3,c4])  # get contacts by giving Emp_id