from Course import Course
from Room import Room
from Curricula import Curricula
from Constraint import Constraint

class Instance:
  def __init__(self, filename: str) -> None:
    file = open(filename, 'r')

    self.name =               file.readline().split()[1]
    self.numCourses =     int(file.readline().split()[1])
    self.numRooms =       int(file.readline().split()[1])
    self.days =           int(file.readline().split()[1])
    self.periodsPerDay =  int(file.readline().split()[1])
    self.numCurricula =   int(file.readline().split()[1])
    self.numConstraints = int(file.readline().split()[1])

    file.readline()
    file.readline()

    # Reading courses
    self.courses = []

    for i in range(self.numCourses):
      line = file.readline().split()

      name =            line[0]
      teacher =         line[1]
      weekClasses =     line[2]
      minWeeekClasses = line[3]
      students =        line[4]

      course = Course(name, teacher, weekClasses, minWeeekClasses, students)
      self.courses.append(course)

    file.readline()
    file.readline()

    # Reading rooms
    self.rooms = []

    for i in range(self.numRooms):
      line = file.readline().split()

      name =         line[0]
      capacity = int(line[1])

      room = Room(name, capacity)
      self.rooms.append(room)

    file.readline()
    file.readline()

    # Reading curricula
    self.curricula = []

    for i in range(self.numCurricula):
      line = file.readline().split()

      name = line[0]

      line.pop(0) # Remaining only courses
      line.pop(0) # Remaining only courses

      courses = set(line)

      curricula = Curricula(name, courses)
      self.curricula.append(curricula)

    file.readline()
    file.readline()

    # Reading constraints
    self.constraints = []

    for i in range(self.numConstraints):
      line = file.readline().split()

      name = line[0]
      day = line[1]
      period = line[2]

      constraint = Constraint(name, day, period)
      self.constraints.append(constraint)

    file.readline()
    file.readline()
    file.close()

  def __str__(self) -> str:
    instance = 'INSTANCE'

    generalData = '\n'.join([
      f'name: {self.name}',
      f'numCourses: {self.numCourses}',
      f'numRooms: {self.numRooms}',
      f'days: {self.days}',
      f'periodsPerDay: {self.periodsPerDay}',
      f'numCurricula: {self.numCurricula}',
      f'numConstraints: {self.numConstraints}',
    ])

    courses = 'COURSES'

    coursesData = '\n'.join([
      course.__str__() for course in self.courses
    ])

    rooms = 'ROOMS'

    roomsData = '\n'.join([
      room.__str__() for room in self.rooms
    ])

    curricula = 'CURRICULA'

    curriculaData = '\n'.join([
      curricula.__str__() for curricula in self.curricula
    ])

    constraints = 'CONSTRAINTS'

    constraintsData = '\n'.join([
      constraint.__str__() for constraint in self.constraints
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

print(Instance('../instances/toy.ctt'))
