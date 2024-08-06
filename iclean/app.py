#!/usr/bin/env python3

from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def root():
    import pdb;pdb.set_trace()
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

# (Pdb) request.application.__globals__['__builtins__']['__import__']('os').popen('id').read()