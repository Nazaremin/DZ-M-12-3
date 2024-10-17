import unittest
from functools import wraps

class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def __eq__(self, other):
        return self.name == other.name

    def run(self, distance):
        self.distance += distance * self.speed

    def walk(self, distance):
        self.distance += distance * self.speed / 2


class Tournament:
    def __init__(self, distance, runners):
        self.distance = distance
        self.runners = runners

    def start(self):
        times = {i: self.distance / runner.speed for i, runner in enumerate(self.runners)}

        sorted_runners = sorted(times, key=times.get)

        results = {i: self.runners[runner_index].name for i, runner_index in enumerate(sorted_runners)}

        return results


def skip_if_frozen(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.__class__.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        pass

    @skip_if_frozen
    def test_run(self):
        pass

    @skip_if_frozen
    def test_walk(self):
        pass

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        pass

    @skip_if_frozen
    def test_second_tournament(self):
        pass

    @skip_if_frozen
    def test_third_tournament(self):
        pass
