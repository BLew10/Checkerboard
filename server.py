from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def standard_board(x = 8, y = 8, color_one = 'black', color_two = 'red'):
    return render_template("index.html", x = x, y = y, color_one = color_one, color_two = color_two)

@app.route('/<int:x>')
def x_board(x = 8, y = 8, color_one = 'black', color_two = 'red'):
    return render_template("index.html", x = x, y = y, color_one = color_one, color_two = color_two)

@app.route('/<int:x>/<int:y>')
def xy_board(x = 8, y = 8, color_one = 'black', color_two = 'red'):
    return render_template("index.html", x = x, y = y, color_one = color_one, color_two = color_two)

@app.route('/<int:x>/<int:y>/<string:color_one>/<string:color_two>')
def custom_board(x = 8, y = 8, color_one = 'black', color_two = 'red'):
    return render_template("index.html", x = x, y = y, color_one = color_one, color_two = color_two)


if __name__ == "__main__":
    app.run(debug=True)