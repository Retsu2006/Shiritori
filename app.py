from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/shiritori', methods=['GET', 'POST'])
def shiritori():
    if request.method == 'GET':
        return "しりとり"
    if request.method == 'POST':
        data = request.json
        return data.get('nextWord', 'No word provided')

if __name__ == '__main__':
    app.run()
