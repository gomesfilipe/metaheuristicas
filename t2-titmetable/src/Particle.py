from TimeTable import TimeTable
from Instance import Instance
from BestParticle import BestParticle
from Slot import Slot
from Course import Course
from typing import Union, List, Dict
import random

class Particle(TimeTable):
  # PSO parameters
  w: int = 1
  c1: int = 1
  c2: int = 1

  # Fitness function parameters
  a1: int = 1
  a2: int = 5
  a3: int = 2
  a4: int = 1

  # Grasp parameter
  alpha: float = 0.1

  # Attempts to generate feasible solutions for each particle
  attempts: int = 10

  GBest: BestParticle = None

  def __init__(self, instance: Instance) -> None:
    super().__init__(instance)

    # try [attempts] times generate a feasible solution.
    # if it don't work, discard the particle.
    attempt = 0
    for _ in range(Particle.attempts):
      if self.graspInit():
        self.__value = self.fitness()
        print('particle:', self.__value)
        break
      attempt += 1
      print('infinity')

    self.__isFeasible: bool = not (attempt == Particle.attempts)

    if not self.__isFeasible:
      self.__value = float('inf')

    self.__PBest: BestParticle = BestParticle(self.get_copy_slots(), self.__value)

  def get_value(self) -> float:
    return self.__value

  def get_pbest(self) -> BestParticle:
    return self.__PBest

  def get_is_feasible(self) -> bool:
    return self.__isFeasible

  def __str__(self) -> str:
    return super().__str__()
    # return super().__str__() + f'\nfitness: {self.fitness()}'
    # return f'fitness: {self.fitness()}'

  def is_feasible(self) -> bool:
    return self.satisfies_h1() and self.satisfies_h2() and self.satisfies_h3() and self.satisfies_h4()

  def fitness(self) -> int:
    if not self.is_feasible():
      self.__value = float('inf')
      return float('inf')

    x1 = Particle.a1 * self.compute_s1()
    x2 = Particle.a2 * self.compute_s2()
    x3 = Particle.a3 * self.compute_s3()
    x4 = Particle.a4 * self.compute_s4()

    # print(x1, x2, x3, x4)

    value = x1 + x2 + x3 + x4
    # print(value)
    # self.__value = value
    return value

  def get_random_slot_from_pbest(self) -> Slot:
    return self.__PBest.get_random_slot()

  def get_random_slot_from_gbest(self) -> Slot:
    return Particle.GBest.get_random_slot()

  def get_random_slot_from_particle(self) -> Slot:
    return random.choice(self.get_slots())

  def swap_courses(self, slotA: Slot, slotB: Slot) -> bool:
    # swap guarantes feasibility
    courseA = slotA.get_allocated_course()
    courseB = slotB.get_allocated_course()

    slotA.remove_allocated_course()
    slotB.remove_allocated_course()

    if courseA is not None:
      if not self.can_alloc_course_in_slot(courseA, slotB):
        slotA.force_update_allocated_course(courseA)
        slotB.force_update_allocated_course(courseB)
        return False

    if courseB is not None:
      if not self.can_alloc_course_in_slot(courseB, slotA):
        slotA.force_update_allocated_course(courseA)
        slotB.force_update_allocated_course(courseB)
        return False

    slotA.force_update_allocated_course(courseB)
    slotB.force_update_allocated_course(courseA)

    courseSlots = self.get_course_slots()

    courseSlots[courseA].remove(slotA)
    courseSlots[courseA].append(slotB)

    courseSlots[courseB].remove(slotB)
    courseSlots[courseB].append(slotA)

    return True

  def rand_mutate(self) -> None:
    # execute [w] swaps, each of them try [attempts] times
    for _ in range(Particle.w):
      for __ in range(Particle.attempts):
        slotA: Slot = self.get_random_slot_from_particle()
        slotB: Slot = self.get_random_slot_from_particle()

        if self.swap_courses(slotA, slotB):
          break

  def rand_change_pbest(self) -> None:
    # execute [c1] swaps, each of them try [attempts] times
    for _ in range(Particle.c1):
      for __ in range(Particle.attempts):
        slotPBest = self.get_random_slot_from_pbest()
        coursePBest = slotPBest.get_allocated_course()

        dayPBest = slotPBest.get_day()
        periodPBest = slotPBest.get_period()
        roomPBest = slotPBest.get_room().get_id()

        courseSlots = self.get_course_slots()

        slotSameCoursePBest = random.choice(courseSlots[coursePBest])
        slotSameDayPeriodRoomPBest = self.get_slot_by_attributes(dayPBest, periodPBest, roomPBest)

        if self.swap_courses(slotSameCoursePBest, slotSameDayPeriodRoomPBest):
          break

  def rand_change_gbest(self) -> None:
    # execute [c2] swaps, each of them try [attempts] times
    for _ in range(Particle.c2):
      for __ in range(Particle.attempts):
        slotGBest = self.get_random_slot_from_gbest()
        courseGBest = slotGBest.get_allocated_course()

        dayGBest = slotGBest.get_day()
        periodGBest = slotGBest.get_period()
        roomGBest = slotGBest.get_room().get_id()

        courseSlots = self.get_course_slots()

        slotSameCourseGBest = random.choice(courseSlots[courseGBest])
        slotSameDayPeriodRoomGBest = self.get_slot_by_attributes(dayGBest, periodGBest, roomGBest)

        if self.swap_courses(slotSameCourseGBest, slotSameDayPeriodRoomGBest):
          break

  def update_position(self):
    self.rand_mutate()
    self.rand_change_pbest()
    self.rand_change_gbest()
    self.__value = self.fitness()

  def update_pbest(self) -> None:
    if self.__value < self.__PBest.get_value():
      self.__PBest.update_best_particle(self.get_copy_slots(), self.__value)

  @staticmethod
  def update_gbest(particle: 'Particle') -> None:
    if particle.__value < Particle.GBest.get_value():
      print(f'BestGlobal! {particle.__value}')
      Particle.GBest.update_best_particle(particle.get_copy_slots(), particle.__value)

  def greedy(self, course: Course, slot: Slot) -> float:
    if not self.can_alloc_course_in_slot(course, slot):
      return float('inf')

    slot.force_update_allocated_course(course)

    x1 = Particle.a1 * self.compute_s1()
    x2 = Particle.a2 * self.compute_s2()
    x3 = Particle.a3 * self.compute_s3()
    x4 = Particle.a4 * self.compute_s4()

    slot.remove_allocated_course()
    return x1 + x2 + x3 + x4

  def graspInit(self) -> bool:
    classesToAlloc: List[Course] = self.get_classes_to_alloc()
    allocatedClasses: List[Course] = self.get_allocated_classes()

    while classesToAlloc: # while there are classes to alloc
      course = self.most_conflitant_class()
      greedyValues: Dict[Slot, float] = {}

      for day in range(self.get_instance().get_days()):
        for period in range(self.get_instance().get_periods_per_day()):
          for room in range(self.get_instance().get_num_rooms()):
            slot = self.get_slot_by_attributes(day, period, room)

            greedy = self.greedy(course, slot)
            greedyValues[slot] = greedy

      values = [value for slot, value in greedyValues.items() if value != float('inf')]

      if not values: # infinity to all slots, unfeasible solution
        self.reset_slots()
        self.reset_classes_to_alloc()
        return False

      minValue = min(values)
      maxValue = max(values)

      lrc: List[Slot] = []

      for slot, value in greedyValues.items():
        if value <= minValue + Particle.alpha * (maxValue - minValue): # grasp condition
          lrc.append(slot)

      # try [attempts] times insert course in slot of lrc
      for _ in range(Particle.attempts):
        slot: Slot = random.choice(lrc)

        if self.can_alloc_course_in_slot(course, slot):
          slot.force_update_allocated_course(course)
          break
        elif _ == Particle.attempts - 1:
          self.reset_slots()
          self.reset_classes_to_alloc()
          return False

        # slot.update_allocated_course(course)

      classesToAlloc.remove(course)
      allocatedClasses.append(course)

    self.update_course_slots()
    return True
