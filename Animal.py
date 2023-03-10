#simple inheritance
class Animal:
    def legs(self):
        print("I have four legs")
    def fur(self):
        print("my body is covered with fur")
class Dog(Animal):
    def bark(self):
        print("the dog barks")
d=Dog()
d.bark()
d.legs()
d.fur()