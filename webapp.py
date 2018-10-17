from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/H1")
def render_Home():
    return render_template('Home.html')

@app.route("/p1")
def render_page1():
    return render_template('Page1.html')

@app.route("/p2")
def render_page2():
    return render_template('Page2.html')

@app.route("/p3")
def render_page3():
  return render_template('Page3.html')

<<<<<<< HEAD
@app.route("/r1")
def render_response1():
    return

@app.route("/r2")
def render_response2():
    return

@app.route("/r3")
def render_response3():
    return

=======
@app.route("/")
def render_res1():
    return render_template('Response1.html')
>>>>>>> 3a3773f180ac246ed2bd20521f657ef6a5613365
if __name__=="__main__":
    app.run(debug=False, port=54321)
