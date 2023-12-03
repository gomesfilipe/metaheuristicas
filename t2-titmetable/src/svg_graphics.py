import pandas as pd
from typing import List
import os
import matplotlib.pyplot as plt

CURRENT_DIR: str = os.getcwd()
ITERATIONS_DIR: str = '../reports/iterations'

iterations:  List[str] = os.listdir(f'{CURRENT_DIR}/{ITERATIONS_DIR}')
iterationsFullPath: List[str] = [f'{ITERATIONS_DIR}/{filename}' for filename in iterations]

for filename in iterationsFullPath:
  df = pd.read_csv(filename)

  x = df['iteration']
  y = df['bestSwarmValue']

  plt.plot(x, y)

  title = filename.split('/')[-1].split('.')[0]

  plt.title(title)
  plt.xlabel('iteration')
  plt.ylabel('best fitness of swarm')

  plt.savefig(f'../reports/graphics/{title}.svg', format='svg')
  plt.clf()
