#Name: Alhussein Eweis

class Appointment:
   
    def __init__(self, Day, Month, Year, Desc ):
        self.day=Day
        self.month=Month
        self.year=Year
        self.desc=Desc
       
    def printname(self):
        return(self.day, self.month, self.year, self.desc)
    def __str__(self):
        return "Date: {} - {} - {} - Appointment Reason: {}".format(self.day, self.month, self.year, self.desc)
 
   
class Day(Appointment):
    def __init__(self, Day):
        self.day = Day
 
    def occurson(self,Day):
        if self.day == Day:
            return True
        else:
            return False
       
class Month(Appointment):
    def __init__(self,Month):
        self.month = Month
 
    def occurson(self,Month):
        if self.month==Month:
            return True
        else:
            return False
        
class Date(Appointment):
    def __init__(self, Day, Month, Year):
        super().__init__(Day, Month, Year, "")
       
    def occurson(self, Day, Month,Year):
        if self.day==Day and self.month==Month and self.year==Year:
            return True
        else:
            return False
   
#Creating a list of Appointments
appt1=Appointment(15,2,2019,"Root")
appt2=Appointment(14,7,2018,"Clean")
appt3=Appointment(13,12,2017,"Tooth Removal")

appt_list = [appt1, appt2, appt3]

#User input
appt_search=input("Please enter date to check, Format example: Year Month Day: ")
appt_exact=input("Would you like to check appointments on this Day, Month, or Date: ")

#Splits user input into day, month, year
date_split = appt_search.split()

year = int(date_split[0])
month = int(date_split[1])
day = int(date_split[2])


 
#what will be printed
answer = []


if appt_exact == "Day" or "day":
    for appt in appt_list:
        if Day(day).occurson(appt.day):
            answer.append(appt)
            
        
elif appt_exact == "Month" or "month":
    for appt in appt_list:
        if Month(appt.month).occurson(month):
            answer.append(appt)

elif appt_exact == "Date" or "date":
    for appt in appt_list:
        if Date(appt).occurson(day, month, year):
            answer.append(appt)
else:
    print("This was not an option")

for i in range(len(answer)):
    print(answer[i])

#Name: Alhussein Eweis
