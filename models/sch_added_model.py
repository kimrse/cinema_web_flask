import pandas as pd


def get_date_id(conn, date):
    cur = conn.cursor()
    id = cur.execute('''
        SELECT date_id FROM date
        WHERE date = (:date)''', {"date":date}
    ).fetchall()[0][0]
    return id

def get_hall_id(conn, hall):
    cur = conn.cursor()
    id = cur.execute('''
    SELECT hall_id FROM hall
    WHERE hall_name = (:hall)''', {"hall":hall}).fetchall()[0][0]
    return id


def get_movie_id(conn, movie):
    cur = conn.cursor()
    id = cur.execute('''
        SELECT movie_id FROM movie
        WHERE movie_name = (:movie)''', {"movie":movie}
    ).fetchall()[0][0]
    return id


def get_price_id(conn, price):
    cur = conn.cursor()
    id = cur.execute('''
        SELECT price_list_id FROM price_list
        WHERE price_list_price = (:price)''', {"price":price}
    ).fetchall()[0][0]
    return id


def add_schedule(conn, schedule_time, date_id, hall_id, movie_id):
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO schedule (schedule_time, date_id, hall_id, movie_id) 
        VALUES (?,?,?,?)''', (schedule_time, date_id, hall_id, movie_id,)
    )
    conn.commit()
    return cur.lastrowid

def set_price(conn, std_price, vip_price, coach_price, schedule_id, hall_id):
    cur = conn.cursor()
    type_id = 1
    if hall_id == 2:
        price_ids = []
        for price in [std_price, vip_price]:
            cur.execute('''
                INSERT INTO price (place_type_id, price_list_id, schedule_id)
                VALUES (?,?,?)''', (type_id, price, schedule_id)
            )
            price_ids.append(cur.lastrowid)
            type_id += 1
    else:    
        price_ids = []
        for price in [std_price, vip_price, coach_price]:
            cur.execute('''
                INSERT INTO price (place_type_id, price_list_id, schedule_id)
                VALUES (?,?,?)''', (type_id, price, schedule_id)
            )
            price_ids.append(cur.lastrowid)
            type_id += 1
    conn.commit()
    return price_ids


def create_ticket(conn, price_ids, hall_id):
    cur = conn.cursor()
    #первый зал
    if hall_id == 1:
        place_number = 1
        #заполняем обычные места
        for i in range(100):
            cur.execute('''
                INSERT INTO ticket (price_id, place_number, ticket_sold)
                VALUES (?, ?, 0)''', (price_ids[0], place_number)
            )
            place_number += 1
        #заполняем vip места
        for i in range(141):
            cur.execute('''
                INSERT INTO ticket (price_id, place_number, ticket_sold)
                VALUES (?, ?, 0)''', (price_ids[1], place_number)
            )
            place_number += 1
        #заполняем диваны
        for i in range(9):
            cur.execute('''
                INSERT INTO ticket (price_id, place_number, ticket_sold)
                VALUES (?, ?, 0)''', (price_ids[2], place_number)
            )
            place_number += 1
    #второй зал
    elif hall_id == 2:
        place_number = 1
        #заполняем обычные места
        for i in range(45):
            cur.execute('''
                INSERT INTO ticket (price_id, place_number, ticket_sold)
                VALUES (?, ?, 0)''', (price_ids[0], place_number)
            )
            place_number += 1
        #заполняем vip места
        for i in range(80):
            cur.execute('''
                INSERT INTO ticket (price_id, place_number, ticket_sold)
                VALUES (?, ?, 0)''', (price_ids[1], place_number)
            )
            place_number += 1
    conn.commit()
