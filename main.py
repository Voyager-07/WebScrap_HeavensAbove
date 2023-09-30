import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

def buildPlanetsData():
    page = requests.get(
        "https://heavens-above.com/PlanetSummary.aspx?lat=28.7533&lng=77.496&loc=Unnamed&alt=0&tz=UCTm5colon30").text
    soup = BeautifulSoup(page, "html.parser")

    planet_info = soup.find(class_='standardTable')
    lst = ['Right ascension', 'Range (AU)', 'Brightness', 'Constellation', 'Rises', 'Sets', 'Altitude']
    planets = ['Planets','Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

    dataList = []
    # dataList.append(lst)
    dataList.append(planets)
    for row in planet_info.find_all('tr'):
        check = row.contents[0]
        check_text = check.get_text()
        curr = []
        if check_text in lst:
            for cell in row.find_all('td'):
                text = cell.get_text()
                # print(text,end='')
                curr.append(text)
            dataList.append(curr)
    return dataList

# Data for the table
data = buildPlanetsData()

print(data,end='')

# Create a figure and axis
fig, ax = plt.subplots()

# Hide the axis
ax.axis('off')

# Create the table
table = ax.table(cellText=data, loc='center', cellLoc='center')

# Style the table
table.auto_set_font_size(True)
table.set_fontsize(14)
table.scale(1.2, 1.2)

# Show the table plot
plt.show()
