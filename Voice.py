import pretty_midi
from Pattern import Pattern

class Voice:
    def __init__(self, ap):
        self.patterns = []
        self.allPatterns = ap
        self.currentPattern = 0
        self.place = 0
        #self.register = 1

        for i in range(0, len(self.allPatterns)):
            self.AddPattern()
            self.AddPattern()
            self.AddPattern()
            self.currentPattern = self.currentPattern + 1
        return

    def AddPattern(self):
        self.patterns.append(self.allPatterns[self.currentPattern])
        return

    def GetMIDIData(self):
        instrument = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Cello'))
        for i in range(0, len(self.patterns)):
            self.patterns[i].GetMIDIData(instrument, self.place)
            self.place = self.place + self.patterns[i].GetLength()
        return instrument
