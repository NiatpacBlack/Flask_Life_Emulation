import random
from threading import Lock
import copy


class SingletonMeta(type):
    """
    Предназначение данного класса в возможности создания лишь одного экземпляра класса во всей программе.
    Если объект уже создан, тогда вернется этот объект, ранее созданный в программе.

    Мета класс хранит в себе экземпляры классов, которые его наследуют, и локеры, предназначенные для блокировки
    доступа к этим объектам, если с ним работает в этот момент другой поток.
    """

    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        """
        Вызывается при использовании объекта.
        Если создать новый объект класса, то он будет просто ссылаться на первый объект класса.
        Если при попытке создания объекта класса передать аргументы, то новый объект создаст себя и заменит собой
        предыдущий объект этого класса.
        """

        with cls._lock:
            if cls not in cls._instances or args or kwargs:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class GameOfLife(metaclass=SingletonMeta):
    def __init__(self, width=20, height=20):
        """
        Конструктор позволяет задать размеры вселенной и генерирует первое поколение и помещает мир в поле world.
        """

        self.__width = width
        self.__height = height
        self.world = self.generate_universe()
        self.old_world = self.world
        self.counter = 0

    def generate_universe(self):
        """
        Клетки заполняются произвольно при помощи вложенных генераторов списков,
        выбрасывая 1 или 0. (жив или мертв)
        """
        return [[random.randint(0, 1) for _ in range(self.__width)] for _ in range(self.__height)]

    def form_new_generation(self):
        """
        Генерирует следующее поколение клеток на основе предыдущего. Изначально создается копия пустого мира.

        Далее обходим каждую клетку и если она живая, то определяем количество соседей вокруг нее.
        Если вокруг нее меньше двух или больше трех соседей - клетка умирает. В противном случае она живет.
        """

        universe = self.world
        new_world = [[0 for _ in range(self.__width)] for _ in range(self.__height)]

        for i in range(len(universe)):
            for j in range(len(universe[0])):

                if universe[i][j]:
                    if self.__get_near(universe, [i, j]) not in (2, 3):
                        new_world[i][j] = 0
                        continue
                    new_world[i][j] = 1
                    continue

                """ Если клетка мертва, а вокруг нее три соседа, тогда в ней зарождается жизнь, и заменяем мир новым """
                if self.__get_near(universe, [i, j]) == 3:
                    new_world[i][j] = 1
                    continue
                new_world[i][j] = 0
        if self.counter == 0:
            self.old_world = new_world
            self.world = new_world
        else:
            self.old_world = copy.deepcopy(self.world)
            self.world = new_world

    @staticmethod
    def __get_near(universe, pos, system=None):
        """
        Принимает вселенную, а так-же индексы текущей клетки для определения количества соседей поблизости
        (от количества соседей зависит то, выживет ли клетка)
        в кортеже system определяется каких соседей считаем
        """

        if system is None:
            system = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

        count = 0
        for i in system:
            if universe[(pos[0] + i[0]) % len(universe)][(pos[1] + i[1]) % len(universe[0])]:
                count += 1
        return count
