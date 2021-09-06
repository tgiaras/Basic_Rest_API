from flask import Flask, request, jsonify, json
from flask_restful import Resource, Api
import pymongo
from bson.objectid import ObjectId


app = Flask(__name__)
api = Api(app)

myClient = pymongo.MongoClient('localhost', 27017)
rDB = myClient["RESTDatabase"]
emp = rDB["employees"]
dep = rDB["departments"]


class Employees(Resource):

    def get(self):

        emps = emp.find()

        empsList = []

        for employee in emps:

            id = str(employee['_id'])
            firstName = employee['firstname']
            lastname = employee['lastname']
            department = employee['department']

            empData = {'_id': id, 'firstname': firstName, 'lastname': lastname, 'department': department}

            empsList.append(empData)

        return empsList


class Departments(Resource):
    def get(self):
        deps = dep.find()

        depsList = []

        for department in deps:

            id = str(department['_id'])
            name = department['name']

            depData = {'_id': id, 'name': name }

            depsList.append(depData)


        return depsList
        

class Employees_Name(Resource):
    def get(self, employee_id):
        myquery = { "_id": ObjectId(employee_id) }
        emps = emp.find(myquery)

        empsList = []

        for employee in emps:

            id = str(employee['_id'])
            firstName = employee['firstname']
            lastname = employee['lastname']
            department = employee['department']

            empData = {'_id': id, 'firstname': firstName, 'lastname': lastname, 'department': department}

            empsList.append(empData)

        return empsList
        

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Departments, '/departments') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
     app.run(port='5002', debug=True)