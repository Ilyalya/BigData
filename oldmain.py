def prepare_data(fetched_info):
    fetched_info = fetched_info.lstrip()
    fetched_info = fetched_info.rstrip()
    fetched_info = fetched_info.replace("\n", "")
    norm_info = fetched_info.replace("  ", "")

    norm_info = norm_info.lstrip()
    norm_info = norm_info.rstrip()
    return norm_info


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from bs4 import BeautifulSoup
    import requests

    lists = []  # список интересных статей
    interesting_items = []  # список конкретного элемента
    n = 100
    # n = int(input(print("Введите количество страниц:")))  # это строковое значение

    counter = 0
    for j in range(n):
        url = f"https://qna.habr.com/questions/latest?page={j+1}"
        page = requests.get(url)
        # print(page.status_code)

        soup = BeautifulSoup(page.text, "html.parser")
        #print soup

        # с помощью findAll перечислим все необходимые нам элементы, сохраняя нужный нам тэг с классом
        lists = soup.findAll('li', class_='content-list__item') #в lists хранятся основные вопросы (их ≈20), а также самые популярные (справа расположенные и они не помечаются тэгами языков программирования или технологий

        for i in range(len(lists)):
            if lists[i].find('div', class_='question__content') is not None:
                buf0 = lists[i].findAll('div', class_='question__content')[0].findAll('div', class_='question__content_fluid')[0]
                buf1 = prepare_data(buf0.findAll('div', class_='question__tags')[0].findAll('ul', class_='tags-list tags-list_short')[0].text)
                buf2 = prepare_data(buf0.findAll('h2', class_='question__title')[0].text)
                interesting_items.append([str(counter+1), buf1, buf2])
                counter += 1

        # for i in range(len(interesting_items)):
            # print(interesting_items[i][0] + '. [' + interesting_items[i][1] + '] ' + interesting_items[i][2])
        # вот это говно сверху нужно максимум для отладки, но точно чтобы не в консоль оно высералось

        # ВЫБИРАЕМ ПАПКУ СОХРАНЕНИЕ ЧЕРЕЗ ДИСПЕТЧЕР ФАЙЛОВ
    import csv
    from tkinter import filedialog
    from tkinter import *
    root = Tk()
    # так можно открывать расположение файлов: myFileName = filedialog.askopenfilename(initialdir="/", title="Se", filetypes=[["av", "*.csv"], ["a", "*.xlsx"]])
    #myPathName = filedialog.askdirectory(initialdir="/", title="Select directory")
    f = filedialog.asksaveasfile(initialdir="/", title="Сохраните файл")
    start_check = f.name.rfind('/')
    if start_check == -1:
        start_check = 0
    f_name = f.name
    import re
    regexp = r'\w.csv$'
    m = re.search(regexp, f_name)
    if m is None:
        f_name += '.csv'
    if f is not None:
        with open(f_name, 'w', encoding='utf-8') as file: #придётся дописывать этот костыль, чтобы ему удавалось сохранять информацию в utf-8 (этот метод хорош тем, что стирает старую информацию (передвигая указатель на начало))
            columns = ["number", "category", "question"]
            writer = csv.DictWriter(file, fieldnames=columns, delimiter="\t")
            writer.writeheader()
            writer = csv.writer(file, delimiter="\t")
            writer.writerows(interesting_items)
