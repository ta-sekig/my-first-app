from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(80),nullable = False)
    def  __repr__(self):
        return f'<User{self.username}>'

with app.app_context():
    db.create_all()

@app.route("/")
def hello():
    all_users = User.query.all()
    my_skills = ["python","Flask","HTML","Data Science", "Monetization"]
    return render_template("index.html",emotion="最高！",skills=my_skills,users=all_users)

@app.route("/receive_name",methods = ["POST"])
def receive_name():
    sent_name = request.form["my_name"]
    new_user = User(username=sent_name)
    db.session.add(new_user)
    db.session.commit()
    return f"<h1>登録完了!こんにちは、{sent_name}さん!データベースに保存しました。</h1>"

@app.route("/user/<name>")
def show_user_profile(name):
    return f"<h1>Welcome,{name}</h1>"

@app.route("/add/<int:num1>/<int:num2>")
def add_numbers(num1,num2):
    Add_num = num1 + num2
    return f"<h1>{num1} + {num2} = {Add_num}</h1>"


if __name__ == "__main__":
    app.run(debug=True,port=5002)