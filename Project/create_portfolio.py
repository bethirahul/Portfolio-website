import myWork # for Project class
import portfolio # to create adn open website

# Here, all the projects are created by calling the
# 'Project' class from projects.py
rubeGoldberg = myWork.Project(
    "Rube Goldberg in VR",
    "images/Rube-Goldberg.png",
    "https://www.youtube.com/watch?v=PX3j331hXHQ",
    """ A Virtual Reality (VR) puzzle game (Oculus Rift) where the player has 
        to through a ball to the goal by guiding through different objects 
        placed appropriately.""",
    "Medium blog-post",
    "https://medium.com/@rahulbethi/rube-goldberg-game-in-vr-rahul-bethi-59c82583eef1",
    "GitHub link",
    "https://github.com/bethirahul/Rube-Goldberg-Game"
)

projects_list = [
    rubeGoldberg
]

# create and open website
portfolio.create_and_open_website()
