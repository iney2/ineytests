import json  
import urllib.request

uh = urllib.request.urlopen("http://dummy.restapiexample.com/api/v1/employees")
parsed_string = uh.read()
js = json.loads(parsed_string.decode("utf-8"))

i = 0
dic1 = {}
while i < len(js["data"]):
    dic1.update({js["data"][i]["employee_name"] : js["data"][i]["employee_salary"]})
    i = i +1
print('Doris Wilder salary is', dic1["Doris Wilder"])



