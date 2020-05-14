# -*- coding: utf-8 -*-
"""
Created on Monday, ‎May ‎11, ‎2020, ‏‎6:31:54 PM

@author: modeaxe
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/1006")
def engi1006():
    return render_template("1006.html")

@app.route("/classes")
def classes():
    return render_template("springClasses.html")  

#start the server
if __name__ == "__main__":
    app.run()