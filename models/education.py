from models.base_model import BaseModel


class Education(BaseModel):
    """A representation of Education"""
    institution_name = ""
    level_of_education = ""
    major = ""
    start_date = None
    end_date = None
    manpower_id = ""
    cv = None