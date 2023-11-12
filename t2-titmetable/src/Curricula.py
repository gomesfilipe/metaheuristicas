class Curricula:
  pass

from Course import Course
from typing import Set

class Curricula:
  def __init__(self, name: str, courses: Set[Course]) -> None:
    self.__name = name
    self.__courses = courses
    self.__numCourses = len(courses)

  def __str__(self) -> str:
    return f'name: {self.__name} | numCourses: {self.__numCourses} | courses: ' + ' '.join([course.__str__() for course in self.__courses])

  def get_name(self) -> str:
    return self.__name

  def get_courses(self) -> Set[Course]:
    return self.__courses

  def get_num_courses(self) -> int:
    return self.__numCourses

