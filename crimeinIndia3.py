import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.offline as ply
import tkinter
from PIL import ImageTk, Image

window = tkinter.Tk()
window.title("MURDER")
window.geometry('700x400')

'''canv = tkinter.Canvas(window, width=700, height=400)
canv.pack()
img = tkinter.PhotoImage(file="img.gif")
canv.create_image(0,0, anchor='center', image=img)'''

window.config(background = "#ff944d")


title = tkinter.Label(window, text='Crime In India State-Wise', bg='pink', fg='blue')
title.config(font = ('Arial Black', 20, 'underline italic'))
title.pack(pady=15)

lbl_state = tkinter.Label(window, text="Enter State", bg="#ff6666")
lbl_state.config(width=10, font = ('sans-serif', 20, 'italic bold'))
ent_state = tkinter.Entry(window)
ent_state.config(width = 10,font=("Calibri",20))


lbl_year = tkinter.Label(window, text="Enter Year", bg="#ff6666")
lbl_year.config(width=10, font = ('sans-serif', 20, 'italic bold'))                      
ent_year = tkinter.Entry(window)
ent_year.config(width = 10,font=("Calibri",20))                             

#state = ent_state.get()
#year = ent_year.get()
           
lbl_state.pack(pady=10)
ent_state.pack()
lbl_year.pack(pady=10)
ent_year.pack()

def State():
    df = pd.read_csv('Crime_Data_Statewise.csv')
    state = ent_state.get()
    year = ent_year.get()
    state = state.upper()
    total = df.loc[(df.STATE_UT == state)&(df.YEAR == int(year)),
                   ['STATE_UT','DISTRICT','YEAR','MURDER']]
    print(total.head())
    i = total[(total.DISTRICT == 'TOTAL')].index
    total = total.drop(i)
    
    trace1 = go.Bar(x = total['DISTRICT'], y = total['MURDER'])
    
    layout = dict(title = 'Murder in : {}'.format(state),
            xaxis = dict(title = 'District'),
            yaxis = dict(title = 'No. of people'))
    
    data = trace1
    fig = dict(data = trace1, layout = layout)
    ply.plot(fig,filename = 'Murder in India DistrictWise in 2012.html')

        
    '''plt.plot(total['DISTRICT'], total['MURDER'], color='g')
    plt.plot(total['DISTRICT'], total['MURDER'], 'Dr')
    plt.xlabel('District of States')
    plt.ylabel('Total No of Deaths')
    plt.xticks(rotation=60)
    plt.show()

    plt.bar(total['DISTRICT'], total['MURDER'], color='g')
    plt.xlabel('District of States')
    plt.ylabel('Total No of Deaths')
    plt.xticks(rotation=60)
    plt.show()'''
    

   
btn = tkinter.Button(window, text="Show Graph", command=State, bg='#00cc00', fg='#800000') 
btn.config(width=10, font = ('italic bold', 20, 'underline italic bold') )  

btn.pack(pady=20)   
    
window.mainloop()



