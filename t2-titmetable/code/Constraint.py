class Constraint:
  def __init__(self, course: str, day: int, period: int) -> None:
    self.course = course
    self.day = day
    self.period = period

  def __str__(self) -> str:
    return f'course: {self.course} | day: {self.day} | period: {self.period}'