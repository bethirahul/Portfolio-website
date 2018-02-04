# Project Class with 3 variables
class Project():
    """ This is the Project Class """
    def __init__(
        self,
        name,
        image_path,
        youtube_url,
        details,
        doc_name,
        doc_url,
        src_name,
        src_url
    ):
        """ This function is called
            when an instance of the Project class is called """
        self.name        = name
        self.image_path  = image_path
        self.youtube_url = youtube_url
        self.details     = details
        self.doc_name    = doc_name
        self.doc_url     = doc_url
        self.src_name    = src_name
        self.src_url     = src_url
