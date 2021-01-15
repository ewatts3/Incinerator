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

        #self.CheckPatterns()

        self.CreateComposition()
        self.WriteFile()
        return

    def FindLengthOfSixteenthNote(self, tempo):
        quarterNoteLength = (60 / tempo)
        sixteenthNoteLength = (quarterNoteLength / 4)
        return sixteenthNoteLength

    def CreateComposition(self):
        allVoicesDone = False
        place = 0
        vl = len(self.voices) #voices length

        while self.CheckIfAllVoicesAreDone() is False:
            #we only want to add something when it's on a proper eighth note beat to avoid innappropriate polyrhythms
            for w in range(0, vl):
                while(self.voices[w].IsNotOnAnEighthNoteBeat(self.lengthOfSixteenthNote)):
                    self.voices[w].AddPattern()   
                    
            currentState = self.GetCurrentState()

            #ensure that all voices are within 2 patterns of each other
            mostAhead = max(currentState)
            for z in range(0, vl):
                if self.voices[z].GetCurrentPattern() < (mostAhead - 2):
                    self.voices[z].ChangePattern()

            #decide when to change - more likely has time goes on
            for x in range(0, vl):
                if random.randint(0, 180) < self.voices[x].GetTimeOnCurrentPattern(): #180 - 90 (max length) * 2 / 25% chance at 45 seconds (optimal minimum length)
                    self.voices[x].ChangePattern()

            #ensure voices don't go on for too long
            for y in range(0, vl):
                if(self.voices[y].GetTimeOnCurrentPattern() >= 90):
                    self.voices[y].ChangePattern()

            self.GoToNextState()
        return

    def GetCurrentState(self):
        currentState = []
        for j in range(0, len(self.voices)):
            currentState.append(self.voices[j].GetCurrentPattern())
        return currentState

    def GoToNextState(self):
        for i in range(0, len(self.voices)):
            self.voices[i].AddPattern()
        return

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
            self.voices[0].ChangePattern()
        return

    def WriteFile(self):
        instrumentNumberForOutput = 1
        for i in range(0, len(self.voices)):
            pm = pretty_midi.PrettyMIDI()
            pm.instruments.append(self.voices[i].GetMIDIData())
            fileName = ('instrument' + str(instrumentinstrumentNumberForOutput) + '.mid')
            pm.write(fileName)
            instrumentNumberForOutput = instrumentinstrumentNumberForOutput + 1
        return

Composition(7, 120) #tempo in quarter bpms