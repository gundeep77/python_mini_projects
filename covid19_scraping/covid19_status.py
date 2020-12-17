from plyer import notification as nt
from bs4 import BeautifulSoup
import requests


addr = "https://www.mygov.in/covid-19/"
html_doc = requests.get(addr)

soup = BeautifulSoup(html_doc.content, 'html5lib')

states = soup.find_all('span', {'class' : 'st_name'})
confirmed = soup.find_all('div', {'class': 'tick-confirmed'})
active = soup.find_all('div', {'class': 'tick-active'})
discharged = soup.find_all('div', {'class': 'tick-discharged'})
deaths = soup.find_all('div', {'class': 'tick-death'})

states_list = []
confirmed_list = []
active_list = []
discharged_list = []
deaths_list = []

states_list = [state.text for state in states]
confirmed_list = [confirm.text.strip('Confirmed ') for confirm in confirmed]
active_list = [activ.text.strip('Active ') for activ in active]
discharged_list = [discharge.text.strip('Discharged ') for discharge in discharged]
deaths_list = [deat.text.strip('Deaths ') for deat in deaths]

noti_data = {}

for i in range(len(states_list)):
    if states_list[i] == 'Jharkhand':
        noti_data[states_list[i]] = f"Confirmed : {confirmed_list[i]}\nActive : {active_list[i]}\nDischarged : {discharged_list[i]}\nDeaths : {deaths_list[i]}"
    elif states_list[i] == 'Karnataka':
        noti_data[states_list[i]] = f"Confirmed : {confirmed_list[i]}\nActive : {active_list[i]}\nDischarged : {discharged_list[i]}\nDeaths : {deaths_list[i]}"
    elif states_list[i] == 'Uttar Pradesh':
        noti_data[states_list[i]] = f"Confirmed : {confirmed_list[i]}\nActive : {active_list[i]}\nDischarged : {discharged_list[i]}\nDeaths : {deaths_list[i]}"

for key, val in noti_data.items():
    values = val.split('\n')
    nt.notify(
        title = f"{key} COVID-19 Status",
        message = values[0] + '\n' + values[1] + '\n' + values[2] + '\n' + values[3],
        timeout = 60,
        app_icon = "D:\PythonProjects\Extras\covid19_scraping\coronavirus.ico"
    )
