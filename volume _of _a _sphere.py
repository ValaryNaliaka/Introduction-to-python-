#volume of a sphere
def volume_of_a_sphere(radius=21):
    radius=int(input("enter the radius;"))
    volume=4/3*3.142*radius*radius*radius
    print("volume",volume)
volume_of_a_sphere()