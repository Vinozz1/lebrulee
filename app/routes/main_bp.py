from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main_bp.route('/learn')
def learn():
    return render_template('learn.html')

@main_bp.route('/news')
def news():
    return render_template('news.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')
