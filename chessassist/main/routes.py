from flask import Blueprint, render_template

#blueprint instance
main = Blueprint('main', __name__)

#blueprint(main) routes
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')