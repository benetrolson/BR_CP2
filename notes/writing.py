#BR 2nd writing files
"""with open("notes\\sample.txt", "a") as file:
    file.write("Joe\n")
    file.write("Israel\n")
    file.write("Zee\n")

print("Run finished. ")"""
"""content = []
with open("notes\\sample.txt", "r+") as file:
    for line in file:
        content.append(line.strip())
    file.truncate(0)
    for name in content:
        file.write(name + "\n")

print("Code ends")"""

import csv
"""with open("notes\\test.csv", "w", newline = "") as csvfile:
    fieldnames = ["username", "favorite color"]
    writer = csv.writer(csvfile)
    #writer.writerow(fieldnames)
    writer.writerow(["user1", "indigo"])
    writer.writerow(["tech_wizard", "turquoise"])"""
users = [{"username": "user1", "favorite color": "red"}, {"username": "user2", "favorite color": "orange"}]
with open("notes\\test.csv", "r+", newline = "") as csvfile:
    fieldnames = ["username", "favorite color"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writerows(users)
