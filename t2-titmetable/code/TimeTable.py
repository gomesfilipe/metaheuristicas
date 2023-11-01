from Instance import Instance
from Slot import Slot
import itertools

class TimeTable:
  def __init__(self, days: int, periodsPerDay: int, rooms: int) -> None:
    self.days = days
    self.periodsPerDay = periodsPerDay
    self.rooms = rooms

    slots = itertools.product(
      range(days), range(periodsPerDay), range(rooms)
    )

    self.slots = [
      Slot(day, period, room) for day, period, room in slots
    ]

  def __str__(self) -> str:
    return '\n'.join([slot.__str__() for slot in self.slots])

print(TimeTable(3, 3, 3))