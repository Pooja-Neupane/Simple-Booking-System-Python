import datetime

BOOKING_FILE = "bookings.csv"

def book_appointment():
    name = input("Enter your name: ").title()
    service = input("Enter service (e.g., Haircut, Facial, Therapy): ").title()
    date = input("Enter appointment date (YYYY-MM-DD): ")
    time = input("Enter appointment time (HH:MM in 24hr format): ")

    try:
        appointment_datetime = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        now = datetime.datetime.now()
        if appointment_datetime < now:
            print("❌ You can't book an appointment in the past!")
            return
    except ValueError:
        print("❌ Invalid date or time format. Try again.")
        return

    with open(BOOKING_FILE, "a") as file:
        file.write(f"{name},{service},{date},{time}\n")
    
    print(f"✅ Appointment booked for {name} on {date} at {time} for {service}.")

def view_bookings():
    try:
        with open(BOOKING_FILE, "r") as file:
            data = file.readlines()
            if not data:
                print("📭 No appointments booked yet.")
                return

            print("\n📅 Booked Appointments:")
            print("Name\t\tService\t\tDate\t\tTime")
            print("---------------------------------------------------------")
            for line in data:
                name, service, date, time = line.strip().split(",")
                print(f"{name}\t\t{service}\t\t{date}\t{time}")
    except FileNotFoundError:
        print("📂 Booking file not found.")

def menu():
    print("💇‍♀️ Welcome to Salon/Clinic Booking System 🏥")
    while True:
        print("\nMenu:")
        print("1. Book Appointment 📋")
        print("2. View Bookings 📄")
        print("3. Exit 🚪")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            book_appointment()
        elif choice == '2':
            view_bookings()
        elif choice == '3':
            print("👋 Thank you for using our booking system!")
            break
        else:
            print("⚠️ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    menu()
