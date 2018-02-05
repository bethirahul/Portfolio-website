# Project Class with 3 variables
class Project():
    """ This is the Project Class """
    def __init__(
        self,
        name,
        img_path,
        vid_url,
        details,
        num_of_links,
        links
    ):
        """ This function is called
            when an instance of the Project class is called """
        self.name     = name
        self.img_path = img_path
        self.vid_url  = vid_url
        self.details  = details
        self.doc_name = doc_name
        self.doc_url  = doc_url
        self.src_name = src_name
        self.src_url  = src_url
