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
        return

    def GetAllPatterns(self):
        return self.allPatterns

    def AddPattern(self):
        self.patterns.append(self.allPatterns[self.currentPattern])
        self.timeOnCurrentPattern = self.timeOnCurrentPattern + self.allPatterns[self.currentPattern].GetLength()
        return

    def ChangePattern(self):
        self.currentPattern = self.currentPattern + 1
        if self.currentPattern == len(self.allPatterns):
            self.IsOnLastPattern = True
        self.timeOnCurrentPattern = 0
        return

    def IsNotOnLastPattern(self):
        return not self.IsOnLastPattern

    def GetPlace(self):
        return self.place

    def GetTimeOnCurrentPattern(self):
        return self.timeOnCurrentPattern

    def GetMIDIData(self):
        instrument = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Cello'))
        for i in range(0, len(self.patterns)):
            self.patterns[i].GetMIDIData(instrument, self.place)
            self.place = self.place + self.patterns[i].GetLength()
        return instrument
