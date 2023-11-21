from models.base_model import BaseModel


class Machinery(BaseModel):
    """A representation of construction machinery"""
    name = ""
    picture = None
    rent = False
    price = None
    application = ""
    tutorial_video = None