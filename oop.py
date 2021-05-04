# 2-5 Class and Instance
class Vehicle:

    def __init__(self, name, weight, release_year):
        self.name = name
        self.weight = weight
        self.release_year = release_year

    def output_name(self):
        return 'My vehicle name is {}'.format(self.name)


veh_1 = Vehicle('A', 300, 2020)

print(veh_1.name, veh_1.weight, veh_1.release_year)
print(veh_1.output_name())


# 2-6 Class variables
class Vehicle:
    total = 0

    def __init__(self, name, weight, release_year):
        self.name = name
        self.weight = weight
        self.release_year = release_year
        Vehicle.total += 1


veh_1 = Vehicle('A', 300, 2020)
veh_2 = Vehicle('B', 400, 2018)

print(Vehicle.total)
print(veh_1.total)
print(veh_2.total)
print(veh_1.__dict__)
print(veh_2.__dict__)
veh_1.total = 0.5
print(veh_1.__dict__)
print(veh_2.__dict__)
print(Vehicle.total)
print(veh_1.total)
print(veh_2.total)


# 2-7 Classmethod and Staticmethod
class Vehicle:
    total = 0
    num_of_wheels = 4

    def __init__(self, name, weight, release_year):
        self.name = name
        self.weight = weight
        self.release_year = release_year
        Vehicle.total += 1

    @classmethod
    def set_num_of_wheels(cls, wheels):
        cls.num_of_wheels = wheels

    @staticmethod
    def mul_two(value):
        return value * 2


veh_1 = Vehicle('A', 300, 2020)

print(Vehicle.num_of_wheels)
Vehicle.set_num_of_wheels(3)
print(Vehicle.num_of_wheels)
print(Vehicle.mul_two(3))
print(veh_1.mul_two(4))


# 2-8 Inheritance
class Vehicle:

    def drive(self):
        print('Driving')

    def brake(self):
        print('Braking')


class EV(Vehicle):

    def regeration(self):
        print('Regenerate battery energy')


class AutonomousEV(EV):

    def autonomous(self):
        print('Autonomous driving')


auto_ev = AutonomousEV()

auto_ev.drive()
auto_ev.brake()
auto_ev.regeration()
auto_ev.autonomous()


class Vehicle:

    def __init__(self, name, weight, release_year):
        self.name = name
        self.weight = weight
        self.release_year = release_year


class EV(Vehicle):

    def __init__(self, name, weight, release_year, battery_capacity):
        super().__init__(name, weight, release_year)
        self.battery_capacity = battery_capacity


ev_1 = EV('C', 300, 2020, 400)

print(ev_1.name, ev_1.weight, ev_1.release_year, ev_1.battery_capacity)


# 2-8 Multiple inheritance
class Developer:

    def __init__(self):
        print('init in developer')

    def complete_task(self):
        print('Task completed by developer')


class ProjectManager:

    def __init__(self):
        print('init in PM')

    def complete_task(self):
        print('Task completed by PM')


class Project(ProjectManager, Developer):

    def __init__(self):
        Developer.__init__(self)
        ProjectManager.__init__(self)
        print('init in project')

    def complete(self):
        Developer.complete_task(self)
        ProjectManager.complete_task(self)


project = Project()
project.complete()


# 2-9 Special method

class Vehicle:

    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year

    def __str__(self):
        return '{} was released in {}'.format(self.name, self.release_year)

    def __len__(self):
        return len(self.name)


veh_1 = Vehicle('ABC', 2020)

print(str(veh_1))
print(veh_1)
print(len(veh_1))


# 2-10 Decorator
class Vehicle:
    num_of_wheels = 4

    def __init__(self, name, weight, release_year):
        self.name = name
        self.weight = weight
        self.release_year = release_year

    def output_name(self):
        return 'My vehicle name is {}'.format(self.name)

    @property
    def full_info(self):
        return '{} is {} [kg] and released in {}'.format(self.name, self.weight, self.release_year)

    @property
    def weight_per_wheel(self):
        return '{} [kg]'.format(self.weight / Vehicle.num_of_wheels)

    @weight_per_wheel.setter
    def weight_per_wheel(self, value):
        if not value:
            value = 0
        self.weight = value * Vehicle.num_of_wheels


veh_1 = Vehicle('A', 300, 2020)
print(veh_1.output_name())
print(veh_1.full_info)
print(veh_1.weight_per_wheel)
veh_1.weight_per_wheel = 50
print(veh_1.weight_per_wheel)
veh_1.weight_per_wheel = None
print(veh_1.weight_per_wheel)


# 2-11 Inner class
class Vehicle:
    class Tire:

        def __init__(self):
            self.diameter = 800
            self.width = 300

        def output_info(self):
            print(self.diameter, self.width)

    def __init__(self, name):
        self.name = name
        self.tire = self.Tire()

    def output_info(self):
        print(self.name)


veh_1 = Vehicle('A')
veh_1.output_info()
veh_1.tire.output_info()
veh_1.tire.diameter = 700
veh_1.tire.output_info()


# 2-12 Override (Method)
class Vehicle:

    def __init__(self, name):
        self.name = name

    def output_name(self):
        return 'My vehicle name is {}'.format(self.name)


class EV(Vehicle):

    def __init__(self, name, battery_capacity):
        super().__init__(name)
        self.battery_capacity = battery_capacity

    def output_name(self):
        return '{} has battery capacity of {}'.format(self.name, self.battery_capacity)


ev_1 = EV('C', 400)
ev_1.output_name()


# 2-13 Mixins
class Vehicle:

    def __init__(self, name, vehicle_height):
        self.name = name
        self.speed = 0
        self.vehicle_height = vehicle_height
        self.room_temp = 25.0

    def drive(self):
        self.speed = 50

    def output_spec(self):
        return 'Vehicle {} {} [km/h] {} [mm] {} [degree]'.format(self.name, self.speed, \
                                                                 self.vehicle_height, self.room_temp)


class BoostMixin:

    def boost(self):
        self.speed += 100


class HeightAdjusterMixin:

    def height_up(self):
        self.vehicle_height += 50

    def height_down(self):
        self.vehicle_height -= 50


class AirConditionerMixin:

    def warm_up(self):
        self.room_temp += 4

    def cool_down(self):
        self.room_temp -= 4


class PremiumVehicle(Vehicle, BoostMixin, HeightAdjusterMixin, AirConditionerMixin):

    def output_spec(self):
        return 'Premium {} {} [km/h] {} [mm] {} [degree]'.format(self.name, self.speed,
                                                                 self.vehicle_height, self.room_temp)


veh_1 = Vehicle('A', 1000)
veh_1.drive()
print(veh_1.output_spec())

prem_veh = PremiumVehicle('B', 1000)
prem_veh.drive()
prem_veh.boost()
prem_veh.cool_down()
prem_veh.height_down()
prem_veh.height_down()
print(prem_veh.output_spec())
