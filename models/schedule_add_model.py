import pandas as pd


def get_titles(conn):
    titles = pd.read_sql('''
    SELECT movie_name FROM movie''', conn)
    return titles


def get_halls(conn):
    halls = pd.read_sql('''
    SELECT hall_name FROM hall''', conn)
    return halls


def get_prices(conn):
    prices = pd.read_sql('''
    SELECT price_list_price FROM price_list''', conn)
    return prices


def get_dates(conn):
    dates = pd.read_sql('''
    SELECT date FROM date''', conn)
    return dates


