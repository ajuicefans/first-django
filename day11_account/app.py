from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template('register.html')
        # 输入url的跳转是GET请求
    
    else:
        print(request.form)
        return "注册成功"


if __name__ == '__main__':
    app.run(debug=True)
