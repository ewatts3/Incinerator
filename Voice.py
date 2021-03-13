import pretty_midi
from Pattern import Pattern
import random
from Silence import Silence

class Voice:
    def __init__(self, ap):
        self.patterns = [] #complete performance
        self.allPatterns = ap #just the set of 53
        self.currentPattern = 0
        self.place = 0
        self.timeOnCurrentPattern = 0
        self.wasChangedThisIteration = False #we don't want to skip patterns, so this ensures that a voice only gets changed once per each iteration
        self.isNotOnAnEightNoteBeat = False
        return

    def AddPattern(self, dynamic):
        self.patterns.append(self.allPatterns[self.currentPattern])
        self.patterns[len(self.patterns) - 1].SetDynamic(dynamic)
        self.place = self.place + self.allPatterns[self.currentPattern].GetLength()
        self.timeOnCurrentPattern = self.timeOnCurrentPattern + self.allPatterns[self.currentPattern].GetLength()
        self.wasChangedThisIteration = False
        return

    def ChangePattern(self):
        if (self.wasChangedThisIteration is False) and (self.IsNotOnLastPattern()):
            self.currentPattern = self.currentPattern + 1
            self.timeOnCurrentPattern = 0
            self.wasChangedThisIteration = True
        return

    def ChangePatternForEnding(self):
        self.currentPattern = self.currentPattern + 1
        return

    def GetAllPatterns(self):
        return self.allPatterns

    def GetCurrentPattern(self):
        return self.currentPattern

    def IsNotOnLastPattern(self):
        return (self.currentPattern != len(self.allPatterns) - 2)

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
        i = 0
        while(i < len(self.patterns) - 1):
            i = self.DecideIfVoiceShouldDropOut(i)
            self.patterns[i].GetMIDIData(instrument, self.place)
            self.place = self.place + self.patterns[i].GetLength()
            i = i + 1
        return instrument

    def DecideIfVoiceShouldDropOut(self, i):
        index = i
        if(random.randint(0, 499) == 0 and self.patterns[index].GetID() != len(self.allPatterns) - 1): #decide when to make silences within the range of the array
            currentPattern = self.patterns[index].GetID()
            while(currentPattern == self.patterns[index].GetID()): #replace patterns with silence until the new pattern is reached
                self.place = self.place + self.patterns[index].GetLength() #replace patterns with silence
                index = index + 1
        return index