from bibliopixel.layout import *
from scoreboard.animations.ScoreBoardSnapshotAnimation import ScoreBoardSnapshotAnimation # import the animation
from bibliopixel.drivers.PiWS281X import *
import scores
import sys

def getLiveMatches(matches):
  return list(filter(lambda match: match.match_time != 'Match Finished', matches))

#create biblio pixel driver and led
thread             = False   # display updates to run in background thread
brightness         = 100     # brightness 0-255
numTeamNameNumLeds = 18*5    # number of leds in the team name
numTimerLeds       = 17*5    # number of leds in the timer section
numScoreLeds       = 3*5     # number of leds in for a single number
driver             = PiWS281X(numTeamNameNumLeds*2 + numTimerLeds + numScoreLeds*4)
led                = Strip(driver, thread, brightness)

# setup animation
scrollDelay  = 0.05
duration     = 10

#run animation
while True:
  # only baseball and basketball for now
  matches     = sports.all_matches()
  basketball  = getLiveMatches(matches['basketball'])
  baseball    = getLiveMatches(matches['baseball'])
  all_matches = basketball + baseball

  for match in all_matches:
    timerDisplay = match.match_time
    homeName     = match.home_team
    awayName     = match.away_team
    homeScore    = match.home_score
    awayScore    = match.away_score
    anim         = ScoreBoardSnapshotAnimation(led, timerDisplay, scrollDelay, homeName, awayName, homeScore, awayScore, duration)
    anim.run()