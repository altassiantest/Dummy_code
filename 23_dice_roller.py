"""Random dice roller supporting various dice types."""

import random


def roll_dice(sides: int = 6, count: int = 1) -> list[int]:
    if sides < 2:
        raise ValueError("Dice must have at least 2 sides")
    if count < 1:
        raise ValueError("Must roll at least 1 die")
    return [random.randint(1, sides) for _ in range(count)]


def roll_notation(notation: str) -> dict:
    """Parse notation like '2d6' or '1d20'."""
    count_str, sides_str = notation.lower().split("d")
    count = int(count_str) if count_str else 1
    sides = int(sides_str)
    rolls = roll_dice(sides, count)
    return {"notation": notation, "rolls": rolls, "total": sum(rolls)}


if __name__ == "__main__":
    print("Rolling 2d6:", roll_notation("2d6"))
    print("Rolling 1d20:", roll_notation("1d20"))
    print("Rolling 4d10:", roll_notation("4d10"))
