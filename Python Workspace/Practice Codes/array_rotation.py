"""Rotate lists left or right without modifying the original list."""


class ArrayRotation:
    def __init__(self, values, rotation_count):
        self.values = list(values)
        if not isinstance(rotation_count, int):
            raise TypeError("rotation_count must be an integer")

        self.rotation_count = rotation_count

    def rotate_left(self):
        """Return a new list rotated left by ``rotation_count`` places."""

        if not self.values:

            return []

        count = self.rotation_count % len(self.values)
        return self.values[count:] + self.values[:count]

    def rotate_right(self):
        """Return a new list rotated right by ``rotation_count`` places."""
        if not self.values:
            return []

        count = self.rotation_count % len(self.values)
        return self.values[-count:] + self.values[:-count] if count else self.values.copy()

    def rotations(self):
        """Return both rotations in a display-friendly string."""
        return (
            f"Left rotation:  {self.rotate_left()}\n"
            f"Right rotation: {self.rotate_right()}"
        )


if __name__ == "__main__":
    examples = [
        ([1, 2, 3, 4, 5], 3),       # standard rotation
        ([10, 20, 30, 40], 6),       # count larger than the list length
        (["a", "b", "c", "d"], -1),  # negative count reverses direction
        ([], 2),                     # empty list
        ([42], 100),                 # one-element list
    ]

    for values, count in examples:
        rotation = ArrayRotation(values, count)
        print(f"Input: {values}, rotation count: {count}")
        print(rotation.rotations())
        print()
