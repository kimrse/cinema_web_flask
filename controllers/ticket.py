from app import app
from flask import render_template, request, redirect, url_for

from models.ticket_model import *
from utils import get_db_connection


@app.route('/movie/ticket', methods=['GET', 'POST'])
def ticket():
    conn = get_db_connection()

    ticket_title = request.form.get('ticket-name')
    ticket_date = request.form.get('ticket-date')
    ticket_time = request.form.get('ticket-time')
    ticket_hall = request.form.get('ticket-hall')
    ticket_price = request.form.get('ticket-price')

    df_tickets = get_tickets(conn, ticket_title, ticket_date, ticket_hall, ticket_time)

    if request.values.get("sold_id"):
        price_id = request.values.get("sold_id")
        numb = request.values.get("sold_numb")
        price = request.values.get("sold_price")
        sell_ticket(conn, price_id, numb, price)
        return redirect(url_for('index'))

    html = render_template(
        'ticket.html',
        ticket_date = ticket_date, ticket_time = ticket_time,
        ticket_hall = ticket_hall, ticket_title = ticket_title,
        ticket_price = ticket_price, df_tickets = df_tickets,
        len = len
    )
    return html



