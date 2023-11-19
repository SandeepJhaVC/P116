# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Sandeep Jha" # write your name
    age = "17" # write your age
    rel = "me"

    return render_template('index.html' , name = name , age = age, rel = rel)

# define the route to father webpage
@app.route('/father')
def father():

    name = "Suman Jha" # write your name
    age = "45" # write your age
    rel = "father"

    return render_template('index.html' , name = name , age = age, rel=rel)

# define the route to mother webpage
@app.route('/mother')
def mother():

    name = "Sudhira Jha" # write your name
    age = "40" # write your age
    rel = "mother"
    return render_template('index.html' , name = name , age = age,rel=rel)

# define the route to friends webpage
@app.route('/friend')
def friend():

    name = "Arsh" # write your name
    age = "17" # write your age
    rel="friend"

    return render_template('index.html' , name = name , age = age,rel=rel)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
