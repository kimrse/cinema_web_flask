from flask import Flask, render_template, session

UPLOAD_FOLDER = './static/posters'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'svg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'



import controllers.index
import controllers.movie
import controllers.schedule
import controllers.schedule_add
import controllers.sch_added
import controllers.ticket
import controllers.movie_add



