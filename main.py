from flask import Flask, render_template
import subprocess
import simplejson
from flask import jsonify
from models import app
from flask import abort
from ohmysportsfeedspy import MySportsFeeds






@app.route("/ballers/api/")
def index():
    msf = MySportsFeeds(version="2.0", verbose = True)
    msf.authenticate("ea5ffd04-787e-4b3b-a516-0ead12", 'MYSPORTSFEEDS')
    stats = msf.msf_get_data(league='mlb',season='current',feed='daily_games',format='json', date = '20190426',force = True)
    print(type(stats))
    return render_template(stats)




if __name__ == '__main__':
    app.run(debug=True)
