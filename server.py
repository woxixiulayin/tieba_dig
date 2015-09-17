#!/usr/bin/env python
#!conding:utf-8
from flask import Flask, render_template, Response, request
from flask.ext.socketio import SocketIO, send, emit
import json

app = Flask(__name__)
socketio = SocketIO(app)

event_name = 'tieba_dig'

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on(event_name)
def handle_search_para(para):
    print para
    posts = []
    emit(event_name, posts)

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
    socketio.run(app, host='0.0.0.0', port=8888)
