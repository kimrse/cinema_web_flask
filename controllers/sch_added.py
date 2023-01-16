import sqlite3

from numpy import std
from app import app
from flask import render_template, request, session

from models.sch_added_model import *
from utils import get_db_connection



@app.route('/schedule/add/done', methods=['GET', 'POST'])
def sch_added():
    conn = get_db_connection()
    #получаем данные из формы
    movie_name = request.form.get('title-box')
    hall_name = request.form.get('hall-radio')
    date = request.form.get('date')
    hour = str(request.form.get('hour'))
    minute = str(request.form.get('minute'))
    stand_price = request.form.get('price-std')
    vip_price = request.form.get('price-vip')
    coach_price = request.form.get('price-coach')
    #конвертируем данные в id
    movie_id = get_movie_id(conn, movie_name)
    date_id = get_date_id(conn, date)
    hall_id = get_hall_id(conn, hall_name)
    std_id = get_price_id(conn, stand_price)
    vip_id = get_price_id(conn, vip_price)
    coach_id = get_price_id(conn, coach_price)
    #задаем формат времени
    if int(minute) in range(10):
        if hour == "9":
            time = "0" + hour + ":" + "0" + minute
        else:
            time = "0" + hour + ":" + minute
    else:
        if hour == "9":
            time = "0" + hour + ":" + minute
        else:
            time = hour + ":" + minute
            
    #добавляем в расписание и запоминаем id
    sch_id = add_schedule(conn, time, date_id, hall_id, movie_id)
    #добавляем цены и запоминаем id
    pr_id = set_price(conn, std_id, vip_id, coach_id, sch_id, hall_id)
    #создаем билеты
    create_ticket(conn, pr_id, hall_id)

    html = render_template(
        'sch_added.html', 
        time=time, date=date, 
        hall_name=hall_name, movie_name=movie_name,
        stand_price=stand_price,vip_price=vip_price,
        coach_price=coach_price,
        #цены
        movie_id = movie_id, hall_id=hall_id,
        date_id = date_id, std_id = std_id,
        vip_id = vip_id, coach_id = coach_id,
        sch_id = sch_id
    )
    return html