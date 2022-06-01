carList = [
    {"carID" : "001", "plateNum" : "B 3456 KTM", "carType" : "SUV", "carName" : "Fortuner", "price" : 550000, "status" : "Available"},
    {"carID" : "002", "plateNum" : "B 1267 STG", "carType" : "SEDAN", "carName" : "Civic", "price" : 250000, "status" : "Available"},
    {"carID" : "003", "plateNum" : "B 2890 TMH", "carType" : "MPV", "carName" : "Avanza", "price" : 350000, "status" : "Available"},
    {"carID" : "004", "plateNum" : "B 5834 TYO", "carType" : "MPV", "carName" : "Innova", "price" : 320000, "status" : "Available"},
    {"carID" : "005", "plateNum" : "B 0824 SHI", "carType" : "MPV", "carName" : "Sienta", "price" : 300000, "status" : "Available"},
    {"carID" : "006", "plateNum" : "B 0754 TGJ", "carType" : "SEDAN", "carName" : "Camry", "price" : 350000, "status" : "Available"},
    {"carID" : "007", "plateNum" : "B 2076 KUT", "carType" : "TRUCK", "carName" : "Hilux", "price" : 700000, "status" : "Available"},
    {"carID" : "008", "plateNum" : "B 1996 KYT", "carType" : "TRUCK", "carName" : "Triton", "price" : 500000, "status" : "Available"},
    {"carID" : "009", "plateNum" : "B 5367 KAR", "carType" : "SUV", "carName" : "Pajero", "price" : 500000, "status" : "Available"},
    {"carID" : "010", "plateNum" : "B 3786 TYS", "carType" : "SUV", "carName" : "Palisade", "price" : 500000, "status" : "Available"},
    ]
rentedCarReport = []

def fnSubMenu(fn, option):
    while True:
        subMenu = input(f'''
    1. {option}
    2. Back to Main Menu

    Enter your request: ''')
        if subMenu == "1":
            fn()  
        elif subMenu == "2":
            break
        continue

def fnSubMenu1(fn, option1, option2):
    while True:
        subMenu = input(f'''
    1. {option1}
    2. {option2}
    3. Back to Main Menu

    Enter your request: ''')
        if subMenu == "1":
            fn()  
        elif subMenu == "2":
            uniqueInput = input("    Enter Car Type: ").upper()
            fn(uniqueInput)
        elif subMenu == "3":
            break
        continue

def fnShowCar(unique = None):
    if unique == None:
        print('''    | carID | Plate Number | Car Type    |   Car Name   |  Price  |    Status    |''')
        for i in range (len(carList)):
            print(f'''    |  {carList[i]["carID"]}  |  {carList[i]["plateNum"]}  |  {carList[i]["carType"]}\t | {carList[i]["carName"]}\t| {carList[i]["price"]}  | {carList[i]["status"]}\t |''')
            continue
    elif unique != None:
        print('''    | carID | Plate Number | Car Type    |   Car Name   |  Price  |    Status    |''')   
        for i in range (len(carList)):
            if carList[i]['carType'] == unique:  
                print(f'''    |  {carList[i]["carID"]}  |  {carList[i]["plateNum"]}  |  {carList[i]["carType"]}\t | {carList[i]["carName"]}\t| {carList[i]["price"]}  | {carList[i]["status"]}\t |''')
                continue
        

def fnAddCar():
    newCarID = input("    Enter New Car ID to : ").title()
    newPlateNum = input(f"    Enter Plate Number for {newCarID}: ").upper()
    newCarType = input(f"    Enter Car Type for {newCarID}: ").upper()
    newCarName = input(f"    Enter Car Name for {newCarID}: ").capitalize()
    newPrice = int(input(f"    Enter Price ID for {newCarID}: "))
    for i in range (len(carList)):
        if newPlateNum == carList[i]["plateNum"]:
            print("\n    This car is already on the database")
            break
    else:
        while True:
            confirmation = input(f"    Are you sure you want to add '{newCarID}' to the database? (Y/N): ").capitalize()
            if confirmation == "Y":
                carList.append({"carID" : newCarID, "plateNum" : newPlateNum, "carType" : newCarType, "carName" : newCarName, "price" : newPrice, "status" : "Available"})
                break
            elif confirmation == "N":
                print("\n    Data cancelled to be add")
                break
            else:
                print("\n    Please try again \n")
                continue

    fnShowCar()

def fnDeleteCar():
    fnShowCar()
    deleteCar = input("\n    Enter Car ID delete: ").lower()
    for i in range (len(carList)):
        if deleteCar == carList[i]["carID"]:
            while True:
                confirmation = input(f"    Are you sure you want to delete '{carList[i]['carID']}'? (Y/N): ").capitalize()
                if confirmation == "Y":
                    del(carList[i])
                    print(f"\n    Data have been deleted on database")
                    break
                elif confirmation == "N":
                    print("\n    Data cancelled to be delete\n")
                    break
                else:
                    print("\n    Please try again \n")
                    continue
            break
    else:
        print("\n    Data doesn't exist")
    fnShowCar()

