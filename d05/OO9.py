class Engine:
    power = 0

    def __init__(self, power) -> None:
        self.power = power

    def __str__(self) -> str:
        return "power:%d " % self.power


class Wheel:
    count = 0

    def __init__(self, count) -> None:
        self.count = count

    def __str__(self) -> str:
        return "count:%d " % self.count


class Motor(Engine, Wheel):
    name = ''

    def __init__(self, power, count, name) -> None:
        super().__init__(power)
        Wheel.__init__(count)
        self.name = name

    def __str__(self) -> str:
        return super().__str__() + Wheel.__str__() + "%s" % self.name


