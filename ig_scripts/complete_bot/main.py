import csv
import option_list


if __name__ == '__main__':
    social_red = input("What acoount do you want to use?: ")
    ACCOUNT = ""
    PASSWORD = ""
    with open('../../src/accounts.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            if(not bool(line)):
                break
            if(line[0] == social_red):
                ACCOUNT = line[1]
                PASSWORD = line[2]
                break

    assert bool(ACCOUNT) and bool(PASSWORD), "Accounts not found"
    option = option_list.option_list()
    option_list.options(option, ACCOUNT, PASSWORD)









