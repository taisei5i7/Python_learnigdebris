import csv

list1 = ["トップガン","リスキービジネス","マイノリティー　レポート"]
list2 = ["タイタニック","レベナント","インセプション"]
list3 = ["トレーニングデイ","マン　オン　ファイア","フライト"]

with open("ムービー.csv","w",encoding="utf-8") as f:
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
