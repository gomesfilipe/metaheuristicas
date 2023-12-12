# Generate a random feasible solution for each instance.

import os
from typing import List
from Test import Test

CURRENT_DIR: str = os.getcwd()
INSTANCES_DIR: str = '../instances'
SOLUTIONS_DIR: str = '../feasible_solutions'

allInstances:  List[str] = os.listdir(f'{CURRENT_DIR}/{INSTANCES_DIR}')
allInstancesFullPath:  List[str] = [f'{INSTANCES_DIR}/{filename}' for filename in allInstances]

for index, instancePath in enumerate(allInstancesFullPath):
  print(f'Generating {instancePath}')
  tester = Test(instancePath)
  tester.generateGraspSolution()
