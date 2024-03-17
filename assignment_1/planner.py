import course


class Planner:
    # TODO: implement and add attributes

    cursus_nog_niet_gedaan = []
    cursus_vereiste_voorkennis = []
    cursus_gewenste_voorkennis = []
    cursus_die_gedaan_kan_worden = []
    cursus_vast_die_gedaan_kan_worden = []
    cursus_variabel_die_gedaan_kan_worden = []


    def __init__(self, preparation):
        self.preparation = preparation

    # TODO: implement

    def compute_current_state(self):

        cursus_nog_niet_gedaan = self.bepaal_cursus_nog_niet_gedaan()

        cursus_vereiste_voorkennis = self.bepaal_cursus_vereiste_voorkennis()

        cursus_gewenste_voorkennis = self.bepaal_cursus_gewenste_voorkennis()

        cursus_die_gedaan_kan_worden = self.bepaal_cursus_die_gedaan_kan_worden()

        cursus_vast_die_gedaan_kan_worden = self.bepaal_cursus_vast_die_gedaan_kan_worden()

        cursus_variabel_die_gedaan_kan_worden = self.bepaal_cursus_variabel_die_gedaan_kan_worden()

    # TODO: implement

    def choose_course(self, quartile):
        """
        :param quartile: int that shows the quartile
        """

    # TODO: implement

    def generate_for_quartile(self, quartile):
        """
       :param quartile: int that shows the quartile
       :return: string for this quartile
       """

    # TODO: implement

    def generate(self):
        """
        :return: string showing the planning
        """
        self.generate_for_quartile(1)

# Check below for errors.
# Check for comparison of done_codes and available_courses

    def bepaal_cursus_nog_niet_gedaan(self)->list[course]:
        """Gives the courses which are not done yet"""
        return_list = list(set(self.preparation.available_courses) - set(self.preparation.done_codes))
        return return_list

    def bepaal_cursus_vereiste_voorkennis(self)->list[course]:
        """Gives the mandatory courses which are needed as "voorkennis" """
        return_list =[]
        for course in self.bepaal_cursus_nog_niet_gedaan():
            return_list.append(course.get_vereiste_voorkennis())
        return return_list

    def bepaal_cursus_gewenste_voorkennis(self)->list[course]:
        """Gives the requested courses which are needed as "voorkennis" """
        return_list = []
        for course in self.bepaal_cursus_nog_niet_gedaan():
            return_list.append(course.get_gewenste_voorkennis())
        return return_list

    def bepaal_cursus_die_gedaan_kan_worden(self)->list[course]:
        """Gives the courses which can be done"""
        None

    def bepaal_cursus_vast_die_gedaan_kan_worden(self)->list[course]:
        """Gives the fixed courses which can be done"""
        None

    def bepaal_cursus_variabel_die_gedaan_kan_worden(self)->list[course]:
        """Gives the variable courses which can be done"""
        None