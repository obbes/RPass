from flask import Flask, render_template
import os
import base64
app = Flask(__name__, template_folder = 'templates')


@app.route('/')
def index():
    return render_template('index.html', generated_password=base64.b64encode(os.urandom(12)))

@app.route('/random_pass/')
@app.route('/random_pass/<int:length>/')
def password(length=12):
    password = base64.b64encode(os.urandom(12))
    pass_string = str(password.decode('ascii'))
    return render_template('index.html', generated_password=pass_string)

if __name__ == '__main__':
    app.run(debug=True)