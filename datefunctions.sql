-- Get the current system date and time
SELECT GETDATE() as CurrentDate;

-- Also returns the current date and time (same as GETDATE)
SELECT CURRENT_TIMESTAMP as DateTime;

-- Returns the current date and time with higher precision (includes fractions of a second)
SELECT SYSDATETIME() as SysDateTime;

-- Adds 5 years to the current date
SELECT DATEADD(YEAR, 5, GETDATE()) as Add5Years;

-- Adds 2 months to the given date ('2025-05-09')
SELECT DATEADD(MONTH, 2, '2025-05-09') as MonthAdd;

-- Adds 20 days to the current date
SELECT DATEADD(DAY, 20, GETDATE()) as DayAdd;

-- Calculates the number of days between today and May 29, 2025
SELECT DATEDIFF(DAY, GETDATE(), '2025-05-29') as DayDiff;

-- Calculates the number of months between today and September 29, 2025
SELECT DATEDIFF(MONTH, GETDATE(), '2025-09-29') as MonthDiff;

-- Calculates the number of years between today and May 29, 2030
SELECT DATEDIFF(YEAR, GETDATE(), '2030-05-29') as YearDiff;

-- Calculates the number of quarters between today and September 29, 2025
SELECT DATEDIFF(QUARTER, GETDATE(), '2025-09-29') as QuarterDiff;

-- Extracts the current year from the current date
SELECT DATEPART(YEAR, GETDATE()) as Year;

-- Extracts the current month from the current date
SELECT DATEPART(MONTH, GETDATE()) as Month;

-- Extracts the day (date) part of the current date
SELECT DATEPART(DAY, GETDATE()) as Date;

-- Gets the start date of the current quarter
SELECT DATEADD(QUARTER, (DATEDIFF(QUARTER, 0, GETDATE())), 0) as CurrentQuarterStartDate;

-- Gets the start date of the next quarter
SELECT DATEADD(QUARTER, (DATEDIFF(QUARTER, 0, GETDATE()) + 1), 0) as NextQuarterStartDate;

-- Gets the start date of the previous quarter
SELECT DATEADD(QUARTER, (DATEDIFF(QUARTER, 0, GETDATE()) - 1), 0) as PreviousQuarterStartDate;

-- Gets the end date of the previous quarter
SELECT DATEADD(DAY, -1, DATEADD(QUARTER, (DATEDIFF(QUARTER, 0, GETDATE())), 0)) as PreviousQuarterEndDate;

-- Gets the end date of the current quarter
SELECT DATEADD(DAY, -1, DATEADD(QUARTER, (DATEDIFF(QUARTER, 0, GETDATE()) + 1), 0)) as CurrentQuarterEndDate;

-- Gets the end date of the next quarter
SELECT DATEADD(DAY, -1, DATEADD(QUARTER, (DATEDIFF(QUARTER, 0, GETDATE()) + 2), 0)) as NextQuarterEndDate;

-- Gets the start date of the previous month
SELECT DATEADD(MONTH, -1, DATEADD(DAY, 1 - DAY(GETDATE()), GETDATE())) as PreviousMonthStartDate;

-- Gets the start date of the current month
SELECT DATEADD(DAY, 1 - DAY(GETDATE()), GETDATE()) as CurrentMonthStartDate;

-- Gets the start date of the next month
SELECT DATEADD(MONTH, 1, DATEADD(DAY, 1 - DAY(GETDATE()), GETDATE())) as NextMonthStartDate;

-- Gets the end date of the previous month
SELECT EOMONTH(DATEADD(MONTH, -1, GETDATE())) as PreviousMonthEndDate;

-- Gets the end date of the current month
SELECT EOMONTH(GETDATE()) as EndOfCurrentMonth;

-- Gets the end date of the next month
SELECT EOMONTH(DATEADD(MONTH, 1, GETDATE())) as NextMonthEndDate;
