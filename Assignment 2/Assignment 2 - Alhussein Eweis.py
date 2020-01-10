#Student Name: Alhussein Eweis
class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a MyTime object initialized to hrs, mins, secs """

            
        totalsecs = hrs*3600 + mins*60 + secs
        if totalsecs < 0:
            totalsecs=0
            print("Note: because the resulted time is negative, time can not be less than zero. The resulted time is now set to zero:")
          
        self.hours = totalsecs // 3600        # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60
        
    #question 3,4 & 5 done
        
    def __str__(self):
        return  "{0}:{1}:{2}".format(self.hours, self.minutes, self.seconds)

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        return MyTime(0, 0, self.to_seconds() - other.to_seconds())

    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()

    def __le__(self, other):
        return self.to_seconds() <= other.to_seconds()

    def __ge__(self, other):
        return self.to_seconds() >= other.to_seconds()

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()

    def __ne__(self, other):
        return self.to_seconds() != other.to_seconds()

    def increment(self, secs):
        self.to_seconds()
        return MyTime(0,0,self.to_seconds()+secs)

    def to_seconds(self):
        """ Return the number of seconds represented
            by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > time2.to_seconds()


    def between(self, t1,t2):
        if t1<=self and self<t2:
            return True
        else:
            return False

        
def add_time(t1, t2):
    h = t1.hours + t2.hours
    m = t1.minutes + t2.minutes
    s = t1.seconds + t2.seconds
       
    sum_t = MyTime(13, 62, 90)
    return sum_t

def add_time2(t1, t2):
    secs = t1.to_seconds() + t2.to_seconds()
    return MyTime(0, 0, secs)

def increment(t, secs):
    t.seconds += secs
    while t.seconds >= 60:
        t.seconds -= 60
        t.minutes += 1

    while t.minutes >= 60:
        t.minutes -= 60
        t.hours += 1



# we have two times here    
X = MyTime(1,2,3)       #Time 1
Y = MyTime(3,4,5)       #Time 2
R= MyTime(2,3,4)
X.increment(1000)
r=R.between(X,Y)
print(r)
Z = Y - X


print(Z)


#Student Name: Alhussein Eweis
