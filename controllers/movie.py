import sqlite3
from app import app
from flask import render_template, request, session, redirect, url_for
from models.movie_model import *
from utils import get_db_connection


@app.route('/movie')
def movie():
    conn = get_db_connection()

    if request.values.get('delete'):
        movie_name = request.values.get('delete')
        delete_movie(conn, movie_name)
        return redirect(url_for('index'))
        
    title_req = request.args.get('title')
    #Получаем инфо о фильме из базы
    title = get_title(conn, title_req)
    duration = get_duration(conn, title_req)
    restriction = get_restriction(conn, title_req)
    director = get_director(conn, title_req)
    actors = get_actors(conn, title_req)
    description = get_description(conn, title_req)
    genres = get_genres(conn, title_req)
    poster = get_poster(conn, title_req)
    rating = get_rating(conn, title)
    revenue = get_revenue(conn, title)
    #Получаем инфо о сеансах из базы
    dates = get_date(conn, title_req)
    schedule = get_schedule(conn, title_req)
    #Словарь дней недели
    weekday_dict = {
        "0":"Sunday", "1":"Monday",
        "2":"Tuesday", "3":"Wednesday",
        "4":"Thursday", "5":"Friday",
        "6":"Saturday", "7":"Sunday"
    }

    html = render_template('movie.html',
        title = title, duration = duration,
        restriction = restriction, director = director,
        actors = actors, description = description,
        genres = genres, poster = poster,
        dates = dates, schedule = schedule,
        weekday_dict = weekday_dict, len = len,
        revenue = revenue, rating = rating, 
        range = range, min = min)
    return html