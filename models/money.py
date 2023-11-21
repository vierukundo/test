from models.base_model import BaseModel


class Money(BaseModel):
    """Representation of money"""
    financing_options = relationship
    blog = None