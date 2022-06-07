import random
import unittest
from itertools import combinations
from typing import Any, List

import dice_calculator as calc


class TestDiceCalculator(unittest.TestCase):
    def setUp(self):
        self._calculator = calc.DiceCalculator()
        random.seed(0)

    def test_single_dice_formula(self):
        mean = self._calculator.get_mean_for_die_formula("1d6")
        self.assertAlmostEqual(mean, 3.5)

    def test_multiple_dice_formulas(self):
        formulas = ["1d4", "1d6", "1d8", "1d10", "1d12", "1d20", "1d100"]
        means = [2.5, 3.5, 4.5, 5.5, 6.5, 10.5, 50.5]

        for formula, true_mean in zip(formulas, means):
            mean = self._calculator.get_mean_for_die_formula(formula)
            self.assertAlmostEqual(mean, true_mean)

    def test_get_num_of_faces_of_dice_from_dice_formula(self):
        formulas = [
            "1d4",
            "1d6",
            "1d8",
            "1d10",
            "1d12",
            "1d20",
            "1d100",
            "4d4",
            "6d4",
            "10d6",
            "15d8",
        ]
        faces = [4, 6, 8, 10, 12, 20, 100, 4, 4, 6, 8]
        for formula, true_faces in zip(formulas, faces):
            faces = self._calculator.get_num_faces(formula)
            self.assertEqual(faces, true_faces)

    def test_get_num_of_die_from_dice_formula(self):
        formulas = [
            "1d4",
            "1d6",
            "1d8",
            "1d10",
            "1d12",
            "1d20",
            "1d100",
            "4d4",
            "6d4",
            "10d6",
            "15d8",
        ]
        num_of_die = [1, 1, 1, 1, 1, 1, 1, 4, 6, 10, 15]
        for formula, true_num_of_die in zip(formulas, num_of_die):
            num_of_die = self._calculator.get_num_of_die(formula)
            self.assertEqual(num_of_die, true_num_of_die)

    def test_mean_for_many_die_of_same_type(self):
        formulas = ["2d6", "4d4", "6d4", "10d6", "15d8", "5d10"]
        means = [7, 10, 15, 35, 67.5, 27.5]

        for formula, true_mean in zip(formulas, means):
            mean = self._calculator.get_mean_for_dice_formula(formula)
            self.assertAlmostEqual(mean, true_mean)

    def test_mean_for_sum_of_two_different_die_types(self):
        formulas = ["2d6", "4d4", "6d4", "10d6", "15d8", "5d10"]
        means = [7, 10, 15, 35, 67.5, 27.5]

        for p1, p2 in combinations(zip(formulas, means), 2):
            formula1 = f"{p1[0]}+{p2[0]}"
            formula2 = f"{p1[0]} +{p2[0]}"
            formula3 = f"{p1[0]}+ {p2[0]}"
            formula4 = f"{p1[0]} + {p2[0]}"
            formula5 = f"{p1[0]}    + {p2[0]}"
            formula6 = f"{p1[0]}    +      {p2[0]}"
            formula7 = f"    {p1[0]} +      {p2[0]}"
            formula8 = f"    {p1[0]} +  {p2[0]}   "
            sum_formulas = [
                formula1,
                formula2,
                formula3,
                formula4,
                formula5,
                formula6,
                formula7,
                formula8,
            ]

            true_mean = p1[1] + p2[1]

            for sum_formula in sum_formulas:
                mean = self._calculator.get_mean_for_dice_formula(sum_formula)
                self.assertAlmostEqual(mean, true_mean)

    def _generate_dice_with_spaces_around(self, dice_str: str) -> str:
        spaces_before = " " * random.randint(0, 5)
        spaces_after = " " * random.randint(0, 5)
        return f"{spaces_before}{dice_str}{spaces_after}"

    def _get_all_combinations(
        self, list1: List[Any], list2: List[Any], num_max_pairs: int
    ):
        all_combinations = list()
        for i in range(1, num_max_pairs + 1):
            combs = combinations(zip(list1, list2), i)
            for comb in combs:
                all_combinations.append(comb)
        return all_combinations

    def test_mean_for_sum_of_many_different_die_types(self):
        formulas = ["2d6", "4d4", "6d4", "10d6", "15d8", "5d10"]
        means = [7, 10, 15, 35, 67.5, 27.5]
        NUM_MAX_PAIRS = 5

        all_combinations = self._get_all_combinations(
            formulas, means, NUM_MAX_PAIRS
        )

        for pairs in all_combinations:
            sum_formula = ""
            for pair in pairs:
                dice_str = self._generate_dice_with_spaces_around(pair[0])
                sum_formula += dice_str + "+"
            sum_formula = sum_formula[:-1]  # remove last '+'

            true_mean = sum(pair[1] for pair in pairs)
            mean = self._calculator.get_mean_for_dice_formula(sum_formula)
            self.assertAlmostEqual(mean, true_mean)

    def test_mean_with_scalar_addiction(self):
        formulas = [
            "2d6",
            "4d4",
            "6d4",
            "10d6",
            "15d8",
            "5d10",
            "5",
            "7",
            "3.6",
        ]
        means = [7, 10, 15, 35, 67.5, 27.5, 5, 7, 3.6]
        NUM_MAX_PAIRS = 7

        all_combinations = self._get_all_combinations(
            formulas, means, NUM_MAX_PAIRS
        )

        for pairs in all_combinations:
            sum_formula = ""
            for pair in pairs:
                dice_str = self._generate_dice_with_spaces_around(pair[0])
                sum_formula += dice_str + "+"
            sum_formula = sum_formula[:-1]  # remove last '+'

            true_mean = sum(pair[1] for pair in pairs)
            mean = self._calculator.get_mean_for_dice_formula(sum_formula)
            self.assertAlmostEqual(mean, true_mean)


if __name__ == "__main__":
    unittest.main()
