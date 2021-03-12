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
        while(i < len(self.patterns)):
            if(i > 0 and i < len(self.patterns) - 1):
                if(self.patterns[i].GetID() != self.patterns[i - 1].GetID() or self.patterns[i].GetID() != self.patterns[i + 1].GetID()): #only include silences between patterns
                    if(random.randint(0, 99) == 0): #decide / make silences
                        print('here')
                        if(len(self.patterns) - i > 25): #avoid going out of range
                            for j in range(0, random.randint(0, 25)): #random length of silence
                                self.place = self.place + self.patterns[i].GetLength() #replace patterns with silence
                                i = i + 1
                        else:
                            self.patterns[i].GetMIDIData(instrument, self.place)
                            self.place = self.place + self.patterns[i].GetLength()
                            i = i + 1
                    else:
                        self.patterns[i].GetMIDIData(instrument, self.place)
                        self.place = self.place + self.patterns[i].GetLength()
                        i = i + 1
                else:
                    self.patterns[i].GetMIDIData(instrument, self.place)
                    self.place = self.place + self.patterns[i].GetLength()
                    i = i + 1
            else:
                self.patterns[i].GetMIDIData(instrument, self.place)
                self.place = self.place + self.patterns[i].GetLength()
                i = i + 1
        return instrument
