from app.models.base_model import BaseModel


class Management(BaseModel):
    """Representation of a management"""
    project_name = ""
    start_date = ""
    end_date = ""
    # gantt_chart = relationship
