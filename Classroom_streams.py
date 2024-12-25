import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power, enemies):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = enemies

    def run(self):
        days = 0

        print(f"{self.name}, на нас напали! Врагов: {self.enemies}")

        while self.enemies > 0:
            self.enemies -= self.power
            self.enemies = max(self.enemies, 0)  # Убедимся, что врагов не меньше нуля
            days += 1
            print(f"{self.name} сражается {days} день(дня)..., осталось {self.enemies} воинов.")
            time.sleep(1)

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


if __name__ == "__main__":

    first_knight = Knight("Sir Lancelot", 10, 100)
    second_knight = Knight("Sir Galahad", 5, 50)

    first_knight.start()
    second_knight.start()

    first_knight.join()
    second_knight.join()

    print("Все битвы закончились!")
