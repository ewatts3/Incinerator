import pretty_midi

class Note:
    def __init__(self, letter, octave, start, end):
        self.letterName = letter
        self.octaveNumber = octave
        self.startInMeasure = start
        self.endInMeasure = end
        return

    def GetMIDIData(self, place, dynamic):
        print(dynamic)
        note = pretty_midi.Note(velocity=dynamic,
                               pitch=pretty_midi.note_name_to_number(self.letterName + str(self.octaveNumber)),
                               start=place + self.startInMeasure,
                               end=place + self.endInMeasure)
        return note