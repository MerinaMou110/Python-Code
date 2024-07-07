
class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self._seats = {}  
        self._show_list = []  
        self._rows = rows  
        self._cols = cols  
        self._hall_no = hall_no  
      

        self._seats[hall_no] = [['0' for _ in range(cols)] for _ in range(rows)]

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self._show_list.append(show_info)

        self._seats[show_id] = [['0' for _ in range(self._cols)] for _ in range(self._rows)]

    def book_seats(self, show_id, seat_list):
        if show_id not in [show[0] for show in self._show_list]:
                print("Invalid show_id")
                return

        for seat in seat_list:
            row, col = seat
            if not (0 <= row < self._rows and 0 <= col < self._cols):
                print(f"Invalid seat ({row}, {col}).")
                return

            elif self._seats[show_id][row][col] == '0':
                self._seats[show_id][row][col] = '1'
            else:
                print(f"Seat {row}-{col} is already booked")

    def view_show_list(self):
        for show in self._show_list:
            print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):    #use flag
        show_exist=False
        if show_id in self._seats:
            show_exist=True
            print(f"Available seats for Show ID {show_id}:")
            
            for row in range(self._rows):
                for col in range(self._cols):
                    if self._seats[show_id][row][col] == '0':
                        print(f"Seat {row}-{col}")
                        
        
        if not show_exist:
            print("Invalid show_id")


class Star_Cinema:
    hall_list = [] 

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class CounterSystem:
   
    def __init__(self, star_cinema):
        self.star_cinema = star_cinema

    def show_menu(self):
        while True:
            print("----------------------------------")
            print("1. View all shows")
            print("2. View available seats in a show")
            print("3. Book tickets in a show")
            print("4. Exit")
            print("----------------------------------")
            
            choice = input("Enter your choice: ")

            if choice == "1":
                self.view_all_shows()
            elif choice == "2":
                self.view_available_seats()
            elif choice == "3":
                self.book_tickets()
            elif choice == "4":
                print("Exiting")
                break
            else:
                print("Invalid choice. Please enter a number between 1 - 4.")

    def view_all_shows(self):
        print("\nAll Shows Today:")
        for hall in self.star_cinema.hall_list:
            hall.view_show_list()

    def view_available_seats(self):
        show_id = input("Enter the show ID: ")

        found = False
        for hall in self.star_cinema.hall_list:
            for show in hall._show_list:
                if show[0] == show_id:
                    found = True
                    hall.view_available_seats(show_id)
                    break
            if found:
                break

        if not found:
            print("Invalid show ID or show not found.")


    def book_tickets(self):
       show_id = input("Enter the show ID to book tickets: ")

       valid_show_id = any(show_id == show[0] for hall in self.star_cinema.hall_list for show in hall._show_list)
       if not valid_show_id:
        print("Invalid show ID. Please enter a valid show ID.")
        return

       num_tickets = input("Enter the number of tickets to book: ")

       if not num_tickets.isdigit():
        print("Invalid input. Please enter a valid number.")
        return

       num_tickets = int(num_tickets)

       seat_list = []
       for i in range(num_tickets):
        row_col = input(f"Enter the row and column for ticket {i + 1}: ")

        row, col = map(int, row_col.split())
        seat_list.append((row, col))

       for hall in self.star_cinema.hall_list:
        hall.book_seats(show_id, seat_list)




star_cinema = Star_Cinema()

hall1 = Hall(rows=5, cols=7, hall_no=1)
star_cinema.entry_hall(hall1)
hall2 = Hall(rows=2, cols=3, hall_no=2)
star_cinema.entry_hall(hall2)


hall1.entry_show(show_id='S101', movie_name='Animal', time='8:00 PM')
hall1.entry_show(show_id='S102', movie_name='Aquaman', time='11:00 PM')

hall2.entry_show(show_id='V201', movie_name='Life of pi', time='8:00 PM')
hall2.entry_show(show_id='V202', movie_name='Superman', time='11:00 PM')

counter_system = CounterSystem(star_cinema)
counter_system.show_menu()

