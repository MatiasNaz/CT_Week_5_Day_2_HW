from app import app
from flask import render_template

@app.route('/')
def homepage():
    my_list = []
    my_second_list = sorted(my_list)
    return render_template('index.html', my_title = "This is the HOME page", name='Shoha', my_list = my_second_list)

@app.route('/testing')
def test():
    return {'hello':'world'}

@auth.route('/logout')
def logMeOut():
    logout_user()
    return redirect(url_for('auth.logMeIn'))