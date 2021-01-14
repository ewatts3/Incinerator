import pretty_midi
from Pattern import Pattern

class Voice:
    def __init__(self, ap, numberOfOctavesToTransposePatternsBy):
        self.patterns = []
        self.allPatterns = ap
        self.TransposePatterns(self.allPatterns, numberOfOctavesToTransposePatternsBy)
        self.currentPattern = 0
        self.place = 0
        self.IsOnLastPattern = False
        self.timeOnCurrentPattern = 0
        self.register = numberOfOctavesToTransposePatternsBy
        return

    def TransposePatterns(self, ap, o):
        for i in range(0, len(ap)):
            currentPatternToTranspose = ap[i].GetPattern()
            for j in range(0, len(currentPatternToTranspose)):
                currentPatternToTranspose[j].Transpose(o)
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

    #for TESTING ONLY
    def ReversePattern(self):
        self.currentPattern = self.currentPattern - 1
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
            self.patterns[i].GetMIDIData(instrument, self.place, self.register)
            self.place = self.place + self.patterns[i].GetLength()
        return instrument
