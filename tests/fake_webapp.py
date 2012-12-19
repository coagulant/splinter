# -*- coding: utf-8 -*-

# Copyright 2012 splinter authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from bottle import abort, request, get, post, run, static_file
from os import path


this_folder = path.abspath(path.dirname(__file__))


def read_static(static_name):
    return open(path.join(this_folder, 'static', static_name)).read()

EXAMPLE_APP = "http://localhost:5000/"
EXAMPLE_HTML = read_static('index.html')
EXAMPLE_IFRAME_HTML = read_static('iframe.html')
EXAMPLE_ALERT_HTML = read_static('alert.html')
EXAMPLE_TYPE_HTML = read_static('type.html')
EXAMPLE_POPUP_HTML = read_static('popup.html')
EXAMPLE_NO_BODY_HTML = read_static('no-body.html')


@get('/')
def index():
    return EXAMPLE_HTML


@get('/iframe')
def iframed():
    return EXAMPLE_IFRAME_HTML


@get('/alert')
def alertd():
    return EXAMPLE_ALERT_HTML


@get('/type')
def type():
    return EXAMPLE_TYPE_HTML


@get('/no-body')
def no_body():
    return EXAMPLE_NO_BODY_HTML


@get('/name')
def get_name():
    return "My name is: Master Splinter"


@get('/useragent')
def get_user_agent():
    return request.environ.get("HTTP_USER_AGENT")


@post('/upload')
@get('/upload')
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        buffer = []
        buffer.append("Content-type: %s" % f.type)
        buffer.append("File content: %s" % f.file.read())
        return '|'.join(buffer)


@get('/foo')
def foo():
    return "BAR!"


@get('/query')
def query_string():
    if request.query_string == "model":
        return "query string is valid"
    else:
        raise abort(500)


@get('/popup')
def popup():
    return EXAMPLE_POPUP_HTML


@get('/static/:filename#.*#', name='css')
def server_static(filename):
    return static_file(filename, root=path.join(this_folder, 'static'))


def start_app(host, port):
    """Runs the server."""
    run(host=host, port=port)


if __name__ == '__main__':
    start_app("localhost", 5000)
