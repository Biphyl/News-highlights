
class Articles:
    '''
    Articles class to define articles objects
    '''
    def __init__(self,id,author,title,description,url,image,date):
        self.id = id
        self.title = title
        self.description = description
        self._url = url
        self.image = image
        self.date = date