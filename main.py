# Игра Donkey.bas на языке Python

import tkinter as tk
import time
from random import randint
import winsound
screen = tk.Tk()
screen.iconbitmap('resources\img\icon.ico')
screen.title('Donkey on Python')
screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()
screen_width = 718
screen_height = 418
x = (screen_width // 2) - (screen_width // 2)
y = (screen_height // 2) - (screen_height // 2)
screen.geometry(f'{screen_width}x{screen_height}+{x}+{y}')
screen.resizable(False, False)
screen.image = tk.PhotoImage(file='resources\img\zf.png')
bg = tk.Label(screen, image=screen.image)
bg.grid(row=0, column=0)
bg.config(bg='#555555')
esc_lbl = tk.Label(screen, text='Press Esc to exit', bg='#555555', fg='#C0C0C0', font=('Comic Sans MS', 16, 'bold'))
esc_lbl.place(x=500, y=345)
def exit(event):
    if event.keysym == 'Escape':
        screen.destroy()
screen.bind('<KeyPress-Escape>', exit)
donkey_lbl = tk.Label(screen, text='Donkey', bg='#555555', fg='#C0C0C0', font=('Comic Sans MS', 16, 'bold'))
donkey_lbl.place(x=26, y=40)
donkey_count = tk.Label(screen, text=0, bg='#555555', fg='#C0C0C0', font=('Comic Sans MS', 16, 'bold'))
donkey_count.place(x=26, y=90)
donkey_loses = tk.Label(screen, text='Donkey loses!', bg='#555555', fg='#C0C0C0', font=('Comic Sans MS', 16, 'bold'))
donkey_loses.place(x=1000, y=1000)
def donkey_points_count():
    donkey_count['text'] = int(donkey_count['text']) + 1
donkey_wins = tk.PhotoImage(file='resources\img\donkey_wins.png')
donkey_wins_label = tk.Label(screen)
donkey_wins_label.image = donkey_wins
donkey_wins_label['image'] = donkey_wins_label.image
donkey_wins_label.place(x=1000, y=1000)
donkey_wins_label.config(bg='#555555')
car_lbl = tk.Label(screen, text='Driver', bg='#555555', fg='#C0C0C0', font=('Comic Sans MS', 16, 'bold'))
car_lbl.place(x=500, y=40)
car_count = tk.Label(screen, text=0, bg='#555555', fg='#C0C0C0', font=('Comic Sans MS', 16, 'bold'))
car_count.place(x=500, y=90)
driver_loses = tk.Label(screen, text='Driver loses!', bg='#555555', fg='#C0C0C0', font=('Comic Sans MS', 16, 'bold'))
driver_loses.place(x=1000, y=1000)
def driver_points_count():
    car_count['text'] = int(car_count['text']) + 1
driver_wins = tk.PhotoImage(file='resources\img\driver_wins.png')
driver_wins_label = tk.Label(screen)
driver_wins_label.image = driver_wins
driver_wins_label['image'] = driver_wins_label.image
driver_wins_label.place(x=1000, y=1000)
driver_wins_label.config(bg='#555555')
car = tk.PhotoImage(file='resources\img\car.png')
car_label = tk.Label(screen)
car_label.image = car
car_label['image'] = car_label.image
car_y = 280
car_label.place(x=250, y=car_y)
car_label.config(bg='#555555')
car_y_initial = 280
def move_car(event):
    if car_y == 100:
        return
    else:
        if event.keysym == 'Right':
            car_label.place(x=380)
        elif event.keysym == 'Left':
            car_label.place(x=250)
        winsound.PlaySound('resources\sounds\move_car.wav', 1)
screen.bind('<KeyPress-Right>', move_car)
screen.bind('<KeyPress-Left>', move_car)
def restart_game():
    global car_y, car_y_initial
    car_y = car_y_initial
    car_label.place(x=250)
    donkey_loses.place(x=1000, y=1000)
    driver_wins_label.place(x=1000, y=1000)
    if car_count['text'] == 10:
        car_count['text'] = int(car_count['text']) * 0
        donkey_count['text'] = int(donkey_count['text']) * 0
    change_road()
donkey = tk.PhotoImage(file='resources\img\donkey.png')
donkey_label = tk.Label(screen)
donkey_label.image = donkey
donkey_label['image'] = donkey_label.image
donkey_x = 365
donkey_y = -40
donkey_label.place(x=donkey_x, y=donkey_y)
donkey_label.config(bg='#555555')
donkey_y_initial = -1340
def restart_game_2():
    global car_y, car_y_initial, donkey_y, donkey_y_initial
    car_y = car_y_initial
    car_label.place(x=250, y=car_y)
    donkey_y = donkey_y_initial
def driver_loses_f():
    driver_loses.place(x=1000, y=1000)
def restart_game_3():
    global car_y, car_y_initial, donkey_y, donkey_y_initial
    car_y = car_y_initial
    car_label.place(x=250, y=car_y)
    donkey_y = donkey_y_initial
    if donkey_count['text'] == 10:
        donkey_count['text'] = int(donkey_count['text']) * 0
        car_count['text'] = int(car_count['text']) * 0
def donkey_wins_f():
    donkey_wins_label.place(x=1000, y=1000)
def check_collision():
    car_x = car_label.winfo_rootx()
    car_y = car_label.winfo_rooty()
    donkey_x = donkey_label.winfo_rootx()
    donkey_y = donkey_label.winfo_rooty()
    if car_x >= donkey_x and car_x <= donkey_x + donkey.width() and \
            car_y >= donkey_y and car_y <= donkey_y + donkey.height():
        donkey_points_count()
        winsound.PlaySound('resources\sounds\image_collision.wav', 1)
        if donkey_count['text'] < 10:
            driver_loses.place(x=26, y=140)
            restart_game_2()
            screen.after(2500, driver_loses_f)
        else:
            donkey_wins_label.place(x=498, y=225)
            restart_game_3()
            screen.after(2500, donkey_wins_f)
moving = False
def donkey_move():
    global moving, donkey_y, car_y
    if moving:
        return
    moving = True
    donkey_y += 50
    donkey_label.place(y=donkey_y)
    screen.after(1000, check_collision)
    if donkey_y == 360:
        donkey_x = 365 if randint(1, 2) == 1 else 230
        donkey_y = -40
        donkey_label.place(x=donkey_x, y=donkey_y)
        car_y -= 20
        car_label.place(y=car_y)
        if car_y == 100:
            driver_points_count()
            donkey_x = 1000
            donkey_label.place(x=donkey_x)
            if car_count['text'] < 10:
                donkey_loses.place(x=500, y=140)
                screen.after(2500, donkey_move)
                screen.after(2500, restart_game)
            else:
                driver_wins_label.place(x=498, y=225)
                screen.after(2500, donkey_move)
                screen.after(2500, restart_game)
        else:
                screen.after(110, donkey_move)
    else:
        screen.after(110, donkey_move)
    moving = False
road_label = tk.Label(screen)
road_label.place(x=308, y=5)
def change_road():
    if car_y == 100:
        return
    else:
        current_time = (int(time.time() * 20) % 3) + 1
        road = tk.PhotoImage(file='resources\img\doroga_{}.png'.format(current_time))
        road_label.image = road
        road_label['image'] = road_label.image
        road_label.config(bg='#555555')
        screen.after(10, change_road)
donkey_move()
change_road()
screen.mainloop()