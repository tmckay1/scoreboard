from bibliopixel.layout import *
from bibliopixel.animation import BaseStripAnim
from ..algorithms.ScrollLeftMessageAlgorithmStrip import ScrollLeftMessageAlgorithmStrip # import the animation
from ..algorithms.StandingMessageAlgorithmStrip   import StandingMessageAlgorithmStrip # import the animation
from ..algorithms.RainbowColorAlgorithm           import RainbowColorAlgorithm  # import the color algorithm
from ..parsers.StandardMessageParser              import StandardMessageParser # import the parser
from ..parsers.TimeMessageParser                  import TimeMessageParser # import the parser
from ..characters.MessageCharacters5x3            import MessageCharacters5x3  # import the character set
import json
import time
import threading

class ScoreBoardSnapshotAnimation(BaseStripAnim):

    _scoresPath = "scores.json"

    # the delay between refreshing the scroll algorithm
    _scrollDelay = 0.01

    # display to put in the timer section
    _timeDisplay = ""

    # time to end the animation
    _animationEndTime = None

    # the duration of the animation in seconds
    _duration = 10

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
    _homeScore             = 0
    homeScoreSection2Start = 280
    homeScoreSection2End   = 294
    homeScoreSection2Rows  = 5

    # score of away team section, start and end index of strip
    awayScoreSection1Start = 295
    awayScoreSection1End   = 309
    awayScoreSection1Rows  = 5
    _awayScore             = 0
    awayScoreSection2Start = 310
    awayScoreSection2End   = 324
    awayScoreSection2Rows  = 5

    def __init__(self, led, timeDisplay, scrollDelay, homeName, awayName, homeScore, awayScore, duration):
        #The base class MUST be initialized by calling super like this
        super(BaseStripAnim, self).__init__(led)
        self._timeDisplay      = timeDisplay
        self._scrollDelay      = scrollDelay
        self._homeName         = homeName
        self._awayName         = awayName
        self._homeScore        = homeScore
        self._awayScore        = awayScore
        self._animationEndTime = duration + time.time()



    # override to write out word for each frame in the animation
    def step(self, amt = 1):

        # end animation if over time
        if self._animationEndTime - time.time() < 0:
            self.stop()

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
        if self._animationEndTime - time.time() < 0:
            self.stop()
        
        time.sleep(self._scrollDelay)



    def drawHomeSection(self, startIndex, endIndex, rows):

        characterSet  = MessageCharacters5x3()
        messageParser = StandardMessageParser(self._homeName,characterSet)
        word          = messageParser.getMessageMatrix()

        colorAlgorithm = RainbowColorAlgorithm()

        messageAlgorithm = ScrollLeftMessageAlgorithmStrip(colorAlgorithm)
        messageAlgorithm.animateLED(self._led, self._step, word, startIndex, endIndex, rows)



    def drawTimerSection(self, startIndex, endIndex, rows):
        characterSet  = MessageCharacters5x3()
        messageParser = TimeMessageParser(self._timeDisplay,characterSet)
        word          = messageParser.getMessageMatrix()

        colorAlgorithm = RainbowColorAlgorithm()

        messageAlgorithm = ScrollLeftMessageAlgorithmStrip(colorAlgorithm)
        messageAlgorithm.animateLED(self._led, self._step, word, startIndex, endIndex, rows)



    def drawAwaySection(self, startIndex, endIndex, rows):

        characterSet  = MessageCharacters5x3()
        messageParser = StandardMessageParser(self._awayName,characterSet)
        word          = messageParser.getMessageMatrix()

        colorAlgorithm = RainbowColorAlgorithm()

        messageAlgorithm = ScrollLeftMessageAlgorithmStrip(colorAlgorithm)
        messageAlgorithm.animateLED(self._led, self._step, word, startIndex, endIndex, rows)



    def drawHomeScoreSection1(self, startIndex, endIndex, rows):

        score = str(int(self._homeScore/10)%10)
        
        characterSet  = MessageCharacters5x3()
        messageParser = StandardMessageParser(score,characterSet)
        word          = messageParser.getMessageMatrix()

        colorAlgorithm = RainbowColorAlgorithm()

        messageAlgorithm = StandingMessageAlgorithmStrip(colorAlgorithm)
        messageAlgorithm.animateLED(self._led, self._step, word, startIndex, endIndex, rows)



    def drawHomeScoreSection2(self, startIndex, endIndex, rows):

        score = str(self._homeScore%10)

        characterSet  = MessageCharacters5x3()
        messageParser = StandardMessageParser(score,characterSet)
        word          = messageParser.getMessageMatrix()

        colorAlgorithm = RainbowColorAlgorithm()

        messageAlgorithm = StandingMessageAlgorithmStrip(colorAlgorithm)
        messageAlgorithm.animateLED(self._led, self._step, word, startIndex, endIndex, rows)



    def drawAwayScoreSection1(self, startIndex, endIndex, rows):

        score = str(int(self._awayScore/10)%10)
        
        characterSet  = MessageCharacters5x3()
        messageParser = StandardMessageParser(score,characterSet)
        word          = messageParser.getMessageMatrix()

        colorAlgorithm = RainbowColorAlgorithm()

        messageAlgorithm = StandingMessageAlgorithmStrip(colorAlgorithm)
        messageAlgorithm.animateLED(self._led, self._step, word, startIndex, endIndex, rows)



    def drawAwayScoreSection2(self, startIndex, endIndex, rows):

        score = str(self._awayScore%10)
        
        characterSet  = MessageCharacters5x3()
        messageParser = StandardMessageParser(score,characterSet)
        word          = messageParser.getMessageMatrix()

        colorAlgorithm = RainbowColorAlgorithm()

        messageAlgorithm = StandingMessageAlgorithmStrip(colorAlgorithm)
        messageAlgorithm.animateLED(self._led, self._step, word, startIndex, endIndex, rows)
