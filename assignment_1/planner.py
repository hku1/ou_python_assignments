import course
import preparation


class Planner:
    """" class to filter and store Course class object"""

    def __init__(self, prep, varcrs=None, fxdcrs=None):
        self.prep = prep
        self.varcrs = varcrs
        self.fxdcrs = fxdcrs

    # TODO: implement

    def compute_current_state(self):
        crs_not_done = course.notdone(self.prep.available_courses, self.prep.done_codes)
        reqprior = course.req_prior(crs_not_done, self.prep.done_codes)
        dsrdprior = course.dsrd_prior(crs_not_done, self.prep.done_codes)
        prior = reqprior + dsrdprior
        self.varcrs = course.var_crses(prior)
        self.fxdcrs = course.fxd_crses(prior)

    # TODO: implement

    def choose_course(self, quartile: int):
        """
        :param quartile: int that shows the quartile
        """
        fxd_quartile = course.courses_in_quartile(self.fxdcrs, quartile)
        if courses_in_quartile(fxdcrs, quartile):
            return

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
