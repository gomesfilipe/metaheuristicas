from Instance import Instance
from Slot import Slot
import itertools

class TimeTable:
  def __init__(self, instance: Instance) -> None:
    self.__instance = instance

    slots = itertools.product(
      range(self.__instance.get_days()),
      range(self.__instance.get_periods_per_day()),
      range(self.__instance.get_num_rooms())
    )

    self.__slots = [
      Slot(day, period, room) for day, period, room in slots
    ]

  def __str__(self) -> str:
    return '\n'.join([slot.__str__() for slot in self.__slots])

  def get_instance(self) -> Instance:
    return self.__instance

  def get_slots(self) -> list:
    return self.__slots

path = '../instances/toy.ctt'
instance = Instance(path)

print(TimeTable(instance))