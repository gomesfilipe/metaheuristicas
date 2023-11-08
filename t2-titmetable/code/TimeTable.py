from Instance import Instance
from Slot import Slot
import itertools
from typing import List

class TimeTable:
  def __init__(self, instance: Instance) -> None:
    self.__instance = instance
    self.__allocatedClasses = 0

    slots = itertools.product(
      range(self.__instance.get_days()),
      range(self.__instance.get_periods_per_day()),
      self.__instance.get_rooms()
    )

    self.__slots: List[Slot] = [
      Slot(day, period, room) for day, period, room in slots
    ]

  def __str__(self) -> str:
    return '\n'.join([slot.__str__() for slot in self.__slots])

  def get_instance(self) -> Instance:
    return self.__instance

  def get_slots(self) -> list:
    return self.__slots

  def get_slot_by_attributes(self, day: int, period: int, room: int) -> Slot:
    numRooms = self.get_instance().get_num_rooms()
    periodsPerDay = self.get_instance().get_periods_per_day()
    index = room + numRooms * period + periodsPerDay * numRooms * day

    return self.__slots[index]

# path = '../instances/toy.ctt'
# instance = Instance(path)
# tt = TimeTable(instance)
# print(tt)
