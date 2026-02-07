#BR 2nd movie recommender
import csv

#create the main function
def main(movies):
    while True:
        check = input("Would you like to: \n1. Search / Get Recommendations \n2. Print Full Movie List \n3. Exit \n").strip()
        if check == "1":
            search(movies)
        elif check == "2":
            show(movies)
        elif check == "3":
            break
        else:
            print("You failed. That was an invalid input. Please try again. ")

#search for all the movies
def search(movies):
    def filter_function(key, name, recommendations):
        return [
            movie for movie in recommendations
            if name in movie[key].lower()
        ]
    while True:
        recommendations = movies.copy()
        check = input("Choose filters to apply (enter numbers separated by commas, e.g., 1,3: \n1. Genre \n2. Director \n3. Actor \n4. Length (min/max) \n5. Quit\n")
        if "5" in check:
            break
        if "1" in check:
            genre = input("What genre do you want to choose? (Please use a one word answer)").lower()
            recommendations = filter_function("Genre", genre, recommendations)
        if "2" in check:
            director = input("Which director do you want to choose? ").lower()
            recommendations = filter_function("Director", director, recommendations)
        if "3" in check:
            actor = input("What is a notable actor you want to see in the movie? ").lower()
            recommendations = filter_function("Notable Actors", actor, recommendations)
        if "4" in check:
            while True:
                min_length = input("What is the minimum length of the movie? (In minutes) ")
                max_length = input("What is the maximum length of the movie? (In minutes) ")
                if min_length.isdigit() and max_length.isdigit():
                    min_length, max_length = int(min_length), int(max_length)
                    if min_length < max_length:
                        break
                    print("Those numbers are not possible, as the min is longer or equal to the max. ")
                    continue
                print("Those were not numbers. Please try again. ")
            recommendations = [
                movie for movie in recommendations
                if min_length <= movie["Length (min)"] <= max_length
            ]
        if recommendations == movies or check.strip() == "":
            print("You chose nothing. Could you please try again? ")
            continue
        if recommendations:
            print("Here are the possibilities: ")
            for movie in recommendations:
                for i in movie.keys():
                    print(f"{i}: {movie[i]}")
            break
        else:
            print("There are no possible results for this search. ")


#show all the movies
def show(movies):
    for movie in movies:
        for i in movie.keys():
            print(f"{i}: {movie[i]}")

#Make the code attempt to open the csv and remember it
try:
    with open("individual_projects\\movie_list.csv", mode = "r") as list_of_movies:
        reader = csv.reader(list_of_movies)
        header = next(reader)
        movies = []
        for line in reader:
            movies.append(
                {
                    header[0]: line[0],
                    header[1]: line[1],
                    header[2]: line[2],
                    header[3]: line[3],
                    header[4]: int(line[4]),
                    header[5]: line[5]
                }
            )
except:
    print("Can't find CSV. ")
else:
    main(movies)
