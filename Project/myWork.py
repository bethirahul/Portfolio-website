# Project Class with 3 variables
class Project():
    """ This is the Project Class """
    def __init__(
        self,
        name,
        img_path,
        vid_url,
        details,
        *link_args
    ):
        """ This function is called
            when an instance of the Project class is called """
        self.name      = name
        self.img_path  = img_path
        self.vid_url   = vid_url
        self.details   = details
        self.link_args = []
        for link_arg in link_args:
            self.link_args.append(link_arg)
