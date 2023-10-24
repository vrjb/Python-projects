from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/cal')
def calc():
    return render_template('index.html')

@app.route('/math', methods = ["POST"])
def calculator():
    ops = request.form['operation']
    f_num = int(request.form['num1'])
    s_num = int(request.form['num2'])

    if ops == 'add':
        result = f_num + s_num
        return f'Addition of {f_num} and {s_num} is {result}'
    
    if ops == 'subtract':
        result = f_num - s_num
        return f'Subtraction of {f_num} and {s_num} is {result}'
    
    if ops == 'multiply':
        result = f_num * s_num
        return f'multiplication of {f_num} and {s_num} is {result}'
    
    if ops == 'divide':
        result = f_num / s_num
        return f'Division of {f_num} and {s_num} is {result}'
    

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port='8002')