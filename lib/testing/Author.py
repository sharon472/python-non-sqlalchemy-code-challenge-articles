

class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    def articles(self):
        """Return all articles written by this author"""
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        """Return unique list of magazines this author has contributed to"""
        return list({article.magazine for article in self.articles()})





