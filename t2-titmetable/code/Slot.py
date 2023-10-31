class Slot:
  def __init__(self, day: int, period: int, room: int) -> None:
    self.day = day
    self.period = period
    self.room = room

  def __str__(self) -> str:
    return f'({self.day}, {self.period}, {self.room})'
