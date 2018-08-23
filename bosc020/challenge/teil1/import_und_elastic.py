import csv;
import datetime
import json
from pprint import pprint

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

INDEX_NAME = "test2"


def str2bool(v):
    return v.lower() in ("ja", "yes", "jaaaaaaa")


class Person():
    id = 0
    searchField = ""
    nachname = ""
    geburtsdatum = ""
    telefon = ""
    email = ""
    newsletter = ""

    def __repr__(self) -> str:
        return self.vorname + " - " + self.nachname


class Address():
    id = 0
    street_name = ""
    street_number = ""
    post_code = ""
    city = ""
    person_id = ""
    person = ""


def jsonDefault(OrderedDict):
    if isinstance(OrderedDict, datetime.date):
        return dict(year=OrderedDict.year, month=OrderedDict.month, day=OrderedDict.day)
    else:
        return OrderedDict.__dict__


es = Elasticsearch()


# es.delete(INDEX_NAME, "address", 44)
# es.create(INDEX_NAME, "address", 44, body={"any": "data", "timestamp": datetime.datetime.now()})

def read_and_insert():
    global person, address
    filename = "../../../challenge/Testdaten_1.csv"
    csvReader = csv.DictReader(open(filename, newline=''), skipinitialspace=True, delimiter=';', quotechar='|')
    for row in csvReader:
        row = {x.strip(): y for x, y in row.items()}
        row = dict(zip(row.keys(), [v.strip() if isinstance(v, str) else v for v in row.values()]))
        print(row)
        person = Person()
        person.vorname = row["Vorname"]
        person.nachname = row["Nachname"]
        person.geburtsdatum = datetime.datetime.strptime(row["Geburtsdatum"].strip(), "%d.%m.%Y").date()
        person.id = row["Nr."]
        person.email = row["E-Mail"]
        person.telefon = row["Telefon"]
        person.newsletter = str2bool(row["Newsletter"])

        strasse = row["Straße"].split(" ")[0]
        str_number = row["Straße"].split(" ")[len(row["Straße"].split(" ")) - 1]

        address = Address()
        address.street_name = strasse
        address.street_number = str_number
        address.post_code = row["PLZ"].strip()
        address.city = row["Stadt"].strip()
        address.id = person.id
        address.person = person

        data = json.dumps(address, default=jsonDefault, indent=4)
        pprint(data)
        es.index(index=INDEX_NAME, doc_type='address', id=address.id, body=data)


#read_and_insert()

searchName = "Bern";
searchField = 'person.vorname'
search = Search(using=es, index=INDEX_NAME ).query("match", **{searchField: {"query": searchName, "fuzziness": "AUTO"}})

response = search.execute()

for hit in response:
    print(hit.meta.score, hit.person.vorname, hit.person.nachname, hit.city, hit.post_code)