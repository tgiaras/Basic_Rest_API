import pymongo

myClient = pymongo.MongoClient('localhost', 27017)
rDB = myClient["RESTDatabase"]
emp = rDB["employees"]
dep = rDB["departments"]

employees = [
  {"firstname": "Themis", "lastname": "Giaras", "department": "Development"},
  {"firstname": "John", "lastname": "Smith", "department": "Human Resources"},
  {"firstname": "Howard", "lastname": "Carpenter", "department": "Finance"},
  {"firstname": "Benjamin", "lastname": "Franklin", "department": "Operations"},
  {"firstname": "Otto", "lastname": "Octavius", "department": "R&D"}
]

departments = [
    {"name": "Development"},
    {"name": "Human Resources"},
    {"name": "Finance"},
    {"name": "Operations"},
    {"name": "R&D"}
]

x = emp.insert_many(employees)
y = dep.insert_many(departments)
