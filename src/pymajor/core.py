

class Interval:

    INTERVALS = {
        '1': 0.0,
        '2m': 0.5,
        '2M': 1.0,
        '3m': 1.5,
        '3M': 2.0,
        '4': 2.5,
        '4+': 3.0,
        '5b': 3.0,
        '5': 3.5,
        '5#': 4.0,
        '6m': 4.0,
        '6M': 4.5,
        '7m': 5.0,
        '7': 5.0,   # 7th minor interval also known only as 7th
        '7M': 5.5,
        '8': 6.0
    }

    def __init__(self, i):
        if type(i) is float or type(i) is int:
            reverse_map = {v: k for k, v in self.INTERVALS.items()}

            if float(i) not in reverse_map:
                raise ValueError('Size {} did not map to a known interval.'.format(i))

            self._interval = reverse_map[i]
            return

        if type(i) is not str:
            raise ValueError('Interval must be a size (number) or a known interval name')

        # interval as str convert to canonical format
        i = i.replace('-', 'm').replace('+', 'M').replace('j', '')
        if i not in self.INTERVALS:
            raise ValueError('Interval name {} not known.'.format(i))

        self._interval = i

    @property
    def size(self):
        return self.INTERVALS[self._interval]


class Note:

    VALID_NOTES = 'C C# Db D D# Eb E F F# Gb G G# Ab A A# Bb B'.split()
    SCALE = 'C C# D D# E F F# G G# A A# B'.split()

    ENHARMONICS = {'Db': 'C#',
                   'Eb': 'D#',
                   'Gb': 'F#',
                   'Ab': 'G#',
                   'Bb': 'A#'}

    @classmethod
    def from_str(cls, note_str):
        return cls(note_str)

    @classmethod
    def from_idx(cls, note_idx):
        ''' Creates Note object from the note index (0 = C, 1 = C#, ...) '''
        note_str = cls.SCALE[note_idx]
        return cls.from_str(note_str)

    def __init__(self, note):
        note = note.capitalize()  # db -> Db, etc
        if note not in self.SCALE and note not in self.ENHARMONICS:
            raise ValueError('{} not one of: {}'.format(note, self.VALID_NOTES))

        self.note = note

        if note in self.ENHARMONICS:
            self.canonical_note = self.ENHARMONICS[note]
        else:
            self.canonical_note = note

        self.note_idx = self.SCALE.index(self.canonical_note)

    def __repr__(self):
        rep = 'Note({})'.format(self.note)
        return rep

    def __str__(self):
        return self.note

    def __hash__(self):
        '''Make Notes hashable so they can be used as keys and in sets'''
        return self.SCALE.index(self.canonical_note)

    def __eq__(self, other):
        if self.canonical_note == other.canonical_note:
            return True

    def __init__(self, *args):
        chord_notes = [x if isinstance(x, Note) else Note(x) for x in args]

        # remove repeats
        unique_chords_idx = list(set([n.note_idx for n in chord_notes]))

        self.chord_notes = tuple([Note.from_idx(i) for i in unique_chords_idx])

    def __contains__(self, note):
        return note in self.chord_notes
