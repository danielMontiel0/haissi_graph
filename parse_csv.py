import pandas as pd
from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt

base_path_data = "./data/"
author_dic = {"Ouangraoua A": "csv-AdaOuangra-set.csv",
              "Ghalei": "csv-HomaGhalei-set.csv",
              "Moore C": "csv-ClaireMoor-set.csv",
              "Léger-Abraham": "csv-MelissaLeg-set.csv",
              "Charette": "csv-MichaelCha-set.csv",
              "Majumder": "csv-MousumiMaj-set.csv",
              "Unrau": "csv-PeterUnrau-set.csv",
              "Ansari": "csv-AtharAnsar-set.csv",
              "MacMillan": "csv-AndrewMacM-set.csv",
              "Kashlev": "csv-MikhailKas-set.csv",
              "Li Y": "csv-YingfuLi-set.csv",
              "Renwick": "csv-NeilRenwic-set.csv",
              "Perreault": "csv-JonathanPe-set.csv",
              "Jaramillo": "csv-MaritzaJar-set.csv",
              "Roussel": "csv-MarcRousse-set.csv",
              "Thakor": "csv-NehalThako-set.csv",
              "Zovoilis": "csv-Athanasios-set.csv",
              "Patel": "csv-TrusharPat-set.csv",
              "Strong": "csv-MichaelStr-set.csv",
              "Joyce": "csv-PaulJoyce-set.csv",
              "Zerges": "csv-WilliamZer-set.csv",
              "Gatignol": "csv-AnneGatign-set.csv",
              "Cousineau": "csv-BenoitCous-set.csv",
              "Gallouzi": "csv-ImedGallou-set.csv",
              "Sonenberg": "csv-NahumSonen-set.csv",
              "Duchaine": "csv-ThomasDuch-set.csv",
              "Major": "csv-FranoisMaj-set.csv",
              "Desgroseillers": "csv-LucDesgros-set.csv",
              "Chartrand": "csv-PascalChar-set.csv",
              "Legault": "csv-PascaleLeg-set.csv",
              "Autexier": "csv-ChantalAut-set.csv",
              "Mouland": "csv-AndrewMoul-set.csv",
              "Sleiman": "csv-HanadiSlei-set.csv",
              "Waldispuhl": "csv-JrmeWaldis-set.csv",
              "Zenklusen": "csv-DanielZenk-set.csv",
              "Vande": "csv-ChristineV-set.csv",
              "Oeffinger": "csv-MarleneOef-set.csv",
              "Richard": "csv-StphaneRic-set.csv",
              "Fabian": "csv-MarcFabian-set.csv",
              "McKeague": "csv-MaureenMcK-set.csv",
              "Lecuyer": "csv-ricLecuyer-set.csv",
              "Sauvageau": "csv-MartinSauv-set.csv",
              "Cote": "csv-JocelynCt-set.csv",
              "Parent": "csv-LesliePare-set.csv",
              "Simard": "csv-MartinSima-set.csv",
              "Tremblay": "csv-Jacques-P.-set.csv",
              "Hussein": "csv-SamerHusse-set.csv",
              "Sephton": "csv-ChantelleS-set.csv",
              "Provost": "csv-PatrickPro-set.csv",
              "Huot": "csv-Marc-Etien-set.csv",
              "Bisaillon": "csv-MartinBisa-set.csv",
              "Jacques": "csv-Pierre-tie-set.csv",
              "Kakumani": "csv-PavanKakum-set.csv",
              "Petzold": "csv-KatjaPetzo-set.csv",
              "Bayfield": "csv-MarkBayfie-set.csv",
              "Blencowe": "csv-BenjaminBl-set.csv",
              "Cordes": "csv-SabineCord-set.csv",
              "Li B": "csv-BowenLi-set.csv",
              "Cui": "csv-HaissiCui-set.csv",
              "Rader": "csv-StephenRad-set.csv",
              "Jan": "csv-EricJan-set.csv",
              "Vu": "csv-LyVu-set.csv",
              "Blakney": "csv-AnnaBlakne-set.csv",
              "Kothe": "csv-UteKothe-set.csv",
              "Wieden": "csv-Hans-Joach-set.csv",
              "Elela": "csv-SherifAbou-set.csv",
              "Bachand": "csv-FranoisBac-set.csv",
              "Scott": "csv-MichelleSc-set.csv",
              "Chabot": "csv-BenoitChab-set.csv",
              "Perreault": "csv-Jean-Pierr-set.csv",
              "Masse": "csv-ricMass-set.csv",
              "Brosseau": "csv-Jean-Phili-set.csv",
              "Laurent": "csv-BenoitLaur-set.csv",
              "Lafontaine": "csv-DanielLafo-set.csv",
              "Bell": "csv-BrendanBel-set.csv",
              "Wellinger": "csv-RaymundWel-set.csv"
              }


def load_csv_file(csv_file):
    path_data = f"{base_path_data}{csv_file}"
    pd_author = pd.read_csv(path_data)
    #print(pd_author.loc[:, "Authors"])
    #return pd_author
    return pd_author.loc[:, "Authors"]


def parse_authors(publications, reference):
    collaborations = {}
    for publication in publications:
        for autor in publication.split(","):
            autor_name = autor.strip()
            for key in author_dic.keys():
                if key in autor_name:
                    if not(reference in autor_name):
                        if reference in collaborations:
                            collaborations[reference].append(key)
                        else:
                            collaborations[reference] = [key]

    #return collaborations
    if reference in collaborations:
        collaborations[reference] = dict(Counter(collaborations[reference]))
        return collaborations
    else:
        collaborations[reference] = {}
        return collaborations


def process_files():
    i = 0
    base_network = []
    for key, value in author_dic.items():
        authors = load_csv_file(value)
        base_network.append(parse_authors(authors, key))
        if i > 100:
            break
        i += 1
    print(base_network)
    return base_network


def build_network(base_network_array):
    G = nx.Graph()

    for author in base_network_array:
        for key, author2 in author.items():
            for collaborator, value in author2.items():
                print(key, collaborator, value)
                G.add_edge(key, collaborator, weight=value)
    return G


def plot_network(G):
    plt.figure(figsize=(10, 10))
    pos = nx.spring_layout(G, k=2, scale=2)
    edge_size = [0.5  for u, v in G.edges()]
    node_size = [G.degree(v)*30  for v in G]
    nx.draw_networkx(G, with_labels=True,
                     pos=pos,
                     width= edge_size,
                     node_size= node_size,
                     edge_color= "gray",
                     node_color= "darkgray",
                     font_color="red",
                     font_size= 8)
    plt.show()
