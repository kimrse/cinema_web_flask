import sqlite3
from app import app
from flask import render_template, request, session

from models.schedule_model import *
from utils import get_db_connection


@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    conn = get_db_connection()

    date = get_every_date(conn)
    hall = get_every_hall(conn)
    schedule = get_schedule(conn)

    html = render_template('schedule.html',
        date = date,
        hall = hall,
        schedule = schedule,
        #prices = prices,
        range = range,
        len = len)
    return html