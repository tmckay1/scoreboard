from bibliopixel.layout import *
from scoreboard.animations.ScoreBoardSnapshotAnimation import ScoreBoardSnapshotAnimation # import the animation
from bibliopixel.drivers.PiWS281X import *
from threading import Thread
import sports
import sys

def filterLiveMatches(matches):
  return list(filter(lambda match: match.match_time != 'Match Finished', matches))

def getLiveMatches(all_matches):
  matches    = sports.all_matches()
  basketball = filterLiveMatches(matches['basketball'])
  baseball   = filterLiveMatches(matches['baseball'])
  all_matches['games'] = basketball + baseball
  print("getLiveMatches")
  print(all_matches)

def getLiveMatchesAsync(all_matches):
  thread = Thread(target = getLiveMatches, args = (all_matches, ))
  thread.start()
  return thread

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

# only baseball and basketball for now
all_matches = { "games": [] }
getLiveMatches(all_matches)

#run animation
while True:

  async_matches = { "games": [] }
  thread = getLiveMatchesAsync(async_matches)

  for match in all_matches['games']:
    timerDisplay = match.match_time
    homeName     = match.home_team
    awayName     = match.away_team
    homeScore    = match.home_score
    awayScore    = match.away_score
    anim         = ScoreBoardSnapshotAnimation(led, timerDisplay, scrollDelay, homeName, awayName, homeScore, awayScore, duration)
    anim.run()

  # ensure we finish the previous thread before continuing
  thread.join()
  all_matches = async_matches