from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/counter')
def route_list():
    return render_template('templates/frontpage.html')


@app.route('/')
def counter():
    count = 0
    redirect ('/counter')


@app.route('/request-counter')
def counter():
    count += 1
    redirect('/counter')



if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
