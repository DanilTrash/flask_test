import os
from flask import Flask, jsonify, request, redirect, url_for
import socket
from database import PandasData

app = Flask(__name__)


@app.route('/')
def index_page():
    return redirect('https://docs.google.com/spreadsheets/d/12U5G94RRohSdDujUKU70LrS3iCKOOe5rRKfVIGmVaf0/edit#gid=687502802')


@app.route('/start')
def start():
    print(request.args)
    if request.args.get('gid') in PandasData('687502802')('gid').dropna().tolist():
        return {'status': 'started'}
    else:
        return {'status': 'ERROR'}


@app.route('/stop')
def stop():
    print(request.args)
    if request.args.get('gid') in PandasData('687502802')('gid').dropna().tolist():
        return {'status': 'stopped'}
    else:
        return {'status': 'ERROR'}


if __name__ == '__main__':
    hostname = socket.gethostname()
    host = socket.gethostbyname(hostname)
    app.run(host=host, debug=True, use_debugger=False, use_reloader=True)
