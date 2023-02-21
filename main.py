# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from send_email import send_email

url = "https://newsapi.org/v2/everything?q=tesla&from=2022-12-24&sortBy=publishedAt&apiKey=" \
      "323f598e45f74073a8a5db1a28005041"
api_key = "323f598e45f74073a8a5db1a28005041"

# made request
request = requests.get(url)

# got a dictionary of data
content = request.json()
print(content)

# accessed article titles and descriptions
body = ""
for article in content["articles"]:
      if article['title'] is not None:
            body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode('utf-8')
send_email(message=body)

print(body)





# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
