import csv

movies = [["トップガン","リスキービジネス","マイノリティー　レポート"],["タイタニック","レベナント","インセプション"],["トレーニングデイ","マン　オン　ファイア","フライト"]]
with open("ムービー as answer.csv", "w",encoding="utf-8") as csvfile:
   spamwriter = csv.writer(csvfile, delimiter=",")
   for movie_list in movies:
        spamwriter.writerow(movie_list)
