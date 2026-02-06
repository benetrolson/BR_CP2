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
    while True:
        filters = []
        check = input("Choose filters to apply (enter numbers separated by commas, e.g., 1,3: \n1. Genre \n2. Director \n3. Actor \n4. Length (min/max) \n")
        if "1" in check:
            filters.append("Genre")
        if "2" in check:
            filters.append("Director")
        if "3" in check:
            filters.append("Notable Actors")
        if "4" in check:
            filters.append("Length")
        if not filters:
            continue


#show all the movies
def show(movies):

#Make the code attempt to open the csv and remember it
try:
    with open("individual_projects\movie_list.csv", mode = "r") as list_of_movies:
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
                    header[4]: line[4],
                    header[5]: line[5]
                }
            )
except:
    print("Can't find CSV. ")
else:
    main(movies)
