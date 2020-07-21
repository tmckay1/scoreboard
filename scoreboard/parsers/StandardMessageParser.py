
class StandardMessageParser(object):

    _message       = ""
    _messageMatrix = []
    _characters    = None

    def __init__(self, message, characters):
        super(StandardMessageParser, self).__init__()
        self._message    = message.upper()
        self._characters = characters
        self.setMessage(self._message)

    def setMessage(self,message):
        #reset message list
        self._messageMatrix = []

        #calculate message list
        for letter in message:
            letterMatrix = self.getLetterMatrixForLetter(letter)
            self._messageMatrix.extend(letterMatrix)
            self._messageMatrix.extend(self._characters.cNULL)

        #set our new message
        self._message = message

    def getMessage(self):
        return self._message

    def getMessageMatrix(self):
        return self._messageMatrix

    def getLetterMatrixForLetter(self,letter):

        letterMatrix = self._characters.cUNKNOWN

        #if we have the letter defined add it to the list, otherwise check for special character
        if hasattr(self._characters,"c"+letter):
            letterMatrix = self._characters.__getattribute__("c"+letter)
        elif letter == " ":
            letterMatrix = self._characters.cSPACE
        elif letter == ".":
            letterMatrix = self._characters.cPERIOD
        elif letter == ",":
            letterMatrix = self._characters.cCOMMA
        elif letter == "!":
            letterMatrix = self._characters.cEXCLAIMATION
        elif letter == "?":
            letterMatrix = self._characters.cQUESTION
        elif letter == "\"":
            letterMatrix = self._characters.cDOUBLEQUOTE
        elif letter == "'":
            letterMatrix = self._characters.cSINGLEQUOTE
        elif letter == ":":
            letterMatrix = self._characters.cCOLON

        return letterMatrix
