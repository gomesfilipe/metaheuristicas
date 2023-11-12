from Room import Room
from Course import Course
from typing import Union

class Slot:
  def __init__(self, day: int, period: int, room: Room, allocatedCourse: Union[Course, None] = None) -> None:
    self.__day = day
    self.__period = period
    self.__room = room
    self.__allocatedCourse = allocatedCourse

  def __str__(self) -> str:
    allocatedCourseName = None if self.__allocatedCourse is None else self.__allocatedCourse.get_name()
    return f'({self.__day}, {self.__period}, {self.__room.get_id()}) [{allocatedCourseName}]'

  def get_day(self) -> int:
    return self.__day

  def get_period(self) -> int:
    return self.__period

  def get_room(self) -> Room:
    return self.__room

  def get_allocated_course(self) -> Union[Course, None]:
    return self.__allocatedCourse

  def is_filled(self) -> bool:
    return self.__allocatedCourse is not None

  def update_allocated_course(self, course: Course) -> None:
    self.__allocatedCourse = course

  def remove_allocated_course(self) -> None:
    self.__allocatedCourse = None

  def copy(self):
    return Slot(self.__day, self.__period, self.__room, self.__allocatedCourse)

  def capacity_overflow(self):
    if not self.is_filled() or self.__room.get_capacity() >= self.__allocatedCourse.get_students():
      return 0

    return self.__allocatedCourse.get_students() - self.__room.get_capacity()
