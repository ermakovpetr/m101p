import pymongo
from pymongo.mongo_client import MongoClient

client = MongoClient()
db = client.school

students_cursor = db.students.find()

for student in students_cursor:
    scores = student['scores']
    homework = [x for x in scores if x['type'] == 'homework']
    min_homework = min(homework, key=lambda x: x['score'])
    scores.remove(min_homework)
    db.students.update({"_id": student['_id']}, {"$set": {"scores": scores}})
