import request
import pandas as pd

pd.set_option('notebook_repr_html',True)
pd.set_option('display.max_columns',300)
pd.set_option('display.width',3000)

class Team_info:
    def __init__(self, teamid, leagueid='00',season='2013-14',seasontype='Regular Season',
    	vsconference='',vsdivision=''):

        self._url = "http://stats.nba.com/stats/teaminfocommon?"
        self._api_param = {
             'LeagueID': leagueid,           
             'Season' :  season,
             'SeasonType' : seasontype,
             'TeamID' : teamid
             }

        self._req = requests.get(self._url, params=self._api_param)
        self._req = self._req.json()
    def info(self):
        return pd.DataFrame(self._req['resultSets'][0]['rowSet'],columns=self._req['resultSets'][0]['headers']) 
