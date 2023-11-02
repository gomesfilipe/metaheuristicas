class Slot:
  def __init__(self, day: int, period: int, room: int) -> None:
    self.__day = day
    self.__period = period
    self.__room = room

  def __str__(self) -> str:
    return f'({self.__day}, {self.__period}, {self.__room})'

  def get_day(self) -> int:
    return self.__day

  def get_period(self) -> int:
    return self.__period

  def get_room(self) -> int:
    return self.__room

  def get_test(self) -> list:
    return self.__test
