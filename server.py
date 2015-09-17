#!/usr/bin/env python
#!conding:utf-8
from flask import Flask, render_template, Response, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/comments.json', methods=['GET', 'POST'])
# def comments_handler():

#     with open('comments.json', 'r') as file:
#         comments = json.loads(file.read())

#     if request.method == 'POST':
#         comments.append(request.form.to_dict())

#         with open('comments.json', 'w') as file:
#             file.write(json.dumps(comments, indent=4, separators=(',', ': ')))

#     return Response(json.dumps(comments), mimetype='application/json', headers={'Cache-Control': 'no-cache'})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
