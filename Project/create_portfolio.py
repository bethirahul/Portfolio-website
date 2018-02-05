import myWork # for Project class
import portfolio # to create adn open website

# Here, all the projects are created by calling the
# 'Project' class from projects.py
rubeGoldberg = myWork.Project(
    "Rube Goldberg VR (game)",
    "img/Rube_Goldberg_y.png",
    "https://www.youtube.com/watch?v=PX3j331hXHQ",
    """ A Virtual Reality (VR) puzzle game (Oculus Rift) where the player has 
        to through a ball to the goal by guiding through different objects 
        placed appropriately.""",
    "Medium blog-post",
    "https://medium.com/@rahulbethi/rube-goldberg-game-in-vr-rahul-bethi-59c82583eef1",
    "Source (GitHub)",
    "https://github.com/bethirahul/Rube-Goldberg-Game",
    "Build (Google drive)",
    "https://goo.gl/M5DZ7m"
)
performanceBounceback = myWork.Project(
    "Performance Bounceback VR (game)",
    "img/pb.png",
    None,
    """ A VR puzzle game compatible with Oculus Rift. Throw the ball on 
        trampolines to score within 1 minute.""",
    "Source & Build (GitHub)",
    "https://github.com/bethirahul/Performance-Bounceback"
)
museum = myWork.Project(
    "VR in Health-care (Museum)",
    "img/museum_y.png",
    "https://youtu.be/TeMLeJ3sD0c?t=1s",
    """ A VR android app which takes to a virtual library environment with 
        stations to watch videos about how VR is influencing healthcare.""",
    "Medium blog-post",
    "https://medium.com/@rahulbethi/vr-museum-healthcare-a2527c214e4b",
    "Source & APK (Google drive)",
    "https://goo.gl/tGQnpj"
)
puzzler = myWork.Project(
    "Puzzler VR (game)",
    "img/puzzler_y.png",
    "https://youtu.be/Xf43ULgdhEo",
    """ A simple VR android game where a sequence of code is shown and is to 
        reproduced again.""",
    "Medium blog-post",
    "https://medium.com/@rahulbethi/rahuls-puzzler-game-e1f402fc8118",
    "Source & APK (GitHub)",
    "https://github.com/bethirahul/Puzzler-game"
)
kinect = myWork.Project(
    "Kinect-Unity game (Masters project)",
    "img/kinect.png",
    None,
    """ A 2.5D scroller game built for children with intellectual ability 
        using Microsoft Kinect device. Children have to jump their way 
        through obstacles to reach the goal.""",
    "Source & Build (GitHub)",
    "https://github.com/bethirahul/Kinect-game-for-Children-with-Intellectual-Dissability"
)
aiga = myWork.Project(
    "Game Programming Portfolio (AIGA)",
    "img/dave.png",
    None,
    """ My game programming portfolio during my Game programming diploma 
        at Asian Institute of Gaming and Animation, Bengaluru (2015).""",
    "GitHub link",
    "https://github.com/bethirahul/Game-Programming-Portfolio-2015"
)

projects = [
    rubeGoldberg,
    performanceBounceback,
    museum,
    puzzler,
    kinect,
    aiga
]

# create and open website
portfolio.create_and_open_website(projects)
