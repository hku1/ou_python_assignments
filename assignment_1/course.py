import datetime


def create_course(courseinfo):
    newcourse = Course(courseinfo['code'], courseinfo['naam'],
                       courseinfo['sbu'], courseinfo['startdatum'],
                       courseinfo['einddatum'])
    newcourse.add_required_courses(courseinfo['voorkennisverplicht'])
    newcourse.add_desired_courses(courseinfo['voorkennisgewenst'])
    newcourse.add_exams(courseinfo['tentamens'])
    newcourse.add_exams_quartile(courseinfo['tentamens'])
    return newcourse


# functions for lists of courses

def available(courses, done):
    """select courses that not have been done from list of all available courses """
    avlble = [course for course in courses if course.code not in done]
    return avlble


# def available_required_satisfied(courses, done):
#     """"select course that have
#         completed courses as required knowledge or no
#         required knowledge condition (empty string)"""
#     reqprior_lst = [course for course in courses if any(req_course in done for req_course in course.required_courses)]
#     return reqprior_lst


def available_required_satisfied(courses, done):
    """Select courses that have completed courses
       as required knowledge or no required knowledge condition
       (empty list)"""
    reqprior_lst = [course for course in courses if all(req_course in done for req_course in course.required_courses)]
    return reqprior_lst


def fxd_crses(courses):
    """"select courses that have a fixed start date"""
    fxd_lst = [course for course in courses if course.dates.nodates() is False]
    return fxd_lst


def dsrd_prior_knwledge(courses, done):
    dsrd_prio = [course for course in courses if any(dsrd_course in done for dsrd_course in course.desired_courses)]
    return dsrd_prio


def req_codes(courses, done):
    dsrd_cdes = [code for course in courses for code in course.desired_courses if code not in done]
    return dsrd_cdes


def dsrd_codes(courses, done):
    dsrd_cdes = [code for course in courses for code in course.desired_courses if code not in done]
    return dsrd_cdes


def future_crses(courses, code_list):
    """select  from a list of courses those course
       that have a non-empty required knowledge field """
    future_lst = [course for course in courses if course.code in code_list]
    return future_lst


# def dsrd_future_crss(courses):
#     """select  from a list of courses those course
#        that have a non-empty desired knowledge field """
#     dsrd_future_lst = [course for course in courses if course.code in course.desired_courses]
#     return dsrd_future_lst

# def req_prior(courses, done):
#     """"select available course that not have been done and that
#         have completed courses as required knowledge"""
#     reqprior_lst = [course for course in courses if any(req_course in done for req_course in course.required_courses)]
#     return reqprior_lst


# def dsrd_prior(courses, done):
#     """select available course that not have been done and that
#             have completed courses as desired knowledge"""
#     dsrdprior_lst = [course for course in courses if any(dsrd_course in done for dsrd_course in course.desired_courses)]
#     return dsrdprior_lst

def var_crses(courses):
    """"select courses that have a variable start date"""
    var_lst = [course for course in courses if course.dates.nodates() is True]
    return var_lst


def courses_in_quartile(courses, quartile: int):
    """ select courses that are given in a given quartile"""
    crs_quart = [course for course in courses if course.dates.quartile() == quartile]
    return crs_quart


def exams_in_quartile(courses, quartile: int):
    """ select courses that have an exam in a given quartile"""
    exms_quart = [course for course in courses if quartile in course.examsq]
    return exms_quart


class Start_and_enddate:
    """ Class for objects with a startdate and an enddate """

    def __init__(self, startdate=None, enddate=None):
        self.startdate = None
        self.enddate = None
        if startdate:
            self.startdate = datetime.date.fromisoformat(startdate)
        if enddate:
            self.enddate = datetime.date.fromisoformat(enddate)

    def __str__(self):
        """ String representation
        no startdate and enddate: returns variable
        otherwise: returns startdate,  enddate """
        if self.nodates():
            return 'variable'
        return str(self.startdate) + ', ' + str(self.enddate)

    def nodates(self):
        """ true when there is no startdate and no enddate """
        return (not self.startdate) and (not self.enddate)

    def quartile(self):
        """ Compute quartile
        startdate in month 9: return 1
        startdate in month 11: return 2
        startdate in month 2: return 3
        startdate in month 4: return 4
        otherwise: return -1
        """
        if self.startdate.month == 9:
            quartile = 1
        elif self.startdate.month == 11:
            quartile = 2
        elif self.startdate.month == 2:
            quartile = 3
        elif self.startdate.month == 4:
            quartile = 4
        else:
            quartile = -1
        return quartile


class Course:
    # TODO: implement and extend with attributes and methods

    def __init__(self, code, title, sbu, startdate, enddate, required_courses=None, desired_courses=None, exams=None,
                 examsq=None):
        # TODO: implement
        self.code: str = code
        self.title: str = title
        self.sbu: int = sbu
        self.startdate: str = startdate
        self.enddate: str = enddate
        self.required_courses: list = required_courses
        self.desired_courses: list = desired_courses
        self.exams: list = exams
        self.dates = Start_and_enddate(startdate, enddate)
        self.examsq = examsq

    def add_required_courses(self, courses):
        self.required_courses = []
        for course in courses:
            self.required_courses.append(course)
        return self.required_courses

    def add_desired_courses(self, courses):
        self.desired_courses = []
        for course in courses:
            self.desired_courses.append(course)
        return self.desired_courses

    def add_exams(self, exams):
        self.exams = []
        for exam in exams:
            self.exams.append(exam)
        return self.exams

    def add_exams_quartile(self, examsq):
        self.examsq = []
        for exam in examsq:
            self.examsq.append(Start_and_enddate(exam).quartile())
        return self.examsq

    def __str__(self):
        """ string with:
        - code,
        - title,
        - period,
        - new line
        - codes of required foreknowledge or 'geen verplichte voorkennis'
        - new line
        - codes of desired foreknowledge or 'geen gewenste voorkennis'
        - new line
        """
        # string representing the required foreknowledge
        required_foreknowledge = ''
        if not required_foreknowledge:
            required_foreknowledge += "Geen verplicht voorkennis"
        else:
            for code in required_foreknowledge:
                required_foreknowledge += ' , ' + str(code)

        # string representing the desire foreknowledge
        desired_foreknowledge = ''
        if not desired_foreknowledge:
            desired_foreknowledge += "Geen gewenste voorkennis"
        else:
            for code in desired_foreknowledge:
                desired_foreknowledge += ' , ' + str(code)

        # exams or 'variable'
        datums = ''
        if self.dates.nodates():
            datums += 'variable'
        else:
            datums += str(self.dates.startdate) + ' , ' + str(self.dates.enddate)

        return str(self.title + ',' + self.code + ' ,' + datums + '\n'
                   + required_foreknowledge + '\n'
                   + desired_foreknowledge + '\n')
