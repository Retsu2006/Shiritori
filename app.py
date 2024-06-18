from flask import Flask, send_from_directory, request, jsonify
import re

app = Flask(__name__, static_folder='public')

previous_word = "しりとり"
used_words = [previous_word]

def is_hiragana(word):
    return re.fullmatch(r'^[\u3040-\u309F]+$', word) is not None

@app.route('/shiritori', methods=['GET'])
def get_previous_word():
    global previous_word
    return jsonify(previous_word=previous_word)

@app.route('/shiritori', methods=['POST'])
def update_previous_word():
    global previous_word, used_words
    request_json = request.get_json()
    if not request_json:
        return jsonify(error="JSONデータがありません"), 400
    
    next_word = request_json.get('nextWord')
    if not next_word:
        return jsonify(error="nextWordがリクエストに含まれていません"), 400

    if not is_hiragana(next_word):
        return jsonify(error="ひらがなのみ使用できます"), 400

    if next_word in used_words:
        return jsonify(error="この単語はすでに使用されています"), 400

    if next_word[-1] == "ん":
        return jsonify(error="※「ん」で終わる単語は使えません‼"), 400
    
    if previous_word[-1] == next_word[0]:
        previous_word = next_word
        used_words.append(next_word)
        return jsonify(previous_word=previous_word)
    else:
        return jsonify(error="単語のつながりがありません"), 400
    
@app.route('/reset', methods=['POST'])
def reset_game():
    global previous_word, used_words
    previous_word = "しりとり"
    used_words = [previous_word]
    return jsonify(previous_word=previous_word)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/styles.css')
def styles():
    return app.send_static_file('styles.css')

if __name__ == '__main__':
    app.run(port=8000)
