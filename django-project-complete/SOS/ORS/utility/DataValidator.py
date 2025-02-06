import re
from datetime import *


class DataValidator:

    @classmethod
    def isNotNull(self, val):
        if (val == None or val == ""):
          return False
        else:
            return True
    @classmethod
    def isNull(self,val):
        if(val==None or val==""):
            return True
        else:
            return False

    @classmethod
    def isDate(self, val):
        if re.match("([0-2]\d{3})-(0\d|1[0-2])-([0-2]\d|3[01])", val):
            if (datetime.strptime(val, "%Y-%m-%d") <= datetime.strptime(str(date.today()),
                                                                        "%Y-%m-%d")):  # Comparing date with current date
                return False
            else:
                return True
        else:
            return True

    @classmethod
    def isCheck(self, val):
        if (val==None or val==""):
            return True
        else:
            if(0<=int(val)<=100):
                return False
            else:
                return True


    @classmethod
    def isCheckRoll(self,val):
        if re.match("^(?=.*[0-9]$)(?=.*[A-Z])", val):
            return False
        else:
            return True

    @classmethod
    def isAlphaCheck(self,val):
        if re.match("^[a-zA-z\s]+$", val):
            return False
        else:
            return True


    @classmethod
    def isMobileCheck(self, val):
        if re.match("^[6-9]\d{9}$", val):
            return False
        else:
            return True

    @classmethod
    def isEmail(self,val):
        if re.match("[^@]+@[^@]+\.[^@]+", val):
            return False
        else:
            return True

    @classmethod
    def isPhoneCheck(self,val):
        if re.match("^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$", val):
            return False
        else:
            return True

    @classmethod
    def isInteger(self, val):
        if re.match("^-?\d+$", val):  # Matches any integer, including negative numbers
            return False  # Returns False if it's a valid integer
        else:
            return True  # Returns True if it's not a valid integer

    @classmethod
    def isAppointmentDate(self, val):
        """Validates if the appointment date is in YYYY-MM-DD format and in the future."""
        if re.match("([0-2]\d{3})-(0\d|1[0-2])-([0-2]\d|3[01])", val):
            # Check if the date is greater than today's date
            if datetime.strptime(val, "%Y-%m-%d") <= datetime.strptime(str(date.today()), "%Y-%m-%d"):
                return True  # Invalid (the appointment date is in the past or today)
            else:
                return False  # Valid (the appointment date is in the future)
        else:
            return True  # Invalid (does not match the expected date format)