import pretty_midi
from Voice import Voice
from Patterns import Patterns
from Dynamic import Dynamic
from Unison import Unison
import os
import random

class Composition:
###############################################################################################################################################################
#init methods
    def __init__(self, numberOfVoices, tempo):
        self.lengthOfSixteenthNote = self.FindLengthOfSixteenthNote(tempo)
        self.voices = self.MakeVoices(numberOfVoices)
        self.dynamic = Dynamic()
        self.unison = Unison()

        #self.DynamicTest()

        self.CreateTxtFile() #for manually analyzing data
        self.CreateComposition()
        #self.CreateAccompaniment() #todo
        self.WriteMIDIFiles()
        return

    def DynamicTest(self):
        pm = pretty_midi.PrettyMIDI()
        instrument = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Cello'))
        place = 0
        i = 0
        while(i <= 127):
            noteOne = pretty_midi.Note(velocity=i,
                    pitch=pretty_midi.note_name_to_number('Bb4'),
                    start=place,
                    end=place + .25)
            noteTwo = pretty_midi.Note(velocity=i,
                    pitch=pretty_midi.note_name_to_number('G4'),
                    start=place + .25,
                    end=place + .5)
            instrument.notes.append(noteOne)
            instrument.notes.append(noteTwo)
            place = place + .5
            i = i + 20
        pm.instruments.append(instrument)
        pm.write('dynamicTest.mid')
        return

    def MakeVoices(self, numberOfVoices):
        voices = []

        #this one is one voice per voice input - for 8 or less instruments
        #for i in range(numberOfVoices, 1, -1):
        #   patterns = Patterns(self.lengthOfSixteenthNote, i)
        #    allPatterns = patterns.GetAllPatterns()
        #    voices.append(Voice(allPatterns))

        for i in range(0, numberOfVoices): #number of unique instruments, with each having distinct ranges (4 voices in 4 octaves per instrument)
            for j in range(5, 2, -1):
                register = j
                patterns = Patterns(self.lengthOfSixteenthNote, register)
                allPatterns = patterns.GetAllPatterns()
                for k in range(0, len(allPatterns)):
                    allPatterns[k].SetID(k)
                voices.append(Voice(allPatterns))
        self.numberOfPatterns = len(allPatterns) + 1

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
            self.WriteTxtFile(str(self.dynamic.GetCurrentDynamic()) + '\n')

            self.CatchUpOffBeatVoices() #we only want to add something when it's on a proper eighth note beat to avoid innappropriate polyrhythms
            
            self.GetCurrentState()

            self.UnisonCheck()

            self.CatchUpLaggingVoices() #ensure that all voices are within 2 patterns of each other

            self.DecideIfVoicesShouldChange() #decide when to change - more likely has time goes on

            self.ChangeVoicesIfTheyAreGoingOnForTooLong() #ensure voices don't go on for too long

            self.DecideHowLongToStayInThisState() #we want to stay in an "interesting" state for a longer amount of time than a "not interesting" state (see below for more info)

            self.GetPlace()

        self.MakeEnding()

        self.AdjustLength()
        return

###############################################################################################################################################################
#Utility methods
    def CatchUpOffBeatVoices(self):
        for i in range(0, len(self.voices)):
                while(self.voices[i].IsNotOnAnEighthNoteBeat(self.lengthOfSixteenthNote)):
                    self.voices[i].AddPattern(self.dynamic.GetCurrentDynamic())
                    self.WriteTxtFile('Fixing off beat voice ' + str(i) + '\n')
        return

    def GetCurrentState(self): #a "state" is an array of the current pattern for each voice
        self.currentState = []
        for i in range(0, len(self.voices)):
            self.currentState.append(self.voices[i].GetCurrentPattern())
        return

    def GetPlace(self): #current length of whole piece
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
        return allVoicesDone

    def AdjustLength(self): #trim to recommend length if too long
        lengthOfPiece = random.randint(43, 47)
        self.GetPlace()
        smallestVoiceSize = len(self.voices[0].GetPatterns())
        while((self.place / 60) > lengthOfPiece):
            for i in range(0, len(self.voices)):
                if(smallestVoiceSize > len(self.voices[i].GetPatterns())):
                    smallestVoiceSize = len(self.voices[i].GetPatterns())
            measureToRemove = random.randint(0, smallestVoiceSize - 1)
            for j in range(0, len(self.voices)):
                self.voices[j].DeletePattern(measureToRemove)
            self.GetPlace()
        return

