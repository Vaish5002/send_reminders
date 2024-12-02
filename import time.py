import time
from plyer import notification

def send_reminder(title, message):
    """
    Function to send notifications.
    """
    notification.notify(
        title=title,
        message=message,
        app_name="Reminder App",
        timeout=10  # Notification duration in seconds
    )

def add_reminder(reminders, title):
    """
    Add a reminder with a specific time.
    """
    reminder_time = input(f"Enter time for {title} reminder (HH:MM, 24-hour format): ")
    reminders[title] = reminder_time
    print(f"{title} reminder set for {reminder_time}.")

def show_reminders(reminders):
    """
    Display all reminders.
    """
    if not reminders:
        print("No reminders set.")
    else:
        print("Your reminders:")
        for title, time in reminders.items():
            print(f"- {title} at {time}")

def main():
    reminders = {}
    print("Welcome to the Study and Work Reminder App!")
    
    # Insert the immediate notification here
    send_reminder("Test Reminder", "This is a test notification!")
    
    while True:
        print("\nOptions:")
        print("1. Set Study Reminder")
        print("2. Set Work Reminder")
        print("3. Show Reminders")
        print("4. Start Reminder Service")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_reminder(reminders, "Study")
        elif choice == "2":
            add_reminder(reminders, "Work")
        elif choice == "3":
            show_reminders(reminders)
        elif choice == "4":
            print("Starting the reminder service. Press Ctrl+C to stop.")
            try:
                while True:
                    current_time = time.strftime("%H:%M")
                    for title, reminder_time in reminders.items():
                        if current_time == reminder_time:
                            send_reminder(f"{title} Reminder", f"It's time for {title.lower()}!")
                            time.sleep(60)  # Avoid sending multiple notifications for the same minute
                    time.sleep(10)  # Check every 10 seconds
            except KeyboardInterrupt:
                print("\nReminder service stopped.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
