from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/genre')
def genre():
    return render_template('genre.html')



@app.route('/languages')
def languages():
    return render_template('languages.html')

@app.route('/english')
def english ():
    return render_template('english.html')

@app.route('/korean')
def korean():
    return render_template('korean.html')

@app.route('/hindi')
def hindi():
    return render_template('hindi.html')

@app.route('/action')
def action ():
    return render_template('action.html')

@app.route('/drama')
def drama ():
    return render_template('drama.html')

@app.route('/comedy')
def comedy ():
    return render_template('comedy.html')



if __name__ == '__main__':
    app.run(debug=True)
