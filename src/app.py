from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    a = '<a href="hi">Click here</a>'
    return f'Hello world! {a}'

@app.route('/hi')
def say_hi():
    return render_template('hi.html', title='The Hi Page')

if __name__ == '__main__':
    app.run()
