class Author:
    def __init__(self, name):
        # call the setter once via attribute assignment
        self.name = name   # goes through our setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # If _name already exists, we forbid changing it (use hasattr)
        if hasattr(self, "_name"):
            raise AttributeError("Author name cannot be changed after instantiation.")

        # Validate the incoming value
        if not isinstance(value, str):
            raise TypeError("Author name must be a string.")
        if len(value.strip()) == 0:
            raise ValueError("Author name must be at least 1 non-whitespace character.")

        # If valid and this is first assignment, set private attr
        self._name = value





            #importance of property
            #it is a decorator that turns a method into a read-only attribute.
#Allows you to access the name
#Prevents others from modifying the name
#Lets the class validate the data before storing it


# setter and getter 
#Getter- A method that reads/returns the value of a property.

#Setter- A method that modifies/sets the value of a property



