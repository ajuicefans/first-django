from flask import Flask, render_template

app = Flask(__name__)

# 创建了网址 /show/info 和 函数 index的对应关系
# 用户在浏览器上访问 /show/info ，网站自动执行 index
@app.route("/show/info")
def index():
    # return "ajuicefans"
    # Flask 会自动打开这个文件并读取内容，并返回，即渲染出网页
    # 默认：去当前项目目录的 templates 文件夹下找
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == '__main__':
    app.run(debug=True)