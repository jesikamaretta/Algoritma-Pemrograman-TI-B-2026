#class anak diluar,yg didalam kurung kelas induk
class Person:
 def __init__(self,name, gender, age):
    self.name = name
    self.gender = gender
    self.age = age

def talking():
  pass
def walking():
  pass
def sleep():
  pass

class Student(Person):
 def __init__(self, name, gender, age):
  super().__init__(name, gender,age)
 #atrubut baru
  self.BirthYear = BirthYear

def belajar():

 
#super itu otomatis merujuk ke kelas induk kalo person itu menunjuk ke suatu kelas
 x = Student('Aqul', 'men', 20, 2005)
    print(x.name)
    print(x.BirthYear)



  