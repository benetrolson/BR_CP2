#BR 2nd reading files
import csv

try:
    with open("notes\\sample.txt", "r") as file:
        contents = []
        for line in file:
            contents.append(line.strip())
except:
    print("Can't find that file. ")
else:
    for line in contents:
        print(f"Hello {line}. ")

try:
    with open("notes\\sample.csv", mode = "r") as sample:
        reader = csv.reader(sample)
        header = next(reader)
        users = []
        for line in reader:
            users.append(
                {
                    header[0]: line[0],
                    header[1]: line[1]
                }
            )
except:
    print("Can't find CSV. ")
else:
    for user in users:
        print(user)
