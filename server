from flask import Flask, send_from_directory, request, jsonify

app = Flask(__name__, static_folder='public')

previous_word = "しりとり"

@app.route('/shiritori', methods=['GET'])
def get_previous_word():
    global previous_word
    return previous_word

@app.route('/shiritori', methods=['POST'])
def update_previous_word():
    # リクエストからJSONデータを取得
    global previous_word
    request_json = request.json
    if not request_json:
        return "JSONデータがありません", 400
    
    next_word = request_json.get('nextWord')
    if not next_word:
        return "nextWordがリクエストに含まれていません", 400

    # previous_wordの末尾とnext_wordの先頭が同じか確認
    if previous_word[-1] == next_word[0]:
        # 同じであれば、previous_wordを更新
        previous_word = next_word
        return previous_word
    else:
        return "単語のつながりがありません", 400

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/styles.css')
def styles():
    return app.send_static_file('styles.css')

if __name__ == '__main__':
    app.run(port=8000)
