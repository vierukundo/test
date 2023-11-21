from models.base_model import BaseModel


class Opportunity(BaseModel):
    """Representation of opportunity. It can be a job, internship, Trainings or Education"""
    title = ""
    employer = ""
    location = ""
    type = "Job"
    requirements = relationship
    remote = False