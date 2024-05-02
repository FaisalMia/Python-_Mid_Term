class Star_Cinema:

    hall_list = []

    def entry_hall(self,hall):
        self.hall = hall
        self.hall_list.append(hall)


class Hall:
    def __init__(self,rows,cols,hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self._rows = rows
        self._cols = cols
        self.hall_no = hall_no
        Star_Cinema().entry_hall(self)

    def entry_show(self,id,movie_name,time):
        show_inf = (id,movie_name,time)
        self.__show_list.append(show_inf)
        allocate_seat = [['0' for _ in range(self._cols)] for _ in range(self._rows)]
        self.__seats[id] = allocate_seat

    def book_seats(self, show_id, number_of_tickets):
        if show_id in self.__seats:
            seat_layout = self.__seats[show_id]
            for i in range(number_of_tickets):
                row = int(input(f"Enter the row number for ticket {i + 1}: "))
                col = int(input(f"Enter the column number for ticket {i + 1}: "))
                if row < len(seat_layout) and col < len(seat_layout[0]):
                    if seat_layout[row][col] == '0':
                        seat_layout[row][col] = '1'
                        print(f"Seat({row},{col}) has been booked for show {show_id}")
                    else:
                        print(f"Seat({row},{col}) is already booked!")
                else:
                    print("Invalid row or column number!")
        else:
            print("Show ID is not found!")


    def view_show_list(self):
        for show_inf in self.__show_list:
            print(f'MOVIE NAME: {show_inf[1]} SHOW ID: {show_inf[0]}  TIME: {show_inf[2]}')
           
    def available_seats(self, show_id):
        for i in range(self._rows):
            row_str = "["
            for j in range(self._cols):
                if self.__seats[show_id][i][j] == '0':
                    row_str += '0 '
                else:
                    row_str += '1 '
            print(row_str.strip()+"]")

hall = Hall(3,4,101)
hall.entry_show(111,'Jawan Maji(111)', '1/5/24 11:00 AM')
hall.entry_show(112,' Sujon Maji(112)', '1/5/24 1:00 PM')

run = True

while run:
    print("Options: \n")

    print("1 : VIEW ALL SHOW TODAY")
    print("2 : VIEW AVAILABLE SEATS")
    print("3 : BOOK TICKETS")
    print("4 : Exit")

    ch = int(input("\nEnter option: "))

    if ch == 1:
        hall.view_show_list()
    elif ch == 2:
        show_id = int(input("ENTER SHOW ID: "))
        hall.available_seats(show_id)
    elif ch == 3:
        show_id = int(input("ENTER SHOW ID: "))
        Number_of_ticket = int(input("ENTER NO OF SEATS: "))
        
        hall.book_seats(show_id,Number_of_ticket)








