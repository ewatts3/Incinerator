import pretty_midi
from Voice import Voice
from Patterns import Patterns

class Composition:
    def __init__(self, numberOfVoices, tempo):
        ap = Patterns(self.FindLengthOfSixteenthNote())
        self.allPatterns = ap.GetAllPatterns()

        self.voices = []
        for i in range(0, numberOfVoices):
            self.voices.append(Voice(self.allPatterns))

        self.CreateComposition()
        self.WriteFile()
        return

    def FindLengthOfSixteenthNote(self, tempo):
        quarterNoteLength = (60 / tempo)
        sixteenthNoteLength = (quarterNoteLength / 4)
        return sixteenthNoteLength

    def CreateComposition(self):
        return

    def WriteFile(self):
        pm = pretty_midi.PrettyMIDI()
        for i in range(0, len(self.voices)):
            instrument = self.voices[i].GetMIDIData()
            pm.instruments.append(instrument)
        pm.write('output.mid')
        return

Composition(1, 120) #tempo in quarter bpms