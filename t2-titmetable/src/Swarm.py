from Particle import Particle
from Instance import Instance
from Slot import Slot
from BestParticle import BestParticle
from typing import Union, List

class Swarm:
  def __init__(self, population: int, instance: Instance, w: int = 1, c1: int = 1, c2: int = 1, a1: int = 1, a2: int = 5, a3: int = 2, a4: int = 1) -> None:
    Particle.w = w
    Particle.c1 = c1
    Particle.c2 = c2

    Particle.a1 = a1
    Particle.a2 = a2
    Particle.a3 = a3
    Particle.a4 = a4

    self.__particles = [Particle(instance) for _ in range(population)]

    Particle.GBest: BestParticle = BestParticle(self.__particles[0].get_copy_slots(), self.__particles[0].get_value())

  def __str__(self) -> str:
    # return '\n'.join([p.__str__() + '\n' for p in self.__particles])
    return '\n'.join([p.__str__() for p in self.__particles])

  def update_swarm(self):
    for particle in self.__particles:
      particle.update_pbest()
      Particle.update_gbest(particle)
      particle.update_position()
