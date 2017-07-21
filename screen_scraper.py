"""Grabs information about Apache open source projects for DB"""
from __future__ import print_function
import time
import ast
import httplib2
from selenium import webdriver

class Projects(object):
    """Projects is a dictionary mapping project name to a JSON dict containg
    info about it"""
    def __init__(self):
        self.projects = {}

    def get(self, name):
        """Returns a new project with the given name"""
        try:
            return self.projects[name]
        except KeyError:
            print("No project called %s was found" %name)

    def add(self, name, project):
        """Adds a project result"""
        self.projects[name] = project

def parse_inception(date):
    """Parses the date from a string containing it + other info"""
    start = 0
    while date[start] != "(":
        start += 1
    end = start
    while date[end] != ")":
        end += 1
    date = date[start+1:end].encode('utf-8')
    date = date.split("-")
    return {"day":int(date[2]), "year":int(date[0]), "month":int(date[1])}

def get_inception(driver):
    """Gets the inception date from a project"""
    try:
        # Get the line containing the last date
        xpath = "//*[@id='contents']/ul[contains(., 'Download')]/li[last()]"
        date = driver.find_element_by_xpath(xpath)
        return parse_inception(date.text)
    except:
        return "N/A"

def get_description(driver, name):
    """Gets the description dict for a project"""
    try:
        # Get the url for the JSON DOAP
        xpath = "//*[@id='contents']/ul[1]/li[contains(., 'Project data file')]/a[2]"
        json = driver.find_element_by_xpath(xpath)
        # Go to the JSON page
        driver.get(json.get_attribute("href"))
        # Add the JSON to the Project info
        json_content = driver.find_element_by_xpath('/html/body/pre').text
        # Convert the JSON string to a dictionary
        description = ast.literal_eval(json_content)
        print("Adding JSON for " + name)
    except:
        description = {}
        print("Unable to scrape JSON for " + name)
    return description

def apache_projects():
    """Scrapes apache project page for info on projects"""
    # path to where I have chrome driver installed
    path_to_chromedriver = '/usr/local/bin/chromedriver'
    # initialize the driver
    driver = webdriver.Chrome(executable_path=path_to_chromedriver)
    # go to the apache projects page
    driver.get('https://projects.apache.org/projects.html')
    # wait for the list of projects to load
    time.sleep(2)

    # get the HTML element with id list
    elem = driver.find_element_by_id('list')
    project_list = elem.text.split("\n")
    # initialize an instance of Projects
    projects = Projects()

    for i in range(1, 3):
        # Get the url of each project
        project_xpath = '//*[@id="list"]/ul/li[%d]/a' %i
        # Get the HTML element that for the current project
        project_link = driver.find_element_by_xpath(project_xpath)
        project_name = project_link.text

        # Open the project page
        driver.get(project_link.get_attribute("href"))
        # Wait for project page to load
        time.sleep(0.5)

        inception = get_inception(driver)
        description = get_description(driver, project_name)

        # get the name without "Apache", make it lowercase, and add dashes
        stripped_name = "-".join(project_name.lower().split(" ")[1:]).encode('utf-8')
        github_mirror = "http://github.com/apache/" + stripped_name

        # see if there's anything at the github url that was generated
        resp = httplib2.Http().request(github_mirror, 'HEAD')
        # this means the github repo with the parsed url doesn't exist
        if int(resp[0]['status']) >= 400:
            github_mirror = "N/A"

        # Add extra attributes to the JSON
        description["GitHub Mirror"] = github_mirror
        description["Host"] = "Apache Software Foundation"
        description["Project Name"] = project_name
        description["Inception"] = inception

        projects.add(project_name, description)

        # Reset the driver
        driver.get('https://projects.apache.org/projects.html')
        time.sleep(0.8)

    return projects

if __name__ == "__main__":
    projects = apache_projects().projects
    try:   
        file = open("projects.json", 'w')
        file.write(str(projects))
        file.close()
        print("Wrote JSON to projects.json")
    except Exception as error: 
        print(error)

