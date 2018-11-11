from flask import (
    render_template,
    url_for,
    flash,
    redirect,
)
from flaskpro import app
from flaskpro.forms import UserRegistrationForm, UserLoginForm
''' The models must imported after database created not before !!!! '''
from flaskpro.models import User, Post


''' 
route in flask use to map to different pages, and decorator in flask use to add 
additional functionality to existing function and in this case this a Prout decorator 
will handle all of the complicated back-end
'''


posts = [
    {
        'title': 'Python',
        'author': 'Dilshad Abdulla',
        'content': "route in flask use to map to different pages, and decorator in flask use to add\
                    additional functionality to existing function and in this case this a Prout decorator \
                    will handle all of the complicated back-end",
        'publish_date': 'November 11 2018'
    },
    {
        'title': 'Google',
        'author': 'Dilshad Abdulla',
        'content': "route in flask use to map to different pages, and decorator in flask use to add\
                    additional functionality to existing function and in this case this a Prout decorator \
                    will handle all of the complicated back-end",
        'publish_date': 'April 12 2016'
    },
    {
        'title': 'Djnago',
        'author': 'Dilshad Abdulla',
        'content': "route in flask use to map to different pages, and decorator in flask use to add\
                    additional functionality to existing function and in this case this a Prout decorator \
                    will handle all of the complicated back-end",
        'publish_date': 'January 3 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    template_name = 'index.html'
    return render_template(template_name, title='Home', posts=posts)


@app.route('/about')
def about():
    template_name = 'about.html'
    return render_template(template_name, title='About us')


@app.route('/account/register', methods=['GET', 'POST'])
def user_register():
    template_name = 'registration/registration_form.html'
    form = UserRegistrationForm()
    if form.validate_on_submit():
        flash(f'You have been successfully registered for the username {form.username.data}',
              'success')
        return redirect(url_for('user_login'))
    context = {
        'title': 'Register',
    }
    return render_template(template_name, title='Register', form=form)


@app.route('/account/login', methods=['GET', 'POST'])
def user_login():
    template_name = 'registration/login_form.html'
    form = UserLoginForm()
    if form.validate_on_submit():
        if form.email.data == 'hello@gmail.com' and form.password.data == 'hello123':
            flash('You have successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Unsuccessful , please check the your detail', 'danger')
    return render_template(template_name, title='Login', form=form)
