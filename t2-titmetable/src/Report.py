import numpy as np
import pandas as pd
from typing import List, Dict, TextIO

class Report:
  @staticmethod
  def generate_data_table(filename: str, data: Dict[str, List[float]], optimalValues: Dict[str, float]):
    csvFilename = f'{filename}.csv'
    file: TextIO = open(csvFilename, 'w')

    file.write('instance,optimal,min,mean,gap_min,gap_mean\n')

    for instance, values in sorted(data.items(), key = lambda item : item[0]):
      file.write(Report.__generate_line_data_table(instance, values, optimalValues[instance]))

    file.close()
    return pd.read_csv(csvFilename)

  def __generate_line_data_table(instance: str, values: List[float], optimal: float) -> str:
    return f'{instance},{optimal},{Report.__min(values)},{Report.__mean(values)},{Report.__min_gap(values, optimal)},{Report.__mean_gaps(values, optimal)}\n'

  def generate_graphic() -> None:
    pass

  @staticmethod
  def __mean(values: List[float]) -> float:
    return np.mean(values)

  @staticmethod
  def __min(values: List[float]) -> float:
    return np.min(values)

  @staticmethod
  def __gap(value: float, optimal: float) -> float:
    return (value - optimal) / optimal

  @staticmethod
  def __generate_gaps(values: List[float], optimal: float) -> List[float]:
    return [Report.__gap(value, optimal) for value in values]

  @staticmethod
  def __mean_gaps(values: List[float], optimal: float) -> float:
    return np.mean(Report.__generate_gaps(values, optimal))

  @staticmethod
  def __min_gap(values: List[float], optimal: float) -> float:
    return np.min(Report.__generate_gaps(values, optimal))

