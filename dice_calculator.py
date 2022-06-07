import re


class DiceCalculator:
    def get_num_faces(self, die_formula: str) -> int:
        faces = die_formula.split("d")[1]
        return int(faces)

    def get_num_of_die(self, die_formula: str) -> int:
        num_die = die_formula.split("d")[0]
        return int(num_die)

    def get_mean_for_die_formula(self, dice_formula: str) -> float:
        faces = self.get_num_faces(dice_formula)
        num_die = self.get_num_of_die(dice_formula)
        return num_die * (int(faces) + 1) / 2

    def get_mean_for_scalar_formula(self, scalar_formula: str) -> float:
        return float(scalar_formula)

    def get_mean_for_formula(self, formula: str) -> float:
        if "d" in formula:
            return self.get_mean_for_die_formula(formula)
        else:
            return self.get_mean_for_scalar_formula(formula)

    def get_mean_for_dice_formula(self, dice_formula: str) -> float:
        dice_formulas = re.split(r"\s*\+\s*", dice_formula)

        mean = sum(
            self.get_mean_for_formula(formula) for formula in dice_formulas
        )

        return mean


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: dice_calculator.py '<formula>'")
        sys.exit(1)

    calc = DiceCalculator()
    print(calc.get_mean_for_dice_formula(sys.argv[1]))
