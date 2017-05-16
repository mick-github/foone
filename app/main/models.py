from .. import problem_db

GRADE = ('6-Fall', '6-Spring', '7-Fall', '7-Spring', '8-Fall', '8-Spring',
         '9-Fall', '9-Spring')

UNIT = ('Unit1', 'Unit2', 'Unit3', 'Unit4', 'Unit5', 'Unit6', 'Unit7',
        'Unit8', 'Unit9', 'Unit10')

class Problem(problem_db.Document):
    question = problem_db.StringField(required=True)
    explain = problem_db.StringField()
    answer = problem_db.StringField(required=True)
    grade = problem_db.StringField(choices=GRADE)
    unit = problem_db.StringField(choices=UNIT)
    tags = problem_db.StringField()