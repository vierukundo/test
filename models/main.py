#!/usr/bin/python3
"""
 Test some classes
"""
from models import storage
from models.opportunity import Opportunity
from models.requirement import Requirement
from models.location import Location
from models.manpower import Manpower
from models.material import Material
from models.machinery import Machinery

"""
 Objects creations
"""
manpower = Manpower(name="California")
print("New manpower: {}".format(manpower))
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

