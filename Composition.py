import pretty_midi
from Voice import Voice
from Patterns import Patterns
import os
import random

class Composition:
    def __init__(self, numberOfVoices, tempo):
        self.lengthOfSixteenthNote = self.FindLengthOfSixteenthNote(tempo)
        self.voices = self.MakeVoices(numberOfVoices)

        self.CreateTxtFile() #for manually analyzing data
        #self.CheckPatterns()
        self.CreateComposition()
        self.WriteMIDIFiles()
        return

    def MakeVoices(self, numberOfVoices):
        voices = []
        for i in range(numberOfVoices, 1, -1):
            patterns = Patterns(self.lengthOfSixteenthNote, i)
            allPatterns = patterns.GetAllPatterns()
            voices.append(Voice(allPatterns))

        #for j in range(7, 1, -1):
        #    register = j
        #    for i in range(0, numberOfVoices):
        #        patterns = Patterns(self.lengthOfSixteenthNote, register)
        #        allPatterns = patterns.GetAllPatterns()
        #        voices.append(Voice(allPatterns))

        return voices

    def FindLengthOfSixteenthNote(self, tempo):
        quarterNoteLength = (60 / tempo)
        sixteenthNoteLength = (quarterNoteLength / 4)
        return sixteenthNoteLength

#####################################################################################################

    def CreateComposition(self):
        allVoicesDone = False
        place = 0

        self.Initialize()

        while self.CheckIfAllVoicesAreDone() is False:
            #we only want to add something when it's on a proper eighth note beat to avoid innappropriate polyrhythms
            #self.CatchUpOffBeatVoices()
            
            self.GetCurrentState()

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

    def Initialize(self):
        self.AddMeasure('Going to first pattern')
        for i in range(0, len(self.voices)): # will remove this later when logic for voices entering is created
            self.voices[i].ChangePattern()
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
            for k in range(0, random.randint(0, 2)): #we want to make the catch up as smooth as possible. so vary the lengths of times patterns change to catch up
                self.AddMeasure('smoothening transition for voices catching up...')

        if (numberOfLaggingVoices > 0):
            self.WriteTxtFile('Finished catching up\n')
        return

    def DecideIfVoicesShouldChange(self):
        for i in range(0, len(self.voices)):
                if random.randint(0, 180) < self.voices[i].GetTimeOnCurrentPattern(): #180 - 90 (max length) * 2 / 25% chance at 45 seconds (optimal minimum length)
                    self.voices[i].ChangePattern()
        return

    def ChangeVoicesIfTheyAreGoingOnForTooLong(self):
        voicesGoingOnForTooLong = []

        #for k in range(0, len(self.voices) - 1): #stops adding if it's totally done / make less regular
        #    print(str(len(self.voices)) + '|' + k)
        #    if self.voices[k].IsNotOnLastPattern() is False and self.voices[k].GetTimeOnCurrentPattern() >= 90:
        #        self.voices.remove(self.voices[k])

        for i in range(0, len(self.voices)):
                if(self.voices[i].GetTimeOnCurrentPattern() >= 90):
                    voicesGoingOnForTooLong.append(self.voices[i])

        numberOfVoicesGoingOnForTooLong = len(voicesGoingOnForTooLong)

        for j in range(0, numberOfVoicesGoingOnForTooLong):
            voiceToChange = random.randint(0, len(voicesGoingOnForTooLong) - 1)
            voicesGoingOnForTooLong[voiceToChange].ChangePattern()
            voicesGoingOnForTooLong.remove(voicesGoingOnForTooLong[voiceToChange])
            for k in range(0, random.randint(0, 2)):
                self.AddMeasure('smoothening transition for voices going on for too long...')

        if (numberOfVoicesGoingOnForTooLong > 0):
            self.WriteTxtFile('Finished transitioning\n')
        return

    def DecideHowLongToStayInThisState(self):
        self.AddMeasure('Automatic addition')

        somethingWasAdded = False
        for i in range(1, len(self.voices)):
            if self.voices[i].GetCurrentPattern() != self.voices[i-1].GetCurrentPattern():
                somethingWasAdded = True
                self.AddMeasure('Adding based on interest level...')
        if(somethingWasAdded is False):
            self.WriteTxtFile('Nothing was added based on interest level\n')
        else:
            self.WriteTxtFile('Finished adding based on interest level\n')
        return

    def GetCurrentState(self):
        self.currentState = []
        for i in range(0, len(self.voices)):
            self.currentState.append(self.voices[i].GetCurrentPattern())
        return

    def AddMeasure(self, stringForOutputFile):
        allPlaces = []
        for k in range(0, len(self.voices)):
            allPlaces.append(self.voices[k].GetPlace())
        averagePlace = (sum(allPlaces)/len(allPlaces))

        voicesToProgress = [] #don't want any voice to get too far ahead in terms of time
        for j in range(0, len(self.voices)):
            if (self.voices[j].GetPlace() < averagePlace + 3): #won't be added if too long
                voicesToProgress.append(self.voices[j])

        for i in range(0, len(voicesToProgress)):
            voicesToProgress[i].AddPattern()

        self.GetCurrentState()
        self.WriteTxtFile(str(self.currentState) + ' ')
        self.WriteTxtFile(stringForOutputFile + '\n')
        return

    def CheckIfAllVoicesAreDone(self):
        allVoicesDone = True
        for i in range(0, len(self.voices)):
            if self.voices[i].IsNotOnLastPattern():
                allVoicesDone = False
                i = len(self.voices)
        return allVoicesDone

#####################################################################################################

    #for TESTING ONLY
    def CheckPatterns(self):
        for i in range(0, len(self.voices[0].GetAllPatterns())):
            self.voices[0].AddPattern()
            self.voices[0].ChangePattern()
        return

    def CreateTxtFile(self):
        os.remove('allStates.txt')
        listOfAllStates = open('allStates.txt', 'x')
        listOfAllStates.close()
        return

    def WriteTxtFile(self, string):
        file = open('allStates.txt', 'a')
        file.write(string)
        file.close()
        return

    def WriteMIDIFiles(self):
        instrumentNumberForOutput = 1
        for i in range(0, len(self.voices)):
            pm = pretty_midi.PrettyMIDI()
            pm.instruments.append(self.voices[i].GetMIDIData())
            fileName = ('instrument' + str(instrumentNumberForOutput) + '.mid')
            pm.write(fileName)
            instrumentNumberForOutput = instrumentNumberForOutput + 1
        return

Composition(7, 120) #tempo in quarter bpms