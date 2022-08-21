from flask import Flask, render_template, request, redirect
from replit import db
app = Flask(__name__)

now_visitors = 1

@app.route('/', methods=['GET','POST'])
def mainpage():
    global now_visitors
    now_visitors += 1
    return render_template('index.html', value=now_visitors)

@app.route('/upload', methods=['GET','POST'])
def upload_scode():
    return render_template('add_scode.html')

@app.route('/post', methods=['GET','POST'])
def post():
    keys = db.keys()
    if request.method == 'POST':
        the_code = request.form['thecode']
        the_code = str(the_code)

        code_name = request.form['codename']
        code_name = str(code_name)
        
        if the_code == 'no_code' or code_name == '':
            return redirect('/upload')
        elif code_name in keys:
            return redirect('/upload')
        else:
            db[f'{code_name}'] = the_code
            return render_template('scodes.html', value=the_code) # 이 코드 말고 다른것으로 고쳐야됨  (정보 db에 올리고 전체 스코드 목록 페이지로 리다이렉트)

@app.route("/scodes")
def scodes():

    
if __name__ == '__main__':
    app.run()
