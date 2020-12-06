from flask import render_template, url_for, flash, redirect, request, json

from random import choice
from string import ascii_letters

from project import app, db
from project.models import Url


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="URL - Shortener")


@app.route('/short_your_url', methods=['POST', 'GET'])
def return_shortener_url():
    if request.method == 'POST':
        default_url = request.form['url']
        short_url = get_short_url()

        # INSERT VALUES INTO THE DB
        url = Url(default_url=default_url, short_url=short_url)
        db.session.add(url)
        db.session.commit()

        return json.dumps({'url': short_url})

    return render_template('home.html', title="Error")


@app.route('/<short_url>')
def view_site(short_url):
    try:
        url = Url.query.filter_by(
            short_url=get_hostname() + str(short_url)).first()

        return redirect(url.default_url, code=302)
    except:
        return render_template("404.html", title="Page not found - 404", code=404)


def get_short_url():
    short_url = get_hostname() + \
        ''.join(choice(ascii_letters) for i in range(12))

    return short_url


def get_hostname():
    return request.host_url  # with port
