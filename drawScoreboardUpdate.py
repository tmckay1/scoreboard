from bibliopixel.layout import *
from scoreboard.animations.ScoreBoardUpdateAnimation import ScoreBoardUpdateAnimation # import the animation
from bibliopixel.drivers.PiWS281X import *
import sys

#create biblio pixel driver and led
thread     = False   # display updates to run in background thread
brightness = 100     # brightness 0-255
driver     = PiWS281X(325)
led        = Strip(driver, thread, brightness)

#run animation
anim  = ScoreBoardUpdateAnimation(led, 1200, .05)
anim.run()
