from datetime import datetime
import pytz

print("----------Below are all TIME ZONES available in PYTZ module----------")
for tz in pytz.all_timezones:
    print(tz)

# 2. Start the interactive loop
running = True
while running:
    # Ask the user for their target timezone
    user_input = input("\nEnter a timezone (or type 'list' to see all, 'exit' to quit): ").strip()

    if user_input.lower() == 'exit':
        print("Goodbye!")
        running = False
    elif user_input.lower() == 'list':
        # Print the entire list if they want to see everything
        for zone in all_zones:
            print(zone)
    elif user_input in pytz.all_timezones_set:
        # 3. If valid, fetch and show the current time in that timezone
        tz = pytz.timezone(user_input)
        localized_time = datetime.now(tz)
        
        print(f"\nTimezone: {user_input}")
        print(f"Current Date & Time: {localized_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")
    else:
        print("\n❌ Invalid timezone name. Please make sure you match the capitalization (e.g., 'America/New_York').")