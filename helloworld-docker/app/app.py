from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        user_name = request.form.get('name')
        return render_template('greet.html', name=user_name)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
