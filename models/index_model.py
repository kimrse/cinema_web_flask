import pandas as pd


def get_ids(conn):
    return pd.read_sql('''
    SELECT movie_id
    FROM movie''', conn)


def get_name(conn, id):
    cur = conn.cursor()
    name = cur.execute('''
        SELECT movie_name
        FROM movie
        WHERE movie_id = ?''', (id,)).fetchall()[0][0]
    return name


def get_duration(conn, id):
    cur = conn.cursor()
    duration = cur.execute('''
        SELECT movie_duration
        FROM movie
        WHERE movie_id = ?''', (id,)).fetchall()[0][0]
    return duration


def get_restriction(conn, id):
    cur = conn.cursor()
    restriction = cur.execute('''
        SELECT age_restriction
        FROM movie
        JOIN age USING (age_id)
        WHERE movie_id = ?''', (id,)).fetchall()[0][0]
    return restriction


def get_director(conn, id):
    cur = conn.cursor()
    director = cur.execute('''
        SELECT director_name
        FROM director_movie
        JOIN director USING (director_id)
        WHERE movie_id = ?''', (id,)).fetchall()[0][0]
    return director


def get_description(conn, id):
    cur = conn.cursor()
    description = cur.execute('''
        SELECT movie_description
        FROM movie
        WHERE movie_id = ?''', (id,)).fetchall()[0][0]
    return description


def get_genres(conn, id):
    cur = conn.cursor()
    genres = cur.execute('''
    SELECT genre_name
    FROM genre_movie
    JOIN genres USING (genre_id)
    WHERE movie_id = ?''', (id,)).fetchall()
    return genres


def get_actors(conn, id):
    cur = conn.cursor()
    actors = cur.execute('''
        SELECT actor_name
        FROM actor_movie
        JOIN actor USING (actor_id)
        WHERE movie_id = ?''', (id,)).fetchall()
    return actors

