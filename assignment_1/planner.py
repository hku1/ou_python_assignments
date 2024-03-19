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

    def compute_current_state(self):

        cursus_nog_niet_gedaan = self.bepaal_cursus_nog_niet_gedaan()

        cursus_vereiste_voorkennis = self.bepaal_cursus_vereiste_voorkennis()

        cursus_gewenste_voorkennis = self.bepaal_cursus_gewenste_voorkennis()

        cursus_die_gedaan_kan_worden = self.bepaal_cursus_die_gedaan_kan_worden()

        cursus_vast_die_gedaan_kan_worden = self.bepaal_cursus_vast_die_gedaan_kan_worden()

        cursus_variabel_die_gedaan_kan_worden = self.bepaal_cursus_variabel_die_gedaan_kan_worden()


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

        result = ''
        for i in range(1, 5):
            self.make_string(self.choose_course(i))
        return result


    # TODO: implement

    def generate(self):
        """
        :return: string showing the planning
        """
        self.generate_for_quartile(1)

    # Check below for errors.
    # Check for comparison of done_codes and available_courses

    def bepaal_cursus_nog_niet_gedaan(self) -> list[course]:
        """Gives the courses which are not done yet
            return: list of courses not done yet
        """
        return_list = list(set(self.preparation.available_courses) - set(self.preparation.done_codes))
        return return_list

    def bepaal_cursus_vereiste_voorkennis(self) -> list[course]:
        """Gives the mandatory courses which are needed as "voorkennis
            return: list of mandatory "Voorkennis"" courses
        """
        return_list = []
        for temp_course in self.bepaal_cursus_nog_niet_gedaan():
            return_list.append(temp_course.get_vereiste_voorkennis())
        return return_list

    def bepaal_cursus_gewenste_voorkennis(self) -> list[course]:
        """Gives the requested courses which are needed as "voorkennis"
            return: list of "Gewenste voorkennis courses"
        """
        return_list = []
        for temp_course in self.bepaal_cursus_nog_niet_gedaan():
            return_list.append(temp_course.get_gewenste_voorkennis())
        return return_list

    def bepaal_cursus_die_gedaan_kan_worden(self) -> list[course]:
        """Gives the courses which can be done
            return: list of courses that could be done
        """
        return_list = []
        for temp_course in self.bepaal_cursus_nog_niet_gedaan():
            if set(temp_course.get_vereiste_voorkennis()).issubset(self.preparation.done_codes):
                return_list.append(temp_course.get_vereiste_voorkennis())
        return return_list

    def bepaal_cursus_vast_die_gedaan_kan_worden(self) -> list[course]:
        """Gives the fixed courses which can be done
            return: list of fixed courses that could be done
        """
        return_list = []
        for temp_course in self.bepaal_cursus_die_gedaan_kan_worden():
            if not temp_course.dates.nodates():
                return_list = return_list.append(course)
        return return_list

    def bepaal_cursus_variabel_die_gedaan_kan_worden(self) -> list[course]:
        """Gives the variable courses which can be done
            return: list of variable courses that could be done
        """
        return_list = []
        for temp_course in self.bepaal_cursus_die_gedaan_kan_worden():
            if temp_course.dates.nodates():
                return_list = return_list.append(course)
        return return_list

    def bepaal_cursus_in_quartaal(self,quarter) -> list[course]:
        """Gives the courses with exams in this quarter
                :param quartile: int that shows the quartile
                :return: list of courses for this quartile
        """
        return_list = []
        for temp_course in self.bepaal_cursus_die_gedaan_kan_worden():
            if temp_course.datesdates.quartile():
                return_list = return_list.append(course)
        return return_list


    def make_string(self,course:course):
        verplichte_voorkennis = []
        gewenste_voorkennis = []

        # get vereiset voorkennis
        if not course.get_vereiste_voorkennis():
            verplichte_voorkennis = 'geen verplichte voorkennis'
        else:
            verplichte_voorkennis = 'verplichte voorkennis: ' + str(course.get_vereiste_voorkennis())

        # get gewenste voorkennis
        if not course.get_gewenste_voorkennis():
            gewenste_voorkennis += 'geen gewenste voorkennis'
        else:
            gewenste_voorkennis += 'gewenset voorkennis: ' + str(course.get_gewenste_voorkennis())

        text = 'Kwartiel: ' + str(course.dates.quartile()) + ' \n' + \
        'voorkennis: ' + self.preparation.done_codes + ' \n' + \
        'Te volgen cursus: ' + course.code  + ', ' + course.title + ' \n' + \
        verplichte_voorkennis + ' \n' + \
        str(gewenste_voorkennis)

        return text