import logging
import runner_and_tournament
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            p = runner_and_tournament.Runner("Anton", -5)
            for i in range(10):
                p.walk()
            self.assertEqual(p.distance, 50)
            logging.info("'test_walk' выполнен успешно")
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)



    def test_run(self):
        try:
            q = runner_and_tournament.Runner(2)
            for i in range(10):
                q.run()
            self.assertEqual(q.distance, 100)
            logging.info("'test_run' выполнен успешно")
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)




    def test_challenge(self):
        a1 = runner_and_tournament.Runner("Nikita")
        a2 = runner_and_tournament.Runner("Dima")
        for i in range(10):
            a1.run()
            a2.walk()
        self.assertNotEqual(a1.distance, a2.distance)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        filename="runner_tests.log",
                        filemode='w',
                        encoding='UTF-8',
                        format='%(levelname)s: %(message)s')




