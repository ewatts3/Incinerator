import random

class Dynamic:
    def __init__(self):
        self.maxDynamic = 127
        self.minimumDynamic = 0
        self.currentDynamic = 63
        self.numberOfTimesChanged = 0
        self.isIncreasing = True
        return

    def DecideDynamic(self):
        if(random.randint(0, 1) == 0):
            if self.currentDynamic == self.maxDynamic or self.currentDynamic == self.minimumDynamic:
                self.isIncreasing = not self.isIncreasing
            if self.isIncreasing is True:
                self.IncreaseDynamic()
            elif self.isIncreasing is False:
                self.DecreaseDynamic()
            #self.numberOfTimesChanged = self.numberOfTimesChanged + 1
        #if(self.numberOfTimesChanged > 30):
        #    if(random.randint(0, 9) == 0):
        #        self.isIncreasing = not self.isIncreasing
        #        self.numberOfTimesChanged = 0
        return

    def GetCurrentDynamic(self):
        return self.currentDynamic

    def IncreaseDynamic(self):
        if self.currentDynamic < self.maxDynamic:
            self.currentDynamic = self.currentDynamic + 1
        return

    def DecreaseDynamic(self):
        if self.currentDynamic > self.minimumDynamic:
            self.currentDynamic = self.currentDynamic - 1
        return

    def InitializeDynamicForEnding(self):
        self.numberOfTimesChanged = 0
        self.isIncreasing = not self.isIncreasing
        return

    def ChangeDynamicForEnding(self):
        if self.numberOfTimesChanged == 30 or self.currentDynamic == self.maxDynamic or self.currentDynamic == self.minimumDynamic:
            self.isIncreasing = not self.isIncreasing
            self.numberOfTimesChanged = 0
        if self.isIncreasing is True:
            self.IncreaseDynamic()
        elif self.isIncreasing is False:
            self.DecreaseDynamic()
        return
