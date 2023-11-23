#!/usr/bin/python3
"""
 Test some classes
"""
import requests
from models.manpower import Manpower
from models.base_model import BaseModel
from models.material import Material
from models.machinery import Machinery
from models.location import Location

"""
 Objects creations
"""

url = 'https://th.bing.com/th/id/R.55330b22d86fdf3138d4b053565fead2?rik=37RCtoxfuW47DA&pid=ImgRaw&r=0'
res = requests.get(url)
profile = res.content if res.ok else None
manpower_dict = {
        "first_name": "Olivier", "last_name": "RUKUNDO",
        "sex": "Male", "experience": "5 years",
        "service": "Architect", "profile": None,
        "email": "vierukundo20@gmail.com", "contacts": "+250783464572"
        }
manpower = Manpower(**manpower_dict)
# print("New manpower: {}".format(manpower))
manpower.save()

"""
 Verification
"""
print("")
all_manpower = storage.all(Manpower)
for manpower_id, manpower in all_manpower.items():
    print(manpower)
    # for city in state.cities:
        # print("Find the city {} in the state {}".format(city, state))

