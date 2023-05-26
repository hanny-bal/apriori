import unittest

class TestFPMUtils(unittest.TestCase):
    """Tests for the basics functions used in the Apriori implementations.
    """

    def setUp(self) -> None:
        """Setup to be done before calling the test cases.
        """
        pass


    def test_read_file_row(self) -> None:
        """Test the row-wise reading of a file.
        """
        with open('./data/retail.dat') as f:
            for i, line in enumerate(f):
                if i==0:
                    self.assertEqual(line, '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 \n')
                if i==10:
                    self.assertEqual(line, '48 70 71 72 \n')

    def test_generate_candidates(self) -> None:
        """Test the generation of candidates from a list of frequent items.
        """
        result: list[set[str]] = [set(['A','B']), set(['A','C']), set(['D','F']), set(['D','B'])]
        candidates = set()
        for a in result:
            for b in result:
                union = frozenset(a.union(b))
                if len(union) == 3 and a != b:
                    candidates.add(union)
                    
        self.assertEqual(candidates,set([frozenset({'B', 'A', 'D'}), frozenset({'B', 'A', 'C'}), frozenset({'F', 'B', 'D'})]))
        
if __name__ == '__main__':
    unittest.main()