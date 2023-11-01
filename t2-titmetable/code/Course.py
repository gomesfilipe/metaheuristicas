class Course:
  def __init__(self, name: str, teacher: str, weekClasses: int, minWeekClasses: int, students: int) -> None:
    self.name = name
    self.teacher = teacher
    self.weekClasses = weekClasses
    self.minWeekClasses = minWeekClasses
    self.students = students
