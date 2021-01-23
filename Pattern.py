import pretty_midi
from Note import Note

class Pattern:
    def __init__(self, lengthOfSixteenthNote):
        self.lengthOfSixteenthNote = lengthOfSixteenthNote
        self.pattern = []
        self.length = 0
        self.place = 0
        return

    def AddNote(self, letter, octave, rhythmicValue):
        if rhythmicValue == 'graceNote':
            lengthOfGraceNote = self.place - (self.lengthOfSixteenthNote * .5)
            self.pattern.append(Note(letter, octave, lengthOfGraceNote, self.place))
            # so self.place = self.place
            return
        elif rhythmicValue == 'sixteenth':
            end = self.place + self.lengthOfSixteenthNote
        elif rhythmicValue == 'eighth':
            end = self.place + (self.lengthOfSixteenthNote * 2)
        elif rhythmicValue == 'dottedEighth':
            end = self.place + (self.lengthOfSixteenthNote * 3)
        elif rhythmicValue == 'quarter':
            end = self.place + (self.lengthOfSixteenthNote * 4)
        elif rhythmicValue == 'dottedQuarter':
            end = self.place + (self.lengthOfSixteenthNote * 6)
        elif rhythmicValue == 'half':
            end = self.place + (self.lengthOfSixteenthNote * 8)
        elif rhythmicValue == 'halfTiedToEighth':
            end = self.place + (self.lengthOfSixteenthNote * 10)
        elif rhythmicValue == 'dottedHalf':
            end = self.place + (self.lengthOfSixteenthNote * 12)
        elif rhythmicValue == 'dottedHalfTiedToSixteenth':
            end = self.place + (self.lengthOfSixteenthNote * 13)
        elif rhythmicValue == 'dottedHalfTiedToEighth':
            end = self.place + (self.lengthOfSixteenthNote * 14)
        elif rhythmicValue == 'whole':
            end = self.place + (self.lengthOfSixteenthNote * 16)
        elif rhythmicValue == 'wholeTiedToQuarter':
            end = self.place + (self.lengthOfSixteenthNote * 20)
        elif rhythmicValue == 'dottedWhole':
            end = self.place + (self.lengthOfSixteenthNote * 24)
        elif rhythmicValue == 'tiedWhole':
            end = self.place + (self.lengthOfSixteenthNote * 32)
   
        self.pattern.append(Note(letter, octave, self.place, end))
        self.place = end
        self.length = self.place
        return

    def AddRest(self, rhythmicValue):
        if rhythmicValue == 'emptyMeasure':
            self.place = self.place + (self.lengthOfSixteenthNote * 4)
            self.length = self.place
            #self.pattern.append(Note('C', 4, 0, 0))
        elif rhythmicValue == 'sixteenth':
            self.place = self.place + self.lengthOfSixteenthNote
        elif rhythmicValue == 'eighth':
            self.place = self.place + (self.lengthOfSixteenthNote * 2)
        elif rhythmicValue == 'dottedEighth':
            self.place = self.place + (self.lengthOfSixteenthNote * 3)
        elif rhythmicValue == 'quarter':
            self.place = self.place + (self.lengthOfSixteenthNote * 4)
        self.length = self.place
        return

    def GetPattern(self):
        return self.pattern

    def GetLength(self):
        return self.length

    def GetMIDIData(self, instrument, place):
        for i in range(0, len(self.pattern)):
            instrument.notes.append(self.pattern[i].GetMIDIData(place))
        return