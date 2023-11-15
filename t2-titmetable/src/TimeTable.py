from Instance import Instance
from Slot import Slot
from Course import Course
from Curricula import Curricula
import itertools
from typing import List, Set, Dict, Union
from collections import Counter
import random

class TimeTable:
  fillAttempts: int = 10
  insertRandomlyAttempts: int = 10

  def __init__(self, instance: Instance) -> None:
    self.__instance = instance

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

    self.__courseSlots: Dict[Course, List[Slot]] = {}

  def __str__(self) -> str:
    return '\n'.join([slot.__str__() for slot in self.__slots])

  def get_instance(self) -> Instance:
    return self.__instance

  def get_slots(self) -> List[Slot]:
    return self.__slots

  def get_copy_slots(self) -> List[Slot]:
    return [slot.copy() for slot in self.__slots]

  def get_slot_by_attributes(self, day: int, period: int, room: int) -> Slot:
    numRooms = self.__instance.get_num_rooms()
    periodsPerDay = self.__instance.get_periods_per_day()
    index = room + numRooms * period + periodsPerDay * numRooms * day

    return self.__slots[index]

  def get_course_slots(self) -> Dict[Course, List[Slot]]:
    return self.__courseSlots

  def fill(self) -> None:
    if self.__numSlots < self.__instance.get_num_classes_to_alloc():
      print(f'There is no feasible solution for [{self.__instance.get_name()}] instance')
      exit()

    # Alloc without conflicts day, period and teacher
    for day in range(self.__instance.get_days()):
      if not self.__classesToAlloc: # Empty
        break

      for period in range(self.__instance.get_periods_per_day()):
        if not self.__classesToAlloc: # Empty
          break

        self.__noConflicts: List[Course] = [course for course in self.__classesToAlloc if course.can_alloc_in_day_period(day, period)]

        for room in range(self.__instance.get_num_rooms()):
          if not self.__noConflicts: # Empty
            break

          slot = self.get_slot_by_attributes(day, period, room)

          course = self.get_random_available_no_conflict_course()
          slot.update_allocated_course(course)
          self.remove_conflicts(course)

          if course in self.__courseSlots:
            self.__courseSlots[course].append(slot)
          else:
            self.__courseSlots[course] = [slot]

          self.__availableSlots.remove(slot)
          self.__unavailableSlots.append(slot)
          self.__classesToAlloc.remove(course)
          self.__allocatedClasses.append(course)

    for course in self.__classesToAlloc:
      slot = self.get_random_available_slot()
      slot.force_update_allocated_course(course)

      if course in self.__courseSlots:
        self.__courseSlots[course].append(slot)
      else:
        self.__courseSlots[course] = [slot]

    noneSlots = [slot for slot in self.__slots if not slot.is_filled()]
    self.__courseSlots[None] = noneSlots

  def __reset_slots(self) -> None:
    for slot in self.__slots:
      slot.reset_slot()

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

  def satisfies_h1(self) -> bool:
    classesToAlloc = self.get_instance().get_num_classes_to_alloc()
    allocatedClasses = len(self.__allocatedClasses)
    return allocatedClasses == classesToAlloc

  def satisfies_h2(self) -> bool:
    return True

  def satisfies_h3(self) -> bool:
    for day in range(self.__instance.get_days()):
      for period in range(self.__instance.get_periods_per_day()):
        for roomI in range(self.__instance.get_num_rooms() - 1):
          for roomJ in range(roomI + 1, self.__instance.get_num_rooms()):
            slotI = self.get_slot_by_attributes(day, period, roomI)
            slotJ = self.get_slot_by_attributes(day, period, roomJ)

            if not slotI.is_filled() or not slotJ.is_filled():
              continue

            courseI = slotI.get_allocated_course()
            courseJ = slotJ.get_allocated_course()

            if courseI.there_is_conflict(courseJ):
              return False
    return True

  def satisfies_h4(self) -> bool:
    for day in range(self.__instance.get_days()):
      for period in range(self.__instance.get_periods_per_day()):
        for room in range(self.__instance.get_num_rooms()):
          slot = self.get_slot_by_attributes(day, period, room)

          if not slot.is_filled():
              continue

          course = slot.get_allocated_course()

          if not course.can_alloc_in_day_period(day, period):
            return False
    return True

  def compute_s1(self) -> int:
    capacityOverflow: int = 0

    for day in range(self.__instance.get_days()):
      for period in range(self.__instance.get_periods_per_day()):
        for room in range(self.__instance.get_num_rooms()):
          slot = self.get_slot_by_attributes(day, period, room)
          capacityOverflow += slot.capacity_overflow()

    return capacityOverflow

  def compute_s2(self) -> int:
    count: Dict[Course, Set[int]] = {}

    for day in range(self.__instance.get_days()):
      for period in range(self.__instance.get_periods_per_day()):
        for room in range(self.__instance.get_num_rooms()):
          slot = self.get_slot_by_attributes(day, period, room)

          if not slot.is_filled():
            continue

          course = slot.get_allocated_course()

          if course in count:
            count[course].add(day)
          else:
            count[course] = set([day])

    minDaysOverflow: int = 0

    for course in self.__instance.get_courses():
      distinctDays = len(count[course])

      if distinctDays < course.get_min_week_classes():
        minDaysOverflow += course.get_min_week_classes() - distinctDays

    return minDaysOverflow

  def compute_s3(self) -> int:
    isolatedCourses: int = 0

    for day in range(self.__instance.get_days()):
      for period in range(self.__instance.get_periods_per_day()):
        for room in range(self.__instance.get_num_rooms()):
          slot = self.get_slot_by_attributes(day, period, room)

          if self.allocated_course_is_isolated(slot):
            isolatedCourses += 1

    return isolatedCourses

  def compute_s4(self) -> int:
    count: Dict[Course, Set[int]] = {}

    for day in range(self.__instance.get_days()):
      for period in range(self.__instance.get_periods_per_day()):
        for room in range(self.__instance.get_num_rooms()):
          slot = self.get_slot_by_attributes(day, period, room)

          if not slot.is_filled():
            continue

          course = slot.get_allocated_course()

          if course in count:
            count[course].add(room)
          else:
            count[course] = set([room])

    roomsOverflow: int = 0

    for course in self.__instance.get_courses():
      distinctRooms = len(count[course])
      roomsOverflow += distinctRooms - 1

    return roomsOverflow

  def allocated_course_is_isolated(self, slot: Slot) -> bool:
    if not slot.is_filled():
      return False

    if self.__instance.get_periods_per_day() == 1:
      return True

    day = slot.get_day()
    period = slot.get_period()
    room = slot.get_room().get_id()

    if period == 0: # First class
      for r in range(self.__instance.get_num_rooms()):
        nextClassCourse = self.get_slot_by_attributes(day, period + 1, r).get_allocated_course()

        if slot.get_allocated_course().belongs_to_same_curricula(nextClassCourse):
          return False
      return True

    elif period == self.__instance.get_periods_per_day() - 1: # Last class
      for r in range(self.__instance.get_num_rooms()):
        previousClassCourse = self.get_slot_by_attributes(day, period - 1, r).get_allocated_course()

        if slot.get_allocated_course().belongs_to_same_curricula(previousClassCourse):
          return False
      return True

    else:
      for r in range(self.__instance.get_num_rooms()):
        nextClassCourse = self.get_slot_by_attributes(day, period + 1, r).get_allocated_course()
        previousClassCourse = self.get_slot_by_attributes(day, period - 1, r).get_allocated_course()

        if slot.get_allocated_course().belongs_to_same_curricula(nextClassCourse) or slot.get_allocated_course().belongs_to_same_curricula(previousClassCourse):
          return False
      return True
