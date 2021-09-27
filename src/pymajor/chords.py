from pymajor.core import Note


class Chord:

    def __init__(self, *args):
        chord_notes = [x if isinstance(x, Note) else Note(x) for x in args]

        # remove repeats
        unique_chords = list(set(chord_notes))

        # create chord tuple preserving input order
        self.chord_notes = tuple(sorted(unique_chords, key=lambda x: chord_notes.index(x)))

    def __contains__(self, note):
        return note in self.chord_notes

    def __repr__(self):
        rep = 'Chord({})'.format(','.join([str(n) for n in self.chord_notes]))
        return rep

    def __eq__(self, other):
        return set(self.chord_notes) == set(other.chord_notes)


class IntervalChord(Chord):

    INTERVALS = None  # list of intervals to add from keynote

    def __init__(self, key, *args):
        '''
          In an IntervalChord, the first argument is the key note, followed by
          a number of intervals to build from the key note.
        '''
        base_intervals = self.INTERVALS or []

        # create key note and corresponding note for each interval
        key_note = key if isinstance(key, Note) else Note(key)
        chord_notes = [key_note] + [key_note + i for i in base_intervals + list(args)]

        super().__init__(*chord_notes)


class MajorTriad(IntervalChord):
    INTERVALS = ['3M', '5j']


class MinorTriad(IntervalChord):
    INTERVALS = ['3m', '5j']


class DimTriad(IntervalChord):
    INTERVALS = ['3m', '5b']


class DimChord(IntervalChord):
    INTERVALS = ['3m', '5b', '6M']  # dim chords have the 7bb (ie 6M)
