from Swarm import Swarm
from Particle import Particle
from Instance import Instance
from typing import Tuple

class PSO:
  def __init__(self, time: int, population: int, instanceFilename: str) -> None:
    self.__instance = Instance(instanceFilename)
    self.__time = time
    self.__swarm = Swarm(population, self.__instance)

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

  def execute(self) -> Tuple[Particle, int]:
    pass

pso = PSO(10, 3, '../instances/toy.ctt')

print(pso)
