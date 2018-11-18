# Date: December 9, 2017
# Author: Edward Tang
# Purpose: This program is designed to assign values to two Date objects through user input and display their arithmetic and relational comparison.
# Input: Keyboard
# Output: Screen, Console
# ===========================================================================================================================================================================

from tkinter import *
from tkinter import messagebox
import random

# Date: November 9, 2017
# Author: Edward Tang
# Purpose: This class is intended to be used to determine a date through user input or preset values and display
#          it as a string, text-based calendar or GUI-based calendar.
# Field Data:
#   intDay - Correlates to the day of the date
#   intMonth - Correlates to the month of the date
#   intYear - Correlates to the year of the date
#   intYearSmall - Correlates to the year (fourth digit) of the date
#   intDecade - Correlates to the decade (third digit) of the date
#   intCentury - Correlates to the century (second digit) of the date
#   intMillenium - Correlates to the millenium (first digit) of the date
# Methods:
#   returnMonthName() - This method is designed to receive the intMonth field of the Date object and return the month's name (e.g. if intMonth is 2, "February" is returned).
#   returnLeapYear() - This method is designed to return True or False based on whether or not the year of the Date object is a leap year.   
#   returnMaxDay() - This method is designed to return the maximum number of days in the month of the Date object depending on the month number and whether returnLeapYear() returns True or False.
#   calcZeller() - This method is designed to determine and return an integer that represents the day of the week of the Date object (e.g. Sunday is represented by 0, Monday is represented by 1, etc.).
#   returnDayName() - This method is designed to return the name of the day of the Date object. 
#   calcValid() - This method is designed to return True or False based on whether or not the Date object meets established requirements (day between 1 and max number of days inclusive, month between 1 and 12 inclusive, year 1600 or later).
#   getDate() - This method is designed to ask the user to input a year, month and day and check to ensure that it is a valid date.
#   __str__() - This method is designed to receive the day, month and year of the Date object and convert the date into a string.
#   dayOfYear() - This method is designed to determine the Date object's day's number in the entire year (1-365).
#   getTotalDays() - This method is designed to determine the total amount of days (from 0) that would have passed to reach the date of the object. 
#   __sub__() - This method is designed to determine the number of days between the date object and another date object
#   __add__() - This method is designed to add the number of days between two dates to the chronologically later date, creating a new date later in time.
#   __gt__() - This method is designed to determine whether or not the object date is "greater" (later chronologically) than a second object date.  
#   __lt__() - This method is designed to determine whether or not the object date is "lesser" (earlier chronologically) than a second object date.
#   __ge__() - This method is designed to determine whether or not the object date is "greater" (later chronologically) than or equal to a second object date.
#   __le__() - This method is designed to determine whether or not the object date is "lesser" (earlier chronologically) than or equal to a second object date.
#   __eq__() - This method is designed to determine whether or not the object date is equal to the second object date.
#   __ne__() - This method is designed to determine whether or not the object date is unequal to the second object date.
#   displayCalendar() - This method is designed to display the month calendar for the Date object.
#   displayCalendarGUI() - This method is designed to display the month calendar for the Date object.
#   adjustNumber() - This method is designed to adjust the value of either the month, day, year, decade, century or millenium 
#                    of the Date object and the global variables month, day, yearSmall, decade, century, millenium and 
#                    fullYear by a given interval and within a low-high range. It will also dynamically adjust the intDay
#                    field and global variable day based on the month and year (e.g. 28 days in February for
#                    non-leap years, 29 days in February for leap years).
#   restoreDefaults() - This method is designed restore the default fields of the Date class and the global variables month day, yearSmall, decade, century, millenium and fullYear. It will also clear the text in a Text widget.
#   getValidInteger() - This method is designed to ask the user for an integer and perform checks to make sure the integer is within a certain range.
#   adjustUpAndDown() - This function is designed to receive a value, low/high thresholds and an interval. If the given value is
#                       within the low-high range, the value will increase by the interval. If the given value is equal to
#                       the high or low threshold, the value will become the low or high number respectively.
#   clearDisplay() - This method is designed to clear all text from the "display" Text widget.
# =============================================================================================================================================================================================================

