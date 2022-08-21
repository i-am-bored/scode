from flask import Flask, render_template, request
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
    if request.method == 'POST':
        value = request.form['thecode']
        value = str(value)
        print(value)
    return render_template('post.html', value=value)
    
if __name__ == '__main__':
    app.run()
