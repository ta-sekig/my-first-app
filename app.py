from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def hello():
    my_skills = ["python","Flask","HTML","Data Science", "Monetization"]
    return render_template("index.html",emotion="最高！",skills=my_skills)
    
@app.route("/user/<name>")
def show_user_profile(name):
    return f"<h1>Welcome,{name}</h1>"

@app.route("/add/<int:num1>/<int:num2>")
def add_numbers(num1,num2):
    Add_num = num1 + num2
    return f"<h1>{num1} + {num2} = {Add_num}</h1>"


if __name__ == "__main__":
    app.run(debug=True,port=5002)