###############################################################################################################################################################
#edge cases
    def MakeIntro(self):
        for i in range(0, 10):
            self.AddMeasure('Empty measure for intro')
        return

    def MakeEnding(self):
        self.WriteTxtFile('Making ending...\n')
        self.GetAllVoicesToSamePlace()

        someAreStillPlaying = True
        while(someAreStillPlaying is True): #true while not empty
            someAreStillPlaying = False
            self.AddMeasureForEnding('Unison ending measure')
            self.GetPlace()
            
            self.WriteTxtFile(str(self.dynamic.GetCurrentDynamic()) + '\n')

            unfinishedVoices = self.GetUnfinishedVoices()
            if(unfinishedVoices): #if it's not empty
                someAreStillPlaying = True

            if((someAreStillPlaying is True) and (random.randint(0, 2) == 0)): #randomly pick when and which one to get rid of
                self.voices[unfinishedVoices[random.randint(0, len(unfinishedVoices) - 1)]].ChangePatternForEnding()

        self.WriteTxtFile(str(self.place / 60)) #length of whole piece
        return

    def GetAllVoicesToSamePlace(self):
        longestVoiceTime = self.place
        for k in range(0, len(self.voices)):
            while(self.voices[k].GetPlace() < longestVoiceTime):
                self.voices[k].AddPattern(self.dynamic.GetCurrentDynamic())
                #print(self.voices[k].GetPlace())
            #print('DONE' + str(k) + ' ' + str(self.voices[k].GetPlace()))
        self.dynamic.InitializeDynamicForEnding()
        self.WriteTxtFile('All voices are on final pattern\n')
        self.WriteTxtFile(str(self.dynamic.GetCurrentDynamic()) + '\n')
        return

    def GetUnfinishedVoices(self):
        unfinishedVoices = []
        for j in range(0, len(self.voices)):
            if(self.voices[j].GetCurrentPattern() < 54):
                unfinishedVoices.append(j)
        return unfinishedVoices

    def AddMeasureForEnding(self, stringForOutputFile):
        self.dynamic.ChangeDynamicForEnding()
        self.ProgressVoices(self.voices)
        self.UpdateTxtFile(stringForOutputFile)
        return

###############################################################################################################################################################
#methods for deciding if composition will become a unison
    def UnisonCheck(self):
        becomeUnison = self.unison.DecideIfCompositionShouldBecomeUnison(min(self.currentState), max(self.currentState), self.numberOfPatterns)
        if(becomeUnison is True):
            self.BecomeUnison()
        return

    def BecomeUnison(self):
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
#methods for catching up voices or moving voices going on for too long, and transitioning them
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

    def ChangeVoicesIfTheyAreGoingOnForTooLong(self): #too long on one pattern
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
        #self.AddMeasure('Automatic addition') #debating the necessity of this

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
        self.dynamic.DecideDynamic()

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
            voices[i].AddPattern(self.dynamic.GetCurrentDynamic())
        return

    def UpdateTxtFile(self, string):
        self.GetCurrentState()
        self.WriteTxtFile(str(self.currentState) + ' ')
        self.WriteTxtFile(string + '\n')
        return

###############################################################################################################################################################
#accompaniment creation methods
    def CreateAccompaniment(self):
        #todo
        return

###############################################################################################################################################################
#file writing methods
    def CheckPatterns(self): #for TESTING ONLY - to see if the patterns made in Pattern.py are correct
        for i in range(0, len(self.voices[0].GetAllPatterns())):
            self.voices[0].AddPattern(self.dynamic.GetCurrentDynamic())
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

numberOfInstruments = 12 #the number of output files for voices is this number times 3
tempoInQuarterNoteBeatsPerMinute = 120
Composition(numberOfInstruments, tempoInQuarterNoteBeatsPerMinute)