
class Vehicul:
    seat=4
    def __init__(self,name,max_speed,mile_age):
        self.name=name
        self.max_speed=max_speed
        self.mile_age=mile_age

    def seating_capacity(self,places):
        return f" name : {self.name} ,places: {places}"

class Bus(Vehicul):
    pass

v=Vehicul(None,200,80)
b=Bus("volovo",150,10)
dic_v={
    "name":v.name,
    "max_speed":v.max_speed,
    "age":v.mile_age
}
dic_b={
    "name":b.name,
    "max_speed":b.max_speed,
    "age":b.mile_age
}

print(f"le nombre des places par bus : {b.seating_capacity(50)} -- ne nombre des place par default : {b.seat}")




   