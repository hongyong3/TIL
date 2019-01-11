from flask import Flask, render_template
app = Flask(__name__)  # main name을 Flask로 인식시키는 것.

# @app.route('/html')
# def index():
#     return render_template("chicken.html")

# if __name__ == '__main__':
#     app.run()

@app.route('/html_name/<string:name>')
def html_name(name):
    return render_template('chicken.html', your_name = name)


if __name__ == '__main__':
    app.run()

@app.route('/dictionary/<string:word>')
def dictionary(word):
    word_dict = {"apple": "사과", "banana": "바나나"}
    return render_template("word.html", word = word, word_dict = word_dict)


if __name__ == '__main__':
    app.run()