import json
import urllib.request
from jsonpath_ng.ext import parse

uh = urllib.request.urlopen("http://dummy.restapiexample.com/api/v1/employees")
parsed_string = uh.read()
json_data = json.loads(parsed_string.decode("utf-8"))

def emp_information(emp_name, emp_info = 'employee_salary'):    
 
    jsonpath_expression = parse("$.data[?(@.employee_name==" + emp_name + ")]." + emp_info)

    for match in jsonpath_expression.find(json_data):
        json_salary = match.value
        
    return json_salary    

def test_Wilder_salary():
    assert emp_information('"Doris Wilder"', 'employee_salary') == '85600'
    
def test_Berry_age():
    assert emp_information('"Yuri Berry"', 'employee_age') == '40'    
    
def test_Davidson_ID():
    assert emp_information('"Rhona Davidson"', 'id') == '8'