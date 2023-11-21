from models.base_model import BaseModel


class Material(BaseModel):
    """A representation of construction material"""
    name = ""
    picture = None
    rent = False
    price = None
    application = ""
    tutorial_video = None