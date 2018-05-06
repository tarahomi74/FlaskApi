from flask_restful import Resource
from BaseModel import Curse


class list(Resource):
    def get(self):
        courses = Curse.select()
        ls = [dict(
             id= c.id,
             list_prerequisite = c.list_prerequisite,
             name = c.name,
             price=c.price,
             presentation= c.presentation,
             status_prerequisite= c.status_prerequisite,
             type=c.type,
             unit_number=c.unit_number,
        )for c in courses
        ]
        return dict(courses= ls)