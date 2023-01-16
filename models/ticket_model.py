import pandas as pd


def get_tickets(conn, title, date, hall, time):
    return pd.read_sql('''
        SELECT price_id, place_number AS Place_number, type AS Place_type, price_list_price AS Price, ticket_sold
        FROM ticket
        JOIN price USING (price_id)
        JOIN place_type USING (place_type_id)
        JOIN price_list USING (price_list_id)
        JOIN schedule USING (schedule_id)
        JOIN movie USING (movie_id)
        JOIN hall USING (hall_id)
        JOIN date USING (date_id)
        WHERE movie_name = (?) AND date = (?) 
            AND schedule_time = (?) AND hall_name = (?)
        ''', conn, params=(title, date, time, hall))


def sell_ticket(conn, price_id, place_numb, price):
    cur = conn.cursor()
    cur.execute('''
    UPDATE ticket SET ticket_sold = 1
    WHERE price_id = (?) AND place_number = (?) ''', (price_id, place_numb))
    title = cur.execute('''
    SELECT movie_name
    FROM price
    JOIN schedule USING (schedule_id)
    JOIN movie USING (movie_id)
    WHERE price_id = (?)''', (price_id,)).fetchall()[0][0]
    cur.execute('''
    UPDATE movie SET revenue = revenue + (?)
    WHERE movie_name = (?) ''', (price, title))
    conn.commit()