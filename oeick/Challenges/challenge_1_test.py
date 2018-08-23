import unittest
from oeick.Challenges.challenge_1 import ChallengerOne


class ChallengerOneTest(unittest.TestCase):

    def test_get_column_names_from_dict(self):

        self.assertEqual(
            ChallengerOne.get_column_names_from_dict({}),
            [])

        self.assertEqual(
            ChallengerOne.get_column_names_from_dict({'Computer': 'HAL-9000'}),
            ['Computer'])

        self.assertEqual(
            ChallengerOne.get_column_names_from_dict({'Nr.': 42, 'E-Mail': 'if@mail.ignore'}),
            ['Nr', 'E_Mail'])

        self.assertRaises(TypeError, ChallengerOne.get_column_names_from_dict)

        a_string_instead_of_the_expected_dict = "Es tut mir Leid, Dave, aber das kann ich nicht tun."
        self.assertRaises(
            AttributeError,
            ChallengerOne.get_column_names_from_dict,
            a_string_instead_of_the_expected_dict)


if __name__ == "__main__":
    unittest.main()