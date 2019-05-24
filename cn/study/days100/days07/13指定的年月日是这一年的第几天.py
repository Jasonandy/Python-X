def is_leap_year(year):
    """
    判断指定的年份是不是闰年
    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    """
    计算传入的日期是这一年的第几天
    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    # [[a],[b]][0] = [a]
    # [[a],[b]][1] = [b]
    # 数据结构 每个月的天数
    total = 0
    # 遍历12个月  1994 11 15
    # 11-1 = 10   也就是10往前每个月加起来 在加上当月的天数
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


def main():
    print(which_day(1994, 12, 17))
    print(which_day(1994, 11, 15))
    print(which_day(1994, 10, 3))
    print(which_day(1997, 5, 26))


def is_leap_years(n=10):
    for year in range(2010, 2010+n):
        if is_leap_year(year):
            print("该年是闰年:", year, is_leap_year(year))
        else:
            print("该年不是闰年:", year, is_leap_year(year))


# 判断是不是闰年
if __name__ == '__main__':
    main()
    is_leap_years()

