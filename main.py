from flask import Flask, render_template
import subprocess
import simplejson
from flask import jsonify
from models import app
import json
from mlb import msf, get_stat
from flask import abort
from ohmysportsfeedspy import MySportsFeeds






@app.route("/ballers/api/scores/<date>")
def scores(date):

    stats = msf.msf_get_data(league='mlb',season='current',feed='daily_games',format='json', date = date,force = True)

    #will open and write to the temporary json file.
    with open('templates/temp.json', 'w') as t:
        json.dump(stats['games'], t)

    return render_template('temp.json')

@app.route("/ballers/api/stats")
def stats():
    stats = msf.msf_get_data(league = 'mlb', feed = 'seasonal_player_stats',season = 'current', format = 'json')

    types = ['homeruns', 'battingAvg', 'runsBattedIn', 'wins', 'earnedRunAvg', 'pitcherStrikeouts']
    # 'wins', 'earnedRunAvg', 'pitcherStrikeouts'
    allStat = []

    for each in types:
        allStat.append(get_stat(stats['playerStatsTotals'],each))

    with open('templates/temp.json', 'w') as t:
        json.dump(allStat, t)

    return render_template('temp.json')


if __name__ == '__main__':
    app.run(debug=True)
