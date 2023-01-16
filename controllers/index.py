import sqlite3
from app import app
from flask import render_template, request, session

from models.index_model import *
from utils import get_db_connection


@app.route('/')
def index():
    conn = get_db_connection()
    ids = get_ids(conn)
    # создаем списки для каждой категории
    name = []
    duration = []
    restriction = []
    director = []
    actors = []
    description = []
    genres = []
    # добавляем значения из базы в списки
    #range(1, count + 1)
    for i in range(len(ids)):
        id = int(ids.loc[i, "movie_id"])
        name.append(get_name(conn, id))
        duration.append(get_duration(conn, id))
        restriction.append(get_restriction(conn, id))
        director.append(get_director(conn, id))
        actors.append(get_actors(conn, id))
        description.append(get_description(conn, id))
        genres.append(get_genres(conn, id))

    html = render_template(
        'index.html',
        name=name, duration=duration,
        restriction=restriction, director=director,
        actors=actors, description=description,
        genres=genres,

        range=range,
        len=len
    )

    return html
