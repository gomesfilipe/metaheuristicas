import os
from PSO import PSO

currentDir: str = os.getcwd()
instancesDir = 'instances'

time: int = 20 # Defined by benchmark
population: int = 20

execsForInstance = 1

instanceFilenames = [f'../{instancesDir}/{filename}' for filename in os.listdir(f'{currentDir}/../{instancesDir}')]

instanceFilenames = ['../instances/toy.ctt']

for filename in instanceFilenames:
  for _ in range(execsForInstance):
    pso = PSO(time, population, filename)
    print(pso)
    bestParticle =  pso.execute()
    print(f'Best PSO: {bestParticle.get_value()}')


