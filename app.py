

class Car:

  def __init__(self, make: str, color: str) -> None:
    self.make = make
    self.color = color

  def __str__(self) -> str:
    return f"make: {self.make}\ncolor: {self.color}"

car1 = Car('chevrolet', 'white')
