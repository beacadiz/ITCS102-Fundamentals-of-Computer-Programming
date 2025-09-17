# Ask the user for the phrase and repetition count
print("🦜 PARROT SIMULATOR – THE ECHO CHAMBER!")
phrase = input("What do you want your parrot to say? ")
times = int(input("How many times should the parrot squawk it? "))

# Print the repeated phrase with squawk!
print("\nListen to your parrot:")
for i in range(times):
    print(f"🦜 Squawk! {phrase}")
