from flask import Flask
from flask_restful import Api
import CourseController
import  PorfossorController

app = Flask(__name__)
api = Api(app)



api.add_resource(CourseController.list , '/courses', endpoint='test')
api.add_resource(PorfossorController.list , '/profossors' , endpoint='test2')


if __name__ == '__main__':
    app.run('127.0.0.1',5000,True)



