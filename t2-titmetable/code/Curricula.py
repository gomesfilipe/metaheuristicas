class Curricula:
  def __init__(self, name: str, courses: set) -> None:
    self.__name = name
    self.__courses = courses
    self.__numCourses = len(courses)

  def __str__(self) -> str:
    return f'name: {self.__name} | numCourses: {self.__numCourses} | courses: ' + ' '.join([course for course in self.__courses])

  def get_name(self) -> str:
    return self.__name

  def get_courses(self) -> set:
    return self.__courses.copy()

  def get_num_courses(self) -> int:
    return self.__numCourses

