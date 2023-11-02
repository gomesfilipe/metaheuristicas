class Curricula:
  def __init__(self, name: str, courses: set) -> None:
    self.name = name
    self.courses = courses
    self.numCourses = len(courses)

  def __str__(self) -> str:
    return f'name: {self.name} | numCourses: {self.numCourses} | courses: ' + ' '.join([course for course in self.courses])
