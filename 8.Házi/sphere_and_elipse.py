import math

class Sphere:
    def __init__(self,radius):
        self.radius = radius
    

    def surface(self):
        return 4*(self.radius**2)*math.pi

    
    def volume(self):
        return (4*(self.radius**3)*math.pi)/3


    def __lt__(self,other_sphere):
        if self.volume()<other_sphere.volume():
            return True
        else:
            return False


    def __gt__(self,other_sphere):
        if self.volume()>other_sphere.volume():
            return True
        else:
            return False


    def __le__(self,other_sphere):
        if self.volume()<=other_sphere.volume():
            return True
        else:
            return False


    def __ge__(self,other_sphere):
        if self.volume()>=other_sphere.volume():
            return True
        else:
            return False
        

class Elipse:
    def __init__(self,radius_one,radius_two):
        self.radius_one = radius_one
        self.radius_two = radius_two


    def perimiter(self):
        return 2*math.pi*math.sqrt((self.radius_one**2+self.radius_two**2)/2)


    def area(self):
        return math.pi*self.radius_one*self.radius_two


def main():
    user_input_elipse_r1 = int(input("Add meg az elipszis első sugarát! "))
    user_input_elipse_r2 = int(input("Add meg az elipszis második sugarát! "))
    e = Elipse(user_input_elipse_r1,user_input_elipse_r2)
    print(f"Az elipszis kerülete: {e.perimiter()}")
    print(f"Az elipszis területe: {e.area()}")

    user_input_sphere1_r = int(input("Add meg az első gömb sugarát! "))
    user_input_sphere2_r = int(input("Add meg az első gömb sugarát! "))
    s1 = Sphere(user_input_sphere1_r)
    s2 = Sphere(user_input_sphere2_r)

    if s1 > s2:
        print("Az első gömb a nagyobb")
    elif s1 < s2:
        print("A második gömb a nagyobb")
    elif s1 >= s2:
        print("Ugyanakkora mindkét gömb")
    elif s1 <= s2:
        print("Ugyanakkora mindkét gömb")

    print(f"Az első gömb területe: {s1.volume()}")
    print(f"Az első gömb felszíne: {s1.surface()}")

    print(f"Az második gömb területe: {s2.volume()}")
    print(f"Az második gömb felszíne: {s2.surface()}")


if __name__=="__main__":
    main()