#!/usr/bin/env python
from flask import Flask,request,jsonify
app = Flask(__name__)

def get_data(page):
    with open(page, 'r') as file:
        data = file.read()
    return data

script = '<script>\n'+ get_data('script_inject.js') +'</script>'
content = get_data('content.html')
key = get_data('key.txt')

page = script + content

@app.route('/')
def load_page():
    #print(key)
    return(page)

@app.route('/verify', methods=['POST'])
def verify():
    data = request.json
    answer = data['answer']
    print(answer)
    return jsonify(data)

