class MessageAlgorithm(object):

    _colorAlgorithm = None

    def __init__(self, colorAlgorithm):
        super(object, self).__init__()
        self._colorAlgorithm = colorAlgorithm

    #Method all subclasses need to override
    def animateLED(self, led, step, word):
        pass
