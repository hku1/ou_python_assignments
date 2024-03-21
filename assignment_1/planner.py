import course

class Planner:
    """" class to filter and store Course class object"""

    def __init__(self, prep):
        self.prep = prep
        self.fxd_courses = []
        self.var_courses = []
        self.course_selected = []

    # TODO: implement

    def compute_current_state(self):
        available_courses = course.available(self.prep.available_courses, self.prep.done_codes)
        done_codes = self.prep.done_codes
        available_req_stfd = course.available_required_satisfied(available_courses, done_codes)
        self.fxd_courses = course.fxd_crses(available_req_stfd)
        self.var_courses = course.var_crses(available_req_stfd)
        lst = [self.fxd_courses, self.var_courses]
        return lst

    # TODO: implement

    def choose_course(self, quartile: int):
        """
        :param quartile: int that shows the quartile
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
                            self.course_selected = self.course_selected[0]
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


    # TODO: implement

    def _generate_for_quartile(self, quartile):
        """
       :param quartile: int that shows the quartile
       :return: string for this quartile
       """
        self.compute_current_state()
        course1 = 'kwartiel {0} \n voorkennis: {1} \n Te volgen cursus: \n'.format(quartile, self.prep.done_codes)
        chosen_course = self.choose_course(quartile)
        course1 = course1 + str(chosen_course)
        print(course1)



    # TODO: implement

    def generate(self):
        """
        :return: string showing the planning
        """
        for quartile in range(1,5):
            self._generate_for_quartile(quartile)
