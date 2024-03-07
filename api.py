from flask import Flask, request, jsonify
import random

app = Flask(__name__)

vegetables = ['carrot', 'broccoli', 'spinach']
fruits = ['apple', 'banana', 'orange']

@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()
    item = data.get('item')
    
    if item.lower() in vegetables:
        return jsonify({'result': "it's a vegetable"})
    elif item.lower() in fruits:
        return jsonify({'result': "it's a fruit"})
    else:
        return jsonify({'result': "unknown"})

if __name__ == '__main__':
    app.run(debug=True)
