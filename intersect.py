'''
Define an intersect method that returns a new intSet containing elements that appear in both sets. In other words,

s1.intersect(s2)
would return a new intSet of integers that appear in both s1 and s2. Think carefully - what should happen if s1 and s2 have no elements in common?

'''




class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []
        #self.temp = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self,other):
        #for i in range(len(other)):
            #if other[i] in self.vals:
                #self.temp.append(e)
        # self.vals = self.temp
        newset = intSet() #new set
        for i in self.vals: 
            if other.member(i): #check if each member is in other
                       # return i in self.vals --> i in other
                newset.insert(i)
        return newset
               
       
    
    def __len__(self):
        #
        return len(self.vals) #use len()