import os
import csv

def yes_no_input():
    while True:
        choice = input("Initialize Logs. OK? Please respond with 'yes' or 'no' [y/N]: ").lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False


def main():
    if not os.path.exists('Logs'):
        os.makedirs('Logs')
    print("Make Logs Dir")

    if not os.path.exists('Images'):
        os.makedirs('Images')
    print("Make Images Dir")

    # create Log file
    if not os.path.exists('Logs/TempLog.csv'):
        with open('Logs/TempLog.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["datetime", "temp"])
    print("Make Logs/TempLog.csv")

    if not os.path.exists('Logs/BatteryLog.csv'):
        with open('Logs/BatteryLog.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["datetime", "V", "A", "W"])
    print("Make Logs/batteryg.csv")



if __name__ == '__main__':
    if yes_no_input():
        print("Initialize Logs...")
        main()
        print("Completed")

    else :
        print("Look forward to trying again!")
