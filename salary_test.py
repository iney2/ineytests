import json
import urllib.request
from jsonpath_ng.ext import parse

uh = urllib.request.urlopen("http://dummy.restapiexample.com/api/v1/employees")
parsed_string = uh.read()
json_data = json.loads(parsed_string.decode("utf-8"))

jsonpath_expression = parse('$.data[?(@.employee_name=="Doris Wilder")].employee_salary')

for match in jsonpath_expression.find(json_data):
    print('Doris Wilder salary is', match.value)