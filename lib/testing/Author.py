
class Author:

    def __init__(self, name):# __init__ it is a magic method
        self._set_name(name)
       
        def _set_name(self, name):
             
         if len(name) == 0:
            raise ValueError("Name must not be empty.")
        
        
            self._name = name
            #importance of property
            #it is a decorator that turns a method into a read-only attribute.
#Allows you to access the name
#Prevents others from modifying the name
#Lets the class validate the data before storing it
@property

def name(self):
        return self._name

# setter and getter 
#Getter- A method that reads/returns the value of a property.

#Setter- A method that modifies/sets the value of a property



