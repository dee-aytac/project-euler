months = [31, 28, 31, 30, 31, 30, 31, 31 , 30, 31, 30, 31]


def count_sundays():
    sunday_count = 0
    day = 1
    for year in range(1901, 2001):
        for idx, month_days in enumerate(months):
            if day % 7 == 6:
                print("New 1th Sunday on 1.{}.{}".format((idx + 1), year))
                sunday_count += 1

            day += month_days
            if year % 4 == 0 and idx == 1:
                day += 1

    return sunday_count

if __name__ == "__main__":
    print(count_sundays())