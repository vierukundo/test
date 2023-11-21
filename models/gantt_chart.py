from models.base_model import BaseModel


class GanttChart(BaseModel):
    """Representation of Gantt Chart"""
    task_name = ""
    management_id = ""
    start_date = ""
    end_date = ""