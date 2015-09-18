#!/usr/bin/env python
#!conding:utf-8
from flask import Flask, render_template, Response, request
from flask.ext.socketio import SocketIO, send, emit
from rat import Tieba_url, Query
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
    print type(para['rep_num'])
    posts = []
    try:
        query = Query(para)
        print 'done'
        posts = query.find()
    except StandardError, e:
        print e
    emit(event_name, posts)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8888)
