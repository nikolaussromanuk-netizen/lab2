import csv
import xml.dom.minidom as minidom

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

def gen_link(books_csv):
    books_csv.seek(0)
    with open("result.txt", 'a') as links:

        reader = csv.DictReader(books_csv, delimiter=';', quotechar='"')
        flag = 1
        for line in reader:
            if flag > 20:
                break
            links.write(f"{flag}. {line['Автор']}. {line['Название']}"
                        f" - {line['Дата поступления']}\n")
            flag += 1

def read_xml():
    with open('currency.xml', 'r', encoding='cp1251') as xml_file:
        xml_data = xml_file.read()
        dom = minidom.parseString(xml_data)
        dom.normalize()
        valutes = dom.getElementsByTagName('Valute')

        num_code = []
        char_code = []

        for valute in valutes:
            num_node = valute.getElementsByTagName('NumCode')[0]
            char_node = valute.getElementsByTagName('CharCode')[0]

            num = num_node.firstChild.nodeValue
            char = char_node.firstChild.nodeValue

            num_code.append(int(num))
            char_code.append(char)

    print(num_code)
    print(char_code)

def find_all_tags(books_csv):
    books_csv.seek(0)
    reader = csv.DictReader(books_csv, delimiter=';', quotechar='"')
    tags = set()
    for line in reader:
        tag_list = line['Жанр книги'].split('#')
        for tag in tag_list:
            tags.add(tag.strip())
    print(tags)

def find_populars(books_csv):
    books_csv.seek(0)
    reader = csv.DictReader(books_csv, delimiter=';', quotechar='"')
    names = [[line['Название'], int(line['Кол-во выдач'])] for line in reader]
    sorted_names = sorted(names, key=lambda x: x[1])[::-1]

    used = set()
    count = 0
    i = 0
    while count < 20:
        if not sorted_names[i][0] in used:
            count += 1
            used.add(sorted_names[i][0])
            print(sorted_names[i][0])
        i += 1

if __name__ == "__main__":
    with open("books.csv", 'r', encoding='cp1251') as books_csv:
        # 1 задание - считает кол-во имен длинее 30
        #count_big_number(books_csv)
        # 2 задание - поиск книги по автору
        #find_name('Людмила Петрановская', books_csv)
        # 3 задание - генерация библиотечных ссылок
        gen_link(books_csv)
        # 5 задание Вывести перечень всех тегов без повторений
        #find_all_tags(books_csv)
        # 6 задание: 20 самый популярных книг
        #find_populars(books_csv)
        pass

    #Задание 4 - прочитать и распарсить xml
    #read_xml()
