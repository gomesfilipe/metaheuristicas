class Course:
  def __init__(self, name: str, teacher: str, weekClasses: int, minWeekClasses: int, students: int) -> None:
    self.name = name
    self.teacher = teacher
    self.weekClasses = weekClasses
    self.minWeekClasses = minWeekClasses
    self.students = students

  def __str__(self) -> str:
    return f'name: {self.name} | teacher: {self.teacher} | weekClasses: {self.weekClasses} | minWeekClasses: {self.minWeekClasses} | students: {self.students}'
