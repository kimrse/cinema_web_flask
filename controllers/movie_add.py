import os
from app import app
from flask import redirect, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

from models.movie_add_model import *
from utils import get_db_connection


@app.route('/movie_add', methods=['GET', 'POST'])
def movie_add():
    conn = get_db_connection()

    age_df = get_age(conn)
    actor_df = get_actor(conn)
    director_df = get_director(conn)
    genre_df = get_genre(conn)

    if request.form.get('add_title'):
        title = request.form.get('add_title')
        dur = request.form.get('add_dur')
        desc = request.form.get('add_description')
        age_id = request.form.get('add_age')
        act_list = request.form.getlist('add_actor')
        dir_list = request.form.getlist('add_dir')
        genre_list = request.form.getlist('add_genre')
        rating = request.form.get('add_rating')

        file = request.files['add_poster']
        if file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            url = "/static/posters/" + filename
        else:
            url = None

        add_movie(conn, title, dur, desc, age_id, act_list, dir_list, genre_list, url, rating)
        return redirect(url_for('index'))
        
    elif request.form.get('new_actor') != None:
        actor_name = request.form.get('new_actor')
        add_actor(conn, actor_name)
        return redirect(url_for('movie_add'))
    elif request.form.get('new_director') != None:
        director_name = request.form.get('new_director')
        add_director(conn, director_name)
        return redirect(url_for('movie_add'))
    elif request.form.get('new_genre') != None:
        genre = request.form.get('new_genre')
        add_genre(conn, genre)
        return redirect(url_for('movie_add'))


    html = render_template(
        'movie_add.html',
        age = age_df,
        actor = actor_df,
        director = director_df,
        genre = genre_df,
        len = len,
        range = range)

    return html