from flask import Flask, render_template
import subprocess
import simplejson
from flask import jsonify
from models import app
import json
from mlb import msf, get_stat, get_scores, get_standings
from flask import abort
from ohmysportsfeedspy import MySportsFeeds


@app.route("/ballers/api/scores/<date>")
def scores(date):

    daily_scores = msf.msf_get_data(league='mlb',season='current',feed='daily_games',format='json', date = date,force = True)
    cleaned_scores = get_scores(daily_scores['games'])


    with open('templates/temp.json', 'w') as t:
        json.dump(cleaned_scores, t)

    return render_template('temp.json')

@app.route("/ballers/api/stats")
def stats():
    stats = msf.msf_get_data(league = 'mlb', feed = 'seasonal_player_stats',season = 'current', format = 'json')

    types = ['homeruns', 'battingAvg', 'runsBattedIn', 'wins', 'earnedRunAvg', 'pitcherStrikeouts']
    # 'wins', 'earnedRunAvg', 'pitcherStrikeouts'
    allStat = []

    for each in types:
        val = {each : get_stat(stats['playerStatsTotals'],each) }
        allStat.append(val)

    with open('templates/temp.json', 'w') as t:
        json.dump(allStat, t)

    return render_template('temp.json')

@app.route("/ballers/api/standings")
def standings():
    standings = msf.msf_get_data(league = 'mlb', feed = 'seasonal_standings', season = 'current', format = 'json', stats = None)

    standings = get_standings(standings['teams'])

    with open('templates/temp.json', 'w') as t:
        json.dump(standings, t)

    return render_template('temp.json')


if __name__ == '__main__':
    app.run(debug=True)
