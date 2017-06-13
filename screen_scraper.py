from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import ast

class Project():

    def __init__(self, name, description):
        self.name = name
        self.description = description

class Projects():

    def __init__(self):
        self.projects = {}
    
    def get(self, name):
        """Returns a new project with the given name"""
        try:
            return self.projects[name]
        except KeyError:
            print("No project called %s was found" %name)

    def add(self, project):
        """Adds a project result"""
        self.projects[project.name] = project

def apache_projects():

    path_to_chromedriver = '/usr/local/bin/chromedriver'
    driver = webdriver.Chrome(executable_path = path_to_chromedriver)
    url = 'https://projects.apache.org/projects.html'
    driver.get(url)
    time.sleep(2)
    elem = driver.find_element_by_id('list')
    project_list = elem.text.split("\n")
    projects = Projects()

    for i in range(1, len(project_list) + 1):
        # Get the url of each project
        project_path = '//*[@id="list"]/ul/li[%d]/a' %i
        link = driver.find_element_by_xpath(project_path)
        name = link.text
        # Open the project page
        driver.get(link.get_attribute("href"))
        time.sleep(0.5)
        # Get the url for the JSON DOAP
        link = "//*[@id='contents']/ul[1]/li[contains(., 'Project data file')]/a[2]"
        try:
            json_link = driver.find_element_by_xpath(link)
            # Go to the JSON page
            driver.get(json_link.get_attribute("href"))
            # Add the JSON to the Project info
            json = driver.find_element_by_xpath('/html/body/pre').text
            description = ast.literal_eval(json)
            description["Host"] = "Apache Software Foundation"
            print("Adding JSON for " + name)
        except:
            description = "None Available"
            print("Unable to scrape JSON for " + name)
        
        project = Project(name, description)
        projects.add(project)

        # Reset the driver
        driver.get(url)
        time.sleep(0.8)

apache_projects()