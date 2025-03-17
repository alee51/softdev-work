from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from database import get_db

story_bp = Blueprint('story', __name__, url_prefix='/story')

@story_bp.route('/home')
def home():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    db = get_db()
    # Retrieve all stories from the database
    stories = db.execute('SELECT id, title FROM stories').fetchall()
    return render_template('story/home.html', stories=stories)

@story_bp.route('/new', methods=['GET', 'POST'])
def new_story():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        user_id = session.get('user_id')
        if not user_id:
            return redirect(url_for('auth.login'))
        db = get_db()
        db.execute('INSERT INTO stories (title, creator_id) VALUES (?, ?)', (title, user_id))
        story_id = db.execute('SELECT last_insert_rowid()').fetchone()[0]
        db.execute('INSERT INTO contributions (story_id, user_id, content) VALUES (?, ?, ?)', (story_id, user_id, content))
        db.commit()
        return redirect(url_for('story.home'))
    return render_template('story/new_story.html')

@story_bp.route('/<int:story_id>', methods=['GET', 'POST'])
def add_to_story(story_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    db = get_db()
    # Check if the user has already contributed to the story
    user_contribution = db.execute('SELECT * FROM contributions WHERE story_id = ? AND user_id = ?', (story_id, user_id)).fetchone()
    if user_contribution:
        flash('You have already contributed to this story and cannot add to it again.')
        return redirect(url_for('story.home'))
    if request.method == 'POST':
        content = request.form['content']
        db.execute('INSERT INTO contributions (story_id, user_id, content) VALUES (?, ?, ?)', (story_id, user_id, content))
        db.commit()
        return redirect(url_for('story.home'))
    latest_contribution = db.execute('SELECT content FROM contributions WHERE story_id = ? ORDER BY id DESC LIMIT 1', (story_id,)).fetchone()
    return render_template('story/add_to_story.html', story_id=story_id, latest_contribution=latest_contribution)