import webbrowser
import os

# main page
main_content ='''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Rahul's Portfolio</title>
        <link rel="stylesheet" href="css/design.css" media="screen">
    </head>

    
    <body>
        <div class = "total-page">
            <main class="main-page">
                <header>
                    <figure class="my-photo">
                        <img src="img/myself.jpg" alt="My Photo">
                    </figure>
                    <h1 class="my-name dark-font">
                        RAHUL BETHI
                    </h1>
                    <p class="nick-name dark-font">
                        FLANKER
                    </p>                
                </header>
                <div class="empty-space"></div>
                <div class="seperator"></div>
                <div class="empty-space"></div>
                <figure class="cover-photo">
                    <img src="img/cover_photo.jpg" alt="Cover Photo">
                </figure>
                <h2 class="featured-heading light-font">
                    Featured Work
                </h2>
                <section class="projects">
                    {projects}
                </section>
                <h3 class="remaining-heading light-font">
                    -- Remaining --
                </h3>
                <section class="projects">
                    <article class="project">
                        <!--<figure class="project-photo">-->
                            <img
                                class="project-image"
                                src="img/github.png"
                                alt="Performance Bounceback Image">
                        <!--</figure>-->
                        <h3 class="project-name dark-font">
                            Other Projects
                        </h3>
                        <!--<details class="project-details dark-font">-->
                            <p class="project-description dark-font">
                                Some of my other projects done during my 
                                masters at Texas A&M University
                            </p>
                        <!--</details>-->
                        <p class="project-link dark-font">
                            <a
                                href="https://github.com/bethirahul?tab=repositories"
                                rel="noopener noreferrer"
                                target="_blank">
                                GitHub Repository
                            </a>
                        </p>
                    </article>
                </section>
                <div class="empty-space"></div>
                <div class="seperator"></div>
                <div class="empty-space"></div>
                <footer>
                    <h4 class="dark-font">
                        My links:
                    </h4>
                    <p class="my-links"
                        <span>
                            <a
                                href="https://github.com/bethirahul"
                                rel="noopener noreferrer"
                                target="_blank">
                                GitHub</a>
                        </span>
                        &nbsp
                        <span>
                            <a
                                href="https://www.linkedin.com/in/rahulbethi"
                                rel="noopener noreferrer"
                                target="_blank">
                                LinkedIn</a>
                        </span>
                        &nbsp
                        <span>
                            <a
                                href="https://www.facebook.com/rahulbethi"
                                rel="noopener noreferrer"
                                target="_blank">
                                Facebook
                            </a>
                        </span>
                    </p>
                </footer>
            </main>
        </div>
    </body>
</html>
'''

# project
proj = '''
<article class="project">
    {vid_or_img}
    <h3 class="project-name dark-font">
        {proj_name}
    </h3>
    <details class="project-details dark-font">
        <p class="project-description dark-font">
            {details}
        </p>
    </details>
    {links}
</article>
'''

proj_vid = '''
<a
    href="{vid_url}"
    rel="noopener noreferrer"
    target="_blank">
    {img}
</a>
'''

proj_img = '''
<img
    class="project-image"
    src="{img_path}"
    alt="{proj_name} Image">
'''

proj_link = '''
<p class="project-link dark-font">
    <a
        href="{link_url}"
        rel="noopener noreferrer"
        target="_blank">
        {link_name}
    </a>
</p>
'''


def create_and_open_website(projects):
    # adding all content
    projects_content = ''
    for project in projects:
        img_content = proj_img.format(
            img_path = project.img_path,
            proj_name = project.name
        )
        vid_or_img_content = ''
        if project.vid_url != '':
            vid_content = proj_vid.format(
                vid_url = project.vid_url,
                img = img_content
            )
            vid_or_img_content = vid_content
        else:
            vid_or_img_content = img_content
        

    content = main_content.format(
        projects = temp
    )

    # Create or overwrite the output file
    output_file = open('portfolio.html', 'w')

    # Output the file
    output_file.write(content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
