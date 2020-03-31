from urllib import request
import re


def visit_web():
    URL = "https://www.gofundme.com/f/jhg4z-6000/donations"
    # open the URL
    req = request.urlopen(URL)
    # read the URL
    html = req.read()
    # decode the URL to utf-8
    decoded = html.decode("utf_8")
    # split at string "donations": and take the end part (pretty much stripping the front)
    data = decoded.split('"donations":', 1)[-1]
    # split at string "identity": and keep the beginning part
    data = data.split(',"identity"', 1)[0]
    # split all the data into a list, every element represents one person
    filtered_list = data.split('},')

    result = []

    for line in filtered_list:
        d = {}
        # keeps data between "amount": and "created_at" (this is where the name and donation amount is located)
        searched = re.search('"amount":(.*)"created_at"', line)
        # removes everything between "is_offline" and "name" (this is the useless info between name and donation)
        stripped = re.sub('"is_offline"(.*)"name"', "", searched.group(1))
        # removes all commas(,) and double quotations(")
        stripped2 = re.sub('[\",]', "", stripped)
        # takes remaining string and splits into list using : as delimeter
        d = stripped2.split(":")
        # append every line (still info per person, this time only has donation and name) into the result list
        result.append(d)

    with open('netrobotresults.csv', 'w') as file:
        file.write('Name,Donation')
        # Write the table's titles of the csv file
        for line in result:
            file.write('\n')
            # insert the name and donation to the csv file
            file.write(line[1] + ',' + line[0])


if __name__ == '__main__':
    visit_web()
