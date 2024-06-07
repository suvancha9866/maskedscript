import requests
import PySimpleGUI as sg


api_key = open('api.txt', 'r').read()
font = ("@Microsoft YaHei UI","12")
sg.theme("LightBrown10")
#LightGreen1
while True:
    layout = [[sg.Text("City Pollen Levels:", font=("@Microsoft YaHei UI","12", "bold"))], [sg.Button("Aurora"), sg.Button("Champaign")]]
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
    #Masked Math:
    grass_val = result.json()["DailyForecasts"][0]["AirAndPollen"][1]["CategoryValue"] * 2
    mold_val = result.json()['DailyForecasts'][0]["AirAndPollen"][2]["CategoryValue"] * 1
    ragweed_val = result.json()['DailyForecasts'][0]["AirAndPollen"][3]["CategoryValue"] * 3
    tree_val = result.json()['DailyForecasts'][0]["AirAndPollen"][4]["CategoryValue"] * 4
    total = (grass_val + mold_val + ragweed_val + tree_val) / 10
    threshold = 2.6
    output_text = ''
    if total >= threshold:
        output_text = 'Yes Mask'
    else:
        output_text = 'No Mask'
    layout2 = [[sg.Text(event, font=("@Microsoft YaHei UI","12", "bold"))],
            [sg.Image('grass.png'), sg.Text("Grass:", font=("@Microsoft YaHei UI","12", "bold")), sg.Text(grass)], 
            [sg.Image('mold.png'), sg.Text("Mold:", font=("@Microsoft YaHei UI","12", "bold")), sg.Text(mold)], 
            [sg.Image('ragweed.png'), sg.Text("Ragweed:", font=("@Microsoft YaHei UI","12", "bold")), sg.Text(ragweed)], 
            [sg.Image('tree.png'), sg.Text("Tree:", font=("@Microsoft YaHei UI","12", "bold")), sg.Text(tree)], 
            [sg.Image('mask.png'), sg.Text("Masked:", font=("@Microsoft YaHei UI","12", "bold")), sg.Text(output_text)], [sg.Button("Back"), sg.Button("Done")]]
    window2 = sg.Window("Masked Results", layout2, margins = (50, 50), font=font)
    event2, values2 = window2.read()
    if event2 == "Done" or event == sg.WIN_CLOSED:
        break
    window2.close()
window2.close()