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
