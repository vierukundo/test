from models.base_model import BaseModel


class Location(BaseModel):
    """Representation of Location"""
    country = ""
    city = ""
    state = ""
    address = ""
    material_id = ""
    machinery_id = ""
    opportunity_id = ""