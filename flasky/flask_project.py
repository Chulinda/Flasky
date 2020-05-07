from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/' )
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/about')
def user():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug = True, port=4567)





