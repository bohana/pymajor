import pytest

from pymajor.core import Note


@pytest.mark.parametrize('note', ['a', 'b', 'B', 'Bb', 'C#', 'Eb', 'eb'])
def test_valids(note):
    assert Note(note)


@pytest.mark.parametrize('note', ['az', 'Z', 'Python', 'e#'])
def test_invalids(note):
    with pytest.raises(ValueError):
        Note(note)


@pytest.mark.parametrize('note_a,note_b', [
    ('A', 'A'),
    ('a', 'A'),
    ('C#', 'C#'),
    ('A#', 'Bb'),
    ('Bb', 'A#'),
    ('C#', 'Db'),
    ('Db', 'C#')
])
def test_equal(note_a, note_b):
    assert Note(note_a) == Note(note_b)


@pytest.mark.parametrize('note_a,note_b', [
    ('A', 'Ab'),
    ('C#', 'C'),
    ('F', 'F#'),
    ('Bb', 'B'),
    ('D', 'C'),
    ('C', 'D')
])
def test_unequal(note_a, note_b):
    assert Note(note_a) != Note(note_b)


@pytest.mark.parametrize('note_a, interval, note_res', [
    ('A', 0, 'A'),
    ('Bb', 0, 'Bb'),
    ('C', 0.5, 'C#'),
    ('C', 0.5, 'Db'),
    ('C', 1.0, 'D'),
    ('C', '2M', 'D'),
    ('C', '5j', 'G'),
    ('C', '3M', 'E'),
    ('B', 1.5, 'D'),
    ('Bb', '2m', 'B')
])
def test_add(note_a, interval, note_res):
    assert Note(note_a) + interval == Note(note_res)


def test_notes_set():
    # can do set operations
    all_notes = set([Note(x) for x in 'C D A# F# C D Bb Gb'.split()])
    assert len(all_notes) == 4

    assert Note('C') in all_notes
    assert Note('Bb') in all_notes
    assert Note('A#') in all_notes
