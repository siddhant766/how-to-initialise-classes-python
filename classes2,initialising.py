class Instructor:
    def __init__(self,name,adress,degree):
        self.Aname=name
        self.Adress=adress
        self.Degree=degree
instructor_1=Instructor("siddhant","bareilly","btech")
instructor_1.name=input("enter the name: ")
instructor_1.adress=input("enter the adress: ")
instructor_1.degree=input("enter the degree: ")
print(f"the name of the instructor is {instructor_1.name}")
print(f"the adress of the instructor is {instructor_1.adress}")
print(f"the degree of the instructor is {instructor_1.degree}")
