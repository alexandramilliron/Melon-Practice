############
#  Part 1  #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, name, is_bestseller = False):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name



    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType("musk", 1998, "green", True, "muskmelon", True)
    casaba = MelonType("cas", 2003, "orange", False, "casaba")
    crenshaw = MelonType("cren", 1996, "green", False, "crenshaw")
    yellow_watermelon = MelonType("yw", 2013, "yellow", False, "yellow watermelon", True)

    muskmelon.add_pairing("mint")
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    crenshaw.add_pairing("proscuitto")
    yellow_watermelon.add_pairing("ice cream")

    all_melon_types.append(muskmelon)
    all_melon_types.append(casaba)
    all_melon_types.append(crenshaw)
    all_melon_types.append(yellow_watermelon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with ")
        for pairing in melon.pairings:
            print(f"- {pairing}")

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_dict = {}

    for melon in melon_types:
        melon_dict[melon.code] = melon

    return melon_dict



#melon_types = make_melon_types()
#print_pairing_info(melon_types)
#print(make_melon_type_lookup(melon_types))

############
#  Part 2  #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Needs __init__ and is_sellable methods

    def __init__(self, melon_type, shape_rating, color_rating, harvest_from, harvest_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_from = harvest_from
        self.harvest_by = harvest_by

#sold if shape and color > 5 && didn't come from field 3

    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.harvest_from != "Field 3":
            return True
        else:
            return False 


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 


melon_1 = Melon("yw", 8, 7, "Field 2", "Sheila")
print(melon_1.is_sellable())

