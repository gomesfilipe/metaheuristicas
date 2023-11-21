from TimeTable import TimeTable
from Instance import Instance
from BestParticle import BestParticle
from Slot import Slot
from typing import Union, List
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

  # GBest: Union[List[Slot], None] = None
  # GBestValue: float = float('inf')

  GBest: BestParticle = None

  def __init__(self, instance: Instance) -> None:
    super().__init__(instance)
    super().fill()
    self.__value = self.fitness()

    self.__PBest: BestParticle = BestParticle(super().get_copy_slots(), self.__value)

  def get_value(self) -> float:
    return self.__value

  def get_pbest(self) -> BestParticle:
    return self.__PBest

  def __str__(self) -> str:
    return super().__str__() + f'\nfitness: {self.fitness()}'
    # return f'fitness: {self.fitness()}'

  def fitness(self) -> int:
    if not self.satisfies_h1() or not self.satisfies_h2() or not self.satisfies_h3() or not self.satisfies_h4():
      self.__value = float('inf')
      return float('inf')

    x1 = Particle.a1 * self.compute_s1()
    x2 = Particle.a2 * self.compute_s2()
    x3 = Particle.a3 * self.compute_s3()
    x4 = Particle.a4 * self.compute_s4()

    value = x1 + x2 + x3 + x4
    self.__value = value
    return value

  def get_random_slot_from_pbest(self) -> Slot:
    return self.__PBest.get_random_slot()

  def get_random_slot_from_gbest(self) -> Slot:
    return Particle.GBest.get_random_slot()

  def get_random_slot_from_particle(self) -> Slot:
    return random.choice(self.get_slots())

  def swap_courses(self, slotA: Slot, slotB: Slot) -> None:
    courseA = slotA.get_allocated_course()
    courseB = slotB.get_allocated_course()

    slotA.force_update_allocated_course(courseB)
    slotB.force_update_allocated_course(courseA)

    courseSlots = self.get_course_slots()

    if courseA is not None:
      courseSlots[courseA].remove(slotA)
      courseSlots[courseA].append(slotB)

    if courseB is not None:
      courseSlots[courseB].remove(slotB)
      courseSlots[courseB].append(slotA)

  def rand_mutate(self) -> None:
    for _ in range(Particle.w):
      slotA: Slot = self.get_random_slot_from_particle()
      slotB: Slot = self.get_random_slot_from_particle()
      self.swap_courses(slotA, slotB)

  def rand_change_pbest(self) -> None:
    for _ in range(Particle.c1):
      slotPBest = self.get_random_slot_from_pbest()
      coursePBest = slotPBest.get_allocated_course()

      dayPBest = slotPBest.get_day()
      periodPBest = slotPBest.get_period()
      roomPBest = slotPBest.get_room().get_id()

      courseSlots = self.get_course_slots()

      slotSameCoursePBest = random.choice(courseSlots[coursePBest])
      slotSameDayPeriodRoomPBest = self.get_slot_by_attributes(dayPBest, periodPBest, roomPBest)

      self.swap_courses(slotSameCoursePBest, slotSameDayPeriodRoomPBest)

  def rand_change_gbest(self) -> None:
    for _ in range(Particle.c2):
      slotGBest = self.get_random_slot_from_gbest()
      courseGBest = slotGBest.get_allocated_course()

      dayGBest = slotGBest.get_day()
      periodGBest = slotGBest.get_period()
      roomGBest = slotGBest.get_room().get_id()

      courseSlots = self.get_course_slots()

      slotSameCourseGBest = random.choice(courseSlots[courseGBest])
      slotSameDayPeriodRoomGBest = self.get_slot_by_attributes(dayGBest, periodGBest, roomGBest)

      self.swap_courses(slotSameCourseGBest, slotSameDayPeriodRoomGBest)

  def update_position(self):
    self.rand_mutate()
    self.rand_change_pbest()
    self.rand_change_gbest()

  def update_pbest(self) -> None:
    if self.__value < self.__PBest.get_value():
      self.__PBest.update_best_particle(self.get_copy_slots(), self.__value)

  @staticmethod
  def update_gbest(particle: 'Particle') -> None:
    if particle.__value < Particle.GBest.get_value():
      print(f'BestGlobal! {particle.__value}')
      Particle.GBest.update_best_particle(particle.get_copy_slots(), particle.__value)

# path = '../instances/toy.ctt'
# instance = Instance(path)
# tt = Particle(instance)

# print(tt)

# tt.rand_change_pbest()

# print(tt)
