import unittest
from tests_12_3 import RunnerTest, TournamentTest

def suite():
    test_suite = unittest.TestSuite()
    test_loader = unittest.TestLoader()
    test_suite.addTests(test_loader.loadTestsFromTestCase(RunnerTest))
    test_suite.addTests(test_loader.loadTestsFromTestCase(TournamentTest))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite()) 
#Вывод:
test_challenge (tests_12_3.RunnerTest.test_challenge) ... ok
test_run (tests_12_3.RunnerTest.test_run) ... ok
test_walk (tests_12_3.RunnerTest.test_walk) ... ok
test_first_tournament (tests_12_3.TournamentTest.test_first_tournament) ... skipped 'Тесты в этом кейсе заморожены'
test_second_tournament (tests_12_3.TournamentTest.test_second_tournament) ... skipped 'Тесты в этом кейсе заморожены'
test_third_tournament (tests_12_3.TournamentTest.test_third_tournament) ... skipped 'Тесты в этом кейсе заморожены'

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK (skipped=3)
