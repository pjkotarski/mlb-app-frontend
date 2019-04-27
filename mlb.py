from ohmysportsfeedspy import MySportsFeeds
import simplejson

msf = MySportsFeeds(version="2.0", verbose = True)
msf.authenticate("ea5ffd04-787e-4b3b-a516-0ead12", 'MYSPORTSFEEDS')

def get_stat(all, stat):

    top = []

    if stat in ['homeruns', 'runsBattedIn', 'battingAvg']:
        mod = 'batting'
    else:
        mod = 'pitching'

    for eachPlayer in all:
        try:
            eachPlayer['stats'][mod]
            print(stat)
            print(mod)

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
            print('nothing found')

    return top
