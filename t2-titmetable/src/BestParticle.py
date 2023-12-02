from Slot import Slot
from typing import List
import random

class BestParticle:
  def __init__(self, slots: List[Slot], value: float) -> None:
    self.__slots = slots
    self.__value = value

  def __str__(self) -> str:
    return '\n'.join([slot.__str__() for slot in self.__slots if slot.is_filled()])
    # return '\n'.join([slot.__str__() for slot in self.__slots]) + f'\nfitness: {self.__value}'

  def get_value(self) -> float:
    return self.__value

  def update_best_particle(self, slots: List[Slot], value: float):
    self.__slots = slots
    self.__value = value

  def get_random_slot(self):
    return random.choice(self.__slots)
