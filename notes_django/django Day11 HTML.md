# day11 ①HTML

```
目的：开发一个平台（网站）
	- 前端开发：HTML、CSS、JavaScript
	- Web框架：接受请求并处理
	- MySQL数据库：存储数据的地方
	
快速上手：基于Flask Web框架让你快速搭建一个网站

深入学习：基于Django框架
```



## 1.快速开发网站

```
pip install flask
```

第一个网站开发程序：web.py

```python
from flask import Flask

app = Flask(__name__)

# 创建了网址 /show/info 和 函数 index的对应关系
# 用户在浏览器上访问 /show/info ，网站自动执行 index
@app.route("/show/info")
def index():
    return "ajuicefans"

if __name__ == '__main__':
    app.run()
```



别人的网站好看 vs 咱们的网站不好看

```
浏览器可以识别很多标签 + 数据，例如：
	<h1>哈哈哈<h1>
	<span style='color: red;'>ajuicefans</span>
	
如果我们能把浏览器能识别的所有标签都学会，我们在网站就可以控制页面到底长什么样子

网站给用户的浏览器返回的本质：字符串

浏览器具备解析特定格式的字符串的能力
```

### Flask框架为了让咱们写标签方便，可以单独写前端的网页文件，如下

这种 return 方式返回 HTML 内容的方式不方便进行管理，因此我们会引入`templates`模板

web.py

```python
from flask import Flask, render_template

app = Flask(__name__)

# 创建了网址 /show/info 和 函数 index的对应关系
# 用户在浏览器上访问 /show/info ，网站自动执行 index
@app.route("/show/info")
def index():
    # Flask 会自动打开这个文件并读取内容，并返回，即渲染出网页
    # 默认：去当前项目目录的 templates 文件夹下找
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
```

templates/index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>哦吼~</title>
</head>
<body>
<h1>哈哈哈哈哈</h1>
</body>
</html>
```



当然这个`templates`目录也可以自定义名称

```python
# 例如目录名称为"xxx"
app = Flask(__name__, template_folder="xxx")
```

---



## 2.浏览器能识别的标签

### 2.1 编码

```html
<meta charset="UTF-8">
```



### 2.2 title

`<meta >` 和 `<title></title>`标签只能放在`<head></head>`标签中

```html
<head>
    # 编码
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    
    <title>网页标题</title>
    
</head>
```



## 以下都写在 body 标签内

### 2.3 标题（块）

```html
<body>
    <h1>一级标题</h1>
    <h2>二级标题</h1>
    <h3>三级标题</h1>
    <h4>四级标题</h1>
    <h5>五级标题</h1>
</body>
```



### 2.4 div（块）和span（行内）

>  这两个标签比较“素”，但结合css可以变模样

```html
<div>内容</div>

<span>内容</span>
```

- div：占一整行【块级标签】
- span：用多少占多少【行内标签 / 内联标签】
  - 两个 span 标签不在同一行，页面显示时会在**同一行**，**中间以一个空格分隔**
  - 两个 span 标签在同一行，页面显示时会在**同一行**，**中间没有空格，连着**

---



### 2.5 超链接（行内）

> 你可以选择跳转自己网站的地址,或者跳转外部的网站

```html
跳转到其他网站
<a href="http://www.chinaunicom.com.cn/about/about.html">点击跳转</a>
```

```html
跳转到自己网站其他的地址：两种方式

<a href="http://127.0.0.1:5000/get/news">点击跳转</a>
<a href="/get/news">点击跳转</a>
```

```html
# 当前页面打开
<a href="/get/news">点击跳转</a>

# 新的Tab页面打开
<a href="/get/news" target="_blank">点击跳转</a>
```



#### **图片超链接**

> 添加 target=“_blank”

```html
<!-- 图片超链接 -->
<body>
    <a href="https://www.mi.com/shop/buy/detail?product_id=16642" target="_blank">
        <img src="https://cdn.cnbj1.fds.api.mi-img.com/nr-pub/202210262033_ef39fca0e37395d07682124770fd3ad9.png" style="width: 150px;"/>
    </a>
</body>

```

---



### 2.6 图片（行内）

可以设置图片的高度和宽度

```html
<img src="图片地址" width="100" height="100"/>
<img src="图片地址" style="height: 100px; width: 100px"/>
```

#### 外部图片

```html
直接显示别人的图片地址（防盗链）
<img src="https://github.com/youngyangyang04/leetcode-master" />
```

#### 内部图片

```html
<img src="图片地址" />
显示自己的图片：
	- 自己的项目中创建：static目录，图片放在static中
	- 在页面上引入图片
		<img src="/static/dog.jpg" />
