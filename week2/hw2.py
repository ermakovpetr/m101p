import pymongo
from pymongo.mongo_client import MongoClient

client = MongoClient()
db = client.students

select_query = {'type': 'homework'}
sort_query = [('student_id', pymongo.ASCENDING), ('score', pymongo.ASCENDING)]
grades = db.grades.find(select_query).sort(sort_query)

prev_student_id = grades[0]['student_id'] - 1
for grade in grades:
    if prev_student_id != grade['student_id']:
        prev_student_id = grade['student_id']
        db.grades.remove(grade)
