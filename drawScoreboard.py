from bibliopixel.layout import *
from scoreboard.animations.ScoreBoardAnimation import ScoreBoardAnimation # import the animation
from bibliopixel.drivers.PiWS281X import *
import sys

#create biblio pixel driver and led
thread             = False   # display updates to run in background thread
brightness         = 100     # brightness 0-255
numTeamNameNumLeds = 18*5    # number of leds in the team name
numTimerLeds       = 17*5    # number of leds in the timer section
numScoreLeds       = 3*5     # number of leds in for a single number
driver             = PiWS281X(numTeamNameNumLeds*2 + numTimerLeds + numScoreLeds*4)
led                = Strip(driver, thread, brightness)

#run animation
anim  = ScoreBoardAnimation(led, 1000, "message")
anim.run()
