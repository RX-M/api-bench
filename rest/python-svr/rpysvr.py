""" REST Server
"""
from __future__ import print_function
import datetime
from flask import Flask
from flask import jsonify
from flask import request

APP = Flask(__name__)

VERSION = "0.1"

@APP.route('/')
def version():
    """ Root IRI returns the API version """
    return jsonify(version=VERSION)

PROJECTS = {}

@APP.route('/projects', methods=['GET', 'POST'])
def projects():
    """ /projects collection allows POST of new projects and GET of all projects """
    if request.method == 'POST':
        proj = request.get_json()
        result = validate_project(proj)
        if result:
            print("ERROR: " + request.url + " : " + result)
            return jsonify(error=result), 400
        PROJECTS[proj["name"]] = proj
        response = jsonify(proj)
        response.status_code = 201
        response.headers['Location'] = "projects/" + str(proj["name"])
        response.autocorrect_name_header = False
        return response
    elif request.method == 'GET':
        return jsonify(list(proj.values()))
    else:
        return jsonify(error="bad HTTP verb, PUT supported"), 400

@APP.route('/projects/<string:project_name>', methods=['GET'])
def project(project_name):
    """ project name project be used as a /projects path param to GET a single project """
    if project_name not in PROJECTS:
        return jsonify(error="project not found"), 404
    if request.method == 'GET':
        return jsonify(PROJECTS[project_name])
    else:
        return jsonify(error="bad HTTP verb, only GET supported"), 400

def validate_project(proj):
    """ DbC checks for required project fields and settings
            returns False if project is valid
            returns a string describing the error otherwise
    """
    try:
        #Test day
        day = int(proj["day"])
        if day < 1 or day > 31:
            raise ValueError("Day must be between 1..31")
        #Test month
        month = int(proj["month"])
        if month < 1 or month > 12:
            raise ValueError("Month must be bewteen [1..12]")
        #Test year
        year = int(proj["year"])
        now = datetime.datetime.now()
        if year < 1990 or year > now.year:
            raise ValueError("Year must be between [1990..", now.year, "]")

    except ValueError as ex:
        return str(ex)
    return False #no errors

