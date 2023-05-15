# Day15 初识Django

- python知识点：函数、面向对象
- 前端开发：HTML、CSS、JavaScript、jQuery、BootStrap
- MySQL数据库
- Python的Web框架
  - Flask，自身短小精悍 + 第三方组件
  - Django，内部已经集成了很多组件 + 第三方组件

---



## 1.安装Django

```
pip install django
```

```
c:\python39
	- python.exe
	- Scripts
		- pip.exe
		- django-admin.exe	【工具，创建django项目中的文件和文件夹】
    - Lib
    	- 内置模块
    	- site-packages
    		- openpyxl
    		- python-docx
    		- flask
    		- django		【框架的源码】
```



## 2.创建项目

> django中项目会有一些默认的文件和默认的文件夹

### 2.1 在终端（用命令创建项目）

- 打开终端

- 进入某个目录（项目存放位置）（尽量不要有中文路径）

  ```
  cd 目录路径
  ```

- 执行命令创建项目

  ```
  "c:\python39\Scripts\django-admin.exe" startproject 项目名称
  ```

  ```
  # 如果 c:python39\Scripts 已经加入环境变量了，则可以直接
  django-admin startproject 项目名称
  ```



### 2.2 在Pycharm专业版

注意：

```
- python解释器目录...
- 项目目录：F:\pycode
```

---

特殊说明：

- 命令行。创建的项目是标准的

- pycharm，在标准的基础上默认加了点东西

  - 一个 templates目录 （不用可删除）
  - 在settings.py中默认生成了templates的目录路径（命令行这块的 [] 中什么也没有）（不用可删除）

  <img src="https://github.com/ajuicefans/first-django/blob/main/notes_django/images/1.png?raw=true" alt="1" style="zoom:67%;" />

---



### 项目的默认文件介绍

- mange.py：【项目的管理，启动项目、创建app、数据库管理】（不用修改，里面是什么就让他是什么就行，但要使用）

- first-django

  - __ init__.py：
  - settings.py：【项目的配置文件】（连接的数据库的信息）（常常操作的文件）
  - urls.py：（flask中 url和函数放在一起）【Django中，url和函数的对应关系会写在这里：url→函数】（常常操作的文件）

  - asgi.py：【接受网络请求】（默认的，不用动，django默认会使用这些东西）（支持异步）
  - wsgi.py：【接受网络请求】（默认的，不用动，django默认会使用这些东西）（同步式的）

---



## 3.创建APP

> 相当于flask中的蓝图

```python
- 项目
（每个app中有 各自独立 的：表结构、函数、HTML模板、CSS、JS）
	- app，用户管理
	- app，订单管理
	- app，后台管理
	- app，网站
	- app，API
	..
注意：我们开发比较简洁，用不到多app，一般情况下，项目下创建1个app即可

# 创建app
(在项目目录下):python3.9 manage.py startapp app01
```

app01中的文件

- __ init__.py
- admin.py：【固定，不用动】（在django后台默认提供admin后台管理的功能，在项目开发时很少用到）
- apps.py：【固定，不用动】（app启动类）
- migrations：【固定，不用动】（修改数据库时做记录的_数据库字段变更记录）
  - __ init__.py
- models.py：**【重要】**（对数据库进行操作）
- tests.py：【固定，不用动】（单元测试）
- views.py：**【重要】**（函数，**urls.py**调用url时会指向这里的函数）（视图函数会写在这）

---



## 4.快速上手

