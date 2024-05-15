import csv
import unittest

file_path = "movies.csv"

movies_data = [
    {"title": "Back to black", "genre": "Drama", "duration": 202},
    {"title": "Marija Montesori", "genre": "Drama", "duration": 140},
    {"title": "President", "genre": "Documentary", "duration": 155},
    {"title": "Arcadian", "genre": "Horror", "duration": 132},
    {"title": "The Fall Guy", "genre": "Comedy", "duration": 206},
    {"title": "Abigail", "genre": "Horror", "duration": 150}
]

# Save the movies data to a CSV file
with open(file_path, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["title", "genre", "duration"])
    writer.writeheader()
    for movie in movies_data:
        writer.writerow(movie)

print(f"File '{file_path}' has been saved in the same directory as the script.")

# Abstraction and Encapsulation
class Movie:
    def __init__(self, title, genre, duration):
        self.title = title
        self.genre = genre
        self.duration = duration

    def get_info(self):
        return f"Title: {self.title}, Genre: {self.genre}, Duration: {self.duration} mins"

class Ticket:
    def __init__(self, movie, seat_number, price):
        self.movie = movie
        self.seat_number = seat_number
        self.price = price
    
    def get_ticket_info(self):
        return f"Movie: {self.movie.title}, Seat Number: {self.seat_number}, Price: ${self.price: .2f}"
    
# Singleton Pattern
class Theater:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Theater, cls).__new__(cls)
            cls._instance.movies = []
        return cls._instance
    
    def add_movie(self, movie):
        self.movies.append(movie)

    def show_movies(self):
        print(f"Movies playing at the theater:")
        for movie in self.movies:
            print(movie.get_info())

# Factory Method Pattern
class TicketFactory:
    @staticmethod
    def create_ticket(movie, seat_number, price):
        return Ticket(movie, seat_number, price)
    
# Data Import/Export
class DataHandler:
    @staticmethod
    def import_movies_from_csv(filename):
        movies = []
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                movies.append(Movie(row['title'], row['genre'], int(row['duration'])))
        return movies
    
    @staticmethod
    def export_tickets_to_csv(tickets, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Movie Title', 'Seat Number', 'Price'])
            for ticket in tickets:
                writer.writerow([ticket.movie.title, ticket.seat_number, ticket.price])

# Unit Tests
class TestMovieTheater(unittest.TestCase):
    def test_import_movies_from_csv(self):
        movies = DataHandler.import_movies_from_csv('movies.csv')
        self.assertEqual(len(movies), 6)  # There are 6 movies in the file

    def test_create_ticket(self):
        movie = Movie("Titanic", "Romantic Disaster", 314)
        ticket = TicketFactory.create_ticket(movie, "A12", 10.50)
        self.assertIsInstance(ticket, Ticket)
        self.assertEqual(ticket.movie.title, "Titanic")

if __name__ == "__main__":
    # Example usage
    theater = Theater()
    movies = DataHandler.import_movies_from_csv('movies.csv')
    for movie in movies:
        theater.add_movie(movie)

    theater.show_movies()

    ticket1 = TicketFactory.create_ticket(movies[0], "A12", 10.50)
    ticket2 = TicketFactory.create_ticket(movies[1], "B7", 12.00)

    tickets = [ticket1, ticket2]
    DataHandler.export_tickets_to_csv(tickets, 'tickets.csv')

    # Run unit tests
    unittest.main()
