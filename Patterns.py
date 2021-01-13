import pretty_midi
from Pattern import Pattern

class Patterns:
    def __init__(self, lengthOfSixteenthNote):
        self.lengthOfSixteenthNote = lengthOfSixteenthNote
        self.allPatterns = []

        self.CreateThirdPattern()
        #self.CreateFourthPattern()
        #self.CreateFifthPattern()
        return

    def GetAllPatterns(self):
        return self.allPatterns

    def CreateThirdPattern(self):
        thirdPattern = Pattern(self.lengthOfSixteenthNote)
        thirdPattern.AddRest('eighth')
        thirdPattern.AddNote('E', 4, 'eighth')
        thirdPattern.AddNote('F', 4, 'eighth')
        thirdPattern.AddNote('E', 4, 'eighth')
        self.allPatterns.append(thirdPattern)
        return

    def CreateFourthPattern(self):
        fourthPattern = Pattern()
        fourthPattern.AddNote(Note('E', 4, self.sixteenthNoteLength * 1, self.sixteenthNoteLength * 2))
        fourthPattern.AddNote(Note('F', 4, self.sixteenthNoteLength * 2, self.sixteenthNoteLength * 3))
        fourthPattern.AddNote(Note('G', 4, self.sixteenthNoteLength * 3, self.sixteenthNoteLength * 4))
        fourthPattern.SetLength(self.sixteenthNoteLength * 4)
        self.allPatterns.append(fourthPattern)
        return

    def CreateFifthPattern(self):
        fifthPattern = Pattern()
        fifthPattern.AddNote(Note('E', 4, self.sixteenthNoteLength * 0, self.sixteenthNoteLength * 1))
        fifthPattern.AddNote(Note('F', 4, self.sixteenthNoteLength * 1, self.sixteenthNoteLength * 2))
        fifthPattern.AddNote(Note('G', 4, self.sixteenthNoteLength * 2, self.sixteenthNoteLength * 3))
        fifthPattern.SetLength(self.sixteenthNoteLength * 4)
        self.allPatterns.append(fifthPattern)
        return