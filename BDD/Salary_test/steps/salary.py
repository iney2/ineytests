from behave import *
import json
import urllib.request
from jsonpath_ng.ext import parse
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

@given('information about employees')
def step_impl(context):
    global json_data
    json_data = json.loads(urllib.request.urlopen(config['url']['URL']).read().decode("utf-8"))
    assert json_data is not None

@when('take salary of Doris Wilder')
def step_impl(context):
    global salary
    for key in json_data["data"]:
        if key["employee_name"] == "Doris Wilder":
            salary = key["employee_salary"]
    assert salary is not None

@then('value of salary is match with expected')
def step_impl(context):
    assert salary == '85600'
