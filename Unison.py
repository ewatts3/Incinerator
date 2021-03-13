import random

class Unison:
    def __init__(self):
        self.numberOfUnisons = 0
        self.patternOfLastUnison = 0
        self.numberOfPatternsSinceLastUnison = 0
        return

    def DecideIfCompositionShouldBecomeUnison(self, lowestPattern, highestPattern, numberOfPatterns):
        if(self.numberOfUnisons < 2): #max 2 unisons per piece
            self.numberOfPatternsSinceLastUnison = lowestPattern - self.patternOfLastUnison
            if((lowestPattern > 10 and highestPattern < numberOfPatterns - 10) and self.numberOfPatternsSinceLastUnison >= 10): #has it been long enough since the last unison and are we in a good range?
                if(random.randint(0, 19) == 0): #if all above is true, randomly decide if unison will happen
                    self.numberOfUnisons = self.numberOfUnisons + 1
                    return True
        return False

    def IncrementNumberOfUnisons(self):
        self.numberOfUnisons = self.numberOfUnisons + 1
        return

    def GetNumberOfUnisons(self):
        return self.numberOfUnisons

    def SetPatternOfLastUnison(self, pattern):
        self.patternOfLastUnison = pattern
        return

    def GetPatternOfLastUnison(self):
        return self.patternOfLastUnison

    def GetNumberOfPatternsSinceLastUnison(self, currentPattern):
        return (currentPattern - self.numberOfPatternsSinceLastUnison)