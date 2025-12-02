from article import Article
class Magazine:
     all_magazines = []  
     def __init__(self, name, category):
        
        self._name = None
        self._category = None

        
        self.name = name
        self.category = category

    
     @property
     def name(self):
        return self._name

     @name.setter
     def name(self, value):
        
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")

        
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters.")

        self._name = value

    
     @property
     def category(self):
        return self._category

     @category.setter
     def category(self, value):
        
        if not isinstance(value, str):
            raise TypeError("Category must be a string.")

        
        if len(value.strip()) == 0:
            raise ValueError("Category must contain at least one character.")

        self._category = value

     def articles(self):
        return [article for article in Article.all_articles if article.magazine == self]

     def contributors(self):
        return list({article.author for article in self.articles()})
    #added bonus 1
     def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None


