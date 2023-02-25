from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import func
from sqlalchemy import (
    Column, String, Integer, Float, DateTime, Boolean
)
import logging

logger = logging.getLogger("__main__")

Base = declarative_base()


class Offer(Base):

    __tablename__ = "offers"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    street = Column(String)
    city = Column(String)
    country_code = Column(String)
    address_text = Column(String)
    marker_icon = Column(String)
    workplace_type = Column(String)
    company_name = Column(String)
    company_url = Column(String)
    company_size = Column(String)
    experience_level = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    published_at = Column(DateTime(timezone=True), server_default=func.now())
    remote_interview = Column(Boolean)
    open_to_hire_ukrainians = Column(Boolean)
    display_offer = Column(Boolean)
    remote = Column(Boolean)
    way_of_apply = Column(String)
    type = Column(String)
    salary_from = Column(Float)
    salary_to = Column(Float)
    salary_currency = Column(String)
    name = Column(String)
    level = Column(Integer)

    def __init__(
            self, title, street, city, country_code,
            address_text, marker_icon, workplace_type, company_name,
            company_url, company_size, experience_level, latitude,
            longitude, published_at, remote_interview, open_to_hire_ukrainians,
            display_offer, way_of_apply, type, salary_from,
            salary_to, salary_currency, name, level):
        self.title = title
        self.street = street
        self.city = city
        self.country_code = country_code
        self.address_text = address_text
        self.marker_icon = marker_icon
        self.workplace_type = workplace_type
        self.company_name = company_name
        self.company_url = company_url
        self.company_size = company_size
        self.experience_level = experience_level
        self.latitude = latitude
        self.longitude = longitude
        self.published_at = published_at
        self.remote_interview = remote_interview
        self.open_to_hire_ukrainians = open_to_hire_ukrainians
        self.display_offer = display_offer
        self.way_of_apply = way_of_apply
        self.type = type
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_currency = salary_currency
        self.name = name
        self.level = level

# this should be an upsert but it is painfully slow
# so for the sake of simplicity I'm keeping
# bulk_insert_mappings as of now
# and truncating the table on every new run

# values = df.to_dict(orient="records")
# insert_stmt = postgresql.insert(Offer.__table__).values(values)
# ids = [x for x in list(Offer.__dict__.keys()) if not x.startswith("__")]
# update_stmt = insert_stmt.on_conflict_do_nothing(
#     index_elements=ids,
#     set_=dict(data=values)
# )
# session.execute(update_stmt)


class PostingsLoader:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        engine = create_engine(self.connection_string)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def load(self, df):
        try:
            self.session.bulk_insert_mappings(
                Offer, df.to_dict(orient="records"))
            self.session.commit()
            logger.info("Data successfully loaded to the database")
        except Exception as e:
            logger.error(f"Exception occured. Details: {e}")
            raise Exception
        finally:
            self.session.close()
