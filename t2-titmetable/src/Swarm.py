from Particle import Particle
from Instance import Instance
from Slot import Slot
from BestParticle import BestParticle
from typing import Union, List
import numpy as np

class Swarm:
  def __init__(self, population: int, instance: Instance,
    w: int, c1: int, c2: int, a1: int, a2: int, a3: int, a4: int
  ) -> None:
    Particle.w = w
    Particle.c1 = c1
    Particle.c2 = c2

    Particle.a1 = a1
    Particle.a2 = a2
    Particle.a3 = a3
    Particle.a4 = a4

    self.__particles = [Particle(instance) for _ in range(population)]

    # filter only feasible solutions
    self.__particles = [particle for particle in self.__particles if particle.get_is_feasible()]

    # if population is empty
    self.__isEmpty: bool = False if self.__particles else True

    if self.__isEmpty:
      Particle.GBest: BestParticle = BestParticle([], float('inf'))
    else:
      Particle.GBest: BestParticle = BestParticle(self.__particles[0].get_copy_slots(), self.__particles[0].get_value())


  def __str__(self) -> str:
    # return '\n'.join([p.__str__() + '\n' for p in self.__particles])
    return '\n'.join([p.__str__() for p in self.__particles])

  def is_empty(self) -> bool:
    return self.__isEmpty

  def update_swarm(self):
    for particle in self.__particles:
      Particle.update_gbest(particle)
      particle.update_pbest()
      particle.update_position()

  def best_value_current_swarm(self) -> float:
    return np.min([particle.get_value() for particle in self.__particles])
