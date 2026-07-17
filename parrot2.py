# instance attributes
class parrot:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# instance method
  def sing(self, song):
    print(f"{self.name} sings {song}")

  def dance(self):
        print(f"{self.name} is now dancing")

        #instantiate the object
blu = parrot("Blu", 10)

        #call our instance methods
blu.sing("'Happy'")
blu.dance()