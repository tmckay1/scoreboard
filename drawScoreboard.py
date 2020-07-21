from bibliopixel.layout import *
from scoreboard.animations.ScoreBoardAnimation import ScoreBoardAnimation # import the animation
from bibliopixel.drivers.PiWS281X import *
import sys

#create biblio pixel driver and led
thread     = False   # display updates to run in background thread
brightness = 100     # brightness 0-255
driver     = PiWS281X(18*5*2 + 17*5)
led        = Strip(driver, thread, brightness)

#run animation
anim  = ScoreBoardAnimation(led, 1000, "message")
anim.run()
