import csv

notes = []


def pridat_radek(notes):
    notes.append(input("vloz poznamku: \n"))


def vypsat(notes):
    print(notes)


def smazat(notes):
    print(notes)
    radek_ke_smazani = int(input("zadejte poradi radku ktery se ma smazat: ")) - 1
    radky = notes.splitlines()
    radky.pop(radek_ke_smazani)


def upravit(notes):
    vypsat(notes)
    poradi = int(input("zadejte poradi radku: ")) - 1
    if 1 <= poradi <= len(notes):
        novy_zapis = input("zadejte novy zapis do radku: ")
        notes[poradi] = novy_zapis


def ulozit(notes):
    file = input("zadejte nazev souboru csv: ")
    file_csv = file + ".csv"
    with open(file_csv, 'a') as work_file:
        writer = csv.writer(work_file)
        for line in notes:
            writer.writerow([line])


def nacist(notes):
    file_csv = input("zadejte nazev souboru k nacteni (s koncovkou .csv): ")
    with open(file_csv, 'r') as file_k_nacteni:
        reader = csv.reader(file_k_nacteni)
        for line in reader:
            notes.append(line)
        print(notes)


def zacit_zapis():
    while True:
        print("pridat, vypsat, smazat, upravit, ulozit, nacist, nebo ukoncit?")

        operace = input("zadejte operaci k provedeni: ")

        if operace == "pridat":
            pridat_radek(notes)
        elif operace == "vypsat":
            vypsat(notes)
        elif operace == "smazat":
            smazat(notes)
        elif operace == "upravit":
            upravit(notes)
        elif operace == "ulozit":
            ulozit(notes)
        elif operace == "nacist":
            nacist(notes)
        elif operace == "ukoncit":
            break
        else:
            print("spatne zadana operace")


zacit_zapis()
