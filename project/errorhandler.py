from project import app
from flask import render_template

#Custom handler for 404-error
@app.errorhandler(404) 
def not_found(error):
    return render_template("404.html", title="Page not found - 404", code=404)