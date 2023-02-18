import parse_csv as parse

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #authors = parse.load_csv_file()
    #parse.parse_authors(authors, "Ouangraoua")
    base_network = parse.process_files()
    graph = parse.build_network(base_network)
    parse.plot_network(graph)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
