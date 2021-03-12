class Silence:
    def __init__(self, beginning):
        self.beginningIndexOfSilence = beginning
        return

    def SetEndingIndexOfSilence(self, ending):
        self.endingIndexOfSilence = ending
        return

    def GetBeginningIndexOfSilence(self):
        return self.beginningIndexOfSilence

    def GetEndingIndexOfSilence(self):
        return self.endingIndexOfSilence
