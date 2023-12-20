from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
import requests

url_api="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
api_file='weather.key'
file_a=ConfigParser()
file_a.read(api_file)
api_key=file_a['api_key']['key']

def weather_find(city):
    final=requests.get(url_api.format(city,api_key))
    if final:
        json_file=final.json()
        city=json_file['name']
        country_name=json_file['sys']['country']
        k_temparature=json_file['main']['temp']
        c_temparature=k_temparature-273.15
        f_temparature=(k_temparature-273.15)*9/5+32
        weather_display=json_file['weather'][0]['main']
        result=(city,country_name,c_temparature,f_temparature,weather_display)

        return result
    else:
        return None

def print_weather():
    city=search_city.get()
    weather=weather_find(city)
    if weather:
        location_entry['text']='{},{}'.format(weather[0],weather[1])
        temperature_entry['text']='{:.2f}C,{:.2f}F'.format(weather[2],weather[3])
        weather_entry['text']=weather[4]

    else:
        messagebox.showerror('ERROR','Please enter corret city.the entered city cant find')


root=Tk()
root.title("WEATHER TELLER")
root.config(background="black")
root.geometry("700x400")

search_city=StringVar()
enter_city=Entry(root,textvariable=search_city,fg="blue",font=("Arial",30,"bold"),width=30)
enter_city.pack()

search_button=Button(root,text='Search Weather!',width=20,bg="red",fg="white",font=("Arial",25,"bold"),command=print_weather)
search_button.pack()

location_entry=Label(root,text='',font=("Arial",35,"bold"),bg="lightblue")
location_entry.pack()

temperature_entry=Label(root,text='',font=("Arial",35,"bold"),bg="lightpink")
temperature_entry.pack()

weather_entry=Label(root,text='',font=("Arial",35,"bold"),bg="lightgreen")
weather_entry.pack()

root.mainloop()
