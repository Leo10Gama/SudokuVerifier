"""Module for testing that the verifier module works."""

from parameterized import parameterized
from unittest import TestCase

from verifier import verify_sudoku, _verify_section


class TestVerifier(TestCase):
    @parameterized.expand([
        ("123456789"),
        ("987654321"),
        ("546372819"),
    ])
    def test_chunk_verifier_is_correct(self, test_chunk):
        self.assertTrue(_verify_section(test_chunk))

    @parameterized.expand([
        ("123456788"),
        ("111111111"),
        ("999999999"),
        ("012345678"),
    ])
    def test_chunk_verifier_returns_false(self, test_chunk):
        self.assertFalse(_verify_section(test_chunk))

    @parameterized.expand([
        # Dummy solutions taken from my sudoku calendar; credits to pageaday.com
        ("178942635295386741634175892826714953549238167317569284452697318983421576761853429"),
        ("891762354657439821432518769589274136143956287726183495215397648964821573378645912"),
        ("917483625684925173523671849342896751156237984879514236238159467495768312761342598"),
    ])
    def test_verifier_is_correct(self, test_puzzle):
        self.assertTrue(verify_sudoku(test_puzzle))

    @parameterized.expand([
        # Using edited versions of previous test puzzle
        ("178942035295386741634175892826704953549238167017569284452697318983420576761853429"),
        ("l7894263529538674l634l758928267l4953549238l673l75692844526973l898342l57676l853429"),
        ("17894263529538674163417589282671495354923816731756928445269731898342157676185342"),
    ])
    def test_fail_if_puzzle_is_invalid(self, test_puzzle):
        self.assertFalse(verify_sudoku(test_puzzle))

    @parameterized.expand([
        # Using edited versions of previous test puzzle
        ("178942635295386741634175892826714593549238167317569284452697318983421576761853429"),
        ("718942635295386741634175892826714953549238167317569284452697318983421576761853429"),
        ("178942635295386741634175892826714953549238167317569284452697318983421576761853492"),
        ("978942635295386741634175892826714953549238167317569284452697318983421576761853421"),
        ("178942635295386741634175892826714953549238167317569284352697318983421576761853429"),
    ])
    def test_fail_if_puzzle_is_incorrect(self, test_puzzle):
        self.assertFalse(verify_sudoku(test_puzzle))
