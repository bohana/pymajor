import pytest

from pymajor.core import Chord, Note


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
