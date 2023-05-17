# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Smithy" # write your name 
    age = "Stalin" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("C:\Users\smith\OneDrive\Desktop\vsc\PRO-C116-Project-Boilerplate-main\family tree\static\father.jpg")

# define the route to mother webpage
@app.route("C:\Users\smith\OneDrive\Desktop\vsc\PRO-C116-Project-Boilerplate-main\family tree\static\mother.jpeg")

# define the route to friends webpage
@app.route("C:\Users\smith\OneDrive\Desktop\vsc\PRO-C116-Project-Boilerplate-main\family tree\static\friend.jpg")

# add other routes, if you want
@app.route("C:\Users\smith\OneDrive\Desktop\vsc\PRO-C116-Project-Boilerplate-main\family tree\static\me.jpg")



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
