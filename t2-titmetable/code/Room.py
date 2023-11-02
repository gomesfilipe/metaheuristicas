class Room:
  def __init__(self, name: str, capacity: int) -> None:
    self.name = name
    self.capacity = capacity

  def __str__(self) -> str:
    return f'name: {self.name} | capacity: {self.capacity}'
