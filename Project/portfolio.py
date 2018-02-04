import webbrowser
import os

# HTML page
main_page_content = """
    {projectsContent}
"""

# The main page 
projects_content = """
    {youtube_url}
    {image_path}
    {name}
    {details}
    {doc_url}
    {doc_name}
    {src_url}
    {src_name}
"""


def create_portfolio_page(projects_list):
    """ This function is called to create HTML content for projects """
    content = ""
    for project in projects_list:
        if project.youtube_url == ""
        content += projects_content.format(
            youtube_url = project.youtube_url;
            image_path = project.image_path,
            name = project.name,
            details = project.details
            doc_url = project.doc_url
            doc_name = project.doc_name
            src_url = project.src_url
            src_name = project.src_name
        )
    return content
