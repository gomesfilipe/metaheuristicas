class Course:
  pass

from typing import List, Set, Dict
from Constraint import Constraint
from Curricula import Curricula
from Slot import Slot

class Course:
  def __init__(self, name: str, teacher: str, weekClasses: int, minWeekClasses: int, students: int) -> None:
    self.__name = name
    self.__teacher = teacher
    self.__weekClasses = weekClasses
    self.__minWeekClasses = minWeekClasses
    self.__students = students
    self.__constraints: List[Constraint] = []
    self.__curricula: List[Curricula] = []
    self.__conflicts: set[Course] = set()

    self.__checkConflicts: Dict[Course, bool] = {} # Conflict curricula and teacher between Courses
    self.__checkConstraints: Dict[str, bool] = {} # Constraint between day, period and Course
    self.__checkCurricula: Dict[Course, bool] = {} # # Conflict curricula between Courses

  def __str__(self) -> str:
    return f'name: {self.__name}'
    # return f'name: {self.__name} | teacher: {self.__teacher} | weekClasses: {self.__weekClasses} | minWeekClasses: {self.__minWeekClasses} | students: {self.__students}'

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

  def get_curricula(self) -> List[Curricula]:
    return self.__curricula

  def get_conflicts(self) -> Set[Course]:
    return self.__conflicts

  def update_constraints(self, constraints: List[Constraint]) -> None:
    self.__constraints = [c for c in constraints if self.__name == c.get_course()]

    for constraint in self.__constraints:
      day = constraint.get_day()
      period = constraint.get_period()

      self.__checkConstraints[f'{day}-{period}'] = True

  def update_curricula(self, curricula: List[Curricula]) -> None:
    tmpCurricula = [c for c in curricula if self in c.get_courses()]
    self.__curricula = set(tmpCurricula)

  def update_conflicts(self):
    for curricula in self.__curricula:
      for course in curricula.get_courses():
        if self.__there_is_conflict_aux(course):
          self.__conflicts.add(course)

    for conflict in self.__conflicts:
      self.__checkConflicts[conflict] = True

      if self.__belongs_to_same_curricula_aux(conflict):
        self.__checkCurricula[conflict] = True

  def __belongs_to_same_curricula_aux(self, course: 'Course') -> bool:
    for c in self.__curricula:
      if course in c.get_courses():
        return True

    return False

  def belongs_to_same_curricula(self, course: 'Course') -> bool:
    if course in self.__checkCurricula:
      return True
    return False

  def has_same_teacher(self, course: 'Course') -> bool:
    return self.__teacher == course.__teacher

  def can_alloc_in_day_period(self, day: int, period: int) -> bool:
    if f'{day}-{period}' in self.__checkConstraints:
      return False
    return True

  def __there_is_conflict_aux(self, course: 'Course') -> bool:
    return self.has_same_teacher(course) or self.__belongs_to_same_curricula_aux(course)

  def there_is_conflict(self, course: 'Course') -> bool:
    if course in self.__checkConflicts:
      return True
    return False
