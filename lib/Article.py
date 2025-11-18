    

class Article:
    
#__init__ a magic method
    def __init__(self, author, magazine, title):
      

        # above 50 words
        if len(title) < 5 or len(title) > 50:
            raise ValueError("title must be between 5 and 50 characters")

 

