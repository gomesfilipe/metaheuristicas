from Slot import Slot
import itertools

class TimeTable:
  def __init__(self, daysPerWeek: int, periodsPerDay: int, availableRooms: int) -> None:
    self.daysPerWeek = daysPerWeek
    self.periodsPerDay = periodsPerDay
    self.availableRooms = availableRooms

    slots = itertools.product(range(daysPerWeek), range(periodsPerDay), range(availableRooms))

    self.slots = [
      Slot(day, period, room) for day, period, room in slots
    ]

  def __str__(self) -> str:
    return '\n'.join([slot.__str__() for slot in self.slots])

print(TimeTable(3, 3, 3))