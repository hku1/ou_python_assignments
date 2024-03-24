import datetime

def create_course(courseinfo):
    """
    Creates a new course object with the info in courseinfo
    :param:courseinfo
    :return:new course object
    """
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
    """
    select courses that not have been done from list of all available courses
    :param:List of all courses and list of done courses
    :return:List of available courses
    """

    avlble = [course for course in courses if course.code not in done]
    return avlble


def available_required_satisfied(courses, done):
    """Select courses that have completed courses
       as required knowledge or no required knowledge condition
       (empty list)
    """
    reqprior_lst = [course for course in courses if all(req_course in done for req_course in course.required_courses)]
    return reqprior_lst


def fxd_crses(courses):
    """"
    select courses that have a fixed start date
    """
    fxd_lst = [course for course in courses if course.dates.nodates() is False]
    return fxd_lst


def dsrd_prior_knwledge(courses, done):
    """"
       select desired courses for which we have the required knowledge
    """
    dsrd_prio = [course for course in courses if any(dsrd_course in done for dsrd_course in course.desired_courses)]
    return dsrd_prio


def req_codes(courses, done):
    """""
       select required courses which are not done yet
    """
    req_codes = [code for course in courses for code in course.required_courses_courses if code not in done]
    return req_codes


def dsrd_codes(courses, done):
    """"
    select desired courses are not done yet
    """
    dsrd_cdes = [code for course in courses for code in course.desired_courses if code not in done]
    return dsrd_cdes


def future_crses(courses, code_list):
    """select  from a list of courses those course
       that have a non-empty required knowledge field """
    future_lst = [course for course in courses if course.code in code_list]
    return future_lst


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

    def __init__(self, code, title, sbu, startdate, enddate, required_courses=None, desired_courses=None, exams=None,
                 examsq=None):

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
        if self.required_courses:
            required_str = 'verplichte voorkennis: {0} '.format(self.required_courses)
        else:
            required_str = 'geen verplichte voorkennis'

        if self.desired_courses:
            desired_str = 'gewenste voorkennis: {0} '.format(self.desired_courses)
        else:
            desired_str = 'geen gewenste voorkennis'

        return '{0}, {1}, \n {2} \n {3} \n'.format(self.code, self.title, required_str, desired_str)
