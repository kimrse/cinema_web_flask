import pandas as pd


def get_every_date(conn):
    cur = conn.cursor()
    date = cur.execute('''
        SELECT date 
        FROM date
        ORDER BY date ASC''').fetchall()
    return date


def get_every_hall(conn):
    cur = conn.cursor()
    hall = cur.execute('''
        SELECT hall_name FROM hall''').fetchall()
    return hall


def get_schedule(conn):
    schedule = pd.read_sql('''
        SELECT price_id, schedule_id, price_list_id, schedule_time, movie_name, price_list_price, place_type_id, hall_name, date
        FROM price
        JOIN price_list USING (price_list_id)
        JOIN schedule USING (schedule_id)
        JOIN movie USING (movie_id)
        JOIN date USING (date_id)
        JOIN hall USING (hall_id)
        GROUP BY movie_name, date, schedule_time
        ORDER BY date, schedule_time ASC
        ''', conn)
    return schedule
