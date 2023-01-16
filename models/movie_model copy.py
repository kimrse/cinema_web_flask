import pandas as pd

def get_title(conn, value):
    cur = conn.cursor()
    title = cur.execute(f'''
        SELECT movie_name 
        FROM movie 
        WHERE movie_name = ?
        ''', (value,)).fetchall()[0][0]
    return title


def get_duration(conn, value):
    cur = conn.cursor()
    duration = cur.execute('''
        SELECT movie_duration
        FROM movie
        WHERE movie_name = ?''', (value,)).fetchall()[0][0]
    return duration


def get_restriction(conn, value):
    cur = conn.cursor()
    restriction = cur.execute('''
        SELECT age_restriction
        FROM movie
        JOIN age USING (age_id)
        WHERE movie_name = ?''', (value,)).fetchall()[0][0]
    return restriction


def get_director(conn, value):
    cur = conn.cursor()
    director = cur.execute('''
        SELECT director_name
        FROM movie
        JOIN director_movie USING (movie_id)
        JOIN director USING (director_id)
        WHERE movie_name = ?''', (value,)).fetchall()[0][0]
    return director


def get_description(conn, value):
    cur = conn.cursor()
    description = cur.execute('''
        SELECT movie_description
        FROM movie
        WHERE movie_name = ?''', (value,)).fetchall()[0][0]
    return description


def get_genres(conn, value):
    cur = conn.cursor()
    genres = cur.execute('''
    SELECT genre_name
    FROM movie
    JOIN genre_movie USING (movie_id)
    JOIN genres USING (genre_id)
    WHERE movie_name = ?''', (value,)).fetchall()
    return genres


def get_actors(conn, value):
    cur = conn.cursor()
    actors = cur.execute('''
        SELECT actor_name
        FROM movie
        JOIN actor_movie USING (movie_id)
        JOIN actor USING (actor_id)
        WHERE movie_name = ?''', (value,)).fetchall()
    return actors


def get_poster(conn, value):
    cur = conn.cursor()
    poster = cur.execute('''
        SELECT poster_url
        FROM movie
        WHERE movie_name = ?''', (value,)).fetchall()[0][0]
    return poster


def get_date(conn, title):
    return pd.read_sql('''
        SELECT DISTINCT date, strftime('%w', date) AS weekday
        FROM movie
        JOIN schedule USING (movie_id)
        JOIN date USING (date_id)
        WHERE movie_name = (?)''', conn, params=(title,))


def get_schedule(conn, title):
    return pd.read_sql('''
        SELECT DISTINCT schedule_time, hall_name, price_list_price, date
        FROM price
        JOIN price_list USING (price_list_id)
        JOIN schedule USING (schedule_id)
        JOIN movie USING (movie_id)
        JOIN hall USING (hall_id)
        JOIN date USING (date_id)
        WHERE movie_name = ?
        GROUP BY schedule_time, hall_name
        ORDER BY date, schedule_time, price_list_price
        ''', conn, params=(title,))


def delete_movie(conn, movie_name):
    cur = conn.cursor()
    cur.execute('''
    DELETE FROM movie
    WHERE movie_name = (?)''', (movie_name,))
    conn.commit()