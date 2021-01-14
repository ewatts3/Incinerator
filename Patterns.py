import pretty_midi
from Pattern import Pattern

class Patterns:
    def __init__(self, lengthOfSixteenthNote):
        self.lengthOfSixteenthNote = lengthOfSixteenthNote
        self.allPatterns = []

        self.CreateThirdPattern()
        self.CreateFourthPattern()
        self.CreateFifthPattern()
        self.CreateSixthPattern()
        self.CreateSeventhPattern()
        self.CreateEighthPattern()
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
        fourthPattern = Pattern(self.lengthOfSixteenthNote)
        fourthPattern.AddRest('eighth')
        fourthPattern.AddNote('E', 4, 'eighth')
        fourthPattern.AddNote('F', 4, 'eighth')
        fourthPattern.AddNote('G', 4, 'eighth')
        self.allPatterns.append(fourthPattern)
        return

    def CreateFifthPattern(self):
        fifthPattern = Pattern(self.lengthOfSixteenthNote)
        fifthPattern.AddNote('E', 4, 'eighth')
        fifthPattern.AddNote('F', 4, 'eighth')
        fifthPattern.AddNote('G', 4, 'eighth')
        fifthPattern.AddRest('eighth')
        self.allPatterns.append(fifthPattern)
        return

    def CreateSixthPattern(self):
        sixthPattern = Pattern(self.lengthOfSixteenthNote)
        sixthPattern.AddNote('C', 5, 'tiedWhole')
        self.allPatterns.append(sixthPattern)
        return

    def CreateSeventhPattern(self):
        seventhPattern = Pattern(self.lengthOfSixteenthNote)
        seventhPattern.AddRest('quarter')
        seventhPattern.AddRest('quarter')
        seventhPattern.AddRest('quarter')
        seventhPattern.AddRest('eighth')
        seventhPattern.AddNote('C', 4, 'sixteenth')
        seventhPattern.AddNote('C', 4, 'sixteenth')
        seventhPattern.AddNote('C', 4, 'eighth')
        seventhPattern.AddRest('quarter')
        seventhPattern.AddRest('quarter')
        seventhPattern.AddRest('quarter')
        seventhPattern.AddRest('quarter')
        self.allPatterns.append(seventhPattern)
        return

    def CreateEighthPattern(self):
        eighthPattern = Pattern(self.lengthOfSixteenthNote)
        eighthPattern.AddNote('G', 4, 'dottedWhole')
        eighthPattern.AddNote('F', 4, 'tiedWhole')
        self.allPatterns.append(eighthPattern)
        return