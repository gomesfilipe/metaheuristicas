from Swarm import Swarm
from Particle import Particle
from Instance import Instance
from typing import Tuple

class PSO:
  def __init__(self, time: int, population: int, instanceFilename: str) -> None:
    instance = Instance(instanceFilename)
    self.__time = time
    self.__swarm = Swarm(population, instance)

  def execute(self) -> Tuple[Particle, int]:
    pass