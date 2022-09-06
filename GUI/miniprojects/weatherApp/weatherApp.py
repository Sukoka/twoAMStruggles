from tkinter import*
import configparser as c#to use the api key in config file
import requests
from requests.api import get 
from tkinter import messagebox #to show the error if the city doesn't exist
from PIL import ImageTk
import PIL.Image

#typical tkinter window
root=Tk()
root.title('What\'s the weather?')
root.geometry('300x220')


#the default api format from the openweather website
#key='api.openweathermap.org/data/2.5/weather?q={city name}&appid={api_key}'
key='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

#getting the data from the config file
config= c.ConfigParser()    
config.read('weatherConfig.ini')
api_key= config['API']['api_key']


#Entry box for your fucking city
c=StringVar()
text= Entry(root,text='Enter your city',width=35,textvariable=c)
text.pack()


def get_weather(city):
    #using get method from requests HTTP 
    #status_code: 200 SUCCESS, 300 REDIRECT, 400 CLIENT ERROR, 500 SERVER ERROR          
    result= requests.get(key.format(city,api_key))
    
    #format i want(country, city, temp_Cel, temp_Fah,icon,condition) according to this tkinter layout
    if result:
        #convert result to json to access it easier
        
        #json data from key link above converted from json formatter website
        #access it like you normally do with json data like dict

        jsonVer= result.json()
        country= jsonVer['sys']['country']
        city= jsonVer['name']
        icon= jsonVer['weather'][0]['icon']
        #the website somehow shows in Kelvin
        temp_Kelvin= jsonVer['main']['temp']
        temp_Cel= temp_Kelvin-273.15    #the fucking formula from (K to C)
        temp_Fah= (temp_Kelvin-273.15) * 9/5 + 32
        condition=jsonVer['weather'][0]['main']
        return_Val=(country, city,icon, temp_Cel, temp_Fah,condition)

        return return_Val   #get_weather function call
    else:
        return None




def search():   #func: for search button
    city_input= c.get()  #user input from the entry box
    weather= get_weather(city_input)
    global img
    if weather:
        #test is an option of location_label
        location_Label['text']= '{}, {}'.format(weather[0], weather[1])
        #icon_holder['bitmap']= 'icons\{}.png'.format(weather[2])
        img['file'] = 'C:\\Users\\LENOVO\\Desktop\\VS\\Python\\GUI shit\\miniprojects\\weatherApp\\icons\\{}.png'.format(weather[2])
        w_temp['text']= '{:.2f}°C , {:.2f}°F'.format(weather[3], weather[4])
        w_condition['text']= '{}'.format(weather[5])
    
    else:
        messagebox.showerror('Error','City not available in this API')

#search button
search_Button=Button(root, text='SEARCH',fg='black', bg='powder blue', command=search)
search_Button.pack()

#Myanmar, Ygn blah blah
location_Label=Label(root, text="", font=(11))
location_Label.pack()

#current date


img = PhotoImage(file= "")
Image = Label(root, image = img)
Image.pack()

#Celsius with Fahrenheit
w_temp=Label(root, text=" ")
w_temp.pack()



#cloudy/rainy blah blah
w_condition=Label(root, text=" ")
w_condition.pack()








root.mainloop()