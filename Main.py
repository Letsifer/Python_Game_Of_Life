import random


class Field:

    @staticmethod
    def __randomField__():
        width = random.randrange(3, 10)
        height = random.randrange(3, 10)
        field = [[0] * width for i in range(height)]
        for i in range(height):
            for j in range(width):
                if random.randrange(0, 2) == 1:
                    field[i][j] = True
                else:
                    field[i][j] = False
        return Field(field)

    @staticmethod
    def __const_variant__():
        return Field([
            [1, 1, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0]
        ])

    @staticmethod
    def create_start_field(variant):
        if variant == 1:
            return Field.__randomField__()
        elif variant == 2:
            return Field.__const_variant__()

    def __init__(self, _field, _previous_field=None):
        self.field = _field
        self.height = self.field.__len__()
        self.width = self.field[0].__len__()
        self.previous_field = _previous_field

    def step(self):
        new_field = [[0] * self.width for i in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                new_field[i][j] = self.is_alive_cell_remains_alive(i, j) or self.is_dead_cell_become_alive(i, j)
        return Field(new_field, self)

    def is_equal_to_previous(self):
        if self.previous_field is None:
            return False
        for i in range(self.height):
            for j in range(self.width):
                if self.field[i][j] != self.previous_field.field[i][j]:
                    return False
        return True

    def is_alive_cell_remains_alive(self, i, j):
        return self.field[i][j] and self.count_alive_cells_around(i, j) in [2, 3]

    def is_dead_cell_become_alive(self, i, j):
        return not self.field[i][j] and self.count_alive_cells_around(i, j) == 3

    def is_cell_alive(self, i, j):
        real_i = i
        if i < 0:
            real_i = self.height + i
        elif i >= self.height:
            real_i = i - self.height
        real_j = j
        if j < 0:
            real_j = self.width + j
        elif j >= self.width:
            real_j = j - self.width
        return self.field[real_i][real_j]

    def count_alive_cells_around(self, i, j):
        counter = 0
        for a in range(i - 1, i + 2):
            for b in range(j - 1, j + 2):
                if (a != i or b != j) and self.is_cell_alive(a, b):
                    counter += 1
        return counter

    def is_alive(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.field[i][j]:
                    return True
        return False

    def print_field(self):
        print("Height =", self.height, "and width =", self.width)
        for i in range(self.height):
            for j in range(self.width):
                if self.field[i][j]:
                    print("*|", end='')
                else:
                    print(" |", end='')
            print()
        print("--------------------------------------------")

    pass


if __name__ == '__main__':
    field = Field.create_start_field(1)
    field.print_field()
    step_counter = 1
    while field.is_alive():
        print("I am alive at step", step_counter)
        if field.is_equal_to_previous():
            print("No changes, finish")
            break
        field = field.step()
        field.print_field()
        step_counter += 1
    else:
        print("I am dead")

