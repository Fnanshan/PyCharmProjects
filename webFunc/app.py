import hashlib

import mysql

print('# 使用Web框架Flask')

# from flask import Flask
# from flask import request
#
# app = Flask(__name__)
#
# print(app)
#
#
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return '<h1>Home</h1>'
#
#
# @app.route('/signin', methods=['GET'])
# def signin_form():
#     return '''<form action="/signin" method="post">
#               <p><input name="username"></p>
#               <p><input name="password" type="password"></p>
#               <p><button type="submit">Sign In</button></p>
#               </form>'''
#
#
# @app.route('/signin', methods=['POST'])
# def signin():
#     # 需要从request对象读取表单内容
#     if request.form['username'] == 'admin' and request.form['password'] == 'password':
#         return '<h3>Hello, admin!</h3>'
#     return '<h3>Bad username or password.</h3>'
#
#
# if __name__ == '__main__':
#     app.run()

print('# 使用模板')

from flask import Flask, request, render_template

app = Flask(__name__)
print(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html', page_list=[1, 2, 3, 4, 5])


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    conn = mysql.connector.connect(user='root', password='root', database='test')
    cursor = conn.cursor()

    # 没有输入用户名/密码
    if username == '' or password == '':
        return render_template('form.html', message='please input username or password', username=username)

    # 数据库---查询操作
    try:
        cursor.execute(r"select * from `user` where username=%s", (username,))
        result = cursor.fetchall()
        print(result)
        # result[0][1] == daemon    result[0][2] == 1234
    finally:
        cursor.close()
        conn.close()

    # 判断用户名、密码是否正确
    if username == result[0][1] and password == result[0][2]:
        return render_template('signinORregister_ok.html', username=username)
    return render_template('form.html', message='username or password error!', username=username)


@app.route('/register', methods=['GET'])
def register_form():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    re_password = request.form['re_password']
    md5_password = hashlib.md5()
    md5_password.update(password.encode('utf-8'))
    print('md5_password.hexdigest :', md5_password.hexdigest())

    conn = mysql.connector.connect(user='root', password='root', database='test')
    cursor = conn.cursor()

    # 数据库---增加用户操作
    try:
        cursor.execute('select username from `user` where username=%s', (username,))
        result = cursor.fetchall()
        print('result :', result)   # result,表示数据库存在这个username； not result, 表示数据库不存在这个username,可以执行insert操作
        if result:                  # 数据唯一性检查
            return render_template('register.html', message='用户名已存在，清直接登录!', username=username)
        elif password != re_password:
            return render_template('register.html', message='两次输入的密码不一致,请检查后重新输入!', username=username)
        elif not username or not password:
            return render_template('register.html', message='用户名和密码不能为空，请检查后重新输入！', username=username)
        print('执行insert操作')
        cursor.execute(r"INSERT INTO user (username, password) VALUES (%s, %s)", [username, md5_password.hexdigest()])
    except mysql.connector.errors.ProgrammingError as e:
        print(e)
    finally:
        conn.commit()
        cursor.close()
        conn.close()
    return render_template('signinORregister_ok.html', username=username)


if __name__ == '__main__':
    app.run()