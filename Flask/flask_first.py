from flask import Flask
app = Flask(__name__)

@app.route('/')

def who():
    return 'who am i?'

if __name__ == '__main__':  
   app.run('0.0.0.0',port=8080,debug=True)

# from flask import Flask, render_template

# app = Flask(__name__)

# student_data = {
#     1: {"name": "슈퍼맨", "score": {"국어": 90, "수학": 65}},
#     2: {"name": "아이언맨", "score": {"국어": 75, "영어": 80, "수학": 75}}
# }

# @app.route('/')
# def index():
#     return render_template("index.html", 
#             template_students = student_data)
            
# @app.route("/student/<int:id>")
# def student(id):
#     return render_template("student.html", 
#             template_name=student_data[id]["name"], 
#             template_score=student_data[id]["score"])
            
# if __name__ == '__main__':
#     app.run(debug=True)
# return render_template("index.html", template_students = student_data)