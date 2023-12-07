from app.models.manpower import Manpower
from app.models.base_model import BaseModel, Base
from app.models.material import Material
from app.models.machinery import Machinery
from app.models.location import Location
from app.models.opportunity import Opportunity
from app.models.requirement import Requirement
from app.models.money import Money
from app.models.management import Management
from app.models.education import Education
from app.models.finance_option import FinanceOption
from app.models.gantt_chart import GanttChart
from app.models.user import User
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
        self.__engine = create_engine('mysql+mysqldb://rukundo:password@localhost/db_portifolio')

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

    def check_user(self, cls, username):
        "Checks if the user exists before login"
        obj = self.__session.query(cls).filter_by(username=username).first()
        return obj

    def load_user_by_id(self, cls, id):
        """Loads user by id"""
        user = self.__session.query(cls).filter_by(id=id).first()
        return user

    def load_user_by_email(self, cls, email):
        """Loads user by email"""
        user = self.__session.query(cls).filter_by(email=email).first()
        return user

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
