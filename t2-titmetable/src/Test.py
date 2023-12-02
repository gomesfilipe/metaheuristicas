from PSO import PSO
from Particle import Particle
from Instance import Instance

class Test:
  def __init__(self, instanceFileName: str) -> None:
    self.__filename = instanceFileName
    self.__instance = Instance(self.__filename)

  def generateGraspSolution(self):
    particle = Particle(self.__instance)
    particle.graspInit()

    file = open(f'{self.__filename}.txt', 'w')
    file.write(particle.__str__())
    print(particle.get_value())

  def generateFillSolution(self):
    particle = Particle(self.__instance)
    particle.fill()

    file = open(f'{self.__filename}.txt', 'w')
    file.write(particle.__str__())
    print(particle.get_value())
    # print(len(particle.get_slots()))

instanceFileName = '../validator/comp01.ctt'
# instanceFileName = '../validator/toy.ctt'

tester = Test(instanceFileName)
# Test.generateGraspSolution(instanceFileName)
tester.generateFillSolution()