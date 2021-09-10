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

    def post(self):

        firstname = request.json['firstname']
        lastname = request.json['lastname']
        department = request.json['department']

        toAdd = { 'firstname': firstname, 'lastname': lastname, 'department': department}

        emp.insert_one(toAdd)

        toAdd['_id'] = str(toAdd['_id'])

        return {'status': 'success', 'addedData': toAdd}



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
    
    def post(self):

        name = request.json['name']

        toAdd = { 'name': name}

        dep.insert_one(toAdd)

        toAdd['_id'] = str(toAdd['_id'])

        return {'status': 'success', 'addedData': toAdd}
        

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

    def put(self, employee_id):

        myquery = { "_id": ObjectId(employee_id) }

        emps = emp.find(myquery)

        for employee in emps:

            oldData = employee

        oldData['_id'] = str(oldData['_id'])

        newData = oldData.copy()

        newValues = { "$set": {} }

        for key in request.json:

            newValues['$set'][key] = request.json[key]
            newData[key] = request.json[key]

        emp.update_one(myquery, newValues)

        return { 'status': 'success', 'oldData': oldData, 'newData': newData}

    def delete(self, employee_id):

        myquery = { "_id": ObjectId(employee_id) }

        emps = emp.find(myquery)

        for employee in emps:

            delData = employee
        
        delData['_id'] = str(delData['_id'])

        emp.delete_one(myquery)

        return { 'status': 'success', 'deleted': delData}

class Department_Name(Resource):

        def get(self, department_id):

            myquery = { "_id": ObjectId(department_id) }

            deps = dep.find(myquery)

            depsList = []

            for department in deps:

                id = str(department['_id'])
                name = department['name']

                empData = {'_id': id, 'name': name}

                depsList.append(empData)

            return depsList

        def put(self, department_id):

            myquery = { "_id": ObjectId(department_id) }

            deps = dep.find(myquery)

            for department in deps:

                oldData = department

            oldData['_id'] = str(oldData['_id'])

            newData = oldData.copy()

            newValues = { "$set": {} }

            for key in request.json:

                newValues['$set'][key] = request.json[key]
                newData[key] = request.json[key]

            dep.update_one(myquery, newValues)

            return { 'status': 'success', 'oldData': oldData, 'newData': newData}

        
        def delete(self, department_id):

            myquery = { "_id": ObjectId(department_id) }

            deps = dep.find(myquery)

            for department in deps:

                delData = department
            
            delData['_id'] = str(delData['_id'])

            dep.delete_one(myquery)

            return { 'status': 'success', 'deleted': delData}

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Departments, '/departments') # Route_2
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3
api.add_resource(Department_Name, '/departments/<department_id>') # Route_4


if __name__ == '__main__':
     app.run(port='5002', debug=True)