#!/usr/bin/env python3
import unittest
from collections.abc import Container, Sized, Iterable, Sequence
from sorted_set import SortedSet


class TestConstruction(unittest.TestCase):
    def test_empty(self):
        SortedSet([])

    def test_from_sequence(self):
        SortedSet([7, 8, 3, 1])

    def test_with_duplicates(self):
        SortedSet([8, 8, 8])

    def test_from_iterable(self):
        SortedSet(i for i in range(10, 0))

    def test_default_empty(self):
        SortedSet()


class TestContainerProtocol(unittest.TestCase):
    def setUp(self):
        self.set = SortedSet([6, 7, 3, 9])

    def test_positive_contained(self):
        self.assertTrue(6 in self.set)

    def test_negative_contained(self):
        self.assertFalse(2 in self.set)

    def test_positive_not_contained(self):
        self.assertTrue(5 not in self.set)

    def test_negative_not_contained(self):
        self.assertFalse(7 not in self.set)

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Container))


class TestSizedProtocol(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(len(SortedSet()), 0)

    def test_one(self):
        self.assertEqual(len(SortedSet([1])), 1)

    def test_ten(self):
        self.assertEqual(len(SortedSet(range(10))), 10)

    def test_with_duplicates(self):
        self.assertEqual(len(SortedSet([5] * 3)), 1)

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Sized))


class TestIterableProtocol(unittest.TestCase):
    def setUp(self):
        self.set = SortedSet([7, 2, 1, 1, 9])

    def test_iter(self):
        i = iter(self.set)
        self.assertEqual(next(i), 1)
        self.assertEqual(next(i), 2)
        self.assertEqual(next(i), 7)
        self.assertEqual(next(i), 9)
        self.assertRaises(StopIteration, lambda: next(i))

    def test_for_loop(self):
        expected = iter([1, 2, 7, 9])
        for item in self.set:
            self.assertEqual(item, next(expected))

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Iterable))


class TestSequenceProtocol(unittest.TestCase):
    def setUp(self):
        self.set = SortedSet([1, 4, 9, 13, 15])

    def test_index_zero(self):
        self.assertEqual(self.set[0], 1)

    def test_index_end(self):
        self.assertEqual(self.set[4], 15)

    def test_index_one_beyond_the_end(self):
        with self.assertRaises(IndexError):
            self.set[5]

    def test_index_minus_one(self):
        self.assertEqual(self.set[-1], 15)

    def test_index_minus_len(self):
        self.assertEqual(self.set[-5], 1)

    def test_index_one_before_the_beginning(self):
        with self.assertRaises(IndexError):
            self.set[-6]

    def test_slice_from_start(self):
        expected = SortedSet([1, 4, 9])
        self.assertEqual(self.set[:3], expected)

    def test_slice_to_end(self):
        expected = SortedSet([13, 15])
        self.assertEqual(self.set[3:], expected)

    def test_slice_empty(self):
        self.assertEqual(self.set[10:], SortedSet([]))

    def test_slice_arbitrary(self):
        self.assertEqual(self.set[2:4], SortedSet([9, 13]))

    def test_slice_full(self):
        self.assertEqual(self.set[:], self.set)

    def test_reversed(self):
        set = SortedSet([1, 3, 7, 9])
        rseq = reversed(set)
        self.assertEqual(next(rseq), 9)
        self.assertEqual(next(rseq), 7)
        self.assertEqual(next(rseq), 3)
        self.assertEqual(next(rseq), 1)
        self.assertRaises(StopIteration, lambda: next(rseq))

    def test_index_positive(self):
        set = SortedSet([1, 3, 5])
        self.assertEqual(set.index(3), 1)

    def test_index_negative(self):
        set = SortedSet([1, 3, 5])
        with self.assertRaises(ValueError):
            set.index(2)

    def test_count_zero(self):
        set = SortedSet([1, 2, 3])
        self.assertEqual(set.count(4), 0)

    def test_count_one(self):
        set = SortedSet([1, 2, 3])
        self.assertEqual(set.count(2), 1)

    def test_protocol(self):
        self.assertTrue(issubclass(SortedSet, Sequence))

    def test_concatenate_disjoint(self):
        first = SortedSet([1, 2, 3])
        second = SortedSet([4, 5, 6])
        self.assertEqual(first + second, SortedSet([1, 2, 3, 4, 5, 6]))

    def test_concatenate_disjoint(self):
        first = SortedSet([1, 2, 3])
        second = SortedSet([1, 2, 3])
        self.assertEqual(first + second, SortedSet([1, 2, 3]))

    def test_concatenate_identical(self):
        set = SortedSet([1, 2, 3])
        self.assertEqual(set + set, set)

    def test_concatenate_intersecting(self):
        first = SortedSet([1, 2, 3])
        second = SortedSet([3, 4, 5])
        self.assertEqual(first + second, SortedSet([1, 2, 3, 4, 5]))

    def test_repitition_zero(self):
        set = SortedSet([1, 2, 3])
        self.assertEqual(set * 0, SortedSet())

    def test_repitition_non_zero(self):
        set = SortedSet([1, 2, 3])
        self.assertEqual(10 * set, set)


class TestReprProtocol(unittest.TestCase):
    def test_repr_empty(self):
        set = SortedSet()
        self.assertEqual(repr(set), "SortedSet()")

    def test_repr_some(self):
        set = SortedSet([1, 3, 7])
        self.assertEqual(repr(set), "SortedSet([1, 3, 7])")


class TestEqualityProtocol(unittest.TestCase):
    def test_positive_equal(self):
        self.assertTrue(SortedSet([3, 2, 1]) == SortedSet([1, 2, 3]))

    def test_negative_equal(self):
        self.assertFalse(SortedSet([1, 2, 3]) == SortedSet([4, 5, 6]))

    def test_type_mismatch(self):
        self.assertFalse(SortedSet([1, 2, 3]) == [1, 2, 3])

    def test_identical(self):
        set = SortedSet([1, 2, 3])
        self.assertTrue(set == set)


if __name__ == "__main__":
    unittest.main()
