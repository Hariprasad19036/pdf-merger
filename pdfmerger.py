from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/merged', methods=['GET', 'POST'])
def merged():
    return "The merged PDF should be rendered here"

if __name__ == '__main__':
   app.run(debug = True)