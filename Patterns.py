import pretty_midi
from Pattern import Pattern

class Patterns:
    def __init__(self, lengthOfSixteenthNote, register):
        self.lengthOfSixteenthNote = lengthOfSixteenthNote
        self.register = register
        self.allPatterns = []

        self.CreateThirdPattern()
        self.CreateFourthPattern()
        self.CreateFifthPattern()
        self.CreateSixthPattern()
        self.CreateSeventhPattern()
        self.CreateEighthPattern()
        self.CreateNinthPattern()
        self.CreateTenthPattern()
        self.CreateEleventhPattern()
        self.CreateTwelfthPattern()
        self.CreateThirteenthPattern()
        self.CreateFourteenthPattern()
        self.CreateFifteenthPattern()
        self.CreateSixteenthPattern()
        self.CreateSeventeenthPattern()
        self.CreateEighteenthPattern()
        self.CreateNineteenthPattern()
        self.CreateTwentiethPattern()
        self.CreateTwentyFirstPattern()
        self.CreateTwentySecondthPattern()
        self.CreateTwentyThirdPattern()
        self.CreateTwentyFourthPattern()
        self.CreateTwentyFifthPattern()
        self.CreateTwentySixthPattern()
        self.CreateTwentySeventhPattern()
        self.CreateTwentyEighthPattern()
        self.CreateTwentyNinthPattern()
        self.CreateThirtiethPattern()
        self.CreateThirtyFirstPattern()
        self.CreateThirtySecondthPattern()
        self.CreateThirtyThirdPattern()
        self.CreateThirtyFourthPattern()
        self.CreateThirtyFifthPattern()
        self.CreateThirtySixthPattern()
        self.CreateThirtyEighthPattern()
        self.CreateThirtyNinthPattern()
        self.CreateFortiethPattern()
        self.CreateFortyFirstPattern()
        self.CreateFortySecondthPattern()
        self.CreateFortyThirdPattern()
        self.CreateFortyFourthPattern()
        self.CreateFortyFifthPattern()
        self.CreateFortySixthPattern()
        self.CreateFortySeventhPattern()
        self.CreateFortyEighthPattern()
        self.CreateFortyNinthPattern()
        self.CreateFiftiethPattern()
        self.CreateFiftyFirstPattern()
        self.CreateFiftySecondthPattern()
        self.CreateFiftyThirdPattern()
        return

    def GetAllPatterns(self):
        return self.allPatterns

    def CreateThirdPattern(self):
        thirdPattern = Pattern(self.lengthOfSixteenthNote)
        thirdPattern.AddRest('eighth')
        thirdPattern.AddNote('E', self.register, 'eighth')
        thirdPattern.AddNote('F', self.register, 'eighth')
        thirdPattern.AddNote('E', self.register, 'eighth')
        self.allPatterns.append(thirdPattern)
        return

    def CreateFourthPattern(self):
        fourthPattern = Pattern(self.lengthOfSixteenthNote)
        fourthPattern.AddRest('eighth')
        fourthPattern.AddNote('E', self.register, 'eighth')
        fourthPattern.AddNote('F', self.register, 'eighth')
        fourthPattern.AddNote('G', self.register, 'eighth')
        self.allPatterns.append(fourthPattern)
        return

    def CreateFifthPattern(self):
        fifthPattern = Pattern(self.lengthOfSixteenthNote)
        fifthPattern.AddNote('E', self.register, 'eighth')
        fifthPattern.AddNote('F', self.register, 'eighth')
        fifthPattern.AddNote('G', self.register, 'eighth')
        fifthPattern.AddRest('eighth')
        self.allPatterns.append(fifthPattern)
        return

    def CreateSixthPattern(self):
        sixthPattern = Pattern(self.lengthOfSixteenthNote)
        sixthPattern.AddNote('C', self.register + 1, 'tiedWhole')
        self.allPatterns.append(sixthPattern)
        return

    def CreateSeventhPattern(self):
        seventhPattern = Pattern(self.lengthOfSixteenthNote)
        seventhPattern.AddRest('quarter')
        seventhPattern.AddRest('quarter')
        seventhPattern.AddRest('quarter')
        seventhPattern.AddRest('eighth')
        seventhPattern.AddNote('C', self.register, 'sixteenth')
        seventhPattern.AddNote('C', self.register, 'sixteenth')
        seventhPattern.AddNote('C', self.register, 'eighth')
        seventhPattern.AddRest('quarter')
        seventhPattern.AddRest('quarter')
        seventhPattern.AddRest('quarter')
        seventhPattern.AddRest('quarter')
        self.allPatterns.append(seventhPattern)
        return

    def CreateEighthPattern(self):
        eighthPattern = Pattern(self.lengthOfSixteenthNote)
        eighthPattern.AddNote('G', self.register, 'dottedWhole')
        eighthPattern.AddNote('F', self.register, 'tiedWhole')
        self.allPatterns.append(eighthPattern)
        return

    def CreateNinthPattern(self):
        ninthPattern = Pattern(self.lengthOfSixteenthNote)
        ninthPattern.AddNote('B', self.register, 'sixteenth')
        ninthPattern.AddNote('G', self.register, 'sixteenth')
        ninthPattern.AddRest('eighth')
        ninthPattern.AddRest('quarter')
        ninthPattern.AddRest('quarter')
        ninthPattern.AddRest('quarter')
        self.allPatterns.append(ninthPattern)
        return

    def CreateTenthPattern(self):
        tenthPattern = Pattern(self.lengthOfSixteenthNote)
        tenthPattern.AddNote('B', self.register, 'sixteenth')
        tenthPattern.AddNote('G', self.register, 'sixteenth')
        self.allPatterns.append(tenthPattern)
        return

    def CreateEleventhPattern(self):
        eleventhPattern = Pattern(self.lengthOfSixteenthNote)
        eleventhPattern.AddNote('F', self.register, 'sixteenth')
        eleventhPattern.AddNote('G', self.register, 'sixteenth')
        eleventhPattern.AddNote('B', self.register, 'sixteenth')
        eleventhPattern.AddNote('G', self.register, 'sixteenth')
        eleventhPattern.AddNote('B', self.register, 'sixteenth')
        eleventhPattern.AddNote('G', self.register, 'sixteenth')
        self.allPatterns.append(eleventhPattern)
        return

    def CreateTwelfthPattern(self):
        twelfthPattern = Pattern(self.lengthOfSixteenthNote)
        twelfthPattern.AddNote('F', self.register, 'eighth')
        twelfthPattern.AddNote('G', self.register, 'eighth')
        twelfthPattern.AddNote('B', self.register, 'whole')
        twelfthPattern.AddNote('C', self.register + 1, 'quarter')
        self.allPatterns.append(twelfthPattern)
        return

    def CreateThirteenthPattern(self):
        thirteenthPattern = Pattern(self.lengthOfSixteenthNote)
        thirteenthPattern.AddNote('B', self.register, 'sixteenth')
        thirteenthPattern.AddNote('G', self.register, 'dottedEighth')
        thirteenthPattern.AddNote('G', self.register, 'sixteenth')
        thirteenthPattern.AddNote('F', self.register, 'sixteenth')
        thirteenthPattern.AddNote('G', self.register, 'eighth')
        thirteenthPattern.AddRest('dottedEighth')
        thirteenthPattern.AddNote('G', self.register, 'dottedHalfTiedToSixteenth')
        self.allPatterns.append(thirteenthPattern)
        return

    def CreateFourteenthPattern(self):
        fourteenthPattern = Pattern(self.lengthOfSixteenthNote)
        fourteenthPattern.AddNote('C', self.register + 1, 'whole')
        fourteenthPattern.AddNote('B', self.register, 'whole')
        fourteenthPattern.AddNote('G', self.register, 'whole')
        fourteenthPattern.AddNote('F#', self.register, 'whole')
        self.allPatterns.append(fourteenthPattern)
        return

    def CreateFifteenthPattern(self):
        fifteenthPattern = Pattern(self.lengthOfSixteenthNote)
        fifteenthPattern.AddNote('G', self.register, 'sixteenth')
        fifteenthPattern.AddRest('dottedEighth')
        fifteenthPattern.AddRest('quarter')
        fifteenthPattern.AddRest('quarter')
        fifteenthPattern.AddRest('quarter')
        self.allPatterns.append(fifteenthPattern)
        return

    def CreateSixteenthPattern(self):
        sixteenthPattern = Pattern(self.lengthOfSixteenthNote)
        sixteenthPattern.AddNote('G', self.register, 'sixteenth')
        sixteenthPattern.AddNote('B', self.register, 'sixteenth')
        sixteenthPattern.AddNote('C', self.register + 1, 'sixteenth')
        sixteenthPattern.AddNote('B', self.register, 'sixteenth')
        self.allPatterns.append(sixteenthPattern)
        return

    def CreateSeventeenthPattern(self):
        seventeenthPattern = Pattern(self.lengthOfSixteenthNote)
        seventeenthPattern.AddNote('B', self.register, 'sixteenth')
        seventeenthPattern.AddNote('C', self.register + 1, 'sixteenth')
        seventeenthPattern.AddNote('B', self.register, 'sixteenth')
        seventeenthPattern.AddNote('C', self.register + 1, 'sixteenth')
        seventeenthPattern.AddNote('B', self.register, 'sixteenth')
        seventeenthPattern.AddRest('sixteenth')
        self.allPatterns.append(seventeenthPattern)
        return

    def CreateEighteenthPattern(self):
        eighteenthPattern = Pattern(self.lengthOfSixteenthNote)
        eighteenthPattern.AddNote('E', self.register, 'sixteenth')
        eighteenthPattern.AddNote('F#', self.register, 'sixteenth')
        eighteenthPattern.AddNote('E', self.register, 'sixteenth')
        eighteenthPattern.AddNote('F#', self.register, 'sixteenth')
        eighteenthPattern.AddNote('E', self.register, 'dottedEighth')
        eighteenthPattern.AddNote('E', self.register, 'sixteenth')
        self.allPatterns.append(eighteenthPattern)
        return

    def CreateNineteenthPattern(self):
        nineteenthPattern = Pattern(self.lengthOfSixteenthNote)
        nineteenthPattern.AddRest('quarter')
        nineteenthPattern.AddRest('eighth')
        nineteenthPattern.AddNote('G', self.register + 1, 'dottedQuarter')
        self.allPatterns.append(nineteenthPattern)
        return

    def CreateTwentiethPattern(self):
        twentiethPattern = Pattern(self.lengthOfSixteenthNote)
        twentiethPattern.AddNote('E', self.register, 'sixteenth')
        twentiethPattern.AddNote('F#', self.register, 'sixteenth')
        twentiethPattern.AddNote('E', self.register, 'sixteenth')
        twentiethPattern.AddNote('F#', self.register, 'sixteenth')
        twentiethPattern.AddNote('G', self.register - 1, 'dottedEighth')
        twentiethPattern.AddNote('E', self.register, 'sixteenth')
        twentiethPattern.AddNote('F#', self.register, 'sixteenth')
        twentiethPattern.AddNote('E', self.register, 'sixteenth')
        twentiethPattern.AddNote('F#', self.register, 'sixteenth')
        twentiethPattern.AddNote('E', self.register, 'sixteenth')
        self.allPatterns.append(twentiethPattern)
        return

    def CreateTwentyFirstPattern(self):
        twentyFirstPattern = Pattern(self.lengthOfSixteenthNote)
        twentyFirstPattern.AddNote('F#', self.register, 'dottedHalf')
        self.allPatterns.append(twentyFirstPattern)
        return

    def CreateTwentySecondthPattern(self):
        return

    def CreateTwentyThirdPattern(self):
        return

    def CreateTwentyFourthPattern(self):
        return

    def CreateTwentyFifthPattern(self):
        return

    def CreateTwentySixthPattern(self):
        return

    def CreateTwentySeventhPattern(self):
        return

    def CreateTwentyEighthPattern(self):
        return

    def CreateTwentyNinthPattern(self):
        return

    def CreateThirtiethPattern(self):
        return

    def CreateThirtyFirstPattern(self):
        return

    def CreateThirtySecondthPattern(self):
        return

    def CreateThirtyThirdPattern(self):
        return

    def CreateThirtyFourthPattern(self):
        return

    def CreateThirtyFifthPattern(self):
        return

    def CreateThirtySixthPattern(self):
        return

    def CreateThirtySeventhPattern(self):
        return

    def CreateThirtyEighthPattern(self):
        return

    def CreateThirtyNinthPattern(self):
        return

    def CreateFortiethPattern(self):
        return

    def CreateFortyFirstPattern(self):
        return

    def CreateFortySecondthPattern(self):
        return

    def CreateFortyThirdPattern(self):
        return

    def CreateFortyFourthPattern(self):
        return

    def CreateFortyFifthPattern(self):
        return

    def CreateFortySixthPattern(self):
        return

    def CreateFortySeventhPattern(self):
        return

    def CreateFortyEighthPattern(self):
        return

    def CreateFortyNinthPattern(self):
        return

    def CreateFiftiethPattern(self):
        return

    def CreateFiftyFirstPattern(self):
        return

    def CreateFiftySecondthPattern(self):
        return

    def CreateFiftyThirdPattern(self):
        return