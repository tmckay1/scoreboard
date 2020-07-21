from .MessageAlgorithm import MessageAlgorithm

class StandingMessageAlgorithmStrip(MessageAlgorithm):

    def __init__(self, colorAlgorithm):
        super(StandingMessageAlgorithmStrip, self).__init__(colorAlgorithm)

    # override to perform word animation
    def animateLED(self,led, step, word, startIndex, endIndex, rows):

        # define variables
        boardWidth   = int((endIndex - startIndex + 1)/rows)
        maxStep      = boardWidth + len(word) # letter is off the board at this step
        colStep      = step
        step         = step % maxStep
        xRange       = boardWidth
        yRange       = rows
        xWordOffset  = 0

        for y in range(yRange):
            for xBoard in range(xRange):

                # get the x coordinate for the strip
                x = y*boardWidth + (xBoard if y%2 == 0 else boardWidth-xBoard-1) + startIndex

                # create mapping to x value of word
                xWord  = xWordOffset + xBoard

                # only continue if the x coordinate of the word exists otherwise draw the empty color to the board
                color = self._colorAlgorithm.getEmptyColor(led,xBoard,y,colStep)
                if xWord >= 0 and xWord < len(word):
                    if word[xWord][y]:
                        color = self._colorAlgorithm.getColor(led,xBoard,y,colStep)
                led.set(x,color)
