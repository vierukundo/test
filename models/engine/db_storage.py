from models.manpower import Manpower
from models.base_model import BaseModel, Base
from models.material import Material
from models.machinery import Machinery
from models.location import Location
from models.opportunity import Opportunity
from models.requirement import Requirement
from models.money import Money
from models.management import Management
from models.education import Education
from models.finance_option import FinanceOption
from models.gantt_chart import GanttChart
from urllib.parse import quote
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


classes = [
        GanttChart, FinanceOption, Education, Management, Requirement, Money, Opportunity,
        Location, Machinery, Material, BaseModel, Manpower
        ]
class DBStorage:
    """Represent database"""
    __engine = None
    __session = None
    def __init__(self):
        """Instantiate a DBStorage object"""
        db_password = 'Olivier@2001'
        encoded_password = quote(db_password)
        self.__engine = create_engine('mysql+mysqldb://rukundo:{}@localhost/5Ms'.format(encoded_password))

    def all(self, cls=None):
        """Query objects from the database"""
        objects = {}
        if cls is None:
            for cls in classes:
                query_result = self.__session.query(cls).all()
                for obj in query_result:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    objects[key] = obj
        else:
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and create a session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
