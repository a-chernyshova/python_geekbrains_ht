# -*- coding: utf-8 -*-
import Dealership.Dealership

Dealership1 = Dealership.Dealership.Dealership('localhost', 'dealership', 'root', 'password')
#Dealership1.printer_models()
#Dealership1.printer_makers()
#Dealership1.printer_car_dealership()
#Dealership1.printer_not_available_car()

#Dealership1.add_car(7, 'Q3', 'Audi', 2016, 2.2, 31500)
#Dealership1.add_lorry(13, "Lorry_ven", "Lorry", 2015, 2.0, 27000, 45)
#Dealership1.add_car_to_dealership(6, 1)

#Dealership1.update_amount(2, 7)
#Dealership1.update_car(1, 33000)
#Dealership1.update_lorry(2, 36)

#Dealership1.delete_car_from_dealership(5) - ПОЧЕМУ ТО НЕ РАБОТАЕТ
#Dealership1.delete_car(7)
#Dealership1.delete_lorry(2)

#Dealership1.search_car_model('Q3')
#Dealership1.search_car_maker('Jeep')

Dealership1.printer_car_dealership()
Dealership1.break_connection()
