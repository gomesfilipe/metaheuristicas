import os
from PSO import PSO
from Report import Report
from typing import Dict, List
import random

TIME_EXECUTION: int = 216 # Defined by benchmark
EXECS_PER_INSTANCES: int = 5 # Defined in project statement
POPULATION_SIZE: int = 20 # Defined by author

# Instances filenames
CURRENT_DIR: str = os.getcwd()
INSTANCES_DIR: str = 'instances'

toyInstances = ['toy.ctt']
easyInstances = ['comp01.ctt', 'comp11.ctt']
hardInstances = ['comp05.ctt', 'comp12.ctt']

allInstances = list(filter(lambda filename: filename not in toyInstances, os.listdir(f'{CURRENT_DIR}/../{INSTANCES_DIR}')))

allInstancesFullPath = [f'../{INSTANCES_DIR}/{filename}' for filename in allInstances]

# Generate reports
data: Dict[str, List[float]] = {}
optimalValues: Dict[str, float] = {}
optimalValuesList: List[float] = len(allInstances) * [2] # Find the optimal values

# Init dictionaries to generate reports
for index, instance in enumerate(allInstances):
  data[instance] = []
  optimalValues[instance] = optimalValuesList[index]

for instance in allInstances:
  for _ in range(EXECS_PER_INSTANCES):
    # pso = PSO(TIME_EXECUTION, POPULATION_SIZE, instance)
    # # print(pso)
    # print('----------')
    # bestParticle =  pso.execute()
    # print(f'Best PSO: {bestParticle.get_value()}')
    # print('----------')

    # data[instance].append(bestParticle.get_value())
    # data[instance].append(random.randint(1, 100))
    data[instance].append(10) # Just testing the Report class, remove afterward


REPORT_FILENAME = '../reports/report'
df = Report.generate_data_table(REPORT_FILENAME, data, optimalValues)

print(df)
