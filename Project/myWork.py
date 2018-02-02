# Project Class with 3 variables
class Project():
    """ This is the Project Class """
    def __init__(self,name,image_path,link):
        """ This function is called
            when an instance of the Project class is called """
        self.name       = name
        self.image_path = image_path
        self.link       = link
