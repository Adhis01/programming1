from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
        <h1>Hello my name is ADHISTHAN GURUNG</h1>
        <p>My student ID is 4240023</p>
        <p>I am studying Computer Science</p>
    '''

if __name__ == '__main__':
    app.run(debug=True)
