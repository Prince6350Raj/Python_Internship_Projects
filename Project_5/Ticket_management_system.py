events = {
    '101': {'name': 'Concert', 'venue': 'City Hall', 'total_seats': 100, 'available_seats': 100},
    '102': {'name': 'Theater Play', 'venue': 'Drama Theater', 'total_seats': 80, 'available_seats': 80},
    '103': {'name': 'Movie Screening', 'venue': 'Cinema World', 'total_seats': 120, 'available_seats': 120}
}

bookings = []
def display_events():
    print("\nAvailable Events:")
    print("----------------")
    print("ID\tName\t\tVenue\t\tAvailable Seats")
    print("----------------")
    for event_id, details in events.items():
        print(f"{event_id}\t{details['name']}\t{details['venue']}\t{details['available_seats']}")

def check_availability(event_id):
    if event_id in events:
        return events[event_id]['available_seats']
    else:
        return None

def book_tickets(event_id, num_tickets):
    if event_id in events:
        available_seats = events[event_id]['available_seats']
        if available_seats >= num_tickets:
            events[event_id]['available_seats'] -= num_tickets
            bookings.append({'event_id': event_id, 'num_tickets': num_tickets})
            print(f"\n{num_tickets} tickets booked successfully for event '{events[event_id]['name']}'")
        else:
            print("Insufficient seats available.")
    else:
        print("Event not found.")

def cancel_booking(event_id, num_tickets):
    for booking in bookings:
        if booking['event_id'] == event_id and booking['num_tickets'] == num_tickets:
            events[event_id]['available_seats'] += num_tickets
            bookings.remove(booking)
            print(f"{num_tickets} tickets cancelled successfully.")
            return
    print("Booking not found.")

while True:
    print("\nTicket Booking System Menu:")
    print("1. Display Available Events")
    print("2. Check Ticket Availability")
    print("3. Book Tickets")
    print("4. Cancel Booking")
    print("5. Display Bookings")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        display_events()
    elif choice == '2':
        event_id = input("Enter Event ID to check availability: ")
        available_seats = check_availability(event_id)
        if available_seats is not None:
            print(f"Available seats for Event '{events[event_id]['name']}': {available_seats}")
        else:
            print("Event not found.")
    elif choice == '3':
        event_id = input("Enter Event ID to book tickets: ")
        num_tickets = int(input("Enter number of tickets to book: "))
        book_tickets(event_id, num_tickets)
    elif choice == '4':
        event_id = input("Enter Event ID to cancel booking: ")
        num_tickets = int(input("Enter number of tickets to cancel: "))
        cancel_booking(event_id, num_tickets)
    elif choice == '5':
        print("\nCurrent Bookings:")
        print("-----------------")
        for booking in bookings:
            print(f"Event: {events[booking['event_id']]['name']}, Tickets: {booking['num_tickets']}")
    elif choice == '6':
        print("\nExiting Ticket Booking System.\nHave a good day!")
        break
    else:
        print("\nInvalid choice. Please enter a valid option (1-6).")
