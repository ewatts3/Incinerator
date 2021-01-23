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

        self.numberOfUnisons = 0
        self.patternOfLastUnison = 0
        self.numberOfPatternsSinceLastUnison = 0

        self.CreateTxtFile() #for manually analyzing data
        #self.CheckPatterns() #TESTING ONLY
        self.CreateComposition()
        #self.CreateAccompaniment() #todo
        self.WriteMIDIFiles()
        return

    def MakeVoices(self, numberOfVoices):
        voices = []
        #for i in range(numberOfVoices, 1, -1):
        #   patterns = Patterns(self.lengthOfSixteenthNote, i)
        #    allPatterns = patterns.GetAllPatterns()
        #    voices.append(Voice(allPatterns))

        for i in range(0, numberOfVoices): #number of unique instruments really
            for j in range(5, 2, -1):
                register = j
                patterns = Patterns(self.lengthOfSixteenthNote, register)
                allPatterns = patterns.GetAllPatterns()
                voices.append(Voice(allPatterns))

        #for j in range(4, 2, -1):
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

            self.UnisonCheck()

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
                    self.WriteTxtFile('Fixing off beat voice ' + str(i) + '\n')
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
            if(someAreStillPlaying is True) and (random.randint(0, 2) == 0): #randomly pick when and which one to get rid of
                self.voices[unfinishedVoices[random.randint(0, len(unfinishedVoices) - 1)]].ChangePatternForEnding()

        self.WriteTxtFile(str(self.place / 60)) #length of whole piece
        return

###############################################################################################################################################################
#methods for deciding if composition will become a unison
    def UnisonCheck(self):
        if(self.numberOfUnisons < 2):
            if(min(self.currentState) > 10 and max(self.currentState) < 50):
                if (self.numberOfUnisons == 1):
                    self.numberOfPatternsSinceLastUnison = max(self.currentState) - self.patternOfLastUnison
                else:
                    self.numberOfPatternsSinceLastUnison = 5 #so next conditional evaluates to true
                if(self.numberOfPatternsSinceLastUnison >= 5):
                    becomeUnison = self.DecideIfCompositionShouldBecomeUnison()
                    if(becomeUnison is True):
                        self.BecomeUnison()
        return

    def DecideIfCompositionShouldBecomeUnison(self):
        patternOne = max(self.currentState)
        patternTwo = patternOne - 1
        patternThree = patternOne - 2
        numberOfPatternOne = 0
        numberOfPatternTwo = 0
        numberOfPatternThree = 0
        for i in range(0, len(self.voices)):
            if(self.voices[i].GetCurrentPattern() == patternOne):
                numberOfPatternOne = numberOfPatternOne + 1
            elif(self.voices[i].GetCurrentPattern() == patternTwo):
                numberOfPatternTwo = numberOfPatternTwo + 1
            else:
                numberOfPatternThree = numberOfPatternThree + 1
        averageOccurenceOfPatterns = numberOfPatternOne + numberOfPatternTwo + numberOfPatternThree / 3

        if(averageOccurenceOfPatterns >= 33 and averageOccurenceOfPatterns <= 36):
            return True
        else:
            return False

    def BecomeUnison(self):
        self.numberOfUnisons = self.numberOfUnisons + 1
        self.numberOfPatternsSinceLastUnison = 0
        self.patternOfLastUnison = max(self.currentState)
        self.WriteTxtFile('Composition will become a unison...\n')

        isAUnison = False
        while(isAUnison is False):
            isAUnison = True
            for j in range(0, len(self.voices)):
                if(self.voices[j].GetCurrentPattern() != max(self.currentState)):
                    isAUnison = False
                    if(random.randint(0, 2) == 0):
                        self.voices[j].ChangePattern()
                        for k in range(0, random.randint(0, 2)):
                            self.AddMeasure('Transitioning towards unison...')
        for l in range(0, random.randint(5, 12)):
            self.AddMeasure('Sitting on unison...')
        self.WriteTxtFile('Unison finished. Moving on...\n')
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
            for j in range(0, random.randint(0, 1)): #we want to make the catch up as smooth as possible. so vary the lengths of times patterns change to catch up
                self.AddMeasure('smoothening transition...')
        return

###############################################################################################################################################################
#methods for deciding if voices should change
    def DecideIfVoicesShouldChange(self):
        self.BasedOnLength()
        self.BasedOnItsNeighborVoices() #may remove...too "calculated"
        return

    def BasedOnLength(self):
        for i in range(0, len(self.voices)):
            if random.randint(0, 180) < self.voices[i].GetTimeOnCurrentPattern(): #180 = (max length=90) * 2, means a 25% chance at 45 seconds (optimal minimum length)
                self.voices[i].ChangePattern()
        return

    def BasedOnItsNeighborVoices(self):
        if self.voices[len(self.voices) - 1].GetCurrentPattern() == self.voices[0].GetCurrentPattern() and self.voices[1].GetCurrentPattern() == self.voices[0].GetCurrentPattern():
            if(random.randint(0, 10) == 0):
                self.voices[0].ChangePattern() #first voice
        for i in range(1, len(self.voices) - 1):
            if self.voices[i - 1].GetCurrentPattern() == self.voices[i].GetCurrentPattern() and self.voices[i + 1].GetCurrentPattern() == self.voices[i].GetCurrentPattern():
                if(random.randint(0, 10) == 0):
                    self.voices[i].ChangePattern()
        if self.voices[len(self.voices) - 2].GetCurrentPattern() == self.voices[len(self.voices) - 1].GetCurrentPattern() and self.voices[0].GetCurrentPattern() == self.voices[len(self.voices) - 1].GetCurrentPattern():
            if(random.randint(0, 10) == 0):
                self.voices[len(self.voices) - 1].ChangePattern() #last voice
        return

###############################################################################################################################################################
#methods for deciding how many times to repeat a pattern
    def DecideHowLongToStayInThisState(self):
        #self.AddMeasure('Automatic addition') #debating the necessity of this#

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

numberOfVoices = 12
tempoInQuarterNoteBeatsPerMinute = 120
Composition(numberOfVoices, tempoInQuarterNoteBeatsPerMinute)