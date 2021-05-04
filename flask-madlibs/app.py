from flask import Flask, request, render_template
from stories import story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "whatnow"
debug = DebugToolbarExtension(app)

@app.route("/")
def homepage():
    """homepage that asks for keywords"""
    words = story.prompts
    # i didn't realize you could access class variables like this

    return render_template("homepage.html", words = words)



@app.route("/story")
def storypage():
    """Story markup"""
    
    book = story.generate(request.args)
    # request.args by itself will return the dictionary of get params, perfect for passing into story.generate


    return render_template("story.html", madlib = book)