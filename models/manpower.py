from models.base_model import BaseModel


class Manpower(BaseModel):
    """Representation of a manpower"""
    first_name = ""
    last_name = ""
    sex = ""
    experience = None
    service = ""
    profile = None
    email = ""
    contacts = None