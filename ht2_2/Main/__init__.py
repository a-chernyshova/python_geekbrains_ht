# -*- coding: utf-8 -*-
import Cars.Cars
import Cars.Lorry
import Car_dealership.Car_dealership

#id, car_model, maker, year_production, engine, cost
new_dilership = Car_dealership.Car_dealership.CarDealership(200)
new_car1 = Cars.Cars.Cars(1, 'Q3', 'Audi', 2016, 2.0, 35000)
new_car2 = Cars.Cars.Cars(2, 'Cherokee', 'Jeep', 2016, 2.5, 34000)
new_car3 = Cars.Cars.Cars(5, 'RAV-4', 'Toyota', 2016, 2.4, 27000)
new_car4 = Cars.Cars.Cars(-1, 'Test', 'Lincoln', '2017', 2, 50000)
new_car5 = Cars.Cars.Cars(1, 'Repeat', 'Audi', 2016, 2.0, 36000)
new_lorry1 = Cars.Lorry.Lorry(3, 'AXLE', 'Lorry', 2013, 2.0, 20000, 40)

new_dilership.add_car(new_car1)
new_dilership.add_car(new_car2)
new_dilership.add_car(new_car3)
new_dilership.add_car(new_car4)
new_dilership.add_car(new_car5)
new_dilership.add_lorry(new_lorry1)

new_dilership.get_car(1)
new_dilership.get_car(2)
new_dilership.get_car(10)
new_dilership.get_car(3)
new_dilership.get_lorry(2)
# new_dilership.get_car('Q3')
# new_dilership.get_car('RAV-4')
# new_dilership.get_lorry('AXLE')
# new_dilership.get_car('Q7')

new_dilership.printer()
