
class Teacher:
  def __init__(self,ID,NAME):
       self.te_id=id
       self.te_name=NAME
  
  
  def introduction (self):
    print(self.te_id)
    print(self.te_name)

te1=Teacher(1,"Shivam")
te1.introduction()

te2=Teacher(2,"Vikas")
te2.introduction()

te3=Teacher(3,"Gyan")
te3.introduction()

te4=Teacher(4,"Dileep")
te4.introduction()

te5=Teacher(5,"Ranjeet")
te5.introduction()