import os
from PSO import PSO
from Report import Report
from typing import Dict, List
from Instance import Instance

TIME_EXECUTION: int = 10 # Defined by benchmark
EXECS_PER_INSTANCES: int = 2 # Defined in project statement
POPULATION_SIZE: int = 2 # Defined by author

C1 = 1
C2 = 1
W = 1

CURRENT_DIR: str = os.getcwd()
INSTANCES_DIR: str = '../instances'
REPORT_DIR: str = '../reports'
REPORT_FILENAME = f'{REPORT_DIR}/report'

# Instances filenames
toyInstances:  List[str] = ['toy.ctt']
easyInstances: List[str] = ['comp01.ctt', 'comp11.ctt']
hardInstances: List[str] = ['comp05.ctt', 'comp12.ctt']
allInstances:  List[str] = list(filter(lambda filename: filename not in toyInstances, os.listdir(f'{CURRENT_DIR}/{INSTANCES_DIR}')))

allInstancesFullPath:  List[str] = [f'{INSTANCES_DIR}/{filename}' for filename in allInstances]
toyInstancesFullPath:  List[str] = [f'{INSTANCES_DIR}/{filename}' for filename in toyInstances]
easyInstancesFullPath: List[str] = [f'{INSTANCES_DIR}/{filename}' for filename in easyInstances]
hardInstancesFullPath: List[str] = [f'{INSTANCES_DIR}/{filename}' for filename in hardInstances]

# Generate reports
data: Dict[str, List[float]] = {} # Values are lists that contain best PSO values
optimalValues: Dict[str, float] = {} # Values are the optimum of given instance

optimalValuesAllInstances: Dict[str, float] = {
  'toy.ctt'   :  10,
  'comp01.ctt':   5,
  'comp02.ctt':  24,
  'comp03.ctt':  64,
  'comp04.ctt':  35,
  'comp05.ctt': 284,
  'comp06.ctt':  27,
  'comp07.ctt':   6,
  'comp08.ctt':  37,
  'comp09.ctt':  96,
  'comp10.ctt':   4,
  'comp11.ctt':   0,
  'comp12.ctt': 294,
  'comp13.ctt':  59,
  'comp14.ctt':  51,
  'comp15.ctt':  62,
  'comp16.ctt':  18,
  'comp17.ctt':  56,
  'comp18.ctt':  61,
  'comp19.ctt':  57,
  'comp20.ctt':   4,
  'comp21.ctt':  74,
}

RUNNING_INSTANCES:           List[str] = easyInstances
RUNNING_INSTANCES_FULL_PATH: List[str] = easyInstancesFullPath

# Init dictionaries to generate reports
for index, instancePath in enumerate(RUNNING_INSTANCES):
  data[instancePath] = []
  optimalValues[instancePath] = optimalValuesAllInstances[instancePath]

# Execute all instances a few times
for index, instancePath in enumerate(RUNNING_INSTANCES_FULL_PATH):
  instanceName = RUNNING_INSTANCES[index]

  reportPath = REPORT_FILENAME
  print('----------')
  print(f'[Instance] {instanceName}')

  reportPath = f'{REPORT_DIR}/{instanceName}'

  instance = Instance(instancePath)

  for _ in range(EXECS_PER_INSTANCES):
    print(f'\n[Execution {_}]\n')

    logFileName = reportPath if _ == 0 else None

    pso = PSO(TIME_EXECUTION, POPULATION_SIZE, instance, w = W, c1 =  C1, c2 = C2, logFileName = logFileName)
    bestParticle =  pso.execute()

    print(f'\n[Best PSO] {bestParticle.get_value()}\n')
    data[instanceName].append(bestParticle.get_value())

  print('----------')

df = Report.generate_data_table(REPORT_FILENAME, data, optimalValues)

print(df)
