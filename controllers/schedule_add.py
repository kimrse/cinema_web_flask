import sqlite3
from app import app
from flask import render_template, request, session

from models.schedule_add_model import *
from utils import get_db_connection


@app.route('/schedule/add', methods=['GET', 'POST'])
def schedule_add():
    conn = get_db_connection()

    titles = get_titles(conn) 
    halls = get_halls(conn)
    prices = get_prices(conn)
    dates = get_dates(conn)

    html = render_template(
        'schedule_add.html',
        combo_box = titles,
        radio_box = halls,
        price_box = prices,
        date_box = dates,
        len = len,
        range = range
    )
    return html