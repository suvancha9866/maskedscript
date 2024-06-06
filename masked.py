import requests
import schedule
import time
import PySimpleGUI as sg


api_key = open('api.txt', 'r').read()
font = ("@Microsoft YaHei UI","12")
sg.theme("TanBlue")
#LightGreen1
layout = [[sg.Text("Pollen Levels:")], [sg.Button("Aurora"), sg.Button("Champaign")]]
window = sg.Window("Masked", layout, margins=(50, 50), font=font)
num_location = ''

event, values = window.read()
if event == "Aurora":
    num_location = "328770"
elif event == "Champaign":
    num_location = '328774'

window.close()

result = requests.get(f'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{num_location}?apikey={api_key}&details=true')
grass = result.json()["DailyForecasts"][0]["AirAndPollen"][1]["Category"]
mold = result.json()['DailyForecasts'][0]["AirAndPollen"][2]["Category"]
ragweed = result.json()['DailyForecasts'][0]["AirAndPollen"][3]["Category"]
tree = result.json()['DailyForecasts'][0]["AirAndPollen"][4]["Category"]

layout2 = [[sg.Image('grass.png'), sg.Text("Grass:"), sg.Text(grass)], [sg.Image('mold.png'), sg.Text("Mold:"), sg.Text(mold)], [sg.Image('ragweed.png'), sg.Text("Ragweed:"), sg.Text(ragweed)], [sg.Image('tree.png'), sg.Text("Tree:"), sg.Text(tree)], [sg.Button("Done")]]
window2 = sg.Window("Masked Results", layout2, margins = (50, 50), font=font)
event2, values2 = window2.read()
if event2 == "Done" or event == sg.WIN_CLOSED:
    window2.close()

'''
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Aurora":
        num_location = "328770"
    elif event == "Champaign":
        num_location = '328774'
    elif event == "OK" or event == sg.WIN_CLOSED:
        break
    
    result = requests.get(f'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{num_location}?apikey={api_key}&details=true')
    

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

window = sg.Window("Masked", layout, margins=(200, 100))

while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()

api_key = open('api.txt', 'r').read()

location = input("Location: ")

num_location = ''
if location == 'A':
    num_location = '328770'
elif location == 'C':
    num_location = '328774'

result = requests.get(f'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{num_location}?apikey={api_key}&details=true')

def job():
    print(result.json()['DailyForecasts'][0]["AirAndPollen"][1]["Category"]) # Grass
    print(result.json()['DailyForecasts'][0]["AirAndPollen"][2]["Category"]) # Mold
    print(result.json()['DailyForecasts'][0]["AirAndPollen"][3]["Category"]) # Ragweed
    print(result.json()['DailyForecasts'][0]["AirAndPollen"][4]["Category"]) # Tree 

schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

    layout = [[sg.Text('Aurora Champaign', size=(30, 1), key='-text-')],
          [sg.T('Font:'),sg.Combo(sg.Text.fonts_installed_list(),default_value=sg.DEFAULT_FONT[0],
                                  key='-font-',  enable_events=True)],
          [sg.CB('Bold', key='-bold-', change_submits=True),
           sg.CB('Italics', key='-italics-', change_submits=True),
           sg.CB('Underline', key='-underline-', change_submits=True),
           sg.CB('OverStrike', key='-overstrike-', change_submits=True)],
          [sg.Slider((6, 50), default_value=sg.DEFAULT_FONT[1], size=(14, 20),
                     orientation='h', key='-slider-', change_submits=True),
           sg.Text('Font size')],
          [sg.Text('Font string = '), sg.Text(f'{sg.DEFAULT_FONT}', size=(50, 1), key='-fontstring-')],
          [sg.Button('Exit')]]

window = sg.Window('Font string builder', layout)

text_elem = window['-text-']
while True:     # Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    values['-font-'] + " "
    str(int(values['-slider-']))
    style = ""
    if values['-bold-']:
        style += 'bold '
    if values['-italics-']:
        style += 'italic '
    if values['-underline-']:
        style += 'underline '
    if values['-overstrike-']:
        style += 'overstrike '
    newFont = (values['-font-'],"{:.0f}".format(values['-slider-']),style)
    #text_elem.update(font=newFont)
    window['-text-'].update(font=newFont)
    window['-fontstring-'].update(value = str(newFont))

window.close()
'''