class Date:
    def __init__(self,day=1,month=1,year=2017,yearSmall=7,decade=1,century=0,millenium=2):
        self.intDay = day
        self.intMonth = month
        self.intYear = year
        self.intYearSmall = yearSmall
        self.intDecade = decade
        self.intCentury = century
        self.intMillenium = millenium
        if not self.calcValid():
            self.intDay = 1
            self.intMonth = 1
            self.intYear = 2017
            self.intYearSmall = 7
            self.intDecade = 1
            self.intCentury = 0
            self.intMillenium = 2   

    # Date: November 9, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to receive the intMonth field of the Date object and return the month's name
    #          (e.g. if intMonth is 2, "February" is returned).
    # Input: N/A
    # Output: [STRING] The month's name
    # ==============================================================================================================

    def returnMonthName(self):
        strMonth = "January"
        if self.intMonth == 2:
            strMonth = "February"
        elif self.intMonth == 3:
            strMonth = "March"
        elif self.intMonth == 4:
            strMonth = "April"
        elif self.intMonth == 5:
            strMonth = "May"
        elif self.intMonth == 6:
            strMonth = "June"
        elif self.intMonth == 7:
            strMonth = "July"
        elif self.intMonth == 8:
            strMonth = "August"
        elif self.intMonth == 9:
            strMonth = "September"
        elif self.intMonth == 10:
            strMonth = "October"
        elif self.intMonth == 11:
            strMonth = "November"
        elif self.intMonth == 12:
            strMonth = "December"
        return strMonth

    # Date: November 9, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to return True or False based on whether or not the year of the Date object
    #          is a leap year.
    # Input: N/A
    # Output: [BOOLEAN] True or False based on whether or not intYear is a leap year
    # =============================================================================================================

    def returnLeapYear(self):
        isLeapYear = False
        if self.intYear % 400 == 0 or self.intYear % 4 == 0:
            isLeapYear = True
        return isLeapYear

    # Date: November 9, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to return the maximum number of days in the month of the Date object depending
    #          on the month number and whether returnLeapYear() returns True or False.
    # Input: N/A
    # Output: [INTEGER] The maximum number of days in the month
    # ================================================================================================================

    def returnMaxDay(self):
        maxDay = 31
        if self.intMonth == 1 or self.intMonth == 3 or self.intMonth == 5 or self.intMonth == 7 or self.intMonth == 8 or self.intMonth == 10 or self.intMonth == 12:
            maxDay = 31
        elif self.intMonth == 4 or self.intMonth == 6 or self.intMonth == 9 or self.intMonth == 11:
            maxDay = 30
        elif self.intMonth == 2 and self.returnLeapYear() == True:
            maxDay = 29
        elif self.intMonth == 2 and self.returnLeapYear() == False:
            maxDay = 28
        return maxDay

    # Date: November 10, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to determine and return an integer that represents the day of the week of the
    #          Date object (e.g. Sunday is represented by 0, Monday is represented by 1, etc.).
    # Input: N/A
    # Output: [INTEGER] The day of the week represented by a number
    # ===============================================================================================================

    def calcZeller(self):
        m = self.intMonth - 2
        y = self.intYear
        if m <= 0:
            m = m+ 12
            y = y -1
        p = y // 100
        r = y % 100
        return(self.intDay+(26*m-2)//10+r+r//4+p//4+5*p)%7

    # Date: November 10, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to return the name of the day of the Date object.
    # Input: N/A
    # Output: [STRING] The name of the day of the week
    # ===================================================================================

    def returnDayName(self):
        dayName = "Sunday"
        if self.calcZeller() == 0:
            dayName = "Sunday"
        elif self.calcZeller() == 1:
            dayName = "Monday"
        elif self.calcZeller() == 2:
            dayName = "Tuesday"
        elif self.calcZeller() == 3:
            dayName = "Wednesday"
        elif self.calcZeller() == 4:
            dayName = "Thursday"
        elif self.calcZeller() == 5:
            dayName = "Friday"
        elif self.calcZeller() == 6:
            dayName = "Saturday"
        return dayName

    # Date: November 10, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to return True or False based on whether or not the Date object meets
    #          established requirements (day between 1 and max number of days inclusive, month between 1 and 12
    #          inclusive, year 1600 or later).
    # Input: N/A
    # Output: [BOOLEAN] True or False based on whether or not the Date object meets the established requirements
    # =============================================================================================================

    def calcValid(self):
        isValid = False
        if self.intDay >= 1 and self.intDay <= self.returnMaxDay() and self.intMonth >= 1 and self.intMonth <= 12 and self.intYear >= 1600:
            isValid = True
        return isValid

    # Date: November 10, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to ask the user to input a year, month and day and check to ensure that it is
    #          a valid date.
    # Input: N/A
    # Output: Console/Screen
    # ===============================================================================================================

    def getDate(self):
        self.intYear = self.getValidInteger(prompt="Enter a year",low="1600")
        self.intMonth = self.getValidInteger(prompt="Enter a month",low="1",high="12")
        self.intDay = self.getValidInteger(prompt="Enter a day",low="1",high=str(self.returnMaxDay()))
        while self.calcValid() == False:
            print()
            if self.intDay < 1 or self.intDay > self.returnMaxDay():
                print("ERROR: Invalid day")
            elif self.intMonth < 1 or self.intMonth > 12:
                print("ERROR: Invalid month")
            elif self.intYear < 1600:
                print("ERROR: Invalid year (cannot be older than 1600)")
            print()
            self.intDay = self.getValidInteger("Enter the day",1,self.returnMaxDay())
            self.intMonth = self.getValidInteger("Enter the month",1,12)
            self.intYear = self.getValidInteger("Enter the year",1600)

    # Date: November 10, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to receive the day, month and year of the Date object and convert the date
    #          into a string.
    # Input: N/A
    # Output: [STRING] The date
    # ===============================================================================================================

    def __str__(self):
        return (self.returnDayName() + ", " + str(self.intDay) + " " + self.returnMonthName() + " " + str(self.intYear))

    # Date: November 11, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to determine the Date object's day's number in the entire year (1-365).
    # Input: N/A
    # Output: [INTEGER] The Date object's day's number in the entire year (1-365)
    # =========================================================================================================

    def dayOfYear(self):
        dayCount = 0
        monthBackup = self.intMonth
        self.intMonth = 0
        for count in range(1,monthBackup):
            self.intMonth = self.intMonth + 1
            dayCount = dayCount + self.returnMaxDay()
        dayCount = dayCount + self.intDay
        self.intMonth = monthBackup
        return dayCount


    # Date: December 9, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to determine the total amount of days (from 0) that would have passed
    #          to reach the date of the object.
    # Input: N/A
    # Output: [INTEGER] The number of days of the date
    # =======================================================================================================

    def getTotalDays(self):
        days = self.dayOfYear()
        yearBackup = self.intYear
        while self.intYear > 0:
            self.intYear = self.intYear - 1
            if self.returnLeapYear():
                days = days + 366
            else:
                days = days + 365
        self.intYear = yearBackup
        return days

    # Date: December 9, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to determine the number of days between the date object and another date object
    # Input: A second date object name
    # Output: [INTEGER] The number of days between the date object and another
    # =================================================================================================================

    def __sub__(self,secondObject):
        return abs(self.getTotalDays() - secondObject.getTotalDays())

    # Date: December 12, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to add the number of days between two dates to the chronologically later
    #          date, creating a new date later in time.
    # Input: A second date object name
    # Output: [STRING] The new date created by "adding" the two date objects
    # ===========================================================================================================

    def __add__(self,secondObject):
        thirdObject = Date()
        dayDifference = self-secondObject
        if self.__gt__(secondObject):
            thirdObject.intYear = self.intYear
            thirdObject.intMonth = self.intMonth
            thirdObject.intDay = self.intDay
        else:
            thirdObject.intYear = secondObject.intYear
            thirdObject.intMonth = secondObject.intMonth
            thirdObject.intDay = secondObject.intDay
        while dayDifference > 0:
            if dayDifference >= thirdObject.returnMaxDay():
                dayDifference = dayDifference-thirdObject.returnMaxDay()
                if thirdObject.intMonth != 12:
                    thirdObject.intMonth = thirdObject.intMonth + 1
                else:
                    thirdObject.intMonth = 1
                    thirdObject.intYear = thirdObject.intYear + 1
            else:
                thirdObject.intDay = thirdObject.intDay + dayDifference
                dayDifference = 0
        return str(thirdObject)

    # Date: December 9, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to determine whether or not the object date is "greater" (later 
    #          chronologically) than a second object date.
    # Input: A second date object name
    # Output: [BOOLEAN] True or False depending on whether or not the object date is greater (later) than the
    #         second
    # ========================================================================================================

    def __gt__(self,secondObject):
        isGreater = False
        if self.intYear > secondObject.intYear:
            isGreater = True
        elif self.intYear == secondObject.intYear:
            if self.intMonth > secondObject.intMonth:
                isGreater = True
            elif self.intMonth == secondObject.intMonth:
                if self.intDay > secondObject.intDay:
                    isGreater = True
        return isGreater

    # Date: December 9, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to determine whether or not the object date is "lesser" (earlier 
    #          chronologically) than a second object date.
    # Input: A second date object name
    # Output: [BOOLEAN] True or False depending on whether or not the object date is lesser (earlier) than the
    #         second
    # =========================================================================================================

    def __lt__(self,secondObject):
        isLesser = False
        if self.intYear < secondObject.intYear:
            isLesser = True
        elif self.intYear == secondObject.intYear:
            if self.intMonth < secondObject.intMonth:
                isLesser = True
            elif self.intMonth == secondObject.intMonth:
                if self.intDay < secondObject.intDay:
                    isLesser = True
        return isLesser

    # Date: December 9, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to determine whether or not the object date is "greater" (later 
    #          chronologically) than or equal to a second object date.
    # Input: A second date object name
    # Output: [BOOLEAN] True or False depending on whether or not the object date is greater (later) than or
    #         equal to the second
    # =========================================================================================================

    def __ge__(self,secondObject):
        isGreaterOrEqual = False
        if self>secondObject or self==secondObject:
            isGreaterOrEqual = True
        return isGreaterOrEqual

    # Date: December 9, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to determine whether or not the object date is "lesser" (earlier 
    #          chronologically) than or equal to a second object date.
    # Input: A second date object name
    # Output: [BOOLEAN] True or False depending on whether or not the object date is lesser (earlier) than or
    #         equal to the second
    # ========================================================================================================

    def __le__(self,secondObject):
        isLesserOrEqual = False
        if self<secondObject or self==secondObject:
            isLesserOrEqual = True
        return isLesserOrEqual

    # Date: December 12, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to determine whether or not the object date is equal to the second object
    #          date.
    # Input: A second date object name
    # Output: [BOOLEAN] True or False depending on whether or not the object date is equal to the second
    # ===========================================================================================================

    def __eq__(self,secondObject):
        isEqual = False
        if self.intDay == secondObject.intDay and self.intMonth == secondObject.intMonth and self.intYear == secondObject.intYear:
            isEqual = True
        return isEqual

    # Date: December 12, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to determine whether or not the object date is unequal to the second object
    #          date.
    # Input: A second date object name
    # Output: [BOOLEAN] True or False depending on whether or not the object date is unequal to the second
    # =============================================================================================================

    def __ne__(self,secondObject):
        notEqual = True
        if self==secondObject:
            notEqual = False
        return notEqual

    # Date: November 11, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to display the month calendar for the Date object.
    # Input: N/A
    # Output: Console/Screen
    # ====================================================================================

    def displayCalendar(self):
        print(self)
        self.intDay = 1
        weekday = 0
        print("%15s"%self.returnMonthName(), self.intYear)
        print("Sun Mon Tue Wed Thu Fri Sat")
        for count in range(1,7):
            if self.intDay <= self.returnMaxDay():
                for count in range(0,7):
                    if self.calcZeller() == count and self.intDay <= self.returnMaxDay():
                        print("%3i"%self.intDay,end=" ")
                        if self.intDay <= self.returnMaxDay():
                            self.intDay = self.intDay + 1
                    else:
                        print("   ",end=" ")
            print()

    # Date: November 13, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to display the month calendar for the Date object.
    # Input: N/A
    # Output: Screen (text widget changes)
    # References: Text widget
    # ====================================================================================

    def displayCalendarGUI(self):
        self.clearDisplay()
        if self.intYear >= 1600:
            dayBackup = self.intDay
            display.config(state=NORMAL)
            display.insert(END,"\n  " + str(self) + "\n\n")
            self.intDay = 1
            weekday = 0
            display.insert(END,"%20s"%self.returnMonthName() + " " + str(self.intYear) + "\n")
            display.insert(END,"  Sun  Mon  Tue  Wed  Thu  Fri  Sat\n")
            for count in range(1,7):
                display.insert(END,"  ")
                if self.intDay <= self.returnMaxDay():
                    for count in range(0,7):
                        if self.calcZeller() == count and self.intDay <= self.returnMaxDay():
                            display.insert(END,"%3i"%self.intDay + "  ")
                            if self.intDay <= self.returnMaxDay():
                                self.intDay = self.intDay + 1
                        else:
                            display.insert(END,"     ")
                display.insert(END,"\n")
            self.intDay = dayBackup
            display.config(state=DISABLED)
        else:
            messagebox.showerror("ERROR","Unable to display calendar: Year must be 1600 or later!")

    # Date: November 13, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to adjust the value of either the month, day, year, decade, century or millenium 
    #          of the Date object and the global variables month, day, yearSmall, decade, century, millenium and 
    #          fullYear by a given interval and within a low-high range. It will also dynamically adjust the intDay
    #          field and global variable day based on the month and year (e.g. 28 days in February for
    #          non-leap years, 29 days in February for leap years).
    # Input: [INTEGER] A low threshhold, a high threshold and an interval number, [STRING] A value
    # Output: N/A
    # References: Global variables: month, day, year, decade, century, millenium and fullYear
    # =============================================================================================================

    def adjustNumber(self,variable="month",low=1,high=12,interval=1):
        if variable == "month":
            self.intMonth = self.adjustUpAndDown(self.intMonth,low,high,interval)
            month.set(self.returnMonthName())
        elif variable == "day":
            self.intDay = self.adjustUpAndDown(self.intDay,low,self.returnMaxDay(),interval)
            day.set(self.intDay)
        elif variable == "year":
            self.intYearSmall = self.adjustUpAndDown(self.intYearSmall,low,high,interval)
            yearSmall.set(self.intYearSmall)
        elif variable == "decade":
            self.intDecade = self.adjustUpAndDown(self.intDecade,low,high,interval)
            decade.set(self.intDecade)
        elif variable == "century":
            self.intCentury = self.adjustUpAndDown(self.intCentury,low,high,interval)
            century.set(self.intCentury)
        elif variable == "millenium":
            self.intMillenium = self.adjustUpAndDown(self.intMillenium,low,high,interval)
            millenium.set(self.intMillenium)
        self.intYear = date.intYearSmall+date.intDecade*10+date.intCentury*100+date.intMillenium*1000
        fullYear.set(" ".join(str(self.intYear)))
        if self.intDay > self.returnMaxDay():
            self.intDay = self.returnMaxDay()
            day.set(self.intDay)

    # Date: November 13, 2017
    # Author: Edward Tang
    # Purpose: This method is designed restore the default fields of the Date class and the global variables month,
    #          day, yearSmall, decade, century, millenium and fullYear. It will also clear the text in a Text widget.
    # Input: N/A
    # Output: Screen (Text widget changes)
    # References: Text widget, global variables: month, day, yearSmall, decade, century, millenium and fullYear
    # ================================================================================================================

    def restoreDefaults(self,dayDefault=1,monthDefault=1,yearDefault=2017,yearSmallDefault=7,decadeDefault=1,centuryDefault=0,milleniumDefault=2):
        self.intDay = dayDefault
        self.intMonth = monthDefault
        self.intYear = yearDefault
        self.intYearSmall = yearSmallDefault
        self.intDecade = decadeDefault
        self.intCentury = centuryDefault
        self.intMillenium = milleniumDefault

        month.set("January")
        day.set(date.intDay)
        yearSmall.set(date.intYearSmall)
        decade.set(date.intDecade)
        century.set(date.intCentury)
        millenium.set(date.intMillenium)
        fullYear.set("2 0 1 7")

        self.clearDisplay()

    # Date: November 10, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to ask the user for an integer and perform checks to make sure the integer
    #          is within a certain range.
    # Input: Keyboard, [STRING] The input prompt phrase, [INTEGER] the lowest possible value and the highest 
    #        possible value
    # Output: Console/Screen, [INTEGER] The user-inputted number
    # =============================================================================================================
        
    def getValidInteger(self,prompt="Enter an integer",low = "",high = ""):
        if low.isdigit() and high.isdigit():
            low = int(low)
            high = int(high)
            intUserInput = low - 1
            while intUserInput < low or intUserInput > high:
                strUserInput = ""
                while not strUserInput.isdigit():
                    strUserInput = input(prompt + " between " + str(low) + " and " + str(high) + ": ")
                    print()
                    if not strUserInput.isdigit():
                        print("[ERROR] You did not enter a valid integer! Please try again.")
                        print()
                intUserInput = int(strUserInput)
                if intUserInput < low or intUserInput > high:
                    print("[ERROR] You did not enter an integer between " + str(low) + " and " + str(high) + ". Please try again.")
                    print()
            return intUserInput
        elif low.isdigit() and not high.isdigit():
            low = int(low)
            intUserInput = low - 1
            while intUserInput < low:
                strUserInput = ""
                while not strUserInput.isdigit():
                    strUserInput = input(prompt + " of at least " + str(low) + ": ")
                    print()
                    if not strUserInput.isdigit():
                        print("[ERROR] You did not enter a valid integer! Please try again.")
                        print()
                intUserInput = int(strUserInput)
                if intUserInput < low:
                    print("[ERROR] You did not enter an integer of at least " + str(low) + ". Please try again.")
                    print()
            return intUserInput

    # Date: November 13, 2017
    # Author: Edward Tang
    # Purpose: This function is designed to receive a value, low/high thresholds and an interval. If the given value is
    #          within the low-high range, the value will increase by the interval. If the given value is equal to
    #          the high or low threshold, the value will become the low or high number respectively.
    # Input: [INTEGER] A value, a low threshhold, a high threshold and an interval number
    # Output: [INTEGER] The updated value
    # ==================================================================================================================

    def adjustUpAndDown(self,value=2,low=1,high=12,interval=1):
        if value + interval <= high and value+interval >= low:
            value = value + interval
        elif interval > 0 and value == high:
            value = low
        elif interval < 0 and value == low:
            value = high
        return value

    # Date: November 13, 2017
    # Author: Edward Tang
    # Purpose: This method is designed to clear all text from the "display" Text widget.
    # Input: N/A
    # Output: N/A
    # References: A Text widget named "display"
    # ===================================================================================

    def clearDisplay(self):
        display.config(state=NORMAL)
        display.delete(1.0,END)
        display.config(state=DISABLED)

# MAIN CODE

restart = ""
date1 = Date()
date2 = Date()

while restart != "stop":
    print("========== Enter the first date below ==========")
    print()
    date1.getDate()
    print()
    print("========== Enter the second date below ==========")
    print()
    date2.getDate()
    print()
    print("========== Arithmetic and Relational Results ==========")
    print()
    print("Date 1:",date1)
    print("Date 2:",date2)
    print()
    print("Subtraction (days between dates):",date1-date2)
    print("Addition (days between dates added to the larger date):",date1+date2)
    print("[First Date] >  [Second Date]:",date1>date2)
    print("[First Date] <  [Second Date]:",date1<date2)
    print("[First Date] >= [Second Date]:",date1>=date2)
    print("[First Date] <= [Second Date]:",date1<=date2)
    print("[First Date] == [Second Date]:",date1==date2)
    print("[First Date] != [Second Date]:",date1!=date2)
    print()
    restart = input("Enter any key to restart the program, or enter 'stop' to end it: ")
    print()
