from Course import Course
from Room import Room
from Curricula import Curricula
from Constraint import Constraint
from typing import List, Set

class Instance:
  def __init__(self, filename: str) -> None:
    file = open(filename, 'r')

    self.__name           =     file.readline().split()[1]
    self.__numCourses     = int(file.readline().split()[1])
    self.__numRooms       = int(file.readline().split()[1])
    self.__days           = int(file.readline().split()[1])
    self.__periodsPerDay  = int(file.readline().split()[1])
    self.__numCurricula   = int(file.readline().split()[1])
    self.__numConstraints = int(file.readline().split()[1])

    self.__courses:     List[Course]     = []
    self.__rooms:       List[Room]       = []
    self.__curricula:   List[Curricula]  = []
    self.__constraints: List[Constraint] = []

    self.__numClassesToAlloc = 0

    file.readline()
    file.readline()

    # Reading courses
    for _ in range(self.__numCourses):
      line = file.readline().split()

      name            =     line[0]
      teacher         =     line[1]
      weekClasses     = int(line[2])
      minWeeekClasses = int(line[3])
      students        = int(line[4])

      self.__numClassesToAlloc += weekClasses

      course = Course(name, teacher, weekClasses, minWeeekClasses, students)
      self.__courses.append(course)

    file.readline()
    file.readline()

    # Reading rooms
    for i in range(self.__numRooms):
      line = file.readline().split()

      name =         line[0]
      capacity = int(line[1])

      room = Room(name, capacity, i)
      self.__rooms.append(room)

    file.readline()
    file.readline()

    # Reading curricula
    for _ in range(self.__numCurricula):
      line = file.readline().split()

      name = line[0]

      line.pop(0) # Remaining only courses
      line.pop(0) # Remaining only courses

      courses: List[Course] = [self.get_course_by_name(courseName) for courseName in line]
      courses: Set[Course] = set(courses)

      curricula = Curricula(name, courses)
      self.__curricula.append(curricula)

    file.readline()
    file.readline()

    # Reading constraints
    for _ in range(self.__numConstraints):
      line = file.readline().split()

      name   = line[0]
      day    = line[1]
      period = line[2]

      constraint = Constraint(name, day, period)
      self.__constraints.append(constraint)

    file.readline()
    file.readline()
    file.close()

    # Updating constraints and curricula in courses
    for course in self.__courses:
      course.update_constraints(self.__constraints)
      course.update_curricula(self.__curricula)
      course.update_conflicts()

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

  def get_courses(self) -> List[Course]:
    return self.__courses

  def get_rooms(self) -> List[Room]:
    return self.__rooms

  def get_curricula(self) -> List[Curricula]:
    return self.__curricula

  def get_constraints(self) -> List[Constraint]:
    return self.__constraints

  def get_num_classes_to_alloc(self) -> int:
    return self.__numClassesToAlloc

  def get_course_by_name(self, name: str) -> Course:
    for course in self.__courses:
      if course.get_name() == name:
        return course

    return None
# print(Instance('../instances/toy.ctt'))

# instance = Instance('../instances/toy.ctt')

# course = instance.get_course_by_name('TecCos')

# print(course)
# print(course.get_conflicts())

# a1 = instance.get_courses()[0]
# a2 = instance.get_courses()[2]

# print(a1.get_curricula())
# print(a2.get_curricula())
# print(a1)
# print(a2)
# print(a2.belongs_to_same_curricula(a1))
