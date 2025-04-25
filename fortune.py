print("🔮 Welcome to Sangarsu Abhijith Fortune Teller (21JE) 🔮0821")
mood = input("How are you feeling today? (happy/sad/neutral): ").lower()

if mood == "happy":
    print("✨ Your fortune: Great things await you, Aryan! Keep smiling. ✨")
elif mood == "sad":
    print("✨ Your fortune: Storms don’t last forever. Better days are coming. ✨")
elif mood == "neutral":
    print("✨ Your fortune: Balance brings clarity. Stay steady. ✨")
else:
    print("❌ Unknown mood. Try again with happy, sad, or neutral.")