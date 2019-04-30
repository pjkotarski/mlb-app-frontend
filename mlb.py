from ohmysportsfeedspy import MySportsFeeds
import simplejson

msf = MySportsFeeds(version="2.0", verbose = True)
msf.authenticate("ea5ffd04-787e-4b3b-a516-0ead12", 'MYSPORTSFEEDS')



def get_standings(standings):

    #dictionary of arrays: arrays contain the team name, wins, losses, pct g
    std = {}
    for team in standings:

        conference = team['conferenceRank']['conferenceName']
        division = team['divisionRank']['divisionName']

        division = conference + ' ' + division

        if division not in std.keys():
            std[division] = [{}]*5

        rank = int(team['divisionRank']['rank'])

        info = {}
        info['team'] = team['team']['abbreviation']
        info['rank'] = rank
        info['wins'] = team['stats']['standings']['wins']
        info['loses'] = team['stats']['standings']['losses']
        info['winPct'] = team['stats']['standings']['winPct']
        info['gamesBack'] = team['divisionRank']['gamesBack']



        std[division][rank-1] = info

    return std


def get_scores(data):

    games = []

    for eachGame in data:

        thisGame = {}
        status = eachGame['schedule']['playedStatus']

        thisGame['status'] = status
        thisGame['homeTeam'] = eachGame['schedule']['homeTeam']['abbreviation']
        thisGame['awayTeam'] = eachGame['schedule']['awayTeam']['abbreviation']


        if status == 'UNPLAYED':
            thisGame['startTime'] = eachGame['schedule']['startTime']

        elif status == 'LIVE':
            thisGame['scores'] = eachGame['score']['innings']
            thisGame['currentInning'] = eachGame['score']['currentInning']
            thisGame['homeScore'] = eachGame['score']['homeScoreTotal']
            thisGame['awayScore'] = eachGame['score']['awayScoreTotal']
            thisGame['homeHits'] = eachGame['score']['homeHitsTotal']
            thisGame['awayHits'] = eachGame['score']['awayHitsTotal']
            thisGame['homeErrors'] = eachGame['score']['homeErrorsTotal']
            thisGame['awayErrors'] = eachGame['score']['awayErrorsTotal']
        else:
            thisGame['scores'] = eachGame['score']['innings']
            thisGame['homeScore'] = eachGame['score']['homeScoreTotal']
            thisGame['awayScore'] = eachGame['score']['awayScoreTotal']
            thisGame['homeHits'] = eachGame['score']['homeHitsTotal']
            thisGame['awayHits'] = eachGame['score']['awayHitsTotal']
            thisGame['homeErrors'] = eachGame['score']['homeErrorsTotal']
            thisGame['awayErrors'] = eachGame['score']['awayErrorsTotal']

        games.append(thisGame)

    return games



def get_stat(all, stat):

    top = []

    if stat in ['homeruns', 'runsBattedIn', 'battingAvg']:
        mod = 'batting'
    else:
        mod = 'pitching'

    for eachPlayer in all:
        try:
            eachPlayer['stats'][mod]

            if mod == 'pitching' and float(eachPlayer['stats'][mod]['inningsPitched']) < 25.0:
                continue
            elif mod == 'batting' and float(eachPlayer['stats'][mod]['atBats']) < 50.0:
                continue


            if len(top) < 5:

                top.append([eachPlayer['player']['firstName'], eachPlayer['player']['lastName'], eachPlayer['stats'][mod][stat]])

            else:

                for place in range(len(top)):

                    repIn = float(top[place][2])
                    repNew = float(eachPlayer['stats'][mod][stat])

                    if stat == 'earnedRunAvg':
                        h = repNew
                        repNew = repIn
                        repIn = h

                    if repNew >= repIn:

                        player = [eachPlayer['player']['firstName'], eachPlayer['player']['lastName'], eachPlayer['stats'][mod][stat]]
                        top.insert(place, player)
                        del top[-1]
                        break
        except:
            continue


    return top
