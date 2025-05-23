def intro():
    print("🔎 Welcome, Detective.")
    print("A crime has been committed in the city. You have 3 leads.")
    print("Will you solve the case or let the criminal get away?\n")
    first_choice()

def first_choice():
    print("1️⃣ Visit the crime scene.")
    print("2️⃣ Interrogate the suspect.")
    print("3️⃣ Check security footage.\n")

    choice = input("What do you want to do? (1/2/3): ")

    if choice == '1':
        crime_scene()
    elif choice == '2':
        suspect()
    elif choice == '3':
        footage()
    else:
        print("❌ Invalid choice.")
        first_choice()

def crime_scene():
    print("\n🏠 At the crime scene, you find a broken vase and muddy footprints.")
    print("1️⃣ Follow the footprints.")
    print("2️⃣ Collect fingerprints from the vase.\n")
    
    choice = input("Your move (1/2): ")
    if choice == '1':
        print("\n🚨 You follow the trail and catch the thief in an alley. Case closed!")
    elif choice == '2':
        print("\n🧪 The fingerprints match a known criminal. You arrest them. Case closed!")
    else:
        print("❌ Invalid choice.")
        crime_scene()

def suspect():
    print("\n🗣️ The suspect is nervous and avoids eye contact.")
    print("1️⃣ Press harder with questions.")
    print("2️⃣ Offer coffee and gain trust.\n")

    choice = input("Your move (1/2): ")
    if choice == '1':
        print("\n😤 The suspect lawyers up. You lose the lead.")
    elif choice == '2':
        print("\n☕ The suspect slips and reveals a clue! You're closer to solving the case.")
        crime_scene()
    else:
        print("❌ Invalid choice.")
        suspect()

def footage():
    print("\n🎥 The footage shows someone wearing a hoodie.")
    print("1️⃣ Try enhancing the video.")
    print("2️⃣ Cross-check time with street camera logs.\n")

    choice = input("Your move (1/2): ")
    if choice == '1':
        print("\n🖼️ You can't make out the face. No new info.")
    elif choice == '2':
        print("\n📁 You find a license plate in a nearby camera — it’s your suspect’s car!")
        suspect()
    else:
        print("❌ Invalid choice.")
        footage()

if __name__ == "__main__":
    intro()
