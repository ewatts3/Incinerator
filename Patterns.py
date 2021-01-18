import pretty_midi
from Pattern import Pattern

class Patterns:
    def __init__(self, lengthOfSixteenthNote, register):
        self.lengthOfSixteenthNote = lengthOfSixteenthNote
        self.register = register
        self.allPatterns = []

        self.CreateZerothPattern()
        self.CreateFirstPattern()
        self.CreateSecondPattern()
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
        self.CreateThirtySeventhPattern()
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

    def CreateZerothPattern(self): # a copy of the first pattern, put with an added eighth note rest to accomodate the first grace note
        zerothPattern = Pattern(self.lengthOfSixteenthNote)
        zerothPattern.AddRest('quarter')
        zerothPattern.AddNote('C', self.register, 'graceNote')
        zerothPattern.AddNote('E', self.register, 'quarter')
        zerothPattern.AddNote('C', self.register, 'graceNote')
        zerothPattern.AddNote('E', self.register, 'quarter')
        zerothPattern.AddNote('C', self.register, 'graceNote')
        zerothPattern.AddNote('E', self.register, 'quarter')
        self.allPatterns.append(zerothPattern)
        return

    def CreateFirstPattern(self):
        firstPattern = Pattern(self.lengthOfSixteenthNote)
        firstPattern.AddNote('C', self.register, 'graceNote')
        firstPattern.AddNote('E', self.register, 'quarter')
        firstPattern.AddNote('C', self.register, 'graceNote')
        firstPattern.AddNote('E', self.register, 'quarter')
        firstPattern.AddNote('C', self.register, 'graceNote')
        firstPattern.AddNote('E', self.register, 'quarter')
        self.allPatterns.append(firstPattern)
        return

    def CreateSecondPattern(self):
        secondPattern = Pattern(self.lengthOfSixteenthNote)
        secondPattern.AddNote('C', self.register, 'graceNote')
        secondPattern.AddNote('E', self.register, 'eighth')
        secondPattern.AddNote('F', self.register, 'eighth')
        secondPattern.AddNote('E', self.register, 'quarter')
        self.allPatterns.append(secondPattern)
        return

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
        seventhPattern.AddRest('eighth')
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
        twentySecondthPattern = Pattern(self.lengthOfSixteenthNote)
        twentySecondthPattern.AddNote('E', self.register, 'dottedQuarter')
        twentySecondthPattern.AddNote('E', self.register, 'dottedQuarter')
        twentySecondthPattern.AddNote('E', self.register, 'dottedQuarter')
        twentySecondthPattern.AddNote('E', self.register, 'dottedQuarter')
        twentySecondthPattern.AddNote('E', self.register, 'dottedQuarter')
        twentySecondthPattern.AddNote('F#', self.register, 'dottedQuarter')
        twentySecondthPattern.AddNote('G', self.register, 'dottedQuarter')
        twentySecondthPattern.AddNote('A', self.register, 'dottedQuarter')
        twentySecondthPattern.AddNote('B', self.register, 'eighth')
        self.allPatterns.append(twentySecondthPattern)
        return

    def CreateTwentyThirdPattern(self):
        twentyThirdPattern = Pattern(self.lengthOfSixteenthNote)
        twentyThirdPattern.AddNote('E', self.register, 'eighth')
        twentyThirdPattern.AddNote('F#', self.register, 'dottedQuarter')
        twentyThirdPattern.AddNote('F#', self.register, 'dottedQuarter')
        twentyThirdPattern.AddNote('F#', self.register, 'dottedQuarter')
        twentyThirdPattern.AddNote('F#', self.register, 'dottedQuarter')
        twentyThirdPattern.AddNote('F#', self.register, 'dottedQuarter')
        twentyThirdPattern.AddNote('G', self.register, 'dottedQuarter')
        twentyThirdPattern.AddNote('A', self.register, 'dottedQuarter')
        twentyThirdPattern.AddNote('B', self.register, 'quarter')
        self.allPatterns.append(twentyThirdPattern)
        return

    def CreateTwentyFourthPattern(self):
        twentyFourthPattern = Pattern(self.lengthOfSixteenthNote)
        twentyFourthPattern.AddNote('E', self.register, 'eighth')
        twentyFourthPattern.AddNote('F#', self.register, 'eighth')
        twentyFourthPattern.AddNote('G', self.register, 'dottedQuarter')
        twentyFourthPattern.AddNote('G', self.register, 'dottedQuarter')
        twentyFourthPattern.AddNote('G', self.register, 'dottedQuarter')
        twentyFourthPattern.AddNote('G', self.register, 'dottedQuarter')
        twentyFourthPattern.AddNote('G', self.register, 'dottedQuarter')
        twentyFourthPattern.AddNote('A', self.register, 'dottedQuarter')
        twentyFourthPattern.AddNote('B', self.register, 'eighth')
        self.allPatterns.append(twentyFourthPattern)
        return

    def CreateTwentyFifthPattern(self):
        twentyFifthPattern = Pattern(self.lengthOfSixteenthNote)
        twentyFifthPattern.AddNote('E', self.register, 'eighth')
        twentyFifthPattern.AddNote('F#', self.register, 'eighth')
        twentyFifthPattern.AddNote('G', self.register, 'eighth')
        twentyFifthPattern.AddNote('A', self.register, 'dottedQuarter')
        twentyFifthPattern.AddNote('A', self.register, 'dottedQuarter')
        twentyFifthPattern.AddNote('A', self.register, 'dottedQuarter')
        twentyFifthPattern.AddNote('A', self.register, 'dottedQuarter')
        twentyFifthPattern.AddNote('A', self.register, 'dottedQuarter')
        twentyFifthPattern.AddNote('B', self.register, 'dottedQuarter')
        self.allPatterns.append(twentyFifthPattern)
        return

    def CreateTwentySixthPattern(self):
        twentySixthPattern = Pattern(self.lengthOfSixteenthNote)
        twentySixthPattern.AddNote('E', self.register, 'eighth')
        twentySixthPattern.AddNote('F#', self.register, 'eighth')
        twentySixthPattern.AddNote('G', self.register, 'eighth')
        twentySixthPattern.AddNote('A', self.register, 'eighth')
        twentySixthPattern.AddNote('B', self.register, 'dottedQuarter')
        twentySixthPattern.AddNote('B', self.register, 'dottedQuarter')
        twentySixthPattern.AddNote('B', self.register, 'dottedQuarter')
        twentySixthPattern.AddNote('B', self.register, 'dottedQuarter')
        twentySixthPattern.AddNote('B', self.register, 'dottedQuarter')
        self.allPatterns.append(twentySixthPattern)
        return

    def CreateTwentySeventhPattern(self):
        twentySeventhPattern = Pattern(self.lengthOfSixteenthNote)
        twentySeventhPattern.AddNote('E', self.register, 'sixteenth')
        twentySeventhPattern.AddNote('F#', self.register, 'sixteenth')
        twentySeventhPattern.AddNote('E', self.register, 'sixteenth')
        twentySeventhPattern.AddNote('F#', self.register, 'sixteenth')
        twentySeventhPattern.AddNote('G', self.register, 'eighth')
        twentySeventhPattern.AddNote('E', self.register, 'sixteenth')
        twentySeventhPattern.AddNote('G', self.register, 'sixteenth')
        twentySeventhPattern.AddNote('F#', self.register, 'sixteenth')
        twentySeventhPattern.AddNote('E', self.register, 'sixteenth')
        twentySeventhPattern.AddNote('F#', self.register, 'sixteenth')
        twentySeventhPattern.AddNote('E#', self.register, 'sixteenth')
        self.allPatterns.append(twentySeventhPattern)
        return

    def CreateTwentyEighthPattern(self):
        twentyEighthPattern = Pattern(self.lengthOfSixteenthNote)
        twentyEighthPattern.AddNote('E', self.register, 'sixteenth')
        twentyEighthPattern.AddNote('F#', self.register, 'sixteenth')
        twentyEighthPattern.AddNote('E', self.register, 'sixteenth')
        twentyEighthPattern.AddNote('F#', self.register, 'sixteenth')
        twentyEighthPattern.AddNote('E', self.register, 'dottedEighth')
        twentyEighthPattern.AddNote('E', self.register, 'sixteenth')
        self.allPatterns.append(twentyEighthPattern)
        return

    def CreateTwentyNinthPattern(self):
        twentyNinthPattern = Pattern(self.lengthOfSixteenthNote)
        twentyNinthPattern.AddNote('E', self.register, 'dottedHalf')
        twentyNinthPattern.AddNote('G', self.register, 'dottedHalf')
        twentyNinthPattern.AddNote('C', self.register + 1, 'dottedHalf')
        self.allPatterns.append(twentyNinthPattern)
        return

    def CreateThirtiethPattern(self):
        thirtiethPattern = Pattern(self.lengthOfSixteenthNote)
        thirtiethPattern.AddNote('C', self.register + 1, 'dottedWhole')
        self.allPatterns.append(thirtiethPattern)
        return

    def CreateThirtyFirstPattern(self):
        thirtyFirstPattern = Pattern(self.lengthOfSixteenthNote)
        thirtyFirstPattern.AddNote('G', self.register, 'sixteenth')
        thirtyFirstPattern.AddNote('F', self.register, 'sixteenth')
        thirtyFirstPattern.AddNote('G', self.register, 'sixteenth')
        thirtyFirstPattern.AddNote('B', self.register, 'sixteenth')
        thirtyFirstPattern.AddNote('G', self.register, 'sixteenth')
        thirtyFirstPattern.AddNote('B', self.register, 'sixteenth')
        self.allPatterns.append(thirtyFirstPattern)
        return

    def CreateThirtySecondthPattern(self):
        thirtySecondthPattern = Pattern(self.lengthOfSixteenthNote)
        thirtySecondthPattern.AddNote('F', self.register, 'sixteenth')
        thirtySecondthPattern.AddNote('G', self.register, 'sixteenth')
        thirtySecondthPattern.AddNote('F', self.register, 'sixteenth')
        thirtySecondthPattern.AddNote('G', self.register, 'sixteenth')
        thirtySecondthPattern.AddNote('B', self.register, 'sixteenth')
        thirtySecondthPattern.AddNote('F', self.register, 'dottedHalfTiedToSixteenth')
        thirtySecondthPattern.AddNote('G', self.register, 'dottedQuarter')
        self.allPatterns.append(thirtySecondthPattern)
        return

    def CreateThirtyThirdPattern(self):
        thirtyThirdPattern = Pattern(self.lengthOfSixteenthNote)
        thirtyThirdPattern.AddNote('G', self.register, 'sixteenth')
        thirtyThirdPattern.AddNote('F', self.register, 'sixteenth')
        thirtyThirdPattern.AddRest('eighth')
        self.allPatterns.append(thirtyThirdPattern)
        return

    def CreateThirtyFourthPattern(self):
        thirtyFourthPattern = Pattern(self.lengthOfSixteenthNote)
        thirtyFourthPattern.AddNote('G', self.register, 'sixteenth')
        thirtyFourthPattern.AddNote('F', self.register, 'sixteenth')
        self.allPatterns.append(thirtyFourthPattern)
        return

    def CreateThirtyFifthPattern(self):
        thirtyFifthPattern = Pattern(self.lengthOfSixteenthNote)
        thirtyFifthPattern.AddNote('F', self.register, 'sixteenth')
        thirtyFifthPattern.AddNote('G', self.register, 'sixteenth')
        thirtyFifthPattern.AddNote('B', self.register, 'sixteenth')
        thirtyFifthPattern.AddNote('G', self.register, 'sixteenth')
        thirtyFifthPattern.AddNote('B', self.register, 'sixteenth')
        thirtyFifthPattern.AddNote('G', self.register, 'sixteenth')
        thirtyFifthPattern.AddNote('B', self.register, 'sixteenth')
        thirtyFifthPattern.AddNote('G', self.register, 'sixteenth')
        thirtyFifthPattern.AddNote('B', self.register, 'sixteenth')
        thirtyFifthPattern.AddNote('G', self.register, 'sixteenth')
        thirtyFifthPattern.AddRest('eighth')
        thirtyFifthPattern.AddRest('quarter')
        thirtyFifthPattern.AddRest('quarter')
        thirtyFifthPattern.AddRest('quarter')
        thirtyFifthPattern.AddNote('Bb', self.register, 'quarter')
        thirtyFifthPattern.AddNote('G', self.register + 1, 'dottedHalf')
        thirtyFifthPattern.AddNote('A', self.register + 1, 'eighth')
        thirtyFifthPattern.AddNote('G', self.register + 1, 'quarter')
        thirtyFifthPattern.AddNote('B', self.register + 1, 'eighth')
        thirtyFifthPattern.AddNote('A', self.register + 1, 'dottedQuarter')
        thirtyFifthPattern.AddNote('G', self.register + 1, 'eighth')
        thirtyFifthPattern.AddNote('E', self.register + 1, 'dottedHalf')
        thirtyFifthPattern.AddNote('G', self.register + 1, 'eighth')
        thirtyFifthPattern.AddNote('F#', self.register + 1, 'dottedHalfTiedToEighth')
        thirtyFifthPattern.AddRest('quarter')
        thirtyFifthPattern.AddRest('quarter')
        thirtyFifthPattern.AddRest('eighth')
        thirtyFifthPattern.AddNote('E', self.register + 1, 'halfTiedToEighth')
        thirtyFifthPattern.AddNote('F', self.register + 1, 'dottedWhole')
        self.allPatterns.append(thirtyFifthPattern)
        return

    def CreateThirtySixthPattern(self):
        thirtySixthPattern = Pattern(self.lengthOfSixteenthNote)
        thirtySixthPattern.AddNote('F', self.register, 'sixteenth')
        thirtySixthPattern.AddNote('G', self.register, 'sixteenth')
        thirtySixthPattern.AddNote('B', self.register, 'sixteenth')
        thirtySixthPattern.AddNote('G', self.register, 'sixteenth')
        thirtySixthPattern.AddNote('B', self.register, 'sixteenth')
        thirtySixthPattern.AddNote('G', self.register, 'sixteenth')
        self.allPatterns.append(thirtySixthPattern)
        return

    def CreateThirtySeventhPattern(self):
        thirtySeventhPattern = Pattern(self.lengthOfSixteenthNote)
        thirtySeventhPattern.AddNote('F', self.register, 'sixteenth')
        thirtySeventhPattern.AddNote('G', self.register, 'sixteenth')
        self.allPatterns.append(thirtySeventhPattern)
        return

    def CreateThirtyEighthPattern(self):
        thirtyEighthPattern = Pattern(self.lengthOfSixteenthNote)
        thirtyEighthPattern.AddNote('F', self.register, 'sixteenth')
        thirtyEighthPattern.AddNote('G', self.register, 'sixteenth')
        thirtyEighthPattern.AddNote('B', self.register, 'sixteenth')
        self.allPatterns.append(thirtyEighthPattern)
        return

    def CreateThirtyNinthPattern(self):
        thirtyNinthPattern = Pattern(self.lengthOfSixteenthNote)
        thirtyNinthPattern.AddNote('B', self.register, 'sixteenth')
        thirtyNinthPattern.AddNote('G', self.register, 'sixteenth')
        thirtyNinthPattern.AddNote('F', self.register, 'sixteenth')
        thirtyNinthPattern.AddNote('F', self.register, 'sixteenth')
        thirtyNinthPattern.AddNote('B', self.register, 'sixteenth')
        thirtyNinthPattern.AddNote('C', self.register + 1, 'sixteenth')
        self.allPatterns.append(thirtyNinthPattern)
        return

    def CreateFortiethPattern(self):
        fortiethPattern = Pattern(self.lengthOfSixteenthNote)
        fortiethPattern.AddNote('B', self.register, 'sixteenth')
        fortiethPattern.AddNote('F', self.register, 'sixteenth')
        self.allPatterns.append(fortiethPattern)
        return

    def CreateFortyFirstPattern(self):
        fortyFirstPattern = Pattern(self.lengthOfSixteenthNote)
        fortyFirstPattern.AddNote('B', self.register, 'sixteenth')
        fortyFirstPattern.AddNote('G', self.register, 'sixteenth')
        self.allPatterns.append(fortyFirstPattern)
        return

    def CreateFortySecondthPattern(self):
        fortySecondthPattern = Pattern(self.lengthOfSixteenthNote)
        fortySecondthPattern.AddNote('C', self.register + 1, 'whole')
        fortySecondthPattern.AddNote('B', self.register, 'whole')
        fortySecondthPattern.AddNote('A', self.register, 'whole')
        fortySecondthPattern.AddNote('C', self.register + 1, 'whole')
        self.allPatterns.append(fortySecondthPattern)
        return

    def CreateFortyThirdPattern(self):
        fortyThirdPattern = Pattern(self.lengthOfSixteenthNote)
        fortyThirdPattern.AddNote('F', self.register + 1, 'sixteenth')
        fortyThirdPattern.AddNote('E', self.register + 1, 'sixteenth')
        fortyThirdPattern.AddNote('F', self.register + 1, 'sixteenth')
        fortyThirdPattern.AddNote('E', self.register + 1, 'sixteenth')
        fortyThirdPattern.AddNote('E', self.register + 1, 'eighth')
        fortyThirdPattern.AddNote('E', self.register + 1, 'eighth')
        fortyThirdPattern.AddNote('E', self.register + 1, 'eighth')
        fortyThirdPattern.AddNote('F', self.register + 1, 'sixteenth')
        fortyThirdPattern.AddNote('E', self.register + 1, 'sixteenth')
        self.allPatterns.append(fortyThirdPattern)
        return

    def CreateFortyFourthPattern(self):
        fortyFourthPattern = Pattern(self.lengthOfSixteenthNote)
        fortyFourthPattern.AddNote('F', self.register + 1, 'eighth')
        fortyFourthPattern.AddNote('E', self.register + 1, 'quarter')
        fortyFourthPattern.AddNote('E', self.register + 1, 'eighth')
        fortyFourthPattern.AddNote('C', self.register + 1, 'quarter')
        self.allPatterns.append(fortyFourthPattern)
        return

    def CreateFortyFifthPattern(self):
        fortyFifthPattern = Pattern(self.lengthOfSixteenthNote)
        fortyFifthPattern.AddNote('D', self.register + 1, 'quarter')
        fortyFifthPattern.AddNote('D', self.register + 1, 'quarter')
        fortyFifthPattern.AddNote('G', self.register, 'quarter')
        self.allPatterns.append(fortyFifthPattern)
        return

    def CreateFortySixthPattern(self):
        fortySixthPattern = Pattern(self.lengthOfSixteenthNote)
        fortySixthPattern.AddNote('G', self.register, 'sixteenth')
        fortySixthPattern.AddNote('D', self.register + 1, 'sixteenth')
        fortySixthPattern.AddNote('E', self.register + 1, 'sixteenth')
        fortySixthPattern.AddNote('D', self.register + 1, 'sixteenth')
        fortySixthPattern.AddRest('eighth')
        fortySixthPattern.AddNote('G', self.register, 'eighth')
        fortySixthPattern.AddRest('eighth')
        fortySixthPattern.AddNote('G', self.register, 'eighth')
        fortySixthPattern.AddRest('eighth')
        fortySixthPattern.AddNote('G', self.register, 'eighth')
        fortySixthPattern.AddNote('G', self.register, 'sixteenth')
        fortySixthPattern.AddNote('D', self.register + 1, 'sixteenth')
        fortySixthPattern.AddNote('E', self.register + 1, 'sixteenth')
        fortySixthPattern.AddNote('D', self.register + 1, 'sixteenth')
        self.allPatterns.append(fortySixthPattern)
        return

    def CreateFortySeventhPattern(self):
        fortySeventhPattern = Pattern(self.lengthOfSixteenthNote)
        fortySeventhPattern.AddNote('D', self.register + 1, 'sixteenth')
        fortySeventhPattern.AddNote('E', self.register + 1, 'sixteenth')
        fortySeventhPattern.AddNote('D', self.register + 1, 'eighth')
        self.allPatterns.append(fortySeventhPattern)
        return

    def CreateFortyEighthPattern(self):
        fortyEighthPattern = Pattern(self.lengthOfSixteenthNote)
        fortyEighthPattern.AddNote('G', self.register, 'dottedWhole')
        fortyEighthPattern.AddNote('G', self.register, 'whole')
        fortyEighthPattern.AddNote('F', self.register, 'wholeTiedToQuarter')
        self.allPatterns.append(fortyEighthPattern)
        return

    def CreateFortyNinthPattern(self):
        fortyNinthPattern = Pattern(self.lengthOfSixteenthNote)
        fortyNinthPattern.AddNote('F', self.register, 'sixteenth')
        fortyNinthPattern.AddNote('G', self.register, 'sixteenth')
        fortyNinthPattern.AddNote('Bb', self.register, 'sixteenth')
        fortyNinthPattern.AddNote('G', self.register, 'sixteenth')
        fortyNinthPattern.AddNote('Bb', self.register, 'sixteenth')
        fortyNinthPattern.AddNote('G', self.register, 'sixteenth')
        self.allPatterns.append(fortyNinthPattern)
        return

    def CreateFiftiethPattern(self):
        fiftiethPattern = Pattern(self.lengthOfSixteenthNote)
        fiftiethPattern.AddNote('F', self.register, 'sixteenth')
        fiftiethPattern.AddNote('G', self.register, 'sixteenth')
        self.allPatterns.append(fiftiethPattern)
        return

    def CreateFiftyFirstPattern(self): #slightly a lie - I repeated the measure to avoid an infinite loop when finding the eighth note beat
        fiftyFirstPattern = Pattern(self.lengthOfSixteenthNote)
        fiftyFirstPattern.AddNote('F', self.register, 'sixteenth')
        fiftyFirstPattern.AddNote('G', self.register, 'sixteenth')
        fiftyFirstPattern.AddNote('Bb', self.register, 'sixteenth')
        fiftyFirstPattern.AddNote('F', self.register, 'sixteenth')
        fiftyFirstPattern.AddNote('G', self.register, 'sixteenth')
        fiftyFirstPattern.AddNote('Bb', self.register, 'sixteenth')
        self.allPatterns.append(fiftyFirstPattern)
        return

    def CreateFiftySecondthPattern(self):
        fiftySecondthPattern = Pattern(self.lengthOfSixteenthNote)
        fiftySecondthPattern.AddNote('G', self.register, 'sixteenth')
        fiftySecondthPattern.AddNote('Bb', self.register, 'sixteenth')
        self.allPatterns.append(fiftySecondthPattern)
        return

    def CreateFiftyThirdPattern(self):
        fiftyThirdPattern = Pattern(self.lengthOfSixteenthNote)
        fiftyThirdPattern.AddNote('Bb', self.register, 'sixteenth')
        fiftyThirdPattern.AddNote('G', self.register, 'sixteenth')
        self.allPatterns.append(fiftyThirdPattern)
        return