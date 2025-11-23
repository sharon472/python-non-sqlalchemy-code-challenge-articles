from author import Author
from magazine import Magazine

class Article:
    def __init__(self, author, magazine, title):
    
        if not isinstance(author, Author):
            raise TypeError("author must be an Author instance")
        
        
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be a Magazine instance")

        
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("title must be between 5 and 50 characters")
        
        self._title = title            
        self.author = author           
        self.magazine = magazine       


    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # This BLOCKS changes after creation
        if hasattr(self, "_title"):
            raise AttributeError("Cannot modify title after creation")
        self._title = value


    
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("author must be an Author instance")
        self._author = value


    
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("magazine must be a Magazine instance")
        self._magazine = value



