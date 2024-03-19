import course
import preparation


class Planner:
    """" class to filter and store Course class object"""

    def __init__(self, prep, varcrs, fxdcrs, reqprior, dsrdprior, selected):
        self.prep = prep
        self.varcrs = varcrs
        self.fxdcrs = fxdcrs
        self.reqprior = reqprior
        self.dsrdprior = dsrdprior
        self.selected = selected

    # TODO: implement

    def _compute_current_state(self):
        crs_not_done = course.notdone(self.prep.available_courses, self.prep.done_codes)
        self.reqprior = course.req_prior(crs_not_done, self.prep.done_codes)
        self.dsrdprior = course.dsrd_prior(crs_not_done, self.prep.done_codes)
        prior = self.reqprior + self.dsrdprior
        non_prior = crs_not_done not in prior
        self.varcrs = course.var_crses(prior)
        self.fxdcrs = course.fxd_crses(prior)





    # TODO: implement

    def _choose_course(self, quartile: int):
        """
        :param quartile: int that shows the quartile
        """

        if course.courses_in_quartile(self.fxdcrs, quartile):
            self.selected = course.courses_in_quartile(self.fxdcrs, quartile)
        elif course.fxd_crses_req_prior(self.selected, self.reqprior):
            self.selected = course.fxd_crses_req_prior(self.selected, self.reqprior)
        elif course.fxd_crses_dsrd_prior(self.selected, self.dsrdprior):
            self.selected = course.fxd_crses_req_prior(self.selected, self.reqprior)
        elif course.fxd_crses_dsrd_prior(self.selected, self.dsrdprior):
            self.selected = course.fxd_crses_req_prior(self.selected, self.reqprior)
        elif

    # TODO: implement

    def _generate_for_quartile(self, quartile):
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
