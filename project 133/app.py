# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Lakshit Munjal" # write your name
    age = "11" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
def home():

    name = "Mr.Arun Munjal" # write your name
    age = "38" # write your age

    return render_template('father.html' , name = name , age = age)

# define the route to mother webpage
def home():

    name = "Mrs.Gitika" # write your name
    age = "11" # write your age

    return render_template('mother.html' , name = name , age = age)

# define the route to friends webpage
def home():

    name = "Aarav" # write your name
    age = "11" # write your age

    return render_template('friend.html' , name = name , age = age)
# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
