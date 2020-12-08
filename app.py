from flask import Flask, render_template, request, jsonify, make_response
import calculate
import graph

app = Flask(__name__)

all_posts = [
    {
        'title': 'Post 1',
        'content': 'content of post 1'
    },
    {
        'title': 'Post 2',
        'content': 'content of post 2'
    }
]

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/calc')
def calc():
    return render_template('calculator.html')

@app.route('/calc/parse', methods=["POST"])
def parse():
    equation = request.get_json()

    # res = make_response(jsonify({"message": "Received"}), 200)
    result = calculate.calculation(equation)
    # print(result)
    graph.graph_it(result, equation)
    return equation

if __name__ == "__main__":
    app.run(host='0.0.0.0')

