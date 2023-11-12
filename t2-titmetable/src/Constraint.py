class Constraint:
  def __init__(self, course: str, day: int, period: int) -> None:
    self.__course = course
    self.__day = day
    self.__period = period

  def __str__(self) -> str:
    return f'course: {self.__course} | day: {self.__day} | period: {self.__period}'

  def get_course(self) -> str:
    return self.__course

  def get_day(self) -> int:
    return self.__day

  def get_period(self) -> int:
    return self.__period
