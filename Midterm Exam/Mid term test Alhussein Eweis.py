#Name: Alhussein Eweis
class Student:
    
    def __init__(self, ID, lastName, creditsEarned=0, courseLoadCredits=0, status=1):
        self.Id=ID
        self.lastName=lastName
        self.creditsEarned=creditsEarned
        self.courseLoadCredits=courseLoadCredits
        self.status=status

        if type(self) is not Graduate_Student:
            if self.creditsEarned<29:
                self.status=1
            elif self.creditsEarned<=60 and self.creditsEarned>=30:
                self.status=2
            elif self.creditsEarned<=90 and self.creditsEarned>=60:
                self.status=3
            elif self.creditsEarned<=120 and self.creditsEarned>=90:
                self.status=4


#Id Error Tackling
        if ID.isnumeric()==False:
            print("Value Error: IDs have to be numeric only, please go and change the ID in the following record:")

    
    def __str__(self):
        return "ID: {}, Last Name: {}, Credits Earned:{}, Semester Course Load Credits:{}, Status:{}".format(self.Id, self.lastName, self.creditsEarned, self.courseLoadCredits, self.status)

#Operations
    def __gt__(self, other):
        return self.creditsEarned() > other.creditsEarned()
    def __lt__(self, other):
        return self.creditsEarned() < other.creditsEarned()
    def __ge__(self, other):
        return self.creditsEarned() >= other.creditsEarned()
    def __le__(self, other):
        return self.creditsEarned() <= other.creditsEarned()



    def registerCourse(self, Credits):
        self.credits=Credits
        
        if (self.credits=="one") or (self.credits=="One") or (self.credits==1):
            self.credits=1
        elif (self.credits=="three") or (self.credits=="Three") or (self.credits==3):
            self.credits=3
        elif (self.credits=="four") or (self.credits=="Four") or (self.credits==4):
            self.credits=4
        elif (self.credits=="Six") or (self.credits=="six") or (self.credits==6):
            self.credits=6
        elif (self.credits=="Nine") or (self.credits=="nine") or (self.credits==9):
            self.credits=9
        elif (self.credits=="Twelve") or (self.credits=="twelve") or (self.credits==12):
            self.credits=12
        elif (self.credits=="Fifteen") or (self.credits=="fifteen") or (self.credits==15):
            self.credits=15
        elif (self.credits=="Eighteen") or (self.credits=="eighteen") or (self.credits==18):
            self.credits=18
        else:
            print("That is not an option,will be reverted to the previous setting(s)                         credit options: 1,3,4,6,9,12,15,18")
            return

        self.courseLoadCredits=self.courseLoadCredits + self.credits
            
        #Error Tackling
        if self.credits<0:
            print("The number of credits can not be less than 0 (zero):")
            return
        if self.courseLoadCredits >18:
            print("The number of credits can not be greater than 18, Note: Maximum: 18 Credits/Semester for undergraduate students")


    def withdraw(self, withdraw_amount):

        self.withdraw_amount=withdraw_amount

        
        if (self.withdraw_amount == "One") or (self.withdraw_amount=="one") or (self.withdraw_amount==1):
            self.withdraw_amount = 1
        elif (self.withdraw_amount == "Three") or (self.withdraw_amount=="three") or (self.withdraw_amount==3):
            self.withdraw_amount = 3
        elif (self.withdraw_amount == "Four") or (self.withdraw_amount=="four") or (self.withdraw_amount==4):
            self.withdraw_amount = 4
        elif (self.withdraw_amount == "Six") or (self.withdraw_amount=="six") or (self.withdraw_amount==6):
            self.withdraw_amount = 6
        elif (self.withdraw_amount == "Nine") or (self.withdraw_amount=="nine") or (self.withdraw_amount==9):
            self.withdraw_amount = 9
        elif (self.withdraw_amount == "Twelve") or (self.withdraw_amount=="twelve") or (self.withdraw_amount==12):
            self.withdraw_amount = 12
        elif (self.withdraw_amount == "Fifteen") or (self.withdraw_amount=="fifteen") or (self.withdraw_amount==15):
            self.withdraw_amount = 15
        elif (self.withdraw_amount == "Eighteen") or (self.withdraw_amount=="eighteen") or (self.withdraw_amount==18):
            self.withdraw_amount = 18
        else:
            print("That is not an option, will be reverted to the previous setting(s):              credit options: 1,3,4,6,9,12,15,18")
            return

        if self.withdraw_amount<0:
            print("The number of credits to be withdrawn can not be less than 0 (zero):")
            return
        
        self.courseLoadCredits = self.courseLoadCredits - self.withdraw_amount

        if self.courseLoadCredits<0:
            print("The number of credits can not be less than 0 (zero)")
            self.courseLoadCredits = self.withdraw_amount + self.courseLoadCredits
        elif self.courseLoadCredits==0:
            pass
            
      
    def passedCourse(self,Credits):
