

class Note:

    VALID_NOTES = 'C C# Db D D# Eb E F F# Gb G G# Ab A A# Bb B'.split()

    ENHARMONICS = {'C#': 'Db',
                   'D#': 'Eb',
                   'F#': 'Gb',
                   'G#': 'Ab',
                   'A#': 'Bb'}

    @classmethod
    def from_str(cls, note_str):
        return cls(note_str)

    @classmethod
    def from_idx(cls, note_idx):
        ''' Creates Note object from the note index (0 = C, 1 = C#, ...) '''
        note_str = cls.VALID_NOTES[note_idx]
        return cls.from_str(note_str)

    def __init__(self, note):
        note = note.capitalize()  # db -> Db, etc
        if note not in self.VALID_NOTES:
            raise ValueError('{} not one of: {}'.format(note, self.VALID_NOTES))

        self.note = note
        self.note_idx = self.VALID_NOTES.index(self.note)

    def __eq__(self, other):
        if self.note == other.note:
            return True

        en_keys = [self.ENHARMONICS[x]
                   for x in [self.note, other.note]
                   if x in self.ENHARMONICS]

        # enharmonic means the matched note was on input
        return any([n in [self.note, other.note] for n in en_keys])


class Chord:

    def __init__(self, *args):
        chord_notes = [x if isinstance(x, Note) else Note(x) for x in args]

        # remove repeats
        unique_chords_idx = list(set([n.note_idx for n in chord_notes]))

        self.chord_notes = tuple([Note.from_idx(i) for i in unique_chords_idx])

    def __contains__(self, note):
        return note in self.chord_notes
