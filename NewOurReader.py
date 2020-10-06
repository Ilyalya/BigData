


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from tkinter import filedialog
    f = filedialog.askopenfile()
    if f is not None:
        import csv
        reader = csv.DictReader(f, delimiter="\t")
        for rows in reader:
            print(rows["категория"] + '. [' + rows["номер"] + '] ' + rows["вопрос"])

    None

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
