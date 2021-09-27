import pytest

from pymajor.core import Note
from pymajor.chords import Chord, MajorTriad, MinorTriad


@pytest.mark.parametrize('notes,must_have', [
    (['c', 'e', 'g'], 'g'),
    (['c', 'e', 'g'], 'e'),
    (['c', 'e', 'g'], 'c')])
def test_chord_create(notes, must_have):
    assert Note(must_have) in Chord(*notes)


@pytest.mark.parametrize('notes', [
    ['c', 'e', 'g'],
    ['c', 'e', 'g', 'g'],
    ['c', 'e', 'g', 'c', 'e', 'g']])
def test_chord_remove_dupes(notes):
    chrd = Chord(*notes)
    assert len(chrd.chord_notes) == 3  # de-duped
    assert all([Note(x) in chrd for x in notes])


@pytest.mark.parametrize('key, chord_notes', [
    ('C', ['C', 'E', 'G']),
    ('A', ['A', 'C#', 'E']),
    ('Bb', ['Bb', 'D', 'F'])
])
def test_chord_major(key, chord_notes):
    assert MajorTriad(key).chord_notes == tuple([Note(x) for x in chord_notes])


@pytest.mark.parametrize('key, chord_notes', [
    ('C', ['C', 'Eb', 'G']),
    ('A', ['A', 'C', 'E']),
    ('Bb', ['Bb', 'Db', 'F'])
])
def test_chord_minor(key, chord_notes):
    assert MinorTriad(key).chord_notes == tuple([Note(x) for x in chord_notes])


@pytest.mark.parametrize('key, chord_notes', [
    ('C', ['C', 'E', 'G', 'Bb']),
    ('A', ['A', 'C#', 'E', 'G']),
    ('Bb', ['Bb', 'D', 'F', 'Ab'])
])
def test_chord_major_7th(key, chord_notes):
    assert MajorTriad(key, '7m').chord_notes == tuple([Note(x) for x in chord_notes])


@pytest.mark.parametrize('key, chord_notes', [
    ('C', ['C', 'E', 'G', 'B']),
    ('A', ['A', 'C#', 'E', 'G#']),
    ('Bb', ['Bb', 'D', 'F', 'A'])
])
def test_chord_major_major7th(key, chord_notes):
    assert MajorTriad(key, '7M').chord_notes == tuple([Note(x) for x in chord_notes])
