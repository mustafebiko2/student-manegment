from flask import Flask

app = Flask(__name__)


@app.get('/')
def index():
  return 'hello world'

@app.get('/students')
def get_all_students():
  return "get all students"

@app.get('/students/<students_id>')
def get_students_by_id(students_id):
  return f"get all {students_id}"

@app.post('/students')
def create_students():
  return "create students"

@app.patch('/students/<students_id>')
def update_students_by_id(students_id):
  return f"update students {students_id}"

@app.delete('/students/<students_id>')
def delete_students_by_id(students_id):
  return f"delete students  {students_id}"
