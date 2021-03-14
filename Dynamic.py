import random

class Dynamic:
    def __init__(self):
        self.maxDynamic = 126
        self.minimumDynamic = 40
        self.currentDynamic = 80
        if(random.randint(0, 1) == 0):
            self.isIncreasing = True
        else:
            self.isIncreasing = False
        return

    def DecideDynamic(self):
        if self.currentDynamic == self.maxDynamic or self.currentDynamic == self.minimumDynamic:
            self.isIncreasing = not self.isIncreasing

        if self.isIncreasing is True:
            self.IncreaseDynamic()
        elif self.isIncreasing is False:
            self.DecreaseDynamic()
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
        self.isIncreasing = not self.isIncreasing
        return

    def ChangeDynamicForEnding(self):
        if self.currentDynamic == self.maxDynamic or self.currentDynamic == self.minimumDynamic:
            self.isIncreasing = not self.isIncreasing

        if self.isIncreasing is True:
            self.currentDynamic = self.currentDynamic + 5
            if self.currentDynamic > self.maxDynamic:
                self.currentDynamic = self.maxDynamic
        elif self.isIncreasing is False:
            self.currentDynamic = self.currentDynamic - 5
            if self.currentDynamic < self.minimumDynamic:
                self.currentDynamic = self.minimumDynamic
        return
