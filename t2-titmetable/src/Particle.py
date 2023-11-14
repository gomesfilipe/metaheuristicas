from TimeTable import TimeTable
from Instance import Instance
from Slot import Slot
from typing import Union, List

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

  GBest: Union[List[Slot], None] = None
  GBestValue: Union[float, None] = None

  def __init__(self, instance: Instance) -> None:
    super().__init__(instance)
    super().fill()
    self.__PBest = super().get_copy_slots()
    self.__PBestValue: Union[float, None] = self.fitness()

  def __str__(self) -> str:
    return super().__str__() + f'\nfitness: {self.fitness()}'

  def fitness(self) -> int:
    if not self.satisfies_h1() or not self.satisfies_h2() or not self.satisfies_h3() or not self.satisfies_h4():
      return float('inf')

    x1 = Particle.a1 * self.compute_s1()
    x2 = Particle.a2 * self.compute_s2()
    x3 = Particle.a3 * self.compute_s3()
    x4 = Particle.a4 * self.compute_s4()

    return x1 + x2 + x3 + x4

  def rand_mutate(self) -> None:
    pass

  def rand_change_pbest(self) -> None:
    pass

  def rand_change_gbest(self) -> None:
    pass

  def update_position(self):
    self.rand_mutate()
    self.rand_change_pbest()
    self.rand_change_gbest()

  def update_pbest(self, value) -> None:
    if value > self.__PBestValue:
      self.__PBestValue = value
      self.__PBest = super().get_copy_slots()


path = '../instances/toy.ctt'
instance = Instance(path)
# print(instance)
tt = Particle(instance)
# tt.fill()
print(tt)

# print(tt.compute_s1())
# print(tt.compute_s2())
# print(tt.compute_s3())
# print(tt.compute_s4())
# print(tt.satisfies_h1())

# print(tt.fitness())