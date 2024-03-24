import course


class Planner:
    """" class to filter and store Course class object"""

    def __init__(self, prep):
        self.prep = prep
        self.fxd_courses = course.Course(code=None, title=None, sbu=None, startdate=None, enddate=None,
                                         required_courses=None, desired_courses=None, exams=None, examsq=None)
        self.var_courses = course.Course(code=None, title=None, sbu=None, startdate=None, enddate=None,
                                         required_courses=None, desired_courses=None, exams=None, examsq=None)
        self.course_selected = course.Course(code=None, title=None, sbu=None, startdate=None, enddate=None,
                                             required_courses=None, desired_courses=None, exams=None, examsq=None)
        self.crse = []

    def __compute_current_state(self):
        """
        Returns list of current fixed adn variable courses
        :return: string for this quartile
        """

        available_courses = course.available(self.prep.available_courses, self.prep.done_codes)
        done_codes = self.prep.done_codes
        available_req_stfd = course.available_required_satisfied(available_courses, done_codes)
        self.fxd_courses = course.fxd_crses(available_req_stfd)
        self.var_courses = course.var_crses(available_req_stfd)
        lst = [self.fxd_courses, self.var_courses]
        return lst

    def __choose_course(self, quartile: int):
        """
        Returns the course chosen for the input quartile
        :return:chosen course
        :param quartile: int that shows the quartile
        # no test as we are testing based on the given input and results in the assignment
        """

        if course.courses_in_quartile(self.fxd_courses, quartile):
            self.course_selected = self.fxd_courses
            if len(self.course_selected) > 1:
                self.course_selected = course.dsrd_prior_knwledge(self.course_selected, self.prep.done_codes)
                if len(self.course_selected) > 1:
                    rqrd_cds = course.req_codes(self.course_selected, self.prep.done_codes)
                    self.course_selected = course.future_crses(self.course_selected, rqrd_cds)
                    if len(self.course_selected) > 1:
                        dsrd_cds = course.dsrd_codes(self.course_selected, self.prep.done_codes)
                        self.course_selected = course.future_crses(self.course_selected, dsrd_cds)
                        if len(self.course_selected) > 1:
                            self.course_selected = self.course_selected
                            return self.course_selected
                        else:
                            return self.course_selected
                    else:
                        return self.course_selected
                else:
                    return self.course_selected
            else:
                return self.course_selected

        self.course_selected = self.var_courses
        if len(self.course_selected) > 1:
            self.course_selected = course.dsrd_prior_knwledge(self.course_selected, self.prep.done_codes)
            if len(self.course_selected) > 1:
                self.var_courses = course.exams_in_quartile(self.course_selected, quartile)
                if len(self.course_selected) > 1:
                    self.course_selected = self.course_selected[0]
                    return self.course_selected
                else:
                    return self.course_selected
            else:
                return self.course_selected
        else:
            self.course_selected = None
            return self.course_selected

    def __generate_for_quartile(self, quartile):
        """
        Generates String with the details for the chosen course in the selected quarter
       :param quartile: int that shows the quartile
       :return: string for this quartile
       """
        self.__compute_current_state()
        self.crse = 'kwartiel {0} \n voorkennis: {1} \n Te volgen cursus: \n'.format(quartile, self.prep.done_codes)
        self.__choose_course(quartile)
        # in case a list is provided, take 1st course element of list, otherwise take course item
        if self.course_selected:
            if isinstance(self.course_selected, list):
                cde = self.course_selected[0].code
                self.crse += self.course_selected[0].__str__()
            else:
                cde = self.course_selected.code
                self.crse += self.course_selected.__str__()
            self.prep.done_codes.add(cde)
        else:
            self.crse += 'geen geschikte cursus in dit kwartiel\n'

        return self.crse

    def generate(self):
        """
        Generate a string output for all quarters with the selected courses and details
        :return: string showing the planning
        """
        course_list = []
        for quartile in range(1, 5):
            self.__generate_for_quartile(quartile)
            print(self.crse + '\n')

    def __print_courselist(self, courselist):
        """
        Help function to print courselists
        :param: courselist
        """
        text = ''
        for c in courselist:
            text += c.code + " - "
        print(text)
