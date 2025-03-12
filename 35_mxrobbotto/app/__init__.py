from flask import Flask, render_template, redirect, url_for, session
from auth import auth_bp
from story import story_bp
from database import init_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

app.register_blueprint(auth_bp)
app.register_blueprint(story_bp)

@app.before_first_request
def initialize_database():
    init_db()

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('story.home'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
