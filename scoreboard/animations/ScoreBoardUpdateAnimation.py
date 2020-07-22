from bibliopixel.layout import *
from bibliopixel.animation import BaseStripAnim
from ..algorithms.ScrollLeftMessageAlgorithmStrip import ScrollLeftMessageAlgorithmStrip # import the animation
from ..algorithms.StandingMessageAlgorithmStrip   import StandingMessageAlgorithmStrip # import the animation
from ..algorithms.RainbowColorAlgorithm           import RainbowColorAlgorithm  # import the color algorithm
from ..parsers.StandardMessageParser              import StandardMessageParser # import the parser
from ..parsers.TimeMessageParser                  import TimeMessageParser # import the parser
from ..characters.MessageCharacters5x3            import MessageCharacters5x3  # import the character set
import time
import threading

class ScoreBoardUpdateAnimation(BaseStripAnim):

    _delay   = 0.01

    # time to run the animation, in seconds, and time the animation started
    _animationTime      = 0
    _animationStartTime = 0

    # event flag to signify when the animation is running
    isDone = threading.Event()

    # name of home team section, start and end index of strip
    homeSectionStart = 0
    homeSectionEnd   = 89
    homeSectionRows  = 5
    _homeName         = "Home"

    # timer section, start and end index of strip
    timerSectionStart = 90
    timerSectionEnd   = 174
    timerSectionRows  = 5

    # name of away team section, start and end index of strip
    awaySectionStart = 175
    awaySectionEnd   = 264
    awaySectionRows  = 5
    _awayName         = "Away"

    # score of home team section, start and end index of strip
    homeScoreSection1Start = 265
    homeScoreSection1End   = 279
    homeScoreSection1Rows  = 5
    homeScore              = 0
    homeScoreSection2Start = 280
    homeScoreSection2End   = 294
    homeScoreSection2Rows  = 5

    # score of away team section, start and end index of strip
    awayScoreSection1Start = 295
    awayScoreSection1End   = 309
    awayScoreSection1Rows  = 5
    awayScore              = 0
    awayScoreSection2Start = 310
    awayScoreSection2End   = 324
    awayScoreSection2Rows  = 5

    def __init__(self, led, animationTime, delay, homeName, awayName):
        #The base class MUST be initialized by calling super like this
        super(BaseStripAnim, self).__init__(led)
        self._animationTime      = animationTime
        self._animationStartTime = time.time()
        self._delay              = delay
        self._homeName           = homeName
        self._awayName           = awayName



    # override to write out word for each frame in the animation
    def step(self, amt = 1):

        # end animation if over time
        if time.time() - self._animationStartTime > self._animationTime:
            self.stop()
            self.isRunning.set()

        # draw all the sections
        self.drawHomeSection(self.homeSectionStart, self.homeSectionEnd, self.homeSectionRows)
        self.drawTimerSection(self.timerSectionStart, self.timerSectionEnd, self.timerSectionRows)
        self.drawAwaySection(self.awaySectionStart, self.awaySectionEnd, self.awaySectionRows)

        self.drawHomeScoreSection1(self.homeScoreSection1Start, self.homeScoreSection1End, self.homeScoreSection1Rows)
        self.drawHomeScoreSection2(self.homeScoreSection2Start, self.homeScoreSection2End, self.homeScoreSection2Rows)

        self.drawAwayScoreSection1(self.awayScoreSection1Start, self.awayScoreSection1End, self.awayScoreSection1Rows)
        self.drawAwayScoreSection2(self.awayScoreSection2Start, self.awayScoreSection2End, self.awayScoreSection2Rows)

        self._step += amt

        # end animation if over time
        if time.time() - self._animationStartTime > self._animationTime:
            self.stop()
            self.isDone.set()
        
        time.sleep(self._delay)




    def drawHomeSection(self, startIndex, endIndex, rows):

        characterSet  = MessageCharacters5x3()
        messageParser = StandardMessageParser(self._homeName,characterSet)
        word          = messageParser.getMessageMatrix()

        colorAlgorithm = RainbowColorAlgorithm()

        messageAlgorithm = ScrollLeftMessageAlgorithmStrip(colorAlgorithm)
        messageAlgorithm.animateLED(self._led, self._step, word, startIndex, endIndex, rows)



    def drawTimerSection(self, startIndex, endIndex, rows):

        # display time
        totalSecondsLeft = int(self._animationTime - time.time() + self._animationStartTime)
        minutes          = int(totalSecondsLeft/60)
        seconds          = int(totalSecondsLeft%60)
        minuteDisplay    = str(minutes) if minutes >= 10 else "0" + str(minutes)
        secondDisplay    = str(seconds) if seconds >= 10 else "0" + str(seconds)
        timeLeft         = minuteDisplay + ":" + secondDisplay

        characterSet  = MessageCharacters5x3()
        messageParser = TimeMessageParser(timeLeft,characterSet)
        word          = messageParser.getMessageMatrix()

        colorAlgorithm = RainbowColorAlgorithm()

        messageAlgorithm = StandingMessageAlgorithmStrip(colorAlgorithm)
        messageAlgorithm.animateLED(self._led, self._step, word, startIndex, endIndex, rows)



    def drawAwaySection(self, startIndex, endIndex, rows):

        characterSet  = MessageCharacters5x3()
        messageParser = StandardMessageParser(self._awayName,characterSet)
        word          = messageParser.getMessageMatrix()

        colorAlgorithm = RainbowColorAlgorithm()

        messageAlgorithm = ScrollLeftMessageAlgorithmStrip(colorAlgorithm)
        messageAlgorithm.animateLED(self._led, self._step, word, startIndex, endIndex, rows)



    def drawHomeScoreSection1(self, startIndex, endIndex, rows):

        score = str(int(self.homeScore/10)%10)
        
        characterSet  = MessageCharacters5x3()
        messageParser = StandardMessageParser(score,characterSet)
        word          = messageParser.getMessageMatrix()

        colorAlgorithm = RainbowColorAlgorithm()

        messageAlgorithm = StandingMessageAlgorithmStrip(colorAlgorithm)
        messageAlgorithm.animateLED(self._led, self._step, word, startIndex, endIndex, rows)



    def drawHomeScoreSection2(self, startIndex, endIndex, rows):

        score = str(self.homeScore%10)

        characterSet  = MessageCharacters5x3()
        messageParser = StandardMessageParser(score,characterSet)
        word          = messageParser.getMessageMatrix()

        colorAlgorithm = RainbowColorAlgorithm()

        messageAlgorithm = StandingMessageAlgorithmStrip(colorAlgorithm)
        messageAlgorithm.animateLED(self._led, self._step, word, startIndex, endIndex, rows)



    def drawAwayScoreSection1(self, startIndex, endIndex, rows):

        score = str(int(self.awayScore/10)%10)
        
        characterSet  = MessageCharacters5x3()
        messageParser = StandardMessageParser(score,characterSet)
        word          = messageParser.getMessageMatrix()

        colorAlgorithm = RainbowColorAlgorithm()

        messageAlgorithm = StandingMessageAlgorithmStrip(colorAlgorithm)
        messageAlgorithm.animateLED(self._led, self._step, word, startIndex, endIndex, rows)



    def drawAwayScoreSection2(self, startIndex, endIndex, rows):

        score = str(self.awayScore%10)
        
        characterSet  = MessageCharacters5x3()
        messageParser = StandardMessageParser(score,characterSet)
        word          = messageParser.getMessageMatrix()

        colorAlgorithm = RainbowColorAlgorithm()

        messageAlgorithm = StandingMessageAlgorithmStrip(colorAlgorithm)
        messageAlgorithm.animateLED(self._led, self._step, word, startIndex, endIndex, rows)
