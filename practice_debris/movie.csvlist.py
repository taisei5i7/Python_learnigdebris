import csv

list1 = ["Top Gun","Risky Business","Minority Report"]
list2 = ["Titanic","The Revenant","Inception"]
list3 = ["Training Day","Man on Fire","Flight"]

with open("movie.csv","w",newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(list1)
    w.writerow(list2)
    w.writerow(list3)

#answer
#movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
#with open("movies.csv", "w") as csvfile:
   # spamwriter = csv.writer(csvfile, delimiter=",")
   # for movie_list in movies:
        #spamwriter.writerow(movie_list)
