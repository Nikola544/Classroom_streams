import time
from threading import Thread, Lock

ENEMIES = 100

enemies_lock = Lock()


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        global ENEMIES
        days = 0

        print(f"{self.name}, на нас напали!")

        while True:
            with enemies_lock:
                if ENEMIES <= 0:
                    break
                ENEMIES -= min(self.power, ENEMIES)

            days += 1
            print(f"{self.name} сражается {days} день(дня)..., осталось {ENEMIES} воинов.")
            time.sleep(1)

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")

if __name__ == "__main__":

    first_knight = Knight("Sir Lancelot", 10)
    second_knight = Knight("Sir Galahad", 10)

    first_knight.start()
    second_knight.start()

    first_knight.join()
    second_knight.join()

    print("Все битвы закончились!")
