import pretty_midi
from Voice import Voice
from Patterns import Patterns

import random

class Composition:
    def __init__(self, numberOfVoices, tempo):
        self.lengthOfSixteenthNote = self.FindLengthOfSixteenthNote(tempo)
        self.voices = self.MakeVoices(numberOfVoices)

        #self.CheckPatterns()

        self.CreateComposition()
        self.WriteFile()
        return

    def MakeVoices(self, numberOfVoices):
        voices = []
        for j in range(7, 1, -1):
            register = j
            for i in range(0, numberOfVoices):
                patterns = Patterns(self.lengthOfSixteenthNote, register)
                allPatterns = patterns.GetAllPatterns()
                voices.append(Voice(allPatterns))
        return voices

    def FindLengthOfSixteenthNote(self, tempo):
        quarterNoteLength = (60 / tempo)
        sixteenthNoteLength = (quarterNoteLength / 4)
        return sixteenthNoteLength

    def CreateComposition(self):
        allVoicesDone = False
        place = 0

        while self.CheckIfAllVoicesAreDone() is False:
            #we only want to add something when it's on a proper eighth note beat to avoid innappropriate polyrhythms
            self.CatchUpOffBeatVoices()
            
            self.currentState = self.GetCurrentState()

            #ensure that all voices are within 2 patterns of each other
            self.CatchUpLaggingVoices()

            #decide when to change - more likely has time goes on
            self.DecideIfVoicesShouldChange()

            #ensure voices don't go on for too long
            self.ChangeVoicesIfTheyAreGoingOnForTooLong()

            #we want to stay in an "interesting" state for a longer amount of time than a "not interesting" state
            #here I am defining an "interesting" state as one where there is great diversity amoung the patterns being played
            #ie, max(self.currentState), max(self.currentState) - 1, max(self.currentState) - 2, are each approximately a third
            #This function finds that, and then stays both in "intersting" states and "not interesting" states for a time 
            #proporitonal to the number of voices (that is, more voices means a longer time for both)
            self.DecideHowLongToStayInThisState()
        return

    def CatchUpOffBeatVoices(self):
        for i in range(0, len(self.voices)):
                while(self.voices[i].IsNotOnAnEighthNoteBeat(self.lengthOfSixteenthNote)):
                    self.voices[i].AddPattern()   
        return

    def CatchUpLaggingVoices(self):
        mostAhead = max(self.currentState)
        laggingVoices = []

        for i in range(0, len(self.voices)):
            if self.voices[i].GetCurrentPattern() < (mostAhead - 2):
                laggingVoices.append(self.voices[i])

        numberOfLaggingVoices = len(laggingVoices)

        for j in range(0, numberOfLaggingVoices):
            voiceToCatchUp = random.randint(0, len(laggingVoices) - 1)
            laggingVoices[voiceToCatchUp].ChangePattern()
            laggingVoices.remove(laggingVoices[voiceToCatchUp])
            for k in range(0, random.randint(1, 5)): #we want to make the catch up as smooth as possible. so vary the lengths of times patterns change to catch up
                self.AddMeasure()
        return

    def DecideIfVoicesShouldChange(self):
        for i in range(0, len(self.voices)):
                if random.randint(0, 180) < self.voices[i].GetTimeOnCurrentPattern(): #180 - 90 (max length) * 2 / 25% chance at 45 seconds (optimal minimum length)
                    self.voices[i].ChangePattern()
        return

    def ChangeVoicesIfTheyAreGoingOnForTooLong(self):
        voicesGoingOnForTooLong = []
        for i in range(0, len(self.voices)):
                if(self.voices[i].GetTimeOnCurrentPattern() >= 90):
                    voicesGoingOnForTooLong.append(self.voices[i])

        numberOfVoicesGoingOnForTooLong = len(voicesGoingOnForTooLong)

        for j in range(0, numberOfVoicesGoingOnForTooLong):
            voiceToChange = random.randint(0, len(voicesGoingOnForTooLong) - 1)
            voicesGoingOnForTooLong[voiceToChange].ChangePattern()
            voicesGoingOnForTooLong.remove(voicesGoingOnForTooLong[voiceToChange])
            for k in range(0, random.randint(1, 5)):
                self.AddMeasure()
        return

    def DecideHowLongToStayInThisState(self):
        self.AddMeasure()

        middlePattern = max(self.currentState) - 1 #arbitiary for middle pattern, could be any voice
        numberOfVoicesOnMiddlePattern = 0
        for i in range(0, len(self.voices)):
            if(self.voices[i].GetCurrentPattern == middlePattern):
                numberOfVoicesOnMiddlePattern = numberOfVoicesOnMiddlePattern + 1

        #the closer it is to the number of voices in a state being a third (meaning they're all almost a third / the first value in the for loop),
        #the longer we stay in that state.
        oneThirdOfAllVoices = int(len(self.voices) / 3)
        for j in range (oneThirdOfAllVoices - numberOfVoicesOnMiddlePattern, oneThirdOfAllVoices):
            self.AddMeasure()
        return

    def GetCurrentState(self):
        currentState = []
        for i in range(0, len(self.voices)):
            currentState.append(self.voices[i].GetCurrentPattern())
        return currentState

    def AddMeasure(self):
        for i in range(0, len(self.voices)):
            self.voices[i].AddPattern()
        return

    def CheckIfAllVoicesAreDone(self):
        allVoicesDone = True
        for i in range(0, len(self.voices)):
            if self.voices[i].IsNotOnLastPattern():
                allVoicesDone = False
                i = len(self.voices)
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
            fileName = ('instrument' + str(instrumentNumberForOutput) + '.mid')
            pm.write(fileName)
            instrumentNumberForOutput = instrumentNumberForOutput + 1
        return

Composition(1, 120) #tempo in quarter bpms