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


def find_name(name, books_csv):
    books_csv.seek(0)
    reader = csv.DictReader(books_csv, delimiter=';', quotechar='"')
    print(f"{name}: ")
    for line in reader:
        if float(line['Цена поступления']) < 200.0:
            continue
        if line['Автор'] == name or line['Автор (ФИО)'] == name:
            print(line['Название'])

if __name__ == "__main__":
    with open("books.csv", 'r', encoding='cp1251') as books_csv:
        # 1 задание - считает кол-во имен длинее 30
        count_big_number(books_csv)
        # 2 задание - поиск книги по автору
        find_name('Людмила Петрановская', books_csv)
