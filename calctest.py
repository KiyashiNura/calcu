from flask import Flask, render_template, request
import random
app = Flask(__name__)


@app.route('/calc')
def calc():
    b = "Введите число"
    if 'a' in request.args:
        b = "{}".format(int(request.args['a'])**2 * 3.14)

    return render_template('calc.html').format(b)


app.run(debug=True, port=8080)
