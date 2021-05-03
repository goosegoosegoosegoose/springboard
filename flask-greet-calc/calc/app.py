from flask import Flask, request

from operations import add, sub, mult, div


app = Flask(__name__)

@app.route('/add')
def return_sum():
    """Returns sum of a and b in html body"""
    
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"<b>{add(a, b)}</b>"

@app.route('/sub')
def return_diff():
    """Returns difference of a and b in html body"""
    
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"<b>{sub(a,b)}</b>"

@app.route('/mult')
def return_prod():
    """Returns product of a and b in html body"""
    
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"<b>{mult(a, b)}</b>"
    
@app.route('/div')
def return_quo():
    """Returns quotient of a and b in html body"""
    
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"<b>{div(a, b)}</b>"

operation = {
    'add': add,
    'sub': sub,
    'div': div,
    'mult': mult
}

@app.route('/math/<op>')
def calc(op):
    """Returns result of math operation depending on what <op> is entered as"""

    a = int(request.args["a"])
    b = int(request.args["b"])
    res = operation[op](a,b)
    return f"<b>{res}</b>"