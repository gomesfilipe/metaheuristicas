from typing import List
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
    self.__curricula: List[Curricula] = []

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
    return self.__constraints.copy()

  def updateConstraints(self, constraints: List[Constraint]) -> None:
    self.__constraints = [c for c in constraints if self.__name == c.get_course()]

  def updateCurricula(self, curricula: List[Curricula]) -> None:
    self.__curricula = [c for c in curricula if self.__name in c.get_courses()]
