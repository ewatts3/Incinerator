import pretty_midi
from Pattern import Pattern

class Voice:
    def __init__(self, ap):
        self.patterns = []
        self.allPatterns = ap
        self.currentPattern = 0
        self.place = 0
        self.IsOnLastPattern = False
        self.timeOnCurrentPattern = 0
        self.wasChangedThisIteration = False #we don't want to skip patterns, so this ensures that a voice only gets changed once per each iteration
        self.isNotOnAnEightNoteBeat = False
        return

    def AddPattern(self):
        self.patterns.append(self.allPatterns[self.currentPattern])
        self.place = self.place + self.allPatterns[self.currentPattern].GetLength()
        self.timeOnCurrentPattern = self.timeOnCurrentPattern + self.allPatterns[self.currentPattern].GetLength()
        self.wasChangedThisIteration = False
        return

    def ChangePattern(self):
        if self.currentPattern == len(self.allPatterns) - 1:
            self.IsOnLastPattern = True
        if (self.wasChangedThisIteration is False) and (self.IsOnLastPattern is False):
            self.currentPattern = self.currentPattern + 1
            self.timeOnCurrentPattern = 0
            self.wasChangedThisIteration = True
        return

    def GetAllPatterns(self):
        return self.allPatterns

    def GetCurrentPattern(self):
        return self.currentPattern

    def IsNotOnLastPattern(self):
        return not self.IsOnLastPattern

    def GetPlace(self):
        return self.place

    def GetTimeOnCurrentPattern(self):
        return self.timeOnCurrentPattern

    def IsNotOnAnEighthNoteBeat(self, lengthOfSixteenthNote):
        if(self.place > 0):
            if((self.place % (lengthOfSixteenthNote * 2)) != 0): 
                return True
            else:
                return False
        return False

    def GetMIDIData(self):
        self.place = 0
        instrument = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Cello'))
        for i in range(0, len(self.patterns)):
            self.patterns[i].GetMIDIData(instrument, self.place)
            self.place = self.place + self.patterns[i].GetLength()
        return instrument
