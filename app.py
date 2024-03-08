from flask import Flask, render_template,jsonify
app = Flask(__name__)
skills= [
{
    'id':1,
    'title':'Data Aanalyst',
    'skill' :'Data cleasing,Hadoop'
},
{
    'id':2,
    'title':'Statistical Machine learning',
    'skill' :'Spark,Python,Hadoop'
},

{
    'id':3,
    'title':'General Development',
    'skill' :'Web development Backend using Python,php'
}
]
@app.route("/")
def hello_world():
    return render_template('home.html',skills=skills,prof_name='Safaa')

@app.route("/api/skills")
def list_skills():
    return jsonify(skills)