import csv;
import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

SQLITE_CONNECTION_STRING = 'sqlite:///adress_person.db'

FIELD_LENGTH = 250


def str2bool(v):
    return v.lower() in ("ja")


Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, nullable=False)
    vorname = Column(String(FIELD_LENGTH), nullable=False)
    nachname = Column(String(FIELD_LENGTH), nullable=False)
    geburtsdatum = Column(Date(), nullable=True)
    telefon = Column(String(FIELD_LENGTH), nullable=True)
    email = Column(String(FIELD_LENGTH), nullable=True)
    newsletter = Column(Boolean(), nullable=True)


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(FIELD_LENGTH))
    street_number = Column(String(FIELD_LENGTH))
    post_code = Column(String(FIELD_LENGTH), nullable=False)
    city = Column(String(FIELD_LENGTH))
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)


engine = create_engine(SQLITE_CONNECTION_STRING)

Base.metadata.create_all(engine)


def read_and_insert():
    global person, address, address
    filename = "../../../challenge/Testdaten_1.csv"
    csvReader = csv.DictReader(open(filename, newline=''), skipinitialspace=True, delimiter=';', quotechar='|')
    for row in csvReader:
        row = {x.strip(): y for x, y in row.items()}
        row = dict(zip(row.keys(), [v.strip() if isinstance(v,str) else v for v in row.values()]))
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

        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        # Insert a Person in the person table
        session.add(person)
        session.commit()

        # Insert an Address in the address table
        session.add(address)
        session.commit()

read_and_insert()

DBSession = sessionmaker(bind=engine)
session = DBSession()
print(session.query(Person).all())

person = session.query(Person).first()
print(person.vorname)

session.query(Address).filter(Address.person == person).all()

session.query(Address).filter(Address.person == person).one()
address = session.query(Address).filter(Address.person == person).one()
print(address.post_code)
