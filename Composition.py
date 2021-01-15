import pretty_midi
from Voice import Voice
from Patterns import Patterns

import random

class Composition:
    def __init__(self, numberOfVoices, tempo):
        self.lengthOfSixteenthNote = self.FindLengthOfSixteenthNote(tempo)
        register = 6
        self.voices = []
        for i in range(0, numberOfVoices):
            patterns = Patterns(self.lengthOfSixteenthNote, register)
            allPatterns = patterns.GetAllPatterns()
            self.voices.append(Voice(allPatterns))
            if(i % 2 == 0):
                register = register - 1

        self.CreateComposition()
        #self.CheckPatterns()
        self.WriteFile()
        return

    def FindLengthOfSixteenthNote(self, tempo):
        quarterNoteLength = (60 / tempo)
        sixteenthNoteLength = (quarterNoteLength / 4)
        return sixteenthNoteLength

    def CreateComposition(self):
        allVoicesDone = False
        place = 0

        while self.CheckIfAllVoicesAreDone() is False:

            #largestPlaceIndex = self.GetLargestPlace()
            largestPlaceIndex = -1

            for i in range(0, len(self.voices)):
                if i != largestPlaceIndex:
                    if self.voices[i].IsNotOnLastPattern() is True:
                        if((self.voices[i].GetPlace() % (self.lengthOfSixteenthNote * 4)) != 0): #we only want to add something when it's on a quarter note beat to avoid innappropriate polyrhythms
                            self.voices[i].AddPattern()

                        if (self.voices[i].GetTimeOnCurrentPattern() >= 45 and self.voices[i].GetTimeOnCurrentPattern() < 90):
                            if(random.randint(0, 9) == 0):
                                self.voices[i].ChangePattern()
                            else:
                                self.voices[i].AddPattern()
                        elif (self.voices[i].GetTimeOnCurrentPattern() < 45):
                            self.voices[i].AddPattern()
                        elif(self.voices[i].GetTimeOnCurrentPattern() >= 90):
                            self.voices[i].ChangePattern()

                        #if(self.voices[i].GetTimeOnCurrentPattern() < 45):
                        #    self.voices[i].AddPattern()
                        #elif(self.voices[i].GetTimeOnCurrentPattern() > 90):
                        #    self.voices[i].ChangePattern() 

        return

    def GetLargestPlace(self):
        largestPlace = 0
        largestPlaceIndex = 0
        for i in range(0, len(self.voices)):
            if self.voices[i].GetPlace() > largestPlace:
                largestPlace = self.voices[i].GetPlace()
                largestPlaceIndex = i
        return largestPlaceIndex

    def CheckIfAllVoicesAreDone(self):
        allVoicesDone = True
        for j in range(0, len(self.voices)):
            if self.voices[j].IsNotOnLastPattern():
                allVoicesDone = False
                j = len(self.voices)
        return allVoicesDone

    #for TESTING ONLY
    def CheckPatterns(self):
        for i in range(0, len(self.voices[0].GetAllPatterns())):
            self.voices[0].AddPattern()
            self.voices[0].AddPattern()
            self.voices[0].AddPattern()
            self.voices[0].ChangePattern()
        return

    def WriteFile(self):
        instrument = 1
        for i in range(0, len(self.voices)):
            pm = pretty_midi.PrettyMIDI()
            pm.instruments.append(self.voices[i].GetMIDIData())
            fileName = ('instrument' + str(instrument) + '.mid')
            pm.write(fileName)
            instrument = instrument + 1
        return

Composition(8, 120) #tempo in quarter bpms