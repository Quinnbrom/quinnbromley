'''
    Title:          Cinema Admin System
    Description:    Assignment 3
    Author:         Quinn Bromley-Hough
'''

"""
    Movie class
"""
class Movie:
    # Constructor Method:
    def __init__(self, name = None, minutes = 0, rating = None):
        # Attributes
        self.name = name.lower()
        self.mins = minutes
        self.rating = rating
    
    # Setter Method for Name
    def set_name(self, name):
        self.name = name
    # Getter Method for Name
    def get_name(self):
        return self.name

    # Setter Method for Minutes
    def set_minutes(self, minutes):
        self.mins = minutes
    # Getter Method for Minutes
    def get_minutes(self):
        return self.mins

    # Setter Method for Rating
    def set_rating(self, rating):
        self.rating = rating
        availableRatings = ['G','PG','R13','M','R18']

        # Check the rating in here as well
        for ratings in availableRatings:
            if ratings in availableRatings:
                self.rating = rating
                return True
            else:
                print("\n" "Invalid Rating please try again" "\n")
                return False

    # Getter Method for Rating
    def get_rating(self):
        return self.rating

    def __str__(self):
        return "Movie Name: " + str(self.name) + " Length of Movie: " + str(self.mins) + " Movie Rating: " + str(self.rating)

"""
    Cinema class
"""

class Cinema:

    # Constructor
    def __init__(self, movies=None):
        # Attribute
        self.movies = []

    # Method to add movies
    def add(self, aNewMovie):
        self.movies.append(aNewMovie)
        #print("***DEBUG*** Method is being used")

    # Method to remove movies
    def remove(self, remove_movie):
        self.movies.remove(remove_movie)
        #print("***DEBUG*** Method is being used")

    # Search method for Name
    def get_movie_name(self, search):
        #print("***DEBUG*** Method is being used")

        #convert the search string to the case that matches how you are storing in set_name
        search = search.lower()

        # Loop through the list of movies
        for name in self.movies:
            if name.get_name () == search:
                return name

    # Search method for Rating
    def get_movie_rating(self, search):
        #print("***DEBUG*** Method is being used")

        #convert the search string to the case that matches how you are storing in set_name
        search = search.lower()

        # Loop through the list of movies
        for rating in self.movies:
            if rating.get_rating () == search:
                return rating

    # Search method for Length
    def get_movie_length(self, search):

        #convert the search string to the case that matches how you are storing in set_name
        search = search.lower()

        # Loop through the list of movies
        for length in self.movies:
            if length.get_rating () == search:
                return length
            
        return False

    # Method to display all exsisting Movies
    def report(self):
        report = ""
        index = 0

        while (index <len(self.movies)):
            report += "\n" "Movie Title: " + self.movies[index].get_name() + ", "
            report += "Movie Length: " + self.movies[index].get_minutes()  + " minutes, "
            report += "Movie Rating: " + self.movies[index].get_rating() + "\n"
            index = index + 1

        return report;

########## Main Program ##########

#Cinema Variable
a_cinema = Cinema()

#Main Menu
main_menu = True
while main_menu:
    # Main Menu Options
    print("\n" "What would you like to do?")
    print("1) Add a new movie to the list")
    print("2) Veiw all movies on the list")
    print("3) Remove a movie from the list")
    print("4) Search for a movie by name")
    print("5) Search for a movie by rating")
    print("6) Search for a movie by length" "\n")
    
    """ 
        Main menu input
    """
    # Main menu input
    mainMenuInput = int(input("Choose: "))

    # Add new movie
    if mainMenuInput == 1:
        print ("\n" "Add new movie: " "\n")
        add_more_movies = True
        while(add_more_movies):
            nameInput = input("What is the name of the movie?" "\n")
            lengthInput = input("\n" "Enter the length of the movie" "\n")

            #Instance # 2nd object
            objMovie = Movie(nameInput, lengthInput)

            # Will check if the rating is correct
            add_movie_rating = True
            while add_movie_rating:
                ratingInput = input("\n" "Enter the rating of the movie" "\n")
                if objMovie.set_rating(ratingInput):
                    add_movie_rating = False
            
            # Adds movie to Cinema class
            a_cinema.add(objMovie)

            # Option to add more movies
            strAnswer = input("\n" "Do you want to enter more movies? (Y/n)" "\n")
            if (strAnswer == "n"):
                add_more_movies = False

    # Shows all movies in the Cinema class
    elif (mainMenuInput == 2):
        print("\n" "All movies in Cinema:" "\n")
        print(a_cinema.report())

    # Removes a movie from the Cinema class
    elif (mainMenuInput == 3):
        print ("\n" "Remove a movie" "\n")
        remove_movie = True
        while remove_movie:
            searchNameInput = input("What would you like to delete?" "\n")
            returnObject = a_cinema.get_movie_name(searchNameInput)

            if returnObject:
                print("Found: " + searchNameInput + "\n")
                repeat = True
                while repeat:
                    deleteValidate = input("Are you sure you want to delete " + searchNameInput + "? (Y/n)" "\n")
                    if deleteValidate == "Y":
                        repeat = False
                        a_cinema.remove(returnObject)
                        remove_movie = False
                    elif deleteValidate == "n":
                        break
                    else:
                        print("Invalid option please try again" "\n")
            else:
                print("\n" "Could not find " + searchNameInput + "\n")
        
    # Search for a movie buy name    
    elif (mainMenuInput == 4):
        #print ("***DEBUG*** Search Name")
        searchNameInput = True
        while searchNameInput:
            searchNameInput = input("What is the name of the movie you want to search for? " "\n")
            returnObject = a_cinema.get_movie_name(searchNameInput)

            if returnObject:
                print("\n" + str(returnObject))
                break
            else:
                print("\n" "Could not find '" + str(searchNameInput) + "' please try again" "\n")
                
    # Search for movie by rating
    elif (mainMenuInput == 5):
        #print ("***DEBUG*** Search Rating")
        search_rating = True
        while search_rating:
            SearchRatingInput = input("\n" "What is the rating of the movie you want to search for? " "\n")
            returnObject = a_cinema.get_movie_rating(SearchRatingInput)

            if returnObject:
                print(str(returnObject))
                print("")
                break
            else:
                print("\n" "Could not find any movies rated '" + str(SearchRatingInput) + "' please try again")
    # Search by length
    elif (mainMenuInput == 6):
        #print ("***DEBUG*** Search Length")
        search_length = True
        while search_length:
            searchLengthInput = int(input("\n" "What is the name of the movie you want to search for? " "\n"))
            returnObject = a_cinema.get_movie_length(searchLengthInput)

            if returnObject:
                print(str(returnObject))
                print("")
                break
            else:
                print("\n" "Could not find '" + str(searchLengthInput) + "' please try again")
    else:
        #print ("***DEBUG*** Invalid Option")
        print ("\n" "Please enter a valid option" "\n")