def fnUpdateCar():
    fnShowCar()
    updateCar = input("\n    Enter Car ID to Update: ").lower()
    for i in range (len(carList)):
        if updateCar == carList[i]["carID"]:
            while True:
                updatePlateNum = input(f"    Enter Plate Number for {updateCar}: ").upper()
                updatePrice = int(input(f"    Enter Price for {updateCar}: ")) 
                confirmation = input(f"    Are you sure you want to update '{updateCar}' from your list? (Y/N): ").capitalize()
                if confirmation == "Y":
                    carList[i]["plateNum"] = updatePlateNum
                    carList[i]["price"] = updatePrice
                    print(f"\n   {updateCar} have been updated on database")
                    break
                elif confirmation == "N":
                    print("\n    ok")
                    break
                else:
                    print("\n    Please try again \n")
                    continue
            break
    else:
        print("\n    Data doesn't exist")
    fnShowCar()

def fnRentCar():
    fnShowCar()
    rentCar = input("\n    Enter Car ID to rent: ").lower()
    for i in range (len(carList)):
        if rentCar == carList[i]["carID"]:
            if carList[i]["status"] == "Available":
                rentTime = int(input("\n    Enter the number of day to rent: "))
                rentName = input("\n    Enter customer name: ").title()
                rentNoHP = input("\n    Enter customer phone number: ").title()
                while True:
                    confirmation = input(f"    Are you sure you want to borrow '{carList[i]['carName']} {carList[i]['plateNum']}' for {rentTime} day(s)? (Y/N): ").capitalize()
                    if confirmation == "Y":
                        carList[i]["status"] = "Rented"
                        total = rentTime * carList[i]["price"]
                        rentedCarReport.append(
                            [rentName, rentNoHP, carList[i]['carID'],carList[i]['plateNum'],carList[i]['carType'], carList[i]['carName'], carList[i]['price'], rentTime, total]
                        )
                        print((f'''
                    --------------------------------------------
                    {rentName} rented {carList[i]['carName']} {carList[i]['plateNum']} for {rentTime} day(s)
                    The data have been updated
                    --------------------------------------------
                    The total bill is IDR {total}'''))
                        break
                    elif confirmation == "N":
                        print("\n    ok")
                        break
                    else:
                        print("\n    Please try again \n")
                        continue
                break
            else:
                print("\n    This car is currently rented")
                break
    else:
        print("\n    Data doesn't exist")

def carReport():
    print('''    | Cust. Name | Telp. Number | carID | Plate Number | Car Type |   Car Name   |  Price  |  Rent Time |  Total   |''')
    for i in range (len(rentedCarReport)):
            print(f'''    |   {rentedCarReport[i][0]}\t | {rentedCarReport[i][1]} |  {rentedCarReport[i][2]}  |  {rentedCarReport[i][3]}  |  {rentedCarReport[i][4]}\t  | {rentedCarReport[i][5]}\t | {rentedCarReport[i][6]}  | \t{rentedCarReport[i][7]}\t|  {rentedCarReport[i][8]} |''')
            continue    

def fnReturnCar():
    carReport()
    returnCar = input("\n    Enter Car ID to return: ").lower()
    for i in range (len(carList)):
        if returnCar == carList[i]["carID"]:
            if carList[i]["status"] != "Available":
                while True:
                    confirmation = input(f"    Are you sure you want to return '{carList[i]['carName']} {carList[i]['plateNum']}'? (Y/N): ").capitalize()
                    if confirmation == "Y":
                        carList[i]["status"] = "Available"
                        print(f"\n    Thank you for returning '{carList[i]['carName']} {carList[i]['plateNum']}' ")
                        for item in range(len(rentedCarReport)):
                            if returnCar == rentedCarReport[item][2]:
                                del rentedCarReport[item]
                        break
                    elif confirmation == "N":
                        print("\n    ok")
                        break
                    else:
                        print("\n    Please try again \n")
                        continue
            else:
                print("\n    This car doesn't need to be returned.")
            break
    else:
        print("\n    Data doesn't exist")


# Loop
while True:
    mainMenu = input('''
    --------------------------------
        Welcome to Tyodh Garage  
    --------------------------------
    1. Show Car on Database 
    2. Add New Car
    3. Delete Data
    4. Update Data
    5. Rent Car
    6. Return Car
    7. Rented Car Report
    8. Exit Garage

    Enter your request (1-8): ''')

    if mainMenu == "1":
        fnSubMenu1(fnShowCar, "Show All Cars in the Garage", "Show Car with Specific Car Type")

    elif mainMenu == "2":
        fnSubMenu(fnAddCar, "Add New Car to The Garage")

    elif mainMenu == "3":
        fnSubMenu(fnDeleteCar, "Delete Existing Car from The Garage") 

    elif mainMenu == "4":
        fnSubMenu(fnUpdateCar, "Update the Data from the list")

    elif mainMenu == "5":
        fnSubMenu(fnRentCar, "Rent Car from The Garage")

    elif mainMenu == "6":
        fnSubMenu(fnReturnCar, "Return Car from The Garage")

    elif mainMenu == "7":
        fnSubMenu(carReport, "Show Rented Car Report")

    elif mainMenu == "8":
        print('''\n    Thank you for visiting Tyodh Garage!
        ''')
        break
    else:
        print('''\n    Please try again ''')