import webbrowser
import os

# HTML page
main_page_content = """
    {projectsContent}
"""

# The main page 
projects_content = """
    {image}
    {name}
    {link}
"""


def create_portfolio_page(projects_list):
    """ This function is called to create HTML content for projects """
    content = ""
    for project in projects_list:
        content += projects_content.format(
            image = project.image,
            name = project.name,
            link = project.link
        )
    return content
