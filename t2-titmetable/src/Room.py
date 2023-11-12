class Room:
  def __init__(self, name: str, capacity: int, id: int) -> None:
    self.__name = name
    self.__capacity = capacity
    self.__id = id

  def __str__(self) -> str:
    return f'name: {self.__name} | capacity: {self.__capacity}'

  def get_name(self) -> str:
    return self.__name

  def get_capacity(self) -> int:
    return self.__capacity

  def get_id(self) -> int:
    return self.__id
