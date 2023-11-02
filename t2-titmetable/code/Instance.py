from Course import Course
from Room import Room
from Curricula import Curricula
from Constraint import Constraint

class Instance:
  def __init__(self, filename: str) -> None:
    file = open(filename, 'r')

    self.__name =               file.readline().split()[1]
    self.__numCourses =     int(file.readline().split()[1])
    self.__numRooms =       int(file.readline().split()[1])
    self.__days =           int(file.readline().split()[1])
    self.__periodsPerDay =  int(file.readline().split()[1])
    self.__numCurricula =   int(file.readline().split()[1])
    self.__numConstraints = int(file.readline().split()[1])

    file.readline()
    file.readline()

    # Reading courses
    self.__courses = []

    for i in range(self.__numCourses):
      line = file.readline().split()

      name =            line[0]
      teacher =         line[1]
      weekClasses =     line[2]
      minWeeekClasses = line[3]
      students =        line[4]

      course = Course(name, teacher, weekClasses, minWeeekClasses, students)
      self.__courses.append(course)

    file.readline()
    file.readline()

    # Reading rooms
    self.__rooms = []

    for i in range(self.__numRooms):
      line = file.readline().split()

      name =         line[0]
      capacity = int(line[1])

      room = Room(name, capacity)
      self.__rooms.append(room)

    file.readline()
    file.readline()

    # Reading curricula
    self.__curricula = []

    for i in range(self.__numCurricula):
      line = file.readline().split()

      name = line[0]

      line.pop(0) # Remaining only courses
      line.pop(0) # Remaining only courses

      courses = set(line)

      curricula = Curricula(name, courses)
      self.__curricula.append(curricula)

    file.readline()
    file.readline()

    # Reading constraints
    self.__constraints = []

    for i in range(self.__numConstraints):
      line = file.readline().split()

      name = line[0]
      day = line[1]
      period = line[2]

      constraint = Constraint(name, day, period)
      self.__constraints.append(constraint)

    file.readline()
    file.readline()
    file.close()

  def __str__(self) -> str:
    instance = 'INSTANCE'

    generalData = '\n'.join([
      f'name: {self.__name}',
      f'numCourses: {self.__numCourses}',
      f'numRooms: {self.__numRooms}',
      f'days: {self.__days}',
      f'periodsPerDay: {self.__periodsPerDay}',
      f'numCurricula: {self.__numCurricula}',
      f'numConstraints: {self.__numConstraints}',
    ])

    courses = 'COURSES'

    coursesData = '\n'.join([
      course.__str__() for course in self.__courses
    ])

    rooms = 'ROOMS'

    roomsData = '\n'.join([
      room.__str__() for room in self.__rooms
    ])

    curricula = 'CURRICULA'

    curriculaData = '\n'.join([
      curricula.__str__() for curricula in self.__curricula
    ])

    constraints = 'CONSTRAINTS'

    constraintsData = '\n'.join([
      constraint.__str__() for constraint in self.__constraints
    ])

    return '\n\n'.join([
      instance,
      generalData,
      courses,
      coursesData,
      rooms,
      roomsData,
      curricula,
      curriculaData,
      constraints,
      constraintsData,
    ])

  def get_name(self) -> str:
    return self.__name

  def get_num_courses(self) -> int:
    return self.__numCourses

  def get_num_rooms(self) -> int:
    return self.__numRooms

  def get_days(self) -> int:
    return self.__days

  def get_periods_per_day(self) -> int:
    return self.__periodsPerDay

  def get_num_curricula(self) -> int:
    return self.__numCurricula

  def get_num_constraints(self) -> int:
    return self.__numConstraints

  def get_courses(self) -> list:
    return self.__courses.copy()

  def get_rooms(self) -> list:
    return self.__rooms.copy()

  def get_curricula(self) -> list:
    return self.__curricula.copy()

  def get_constraints(self) -> list:
    return self.__constraints.copy()

# print(Instance('../instances/toy.ctt'))
