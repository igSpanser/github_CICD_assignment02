# import add
# Inmporting Flask
from flask import Flask
# Create the server
app=Flask(__name__)

####
@app.route("/")
def hello():
    return "Hello World"

if (__name__ == "__main__"):
    app.run(debug=True)

##### Copy IP from terminal output and put it it web browser. 
