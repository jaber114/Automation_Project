# Importing configuration reader utility to fetch credentials from the config file
from utils.config import ConfigReader

# Reading the valid username and password from the config file under the 'login_info' section
username = ConfigReader.read_config("login_info", "User")
password = ConfigReader.read_config("login_info", "Password")

# A list of tuples representing different login scenarios to be used in parameterized tests
users = [
    # Test L07 - Invalid username and invalid password
    ("stamnmfsgfd", "dsadnakdssada"),

    # Test L06 - Empty username (email), valid password
    ("", password),

    # Test L05 - Valid username (email), empty password
    (username, ""),

    # Test L04 - Incorrect username (email), valid password
    ("wrong", password),

    # Test L03 - Valid username, incorrect password
    (username, "wrong"),

    # Test L02 - Valid username and valid password (happy path)
    (username, password),
]


CATEGORY_NAMES=\
[
    "Desktops",
    "Laptops & Notebooks"
    ,"Components",
    "Tablets",
    "Software",
    "Phones & PDAs",
    "Cameras",
    "MP3 Players"
]

DROP_DOWN_CATEGORIES=\
[
"Desktops",
"MP3 Players",
"Laptops & Notebooks",
"Components"
]

NON_DROP_DOWN_CATEGORIES=\
[
"Phones & PDAs",
"Cameras",
"Tablets",
"Software",
]