```



### 小结

- 学习的标签

  ```html
  标题标签：<h1></h1>
  <div></div>
  <span></span>
  链接标签：<a></a>
  图片标签：<img />
  ```

- 划分

  ```html
  - 块级标签
  	标题标签：<h1></h1>
  	<div></div>
  - 行内标签
  	<span></span>
  	链接标签：<a></a>
  	图片标签：<img />
  ```

- 嵌套

  ```html
  <div>
      <span>xxx</span>
      <img />
      <a></a>
  </div>
  ```

  再例如：图片超链接
  
  ```html
  <a href="https://www.vivo.com.cn/vivo/x90proplus/">
      <img src="https://wwwstatic.vivo.com.cn/vivoportal/files/image/series/20221118/c2879159ce9f82e80825eaf52f953d0b.png" >
  </a>
  ```
  



---

### 2.7 列表标签

- 无序列表

  ```html
  <ul>
  	<li>中国移动</li>
  	<li>中国联通</li>
  	<li>中国电信</li>
  </ul>
  ```

1. 有序列表

   ```html
   <ol>
   	<li>中国移动</li>
   	<li>中国联通</li>
   	<li>中国电信</li>
   </ol>
   ```

   



### 2.8 表格

```html
<table border="1px">	<!--border是边框-->
    <thead>
        <tr>
            <th>ID</th>
            <th>姓名</th>
            <th>年龄</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>10</td><td>张三</td><td>20</td>
        </tr>
        <tr>
            <td>11</td><td>李四</td><td>20</td>
        </tr>
        <tr>
            <td>12</td><td>王五</td><td>20</td>
        </tr>
        <tr>
            <td>13</td><td>赵六</td><td>20</td>
        </tr>
    </tbody>
</table>
```

#### `<table>`：定义表格

```html
<table>
  <!-- 表格内容 -->
    <thead>表格的头 用来放标题之类的东西</thead>
    <tbody>表格的身体 放数据本体</tbody>
    <tfoot>表格的脚 放表格的脚注之类</tfoot>
</table>
```

> 不管你的行代码顺序如何。也就是说如果thead写在了tbody的后面，html显示时，还是以先thead后tbody显示



#### `<tr>`：定义表格中的一行。

```html
<tr>
  <!-- 行内单元格 -->
</tr>
```

#### `<th>`：定义表格中的表头单元格。

```html
<th>表头</th>
```

#### `<td>`：定义表格中的普通单元格。

```html
<td>单元格内容</td>
```



#### 案例

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>哦吼~</title>
</head>
<body>

<h1>用户列表</h1>
<table border="1">
    <thead>
        <tr>
            <th>ID</th>
            <th>头像</th>
            <th>姓名</th>
            <th>邮箱</th>
            <th>更多信息</th>
        </tr>
    </thead>

    <tbody>
        <tr>
            <td>1</td>
            <td>
                <img src="/static/bb.jpg" alt="" style="height: 50px">
            </td>
            <td>ajuicefans</td>
            <td>ajuicefans@qq.com</td>
            <td>
                <a href="https://www.baidu.com/" target="_blank">点击查看详细</a>
            </td>
        </tr>
    </tbody>
</table>

</body>
</html>
```

---



### 2.9 input系列（7个）

```html
（最普通的输入框，文本框）
<input type="text" />

（密码框，不显示具体内容）
<input type="password">

（选择文件的框）
<input type="file">

（单选框）
<input type="radio" name="n1">男
<input type="radio" name="n1">女

（复选框）
<input type="checkbox">篮球
<input type="checkbox">足球
<input type="checkbox">乒乓球
<input type="checkbox">棒球

（普通的按钮）
<input type="button" value="提交">

（可以提交表单的按钮）
<input type="submit" value="提交">
```



### 2.10 下拉框

```html
（单选的下拉框）
<select>
    <option>北京</option>
    <option>上海</option>
    <option>深圳</option>
</select>

（多选的下拉框 按住shift或ctrl下拉）
<select multiple>
    <option>北京</option>
    <option>上海</option>
    <option>深圳</option>
</select>
```



### 2.11 多行文本

```html
<textarea></textarea>
```



### 案例：用户注册

我自己写的

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>注册</title>
</head>
<body>

<h1>用户注册</h1>

<!--块级标签 一个占一整行-->
<div>
    用户名：<input type="text" />
</div>

<div>
    密码：<input type="password" />
</div>

<div>
    性别：
        <input type="radio" value="maie" />男
        <input type="radio" value="femaie" />女
</div>

<div>
    爱好：
        <input type="checkbox" />篮球
        <input type="checkbox" />足球
        <input type="checkbox" />乒乓球
</div>

<div>
    国家：
        <select name="city" >
            <option value="China">中国</option>
            <option value="US">美国</option>
            <option value="UK" selected>英国</option>
            <option value="India">印度</option>
        </select>
</div>

<div>
    擅长领域：
    <select multiple name="good_at">
        <option value="sports">运动</option>
        <option value="music">音乐</option>
        <option value="moives">电影</option>
    </select>
</div>

<div>
    备注：
    <textarea name="beizhu" id="" cols="30" rows="10"></textarea>
</div>

<div>
    <input type="submit">
</div>

