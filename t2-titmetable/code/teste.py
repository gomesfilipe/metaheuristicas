class Test:
  def __init__(self, name) -> None:
    self.name = name

  # def __str__(self) -> str:
  #   return self.name

a = Test('a')
b = Test('a')

print(a)
print(b)
print()

x = set([a])

print(x)
x.add(b)
print(x)