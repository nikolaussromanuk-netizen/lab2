import csv

def count_big_number(books_csv):
    books_csv.seek(0)
    reader = csv.DictReader(books_csv, delimiter=';', quotechar='"')
    titles = [line["Название"] for line in reader]
    ans = 0
    for title in titles:
        if len(title) > 30:
            ans += 1
    print(ans)

if __name__ == "__main__":
    with open("books.csv", 'r', encoding='cp1251') as books_csv:
        # 1 задание - считает кол-во имен длинее 30
        count_big_number(books_csv)
