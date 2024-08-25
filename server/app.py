#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:print_string>')
def user(print_string):
    print(print_string)
    return f'{print_string}'

@app.route('/count/<int:parameter>')
def count(parameter):
    output = ""
    for num in range(parameter):
        output += str(num) + '\n'
    return output

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        output = num1 + num2
    elif operation == '-':
        output = num1 - num2
    elif operation == '*':
        output = num1 * num2
    elif operation == 'div':
        output = num1 / num2
    elif operation == '%':
        output = num1 % num2
    else:
        pass
    return f'{output}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
