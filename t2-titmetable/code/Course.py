class Course:
  pass

from typing import List, Set
from Constraint import Constraint
from Curricula import Curricula

class Course:
  def __init__(self, name: str, teacher: str, weekClasses: int, minWeekClasses: int, students: int) -> None:
    self.__name = name
    self.__teacher = teacher
    self.__weekClasses = weekClasses
    self.__minWeekClasses = minWeekClasses
    self.__students = students
    self.__constraints: List[Constraint] = []
    self.__curricula: Set[Curricula] = []

  def __str__(self) -> str:
    return f'name: {self.__name} | teacher: {self.__teacher} | weekClasses: {self.__weekClasses} | minWeekClasses: {self.__minWeekClasses} | students: {self.__students}'

  def get_name(self) -> str:
    return self.__name

  def get_teacher(self) -> str:
    return self.__teacher

  def get_week_classes(self) -> int:
    return self.__weekClasses

  def get_min_week_classes(self) -> int:
    return self.__minWeekClasses

  def get_students(self) -> int:
    return self.__students

  def get_constraints(self) -> List[Constraint]:
    return self.__constraints

  def get_curricula(self) -> Set[Curricula]:
    return self.__curricula

  def updateConstraints(self, constraints: List[Constraint]) -> None:
    self.__constraints = [c for c in constraints if self.__name == c.get_course()]

  def updateCurricula(self, curricula: Set[Curricula]) -> None:
    tmpCurricula = [c for c in curricula if self in c.get_courses()]
    self.__curricula = set(tmpCurricula)

  def belongs_to_same_curricula(self, course: 'Course') -> bool:
    for c in self.__curricula:
      if course in c.get_courses():
        return True

    return False
    # return course in self.__curricula