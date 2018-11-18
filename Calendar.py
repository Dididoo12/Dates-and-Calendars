# Date: November 9, 2017
# Author: Edward Tang
# Purpose: This program is designed to display a text-based calendar based on user input.
# Input: Mouse and/or Keyboard
# Output: Screen, Console and/or GUI
# ========================================================================================

from tkinter import *
from tkinter import messagebox

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

# Date: November 17, 2017
# Author: Edward Tang
# Purpose: This program is designed to create a window with five labels and a close button. The background and text colours are drawn from global variables, allowing customization.
# Input: Title name, five string values and the width and height of the window
# Output: Screen
# References: Global variables bgColour and textColour
# ===================================================================================================================================================================================

def window6LabelsCustomColours(title,text1,text2,text3,text4,text5,text6,width,height):
    window = Toplevel(main)
    window.title(title)
    window.resizable(False,False)
    window.config(width=width,height=height,bg=bgColour.get())
    ws = main.winfo_screenwidth()
    hs = main.winfo_screenheight()
    x = (ws/2) - (width/2)
    y = (hs/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window.grab_set()
    Label(window,text=text1,font=("Arial",12,"bold"),fg=textColour.get(),bg=bgColour.get()).place(x=5,y=5)
    Label(window,text=text2,font=("Arial",10,"normal"),fg=textColour.get(),bg=bgColour.get()).place(x=5,y=30)
    Label(window,text=text3,font=("Arial",10,"normal"),fg=textColour.get(),bg=bgColour.get()).place(x=5,y=55)   
    Label(window,text=text4,font=("Arial",10,"normal"),fg=textColour.get(),bg=bgColour.get()).place(x=5,y=80)
    Label(window,text=text5,font=("Arial",10,"normal"),fg=textColour.get(),bg=bgColour.get()).place(x=5,y=105)
    Label(window,text=text6,font=("Arial",10,"normal"),fg=textColour.get(),bg=bgColour.get()).place(x=5,y=130)
    Button(window,text="Close",font=("Arial",10,"bold"),relief=FLAT,cursor="hand2",command=lambda:window.destroy(),bg="tomato2").place(x=width-60,y=height-40)


# Date: November 18, 2017
# Author: Edward Tang
# Purpose: This function is designed change GUI widgets' colours based on a given "theme" value.
# Input: [STRING] Theme parameter
# Output: Screen
# References: Global variable exposureState, GUI widgets: [Menu] fileMenu, [Canvas] display, [Label] monthLabel, dayLabel, yearLabel, [Button] monthUp, monthDown, dayUp, dayDown, milleniumUp, milleniumDown, centuryUp, centuryDown, 
#             decadeUp, decadeDown, yearSmallUp, yearSmallDown, displayButton
# ===============================================================================================================================

def swapGUIColours(theme):
    if theme == "Default":
        bgColour.set("#fcfcfc") # Background Colour
        buttonColour.set("#e2e2e2") # Button Colour
        canvasColour.set("white") # Canvas Colour
        highlightColour.set("chartreuse3") # Contrasting Colour (used for Display button)
        textColour.set("black") # Text of Canvas Colour
    elif theme == "Day":
        bgColour.set("#80d5ed")
        buttonColour.set("#64b6d6")
        canvasColour.set("white")
        highlightColour.set("#d7e50d")
        textColour.set("black")
    elif theme == "Night":
        bgColour.set("#0f0f0f")
        buttonColour.set("#424242")
        canvasColour.set("black")
        highlightColour.set("#336025")
        textColour.set("white")
    elif theme == "Peachy":
        bgColour.set("#FBD7B7")
        buttonColour.set("#ECB4BF")
        canvasColour.set("#FDF3B8")
        highlightColour.set("#C2E3EC")
        textColour.set("black")
    elif theme == "Cupcake":
        bgColour.set("#fffbcb")
        buttonColour.set("#a97cdf")
        canvasColour.set("#bad8eb")
        highlightColour.set("#f8b6b6")
        textColour.set("black")
    elif theme == "Nightlife":
        bgColour.set("#0f0f0f")
        buttonColour.set("#630426")
        canvasColour.set("#5b1560")
        highlightColour.set("#3b7287")
        textColour.set("white")
    elif theme == "Casino":
        bgColour.set("#205916")
        buttonColour.set("#593716")
        canvasColour.set("#114217")
        highlightColour.set("#593716")
        textColour.set("white")
    elif theme == "Bling":
        bgColour.set("#c4a500")
        buttonColour.set("#aa8f00")
        canvasColour.set("#56af68")
        highlightColour.set("#56af68")
        textColour.set("black")
    elif theme == "Fruity":
        bgColour.set("#24ad3d")
        buttonColour.set("#c1b949")
        canvasColour.set("#ad3f20")
        highlightColour.set("#178282")
        textColour.set("white")
    elif theme == "Dry":
        bgColour.set("#bc6e43")
        buttonColour.set("#a8562a")
        canvasColour.set("#b26a52")
        highlightColour.set("#9e3614")
        textColour.set("black")
    elif theme == "Cool":
        bgColour.set("#3973ad")
        buttonColour.set("#26517c")
        canvasColour.set("#26517c")
        highlightColour.set("#1a4b7c")
        textColour.set("white")
    elif theme == "Christmas":
        bgColour.set("#87110d")
        buttonColour.set("#12820d")
        canvasColour.set("#12820d")
        highlightColour.set("#12820d")
        textColour.set("white")
    elif theme == "Halloween":
        bgColour.set("#0f0f0f")
        buttonColour.set("#966206")
        canvasColour.set("#966206")
        highlightColour.set("#966206")
        textColour.set("white")
    elif theme == "Chinese New Year":
        bgColour.set("#be0002")
        buttonColour.set("#930001")
        canvasColour.set("#930001")
        highlightColour.set("#930001")
        textColour.set("#f9c613")
    display.config(bg=canvasColour.get(),fg=textColour.get())
    displayButton.config(bg=highlightColour.get(),fg=textColour.get())
    main.config(bg=bgColour.get())
    monthLabel.config(bg=bgColour.get(),fg=textColour.get())
    dayLabel.config(bg=bgColour.get(),fg=textColour.get())
    yearLabel.config(bg=bgColour.get(),fg=textColour.get())
    monthUp.config(bg=buttonColour.get(),fg=textColour.get())
    monthDown.config(bg=buttonColour.get(),fg=textColour.get())        
    dayUp.config(bg=buttonColour.get(),fg=textColour.get())
    dayDown.config(bg=buttonColour.get(),fg=textColour.get())
    milleniumUp.config(bg=buttonColour.get(),fg=textColour.get())
    milleniumDown.config(bg=buttonColour.get(),fg=textColour.get())        
    centuryUp.config(bg=buttonColour.get(),fg=textColour.get())
    centuryDown.config(bg=buttonColour.get(),fg=textColour.get()) 
    decadeUp.config(bg=buttonColour.get(),fg=textColour.get())
    decadeDown.config(bg=buttonColour.get(),fg=textColour.get())
    yearSmallUp.config(bg=buttonColour.get(),fg=textColour.get())
    yearSmallDown.config(bg=buttonColour.get(),fg=textColour.get())

#MAIN CODE

date = Date()

main = Tk()
main.title("Calendar Generator")
main.resizable(False,False)

month = StringVar()
month.set("January")

day = IntVar()
day.set(date.intDay)

yearSmall = IntVar()
yearSmall.set(date.intYearSmall)
decade = IntVar()
decade.set(date.intDecade)
century = IntVar()
century.set(date.intCentury)
millenium = IntVar()
millenium.set(date.intMillenium)

fullYear = StringVar()
fullYear.set("2 0 1 7")

bgColour = StringVar()
bgColour.set("#fcfcfc")
buttonColour = StringVar()
buttonColour.set("#e2e2e2")
canvasColour = StringVar()
canvasColour.set("white")
highlightColour = StringVar()
highlightColour.set("chartreuse3")
textColour = StringVar()
textColour.set("black")

monthLabel = Label(main,textvariable=month,font=("Arial",12,"bold"),width=8,bg="#fcfcfc")
monthLabel.place(x=15,y=75)
monthUp = Button(main,command=lambda:date.adjustNumber("month",1,12,1),width=8,text="▲",font=("Arial",12,"bold"),relief=FLAT,bg="#e2e2e2")
monthUp.place(x=15,y=35)
monthDown = Button(main,command=lambda:date.adjustNumber("month",1,12,-1),width=8,text="▼",font=("Arial",12,"bold"),relief=FLAT,bg="#e2e2e2")
monthDown.place(x=15,y=105)

dayLabel = Label(main,textvariable=day,font=("Arial",12,"bold"),width=2,anchor=E,bg="#fcfcfc")
dayLabel.place(x=100,y=75)
dayUp = Button(main,command=lambda:date.adjustNumber("day",1,31,1),text="▲",font=("Arial",12,"bold"),relief=FLAT,bg="#e2e2e2")
dayUp.place(x=100,y=35)
dayDown = Button(main,command=lambda:date.adjustNumber("day",1,31,-1),text="▼",font=("Arial",12,"bold"),relief=FLAT,bg="#e2e2e2")
dayDown.place(x=100,y=105)

yearLabel = Label(main,textvariable=fullYear,font=("Arial",12,"bold"),bg="#fcfcfc")
yearLabel.place(x=135,y=75)
milleniumUp = Button(main,command=lambda:date.adjustNumber("millenium",1,9,1),text="▲",width=1,font=("Arial",12,"bold"),relief=FLAT,bg="#e2e2e2")
milleniumUp.place(x=130,y=35)
milleniumDown = Button(main,command=lambda:date.adjustNumber("millenium",1,9,-1),text="▼",width=1,font=("Arial",12,"bold"),relief=FLAT,bg="#e2e2e2")
milleniumDown.place(x=130,y=105)

centuryUp = Button(main,command=lambda:date.adjustNumber("century",0,9,1),text="▲",width=1,font=("Arial",12,"bold"),relief=FLAT,bg="#e2e2e2")
centuryUp.place(x=145,y=35)
centuryDown = Button(main,command=lambda:date.adjustNumber("century",0,9,-1),text="▼",width=1,font=("Arial",12,"bold"),relief=FLAT,bg="#e2e2e2")
centuryDown.place(x=145,y=105)

decadeUp = Button(main,command=lambda:date.adjustNumber("decade",0,9,1),text="▲",width=1,font=("Arial",12,"bold"),relief=FLAT,bg="#e2e2e2")
decadeUp.place(x=160,y=35)
decadeDown = Button(main,command=lambda:date.adjustNumber("decade",0,9,-1),text="▼",width=1,font=("Arial",12,"bold"),relief=FLAT,bg="#e2e2e2")
decadeDown.place(x=160,y=105)

yearSmallUp = Button(main,command=lambda:date.adjustNumber("year",0,9,1),text="▲",width=1,font=("Arial",12,"bold"),relief=FLAT,bg="#e2e2e2")
yearSmallUp.place(x=175,y=35)
yearSmallDown = Button(main,command=lambda:date.adjustNumber("year",0,9,-1),text="▼",width=1,font=("Arial",12,"bold"),relief=FLAT,bg="#e2e2e2")
yearSmallDown.place(x=175,y=105)

#Calendar Text
display = Text(main,font=("Courier",12,"normal"),bd=2,relief=GROOVE,height=12,width=37,bg="white")
display.place(x=220,y=10)
display.config(state=DISABLED)

#"Print Calendar" Button
displayButton = Button(main,text="Display Calendar",width=17,cursor="hand2",font=("Arial",12,"bold"),relief=FLAT,bg="chartreuse3",command=lambda:date.displayCalendarGUI())
displayButton.place(x=15,y=155)

menu = Menu(main)

#"File" Menu
fileMenu = Menu(menu,tearoff=0)
fileMenu.add_command(label="Restore Defaults",command=lambda:date.restoreDefaults())
fileMenu.add_command(label="Exit",command=lambda:main.destroy())
menu.add_cascade(label="File",menu=fileMenu)

themes = Menu(fileMenu)
themes.add_command(label="Simple [Default]",command=lambda:swapGUIColours("Default"))
themes.add_command(label="Day",command=lambda:swapGUIColours("Day"))
themes.add_command(label="Night",command=lambda:swapGUIColours("Night"))
themes.add_command(label="Peachy",command=lambda:swapGUIColours("Peachy"))
themes.add_command(label="Cupcake",command=lambda:swapGUIColours("Cupcake"))
themes.add_command(label="Nightlife",command=lambda:swapGUIColours("Nightlife"))
themes.add_command(label="Casino",command=lambda:swapGUIColours("Casino"))
themes.add_command(label="Bling",command=lambda:swapGUIColours("Bling"))
themes.add_command(label="Fruity",command=lambda:swapGUIColours("Fruity"))
warmthThemes = Menu(themes,tearoff=0)
warmthThemes.add_command(label="Dry",command=lambda:swapGUIColours("Dry"))
warmthThemes.add_command(label="Cool",command=lambda:swapGUIColours("Cool"))
holidayThemes = Menu(themes,tearoff=0)
holidayThemes.add_command(label="Christmas",command=lambda:swapGUIColours("Christmas"))
holidayThemes.add_command(label="Halloween",command=lambda:swapGUIColours("Halloween"))
holidayThemes.add_command(label="Chinese New Year",command=lambda:swapGUIColours("Chinese New Year"))
themes.add_cascade(label="Climate",menu=warmthThemes)
themes.add_cascade(label="Holidays",menu=holidayThemes)
menu.add_cascade(label="Themes",menu=themes)

#"Help" Menu
helpMenu = Menu(menu,tearoff=0)
helpMenu.add_command(label="About",command=lambda:window6LabelsCustomColours("About","Calendar Generator","Version: 2.0","Author: Edward Tang","E-Mail: 335433173@gapps.yrdsb.ca","","",300,110))
helpMenu.add_command(label="Hotkeys",command=lambda:window6LabelsCustomColours("Hotkeys","Hotkeys:","D = Display Calendar","R = Restore Defaults","T/Y/U/I/O/P = Adjust Date Up","G/H/J/K/L/; = Adjust Date Down","F4 = Exit Program",300,160))
menu.add_cascade(label="Help", menu=helpMenu)

main.config(width=605,height=240,menu=menu,bg="#fcfcfc")

main.bind("<d>",lambda _:date.displayCalendarGUI())
main.bind("<r>",lambda _:date.restoreDefaults())
main.bind("<t>",lambda _:date.adjustNumber("month",1,12,1))
main.bind("<g>",lambda _:date.adjustNumber("month",1,12,-1))
main.bind("<y>",lambda _:date.adjustNumber("day",1,31,1))
main.bind("<h>",lambda _:date.adjustNumber("day",1,31,-1))
main.bind("<u>",lambda _:date.adjustNumber("millenium",1,9,1))
main.bind("<j>",lambda _:date.adjustNumber("millenium",1,9,-1))
main.bind("<i>",lambda _:date.adjustNumber("century",0,9,1))
main.bind("<k>",lambda _:date.adjustNumber("century",0,9,-1))
main.bind("<o>",lambda _:date.adjustNumber("decade",0,9,1))
main.bind("<l>",lambda _:date.adjustNumber("decade",0,9,-1))
main.bind("<p>",lambda _:date.adjustNumber("year",0,9,1))
main.bind("<;>",lambda _:date.adjustNumber("year",0,9,-1))
main.bind("<F4>",lambda _:main.destroy())

mainloop()