</body>
</html>
```

<img src="F:\lifeProject\first-django\notes_django\images\2.png" alt="image-20230515222118343" style="zoom:67%;" />



视频里的

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>


<h1>用户注册</h1>
<div>
    用户名：<input type="text"/>
</div>
<div>
    密码：<input type="password"/>
</div>

<div>
    性别：
    <input type="radio">男
    <input type="radio">女
</div>

<div>
    爱好：
    <input type="checkbox">篮球
    <input type="checkbox">足球
    <input type="checkbox">乒乓球
</div>

<div>
    城市：
    <select>
        <option>北京</option>
        <option>上海</option>
        <option>深圳</option>
    </select>
</div>

<div>
    擅长领域：
    <select multiple>
        <option>打游戏</option>
        <option>睡觉</option>
        <option>吃饭</option>
        <option>刷抖音</option>
    </select>
</div>

<div>
    备注：<textarea></textarea>
</div>

<div>
    <input type="button" value="button按钮">
    <input type="submit" value="submit按钮">
</div>
</body>
</html>
```



### 知识点回顾和补充

1. 网站请求的流程
   ![5](F:\lifeProject\first-django\notes_django\images\5.png)

2. 一大堆的标签

   ```
   h/div/span/a/img/ul/li/table/input/textarea/select
   ```

3. 网络请求

   - 在浏览器的URL中写入地址，点击回车，访问。

     ```
     浏览器会发送数据过去，本质上发送的是字符串：
     "GET /explore http1.1\r\nhost:...\r\nuser-agent\r\n..\r\n\r\n"
     
     浏览器会发送数据过去，本质上发送的是字符串：
     "POST /explore http1.1\r\nhost:...\r\nuser-agent\r\n..\r\n\r\n数据库"
     ```

   - 浏览器向后端发送请求时

     - GET请求【URL方法 / 表单提交】

       - 现象：GET请求、跳转、向后台传入数据数据会 **<u>拼接</u>** 在URL上

         ```
         https://www.sogou.com/web?query=安卓&age=19&name=xx
         ```

         注意：GET请求数据会在URL中体现。

     - POST请求【表单提交】

       - 现象：提交数据不在URL中而是在请求体中。

![3](F:\lifeProject\first-django\notes_django\images\3.png)





### 案例：用户注册

- 新创建项目

- 创建Flask代码

  ```python
  from flask import Flask, render_template, request
  
  app = Flask(__name__)
  
  
  @app.route('/register', methods=['GET', "POST"])
  def register():
      if request.method == "GET":
          return render_template('register.html')
      	# 输入url的跳转是GET请求
  
      else:
          user = request.form.get("user")
          pwd = request.form.get("pwd")
          gender = request.form.get("gender")
          hobby_list = request.form.getlist("hobby") # 这里是list
          city = request.form.get("city")
          skill_list = request.form.getlist("skill")
          more = request.form.get("more")
          print(user, pwd, gender, hobby_list, city, skill_list, more)
          # 将用户信息写入文件中实现注册、写入到excel中实现注册、写入数据库中实现注册
  
          # 2.给用户再返回结果
          return "注册成功"
  
  
  if __name__ == '__main__':
      app.run()
  
  ```

- HTML代码

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Title</title>
  </head>
  <body>
  <h1>用户注册</h1>
  
      
  <form method="post" action="/register">
      <div>
          用户名：<input type="text" name="user"/>
      </div>
      <div>
          密码：<input type="password" name="pwd"/>
      </div>
      <div>
          性别：
          <input type="radio" name="gender" value="1">男
          <input type="radio" name="gender" value="2">女
      </div>
      <div>
          爱好：
          <input type="checkbox" name="hobby" value="10">篮球
          <input type="checkbox" name="hobby" value="20">足球
          <input type="checkbox" name="hobby" value="30">乒乓球
          <input type="checkbox" name="hobby" value="40">棒球
      </div>
  
      <div>
          城市：
          <select name="city">
              <option value="bj">北京</option>
              <option value="sh">上海</option>
              <option value="sz">深圳</option>
          </select>
      </div>
  
      <div>
          擅长领域：
          <select name="skill" multiple>
              <option value="100">吃饭</option>
              <option value="101">睡觉</option>
              <option value="102">打球</option>
          </select>
      </div>
  
      <div>
          备注：<textarea name="more"></textarea>
      </div>
  
      <input type="submit" value="submit按钮">
  </form>
  
  </body>
  </html>
  
  ```

  



### 案例：登录()

见代码示例。





页面上的数据，想要提交到后台（只有用户可以交互的才会提交到后台）：

- form标签包裹要提交的数据的标签。
  - 提交方式：`method="get"`
  - 提交的地址：`action="/xxx/xxx/xx"`
  - 在form标签里面必须有一个submit标签。
- 在form里面的一些标签：input/select/textarea
  - 一定要写name属性 `<input type="text" name="uu"/>`

![4](F:\lifeProject\first-django\notes_django\images\4.png)



### 总结

1. 称呼

   ```
   - 浏览器能够识别的标签（不专业）
   - HTML标签。
   
   什么是是HTML？超文本传输语言（与浏览器搭配）。
   ```

2. HTML标签（默认格式样式、以后通过手段可以修改）

3. HTML标签与编程语言无关

   - java + HTML
   - c# + HTML
   - php + HTML
   - python + HTML

4. 提醒：HTML标签比较多，标签还有很多很多，不必逐一学会。
