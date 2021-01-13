import pretty_midi

class Note:
    def __init__(self, letter, octave, start, end):
        self.letterName = letter
        self.octaveNumber = octave
        self.startInMeasure = start
        self.endInMeasure = end
        return

    def TransposeNote(self, numberOfOctavesToTranspose):
        self.octaveNumber = self.octaveNumber + numberOfOctavesToTranspose
        return

    def GetMIDIData(self, place):
        note = pretty_midi.Note(velocity=100,
                                pitch=pretty_midi.note_name_to_number(self.letterName + str(self.octaveNumber)),
                                start=place + self.startInMeasure,
                                end=place + self.endInMeasure)
        return note