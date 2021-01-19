import pretty_midi
from Voice import Voice
from Patterns import Patterns
import os
import random

class Composition:
###############################################################################################################################################################
#init methods
    def __init__(self, numberOfVoices, tempo):
        self.lengthOfSixteenthNote = self.FindLengthOfSixteenthNote(tempo)
        self.voices = self.MakeVoices(numberOfVoices)

        self.CreateTxtFile() #for manually analyzing data
        #self.CheckPatterns()
        self.CreateComposition()
        #self.CreateAccompaniment()
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

###############################################################################################################################################################

    def CreateComposition(self):
        allVoicesDone = False
        self.place = 0

        self.MakeIntro()

        while self.CheckIfAllVoicesAreDone() is False:   
            self.CatchUpOffBeatVoices() #we only want to add something when it's on a proper eighth note beat to avoid innappropriate polyrhythms
            
            self.GetCurrentState()

            self.CatchUpLaggingVoices() #ensure that all voices are within 2 patterns of each other

            self.DecideIfVoicesShouldChange() #decide when to change - more likely has time goes on

            self.ChangeVoicesIfTheyAreGoingOnForTooLong() #ensure voices don't go on for too long

            self.DecideHowLongToStayInThisState() #we want to stay in an "interesting" state for a longer amount of time than a "not interesting" state (see below for more info)

            self.GetPlace()

        self.MakeEnding()
        return

###############################################################################################################################################################
#Utility methods
    def CatchUpOffBeatVoices(self):
        for i in range(0, len(self.voices)):
                while(self.voices[i].IsNotOnAnEighthNoteBeat(self.lengthOfSixteenthNote)):
                    self.voices[i].AddPattern()   
        return

    def GetCurrentState(self):
        self.currentState = []
        for i in range(0, len(self.voices)):
            self.currentState.append(self.voices[i].GetCurrentPattern())
        return

    def GetPlace(self):
        allPlaces = []
        for i in range(0, len(self.voices)):
            allPlaces.append(self.voices[i].GetPlace())
        self.place = max(allPlaces)
        return

    def CheckIfAllVoicesAreDone(self):
        allVoicesDone = True
        for i in range(0, len(self.voices)):
            if self.voices[i].IsNotOnLastPattern():
                allVoicesDone = False
                i = len(self.voices)
        return allVoicesDone

###############################################################################################################################################################
#edge cases
    def MakeIntro(self):
        for i in range(0, 10):
            self.AddMeasure('Empty measure for intro')
        return

    def MakeEnding(self):
        for i in range(0, 9):
            self.AddMeasure('Automatic unison ending measure')

        someAreStillPlaying = True
        while(someAreStillPlaying is True): #true while not empty
            self.AddMeasure('Unison ending measure')
            self.GetPlace()

            unfinishedVoices = []
            someAreStillPlaying = False
            for j in range(0, len(self.voices)):
                if(self.voices[j].GetCurrentPattern() < 54):
                    unfinishedVoices.append(j)
                    someAreStillPlaying = True
            if(someAreStillPlaying is True) and (random.randint(0, 9) == 0): #randomly pick when and which one to get rid of
                self.voices[unfinishedVoices[random.randint(0, len(unfinishedVoices) - 1)]].ChangePatternForEnding()
        return

###############################################################################################################################################################
#methods for catching up / moving voices going on for too long, and transitioning them
    def CatchUpLaggingVoices(self):
        laggingVoices = self.GetLaggingVoices()
        self.TransitionVoices(laggingVoices)
        return

    def GetLaggingVoices(self):
        mostAhead = max(self.currentState)
        laggingVoices = []
        for i in range(0, len(self.voices)):
            if self.voices[i].GetCurrentPattern() < (mostAhead - 2):
                laggingVoices.append(self.voices[i])
        return laggingVoices

    def ChangeVoicesIfTheyAreGoingOnForTooLong(self):
        voicesGoingOnForTooLong = self.GetVoicesThatAreGoingOnForTooLong()
        self.TransitionVoices(voicesGoingOnForTooLong)
        return

    def GetVoicesThatAreGoingOnForTooLong(self):
        voicesGoingOnForTooLong = []
        for i in range(0, len(self.voices)):
                if(self.voices[i].GetTimeOnCurrentPattern() >= 90):
                    voicesGoingOnForTooLong.append(self.voices[i])
        return voicesGoingOnForTooLong

    def TransitionVoices(self, voicesToTransition):
        numberOfVoicesToTransition = len(voicesToTransition)
        for i in range(0, numberOfVoicesToTransition):
            voiceToTransition = random.randint(0, len(voicesToTransition) - 1)
            voicesToTransition[voiceToTransition].ChangePattern()
            voicesToTransition.remove(voicesToTransition[voiceToTransition])
            for j in range(0, random.randint(0, 2)): #we want to make the catch up as smooth as possible. so vary the lengths of times patterns change to catch up
                self.AddMeasure('smoothening transition...')
        return

