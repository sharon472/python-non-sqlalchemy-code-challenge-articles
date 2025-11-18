

class Magazine:
    
 def __init__(self, name, category):
        self.name = name            
        self.category = category 

        
 @property
 def name(self):
        return self._name


