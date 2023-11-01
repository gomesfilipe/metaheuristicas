from Course import Course
from Room import Room
from Curricula import Curricula

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
      courses = set(line)

      curricula = Curricula(name, courses)
      self.curricula.append(curricula)

    print(self.courses, self.rooms, self.curricula)

    file.readline()
    file.readline()

    # Reading constraints
    self.constraints = []

    for i in range(self.numConstraints):
      line = file.readline().split()
      # ...
      pass

Instance('../instances/toy.ctt')