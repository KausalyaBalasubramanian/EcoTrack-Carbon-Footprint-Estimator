def calculate_transport():
    print("\nTransport Mode:")
    print("1. Walking / Cycling")
    print("2. Public Transport")
    print("3. Bike")
    print("4. Car")

    choice = int(input("Choose option (1-4): "))

    if choice == 1:
        return 0
    elif choice == 2:
        return 1.5
    elif choice == 3:
        return 2.5
    elif choice == 4:
        return 4.5
    else:
        print("Invalid choice, assuming 0")
        return 0


def calculate_energy():
    units = float(input("\nElectricity units used per day: "))
    return units * 0.85


def calculate_food():
    print("\nFood Habit:")
    print("1. Vegetarian")
    print("2. Mixed")
    print("3. Non-Vegetarian")

    choice = int(input("Choose option (1-3): "))

    if choice == 1:
        return 1.2
    elif choice == 2:
        return 2.5
    elif choice == 3:
        return 3.3
    else:
        return 0


def main():
    print("🌍 Welcome to EcoTrack 🌍")

    transport = calculate_transport()
    energy = calculate_energy()
    food = calculate_food()

    total = transport + energy + food

    print("\n📊 Your Estimated Daily Carbon Footprint:", round(total, 2), "kg CO₂")

    if total < 5:
        print("🌱 Great job! Your carbon footprint is low.")
    elif total < 10:
        print("⚠️ Moderate footprint. Try saving energy.")
    else:
        print("🚨 High footprint! Consider eco-friendly alternatives.")

main()
