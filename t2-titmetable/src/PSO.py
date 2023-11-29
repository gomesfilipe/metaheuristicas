from Swarm import Swarm
from Particle import Particle
from Instance import Instance
from BestParticle import BestParticle
from typing import Tuple, TextIO
import time
import numpy as np

class PSO:
  def __init__(
    self, time: int, population: int, instance: Instance, logFile: TextIO = None,
    w: int = 1, c1: int = 1, c2: int = 1, a1: int = 1, a2: int = 5, a3: int = 2, a4: int = 1
  ) -> None:
    self.__instance = instance
    self.__time = time
    self.__swarm = Swarm(population, self.__instance, w, c1, c2, a1, a2, a3, a4)
    self.__logFile = logFile

  def __str__(self) -> str:
    return '\n'.join([
      f'Time (sec): {self.__time}',
      f'Swarm:\n',
      f'{self.__swarm}'
    ])

  def get_instance(self) -> Instance:
    return self.__instance

  def get_time(self) -> int:
    return self.__time

  def get_swarm(self) -> Swarm:
    return self.__swarm

  def execute(self) -> BestParticle:
    iteration: int = 0
    end: float = time.time() + self.__time
    last = -1

    while True:
      now = time.time()

      if now > end:
        break

      remaining = int(end - now)
      if remaining % 30 == 0 and remaining != last:
        print(f'{remaining} secs to end execution')
        last: int = remaining

      self.__swarm.update_swarm()
      iteration += 1

    print(f'total iterations: {iteration + 1}')
    return Particle.GBest
