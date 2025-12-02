from article import Article 
class Author:
    def __init__(self, name):
        
        self.name = name   

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        
        if hasattr(self, "_name"):
            raise AttributeError("Author name cannot be changed after instantiation.")

        
        if not isinstance(value, str):
            raise TypeError("Author name must be a string.")
        if len(value.strip()) == 0:
            raise ValueError("Author name must be at least 1 non-whitespace character.")

    
        self._name = value

    def articles(self):
        return [article for article in Article.all_articles if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})
    
    def add_article(self, magazine, title):
     return Article(self, magazine, title)

    def topic_areas(self):
        magz = self.magazines()
        if not magz:
         return None    
        return list({mag.category for mag in magz})






            #importance of property
            #it is a decorator that turns a method into a read-only attribute.
#Allows you to access the name
  #Prevents others from modifying the name
 #Lets the class validate the data before storing it


# setter and getter 
  #Getter- A method that reads/returns the value of a property.

 #Setter- A method that modifies/sets the value of a property




