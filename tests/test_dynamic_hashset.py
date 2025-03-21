import pytest
from ..src.dynamic_hashset import DynamicHashSet


@pytest.fixture
def hashset():
    return DynamicHashSet()


def test_size(hashset):
    hashset.add(1)
    hashset.add(2)

    assert len(hashset) == 2

    hashset.remove(1)
    hashset.remove(2)

    assert len(hashset) == 0


def test_contains(hashset):
    hashset.add(1)
    hashset.add(2)

    assert 1 in hashset
    assert 2 in hashset

    hashset.remove(2)

    assert 2 not in hashset


def test_no_duplicate_elements(hashset):
    hashset.add(1)
    hashset.add(1)

    assert len(hashset) == 1


def test_resize_up(hashset):
    for i in range(8):
        hashset.add(i)

    assert hashset.capacity == 20


def test_resize_up_two_times(hashset):
    for i in range(16):
        hashset.add(i)

    assert hashset.capacity == 40


def test_resize_down(hashset):
    for i in range(8):
        hashset.add(i)

    for i in range(4):
        hashset.remove(i)

    assert hashset.capacity == 10


def test_remove(hashset):
    with pytest.raises(Exception):
        hashset.remove(1)


def test_string_set(hashset):
    assert str(hashset) == "{}"

    hashset.add(1)

    assert str(hashset) == "{1}"

    hashset.add(2)
    hashset.add(3)

    assert str(hashset) == "{1, 2, 3}"


if __name__ == '__main__':
    print("MAIN")