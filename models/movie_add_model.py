import pandas as pd


def get_age(conn):
    return pd.read_sql('''
    SELECT age_id, age_restriction
    FROM age''', conn)


def get_actor(conn):
    return pd.read_sql('''
    SELECT actor_id, actor_name
    FROM actor
    ORDER by actor_name''', conn)


def get_director(conn):
    return pd.read_sql('''
    SELECT director_id, director_name
    FROM director''', conn)


def get_genre(conn):
    return pd.read_sql('''
    SELECT genre_id, genre_name
    FROM genres''', conn)


def add_movie(conn, title, dur, desc, age_id, act_list, dir_list, genre_list, url, rating):
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO movie (movie_name, movie_duration, movie_description, 
            age_id, poster_url, movie_rating, revenue)
        VALUES (?, ?, ?, ?, ?, ?, 0) ''', (title, dur, desc, age_id, url, rating)
    )
    id = cur.lastrowid

    for actor_id in act_list:
        cur.execute('''
            INSERT INTO actor_movie (actor_id, movie_id)
            VALUES (?, ?)''', (actor_id, id))

    for dir_id in dir_list:
        cur.execute('''
            INSERT INTO director_movie (director_id, movie_id)
            VALUES (?, ?)''', (dir_id, id))

    for genre_id in genre_list:
        cur.execute('''
            INSERT INTO genre_movie (genre_id, movie_id)
            VALUES (?, ?)''', (genre_id, id))

    conn.commit()


def add_actor(conn, actor_name):
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO actor (actor_name)
    VALUES (?) ''', (actor_name,))
    conn.commit()


def add_director(conn, director_name):
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO director (director_name)
    VALUES (?) ''', (director_name,))
    conn.commit()


def add_genre(conn, genre_name):
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO genres (genre_name)
    VALUES (?) ''', (genre_name,))
    conn.commit()