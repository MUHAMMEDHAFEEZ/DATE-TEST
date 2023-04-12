import PySimpleGUI as psg
import calendar
from datetime import datetime

dates = [i for i in range(1,32)]
day = psg.Spin(dates,initial_value=1,readonly=True,size=3,enable_events=True,key='-DAY-')
months = calendar.month_abbr[1:]
month = psg.Spin(months,initial_value='Jan',readonly=True, size=10,enable_events=True,key='-MON-')
years = [ i for i in range(2000,3000)]
year = psg.Spin(years,initial_value=2000,readonly=True,size=5,enable_events=True,key="-YR-")
layout=[
    [psg.Text('DATE'),day,psg.Text("MONTH"),month,psg.Text("YEAR"),year],
    [psg.Ok(),psg.Text("",key='-OUT-'),psg.Button("close",key='-CLOSE-')]
]

window = psg.Window('DATE', layout, font='_ 18', size=(700, 100))
while True:
    event, values = window.read()
    if(event == 'Ok'):
        date = str(values['-DAY-']) + " " + str(values['-MON-']) + "," +str(values['-YR-'])
    try:
       d = datetime.strptime(date, '%d %b,%Y')
       window['-OUT-'].update("Date: {}".format(date))
    except:
        window['-OUT-'].update("")
        psg.popup("INvaild date")
        if event == psg.WIN_CLOSED:
            break
    if event == '-CLOSE-':
            break     
window.close()
