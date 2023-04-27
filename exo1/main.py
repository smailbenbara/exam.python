# main.py

from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
from bus import Bus
from metro import Metro

def main():
    vehicles = []

    while True:
        print("Choiser une option:")
        print("1. ajouter un vehicle")
        print("2. supprimer un vehicle")
        print("3. mettre a jour vehicle")
        print("4. Voir tout vehicles")
        print("5. Voit lesstatistics")
        print("6. Exit")

        choice = input("Enter votre choix: ")

        if choice == "1":
            vehicle_type = input("Enter le type de  vehicle (car, motorcycle, bus, metro): ")
            if vehicle_type == "car":
                vehicles.append(Car())
            elif vehicle_type == "motorcycle":
                vehicles.append(Motorcycle())
            elif vehicle_type == "bus":
                vehicles.append(Bus())
            elif vehicle_type == "metro":
                vehicles.append(Metro())
            else:
                print("Invalid le type devehicle")
        elif choice == "2":
            plate_number = input("Entrez le numéro de plaque du véhicule à supprimer: ")
            for vehicle in vehicles:
                if vehicle.plate_number == plate_number:
                    vehicles.remove(vehicle)
                    break
            else:
                print("Véhicule introuvable")
        elif choice == "3":
            plate_number = input("Entrez le numéro de plaque du véhicule à mettre à jour: ")
            for vehicle in vehicles:
                if vehicle.plate_number == plate_number:
                    vehicle.update()
                    break
            else:
                print("Véhicule introuvable")
        elif choice == "4":
            for vehicle in vehicles:
                print(vehicle)
        elif choice == "5":
            print("Statistiques non implémentées ouit")
        elif choice == "6":
            break
        else:
            print("choix invalide")

if __name__ == "__main__":
    main()
