from Instance import Instance
from Slot import Slot
from Course import Course
from Curricula import Curricula
import itertools
from typing import List, Set, Dict, Union
from collections import Counter
import random

class TimeTable:
  def __init__(self, instance: Instance) -> None:
    self.__instance = instance

    # unallocatedClassesAux: List[Course] = []

    # for course in self.__instance.get_courses():
    #   for _ in range(course.get_week_classes()):
    #     unallocatedClassesAux.append(course)

    # self.__classesToAlloc: Dict[Course, int] = Counter(unallocatedClassesAux)
    # self.__allocatedClasses: Dict[Course, int] = Counter([])

    self.__classesToAlloc: List[Course] = []
    self.__allocatedClasses: List[Course] = []

    for course in self.__instance.get_courses():
      for _ in range(course.get_week_classes()):
        self.__classesToAlloc.append(course)

    slots = itertools.product(
      range(self.__instance.get_days()),
      range(self.__instance.get_periods_per_day()),
      self.__instance.get_rooms()
    )

    self.__slots: List[Slot] = [
      Slot(day, period, room) for day, period, room in slots
    ]

    self.__numSlots = len(self.__slots)

    self.__availableSlots: List[Slot] = self.__slots.copy()
    self.__unavailableSlots: List[Slot] = []

  def __str__(self) -> str:
    return '\n'.join([slot.__str__() for slot in self.__slots])

  def get_instance(self) -> Instance:
    return self.__instance

  def get_slots(self) -> list:
    return self.__slots

  def get_slot_by_attributes(self, day: int, period: int, room: int) -> Slot:
    numRooms = self.get_instance().get_num_rooms()
    periodsPerDay = self.get_instance().get_periods_per_day()
    index = room + numRooms * period + periodsPerDay * numRooms * day

    return self.__slots[index]

  def fill(self) -> None:
    if self.__numSlots < self.__instance.get_num_classes_to_alloc():
      print(f'There is no feasible solution for [{self.__instance.get_name()}] instance')
      exit()

    # random.shuffle(self.__instance.get_curricula())

    # TRATAR CONSTRAINT DE COURSE
    for day in range(self.__instance.get_days()):
      if not self.__classesToAlloc:
        break

      for period in range(self.__instance.get_periods_per_day()):
        if not self.__classesToAlloc:
          break

        self.__noConflicts: List[Course] = self.__classesToAlloc.copy()

        for room in range(self.__instance.get_num_rooms()):
          if not self.__noConflicts: # Empty
            break

          slot = self.get_slot_by_attributes(day, period, room)

          course = self.get_random_available_no_conflict_course()
          slot.update_allocated_course(course)
          self.remove_conflicts(course)

          self.__classesToAlloc.remove(course)
          self.__allocatedClasses.append(course)


    # for curricula in self.__instance.get_curricula():
    #   for course in curricula.get_courses():
    #     for _ in range(self.__classesToAlloc[course]):
    #       while(True):
    #         print(len(self.__availableSlots), len(self.__unavailableSlots))
    #         slot = self.get_random_available_slot()

    #         if self.canAllocCourseOnSlot(course, slot):
    #           slot.update_allocated_course(course)
    #           break
    #         else:
    #           self.__availableSlots.append(slot)
    #           self.__unavailableSlots.remove(slot)

    #     self.__classesToAlloc[course] = 0 # All classes have been allocated already

  def canAllocCourseOnSlot(self, course: Course, slot: Slot) -> bool:
    if slot.is_filled():
      return False

    day = slot.get_day()
    period = slot.get_period()

    # Given fixed day, period, check if there is conflict in some room
    for room in range(self.__instance.get_num_rooms()):
      slotAux = self.get_slot_by_attributes(day, period, room)
      courseAux = slotAux.get_allocated_course()

      if slotAux.is_filled() and (courseAux.belongs_to_same_curricula(course) or courseAux.has_same_teacher(course)):
        return False

    return True

  def get_random_available_slot(self) -> Slot:
    slot = random.choice(self.__availableSlots)
    self.__availableSlots.remove(slot)
    self.__unavailableSlots.append(slot)
    return slot

  def get_random_available_course(self) -> Course:
    course = random.choice(self.__classesToAlloc)
    self.__classesToAlloc.remove(course)
    self.__allocatedClasses.append(course)
    return course

  def get_random_available_no_conflict_course(self) -> Course:
    return random.choice(self.__noConflicts)

  def remove_conflicts(self, course: Course) -> None:
    self.__noConflicts = [c for c in self.__noConflicts if c not in course.get_conflicts()]

path = '../instances/toy.ctt'
instance = Instance(path)
tt = TimeTable(instance)
tt.fill()
print(tt)