#####
        self.credits=Credits

        if (self.credits=="one") or (self.credits=="One") or (self.credits==1):
            self.credits=1
        elif (self.credits=="three") or (self.credits=="Three") or (self.credits==3):
            self.credits=3
        elif (self.credits=="four") or (self.credits=="Four") or (self.credits==4):
            self.credits=4
        elif (self.credits=="Six") or (self.credits=="six") or (self.credits==6):
            self.credits=6
        elif (self.credits=="Nine") or (self.credits=="nine") or (self.credits==9):
            self.credits=9
        elif (self.credits=="Twelve") or (self.credits=="twelve") or (self.credits==12):
            self.credits=12
        elif (self.credits=="Fifteen") or (self.credits=="fifteen") or (self.credits==15):
            self.credits=15    
        elif (self.credits=="Eighteen") or (self.credits=="eighteen") or (self.credits==18):
            self.credits=18
            if type(self) is Graduate_Student:
                print("For graduate students, your maximum is 15")
                return
        else:
            print("That is not an option,will be reverted to the previous setting(s)                         credit options: 1,3,4,6,9,12,15,18")
            return
#####        
        self.creditsEarned = self.creditsEarned + self.credits
        self.courseLoadCredits = self.courseLoadCredits - self.credits

        if self.courseLoadCredits<0:
            print("you can not pass more courses than what you took during the semester")
            return


        #status code
        if type(self) is not Graduate_Student:
            if self.creditsEarned<29:
                self.status=1
            elif self.creditsEarned<=60 and self.creditsEarned>=30:
                self.status=2
            elif self.creditsEarned<=90 and self.creditsEarned>=60:
                self.status=3
            elif self.creditsEarned<=120 and self.creditsEarned>=90:
                self.status=4
        

    def createEmail(self):
        return "Student's Email: " + self.lastName + self.Id + "@rutgers.edu"



class Graduate_Student(Student):
    def __init__(self, ID, lastName, creditsEarned=0, courseLoadCredits=0, status=5):
        super().__init__( ID, lastName, creditsEarned, courseLoadCredits, status=5)

            
    def registerCourse(self, Credits):
        self.credits=Credits
        
        if (self.credits=="one") or (self.credits=="One") or (self.credits==1):
            self.credits=1
        elif (self.credits=="three") or (self.credits=="Three") or (self.credits==3):
            self.credits=3
        elif (self.credits=="four") or (self.credits=="Four") or (self.credits==4):
            self.credits=4
        elif (self.credits=="Six") or (self.credits=="six") or (self.credits==6):
            self.credits=6
        elif (self.credits=="Nine") or (self.credits=="nine") or (self.credits==9):
            self.credits=9
        elif (self.credits=="Twelve") or (self.credits=="twelve") or (self.credits==12):
            self.credits=12
        elif (self.credits=="Fifteen") or (self.credits=="fifteen") or (self.credits==15):
            self.credits=15

        else:
            print("That is not an option,will be reverted to the previous setting(s)                         credit options: 1,3,4,6,9,12,15,18")
            return

        self.courseLoadCredits=self.courseLoadCredits + self.credits
            
        #Error Tackling
        if self.credits<0:
            print("The number of credits can not be less than 0 (zero):")
            return
        if self.courseLoadCredits >15:
            print("The number of credits can not be greater than 15, Note: Maximum: 15 Credits/Semester for graduate students")






undergraduate_student1=Student('1','Jerry Harry',0,15,1)
print(undergraduate_student1)

undergraduate_student1.passedCourse(3)
print(undergraduate_student1)

undergraduate_student1.withdraw(6)
print(undergraduate_student1)

undergraduate_student2=Student('2','Emily',30,15,2)
print(undergraduate_student2)

print(undergraduate_student2.createEmail())


undergraduate_student3=Student('3','Kate',73,15)
print(undergraduate_student3)

undergraduate_student3.registerCourse(3)
print(undergraduate_student3)
undergraduate_student3.passedCourse(18)
print(undergraduate_student3)


graduate_student1=Graduate_Student("4","Muller")
print(graduate_student1)

graduate_student2=Graduate_Student("5","Tom",6,6,5)

print(graduate_student2)
graduate_student2.registerCourse(9)
print(graduate_student2)
graduate_student2.passedCourse(4)
print(graduate_student2)



#Name: Alhussein Eweis