###############################################################################################################################################################
#methods for deciding if voices should change
    def DecideIfVoicesShouldChange(self):
        self.BasedOnLength()
        return

    def BasedOnLength(self):
        for i in range(0, len(self.voices)):
            if random.randint(0, 180) < self.voices[i].GetTimeOnCurrentPattern(): #180 - 90 (max length) * 2 / 25% chance at 45 seconds (optimal minimum length)
                self.voices[i].ChangePattern()
        return

###############################################################################################################################################################
#methods for deciding how many times to repeat a pattern
    def DecideHowLongToStayInThisState(self):
        self.AddMeasure('Automatic addition')

        somethingWasAdded = False
        #here I am defining an "interesting" state as one where there is great diversity amoung the patterns being played
        #ie, max(self.currentState), max(self.currentState) - 1, max(self.currentState) - 2, are each approximately a third
        #This function finds that, and then stays both in "intersting" states and "not interesting" states for a time 
        #proporitonal to the number of voices (that is, more voices means a longer time for both)
        for i in range(1, len(self.voices)):
            if self.voices[i].GetCurrentPattern() != self.voices[i-1].GetCurrentPattern():
                somethingWasAdded = True
                self.AddMeasure('Adding based on interest level...')
        if(somethingWasAdded is False):
            self.WriteTxtFile('Nothing was added based on interest level\n')
        else:
            self.WriteTxtFile('Finished adding based on interest level\n')
        return

###############################################################################################################################################################
#methods for adding measures
    def AddMeasure(self, stringForOutputFile):
        voicesToAddMeasuresForBasedOnLength = self.GetVoicesToAddMeasuresForBasedOnTheirLength()

        voicesToProgress = self.GetAllVoicesToProgress(voicesToAddMeasuresForBasedOnLength)

        self.ProgressVoices(voicesToProgress)
        self.UpdateTxtFile(stringForOutputFile)
        return

    def GetVoicesToAddMeasuresForBasedOnTheirLength(self):
        allPlaces = []
        for k in range(0, len(self.voices)):
            allPlaces.append(self.voices[k].GetPlace())
        averagePlace = (sum(allPlaces)/len(allPlaces))

        voicesToProgress = [] #don't want any voice to get too far ahead in terms of time
        for j in range(0, len(self.voices)):
            if (self.voices[j].GetPlace() < averagePlace + 3): #won't be added if too long
                voicesToProgress.append(self.voices[j])
        return voicesToProgress

    def GetAllVoicesToProgress(self, basedOnLength):
        voicesToProgress = []
        for i in range(0, len(basedOnLength)):
            voicesToProgress.append(basedOnLength[i])
        return voicesToProgress

    def ProgressVoices(self, voices):
        for i in range(0, len(voices)):
            voices[i].AddPattern()
        return

    def UpdateTxtFile(self, string):
        self.GetCurrentState()
        self.WriteTxtFile(str(self.currentState) + ' ')
        self.WriteTxtFile(string + '\n')
        return

###############################################################################################################################################################
#accompaniment creation methods
    def CreateAccompaniment(self):
        #finish
        return

###############################################################################################################################################################
#file writing methods
    def CheckPatterns(self): #for TESTING ONLY
        for i in range(0, len(self.voices[0].GetAllPatterns())):
            self.voices[0].AddPattern()
            self.voices[0].ChangePattern()
        return

    def CreateTxtFile(self):
        if os.path.exists('allStates.txt'):
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

###############################################################################################################################################################

Composition(7, 120) #(number of voices, tempo in quarter bpms)