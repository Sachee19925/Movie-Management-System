
#Main Frame
from pathlib import Path
import tkinter as tk
from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk, ImageOps
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\course\tkinter proj\MMS\build\assets\frame5")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1920x1024")
window.configure(bg = "#13101D")
window.state("zoomed") #Enter Full screen

frame1 = tk.Frame(window,bg="#13101D")
frame1.place(relwidth=1,relheight=1)
# Shift Frames
def gotoframes(frame):
    frame.tkraise()

canvas = Canvas(
    frame1,
    bg = "#13101D",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1920.0,
    146.0,
    fill="#251443",
    outline="")

canvas.create_text(
    625.0,
    15.0,
    anchor="nw",
    text="Cinema World",
    fill="#A2C496",
    font=("Irish Grover", 96 * -1),
    justify="center"
)

canvas.create_text(
    55.0,
    865.0,
    anchor="nw",
    text="Movies, also known as films, are one of the most powerful and popular forms of storytelling and entertainment in the modern world. Combining visual imagery, sound, dialogue, and music, ",
    fill="#A2C496",
    font=("Sansita", 18),
    justify="center"
)
canvas.create_text(
    115.0,
    905.0,
    anchor="nw",
    text="movies transport audiences into different worlds real or imagined to evoke emotion, convey messages, and tell stories that reflect cultures, histories, and human experiences.",
    fill="#A2C496",
    font=("Sansita", 18),
    justify="center"
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    frame1,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: gotoframes(frame2_add_movie),
    relief="flat",
    bg="#13101D",
    activebackground="#13101D"
)
button_1.place(
    x=460.0,
    y=320.0,
    width=151.0,
    height=55.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    frame1,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: gotoframes(frame3_Update_frame),
    relief="flat",
    bg="#13101D",
    activebackground="#13101D"
)
button_2.place(
    x=680.0,
    y=320.0, #178
    width=218.0,
    height=55.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    frame1,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: gotoframes(frame4_browse_frame),
    relief="flat",
    bg="#13101D",
    activebackground="#13101D"
)
button_3.place(
    x=970.0,
    y=320.0,
    width=201.0,
    height=55.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    frame1,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: gotoframes(frame5_delete_frame),
    relief="flat",
    bg="#13101D",
    activebackground="#13101D"
)
button_4.place(
    x=1251.0,
    y=320.0,
    width=201.0,
    height=55.0
)

canvas.create_text(
    460.0, #49
    240.0, #240
    anchor="nw",
    text="Your centralized platform for efficiently managing your movie database",
    fill="#B4E45C",
    font=("Inknut Antiqua", 25 * -1)
)

canvas.create_text(
    279.0, #49
    140.0, #240
    anchor="nw",
    text="🎬 Welcome to Cinema World - Your Ultimate Movie Destination!",
    fill="#DEB743",
    font=("Inknut Antiqua", 40 * -1)
)

canvas.create_text(
    40.0, #49
    440.0, #240
    anchor="nw",
    text="Popular Movies",
    fill="#B4E45C",
    font=("Inknut Antiqua", 25 * -1)
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    frame1,
    image=button_image_5,
    borderwidth=6,
    highlightthickness=0,
    command=lambda: print("dark-knight"),
    relief="flat",
    bg="#B6B3B3",
    activebackground="#13101D"
)

button_5.place(
    x=40.0,
    y=520.0,
    width=180.0,
    height=270.0
)

canvas.create_text(
    40.0, #49
    788.0, #240
    anchor="nw",
    text="The Dark Knight",
    fill="#EFCED2",
    font=("Inknut Antiqua", 12 * -1)
)

canvas.create_text(
    40.0, #49
    805.0, #240
    anchor="nw",
    text="2008",
    fill="#EFCED2",
    font=("Inknut Antiqua", 12 * -1)
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    frame1,
    image=button_image_6,
    borderwidth=6,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat",
    bg="#B6B3B3",
    activebackground="#13101D"
)

button_6.place(
    x=240.0,
    y=520.0,
    width=180.0,
    height=270.0
)

canvas.create_text(
    240.0, #49
    788.0, #240
    anchor="nw",
    text="Avengers: Infinity War",
    fill="#EFCED2",
    font=("Inknut Antiqua", 12 * -1)
)

canvas.create_text(
    240.0, #49
    805.0, #240
    anchor="nw",
    text="2018",
    fill="#EFCED2",
    font=("Inknut Antiqua", 12 * -1)
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    frame1,
    image=button_image_7,
    borderwidth=6,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat",
    bg="#B6B3B3",
    activebackground="#13101D"
)

button_7.place(
    x=445.0,
    y=520.0,
    width=180.0,
    height=270.0
)
canvas.create_text(
    445.0, #49
    788.0, #240
    anchor="nw",
    text="Avengers: Endgame",
    fill="#EFCED2",
    font=("Inknut Antiqua", 12 * -1)
)

canvas.create_text(
    445.0, #49
    805.0, #240
    anchor="nw",
    text="2019",
    fill="#EFCED2",
    font=("Inknut Antiqua", 12 * -1)
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    frame1,
    image=button_image_8,
    borderwidth=6,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat",
    bg="#B6B3B3",
    activebackground="#13101D"
)

button_8.place(
    x=655.0,
    y=520.0,
    width=180.0,
    height=270.0
)

canvas.create_text(
    655.0, #49
    788.0, #240
    anchor="nw",
    text="Venom: The Last Dance",
    fill="#EFCED2",
    font=("Inknut Antiqua", 12 * -1)
)

canvas.create_text(
    655.0, #49
    805.0, #240
    anchor="nw",
    text="2024",
    fill="#EFCED2",
    font=("Inknut Antiqua", 12 * -1)
)

Interstellar_2014 = PhotoImage(
    file=relative_to_assets("Interstellar.png"))
Interstellar = Button(
    frame1,
    image=Interstellar_2014,
    borderwidth=6,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat",
    bg="#B6B3B3",
    activebackground="#13101D"
)

Interstellar.place(
    x=865.0,
    y=520.0,
    width=180.0,
    height=270.0
)

canvas.create_text(
    865.0, #49
    788.0, #240
    anchor="nw",
    text="Interstellar",
    fill="#EFCED2",
    font=("Inknut Antiqua", 12 * -1)
)

canvas.create_text(
    865.0, #49
    805.0, #240
    anchor="nw",
    text="2014",
    fill="#EFCED2",
    font=("Inknut Antiqua", 12 * -1)
)

inception_2010 = PhotoImage(
    file=relative_to_assets("inception.png"))
inception = Button(
    frame1,
    image=inception_2010,
    borderwidth=6,
    highlightthickness=0,
    command=lambda: print("inception clicked"),
    relief="flat",
    bg="#B6B3B3",
    activebackground="#13101D"
)

inception.place(
    x=1075.0,
    y=520.0,
    width=180.0,
    height=270.0
)

canvas.create_text(
    1075.0, #49
    788.0, #240
    anchor="nw",
    text="Inception",
    fill="#EFCED2",
    font=("Inknut Antiqua", 12 * -1)
)

canvas.create_text(
    1075.0, #49
    805.0, #240
    anchor="nw",
    text="2010",
    fill="#EFCED2",
    font=("Inknut Antiqua", 12 * -1)
)

Oppenheimer_2023 = PhotoImage(
    file=relative_to_assets("Oppenheimer.png"))
Oppenheimer = Button(
    frame1,
    image=Oppenheimer_2023,
    borderwidth=6,
    highlightthickness=0,
    command=lambda: print("Oppenheimer clicked"),
    relief="flat",
    bg="#B6B3B3",
    activebackground="#13101D"
)

Oppenheimer.place(
    x=1280.0,
    y=520.0,
    width=180.0,
    height=270.0
)

canvas.create_text(
    1280.0, #49
    788.0, #240
    anchor="nw",
    text="Oppenheimer",
    fill="#EFCED2",
    font=("Inknut Antiqua", 12 * -1)
)

canvas.create_text(
    1280.0, #1310
    805.0, #240
    anchor="nw",
    text="2023",
    fill="#EFCED2",
    font=("Inknut Antiqua", 12 * -1)
)

John_Wick_2014 = PhotoImage(
    file=relative_to_assets("John Wick.png"))
JohnWick = Button(
    frame1,
    image=John_Wick_2014,
    borderwidth=6,
    highlightthickness=0,
    command=lambda: print("John Wick clicked"),
    relief="flat",
    bg="#B6B3B3",
    activebackground="#13101D"
)

JohnWick.place(
    x=1485.0,
    y=520.0,
    width=180.0,
    height=270.0
)

canvas.create_text(
    1485.0, #49
    788.0, #240
    anchor="nw",
    text="John Wick",
    fill="#EFCED2",
    font=("Inknut Antiqua", 12 * -1)
)

canvas.create_text(
    1485.0, #1310
    805.0, #240
    anchor="nw",
    text="2014",
    fill="#EFCED2",
    font=("Inknut Antiqua", 12 * -1)
)

How_to_Train_Your_Dragon_2025 = PhotoImage(
    file=relative_to_assets("How to Train Your Dragon.png"))
How_to_Train_Your_Dragon = Button(
    frame1,
    image=How_to_Train_Your_Dragon_2025,
    borderwidth=6,
    highlightthickness=0,
    command=lambda: print("How to Train Your Dragon clicked"),
    relief="flat",
    bg="#B6B3B3",
    activebackground="#13101D"
)

How_to_Train_Your_Dragon.place(
    x=1692.0,
    y=520.0,
    width=180.0,
    height=270.0
)

canvas.create_text(
    1692.0, #49
    788.0, #240
    anchor="nw",
    text="How to Train Your Dragon",
    fill="#EFCED2",
    font=("Inknut Antiqua", 12 * -1)
)

canvas.create_text(
    1692.0, #1520
    805.0, #240
    anchor="nw",
    text="2025",
    fill="#EFCED2",
    font=("Inknut Antiqua", 12 * -1)
)


#Add Movie Frame


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\course\tkinter proj\MMS\build\assets\frame4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


frame2_add_movie = tk.Frame(window)
frame2_add_movie.place(relwidth=1,relheight=1)

canvas = Canvas(
    frame2_add_movie,
    bg = "#13101D",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1920.0,
    146.0,
    fill="#251443",
    outline="")

canvas.create_text(
    625.0,
    15.0,
    anchor="nw",
    text="Cinema World",
    fill="#A2C496",
    font=("Irish Grover", 96 * -1),
    justify="center"
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 =tk.Button(
    frame2_add_movie,
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: gotoframes(frame1),
    relief="flat",
    bg="#13101D",
    activebackground="#13101D"

)
button_9.place(
    x=15.0,
    y=165.0,
    width=109.0,
    height=47.0
)

def press_add_button():
    try:
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "movielist"
        )

        if conn.is_connected():
            print("connected")

        cursor = conn.cursor()
        sql_1 = "insert into moviedetails values (%s,%s,%s,%s,%s,%s,%s)"
        data = (
            id_entry_1.get(),
            name_entry_1.get(),
            year_entry_1.get(),
            language_entry_1.get(),
            genre_entry_1.get(),
            rating_entry_1.get(),
            quality_entry_1.get()
            )
        cursor.execute(sql_1,data)
        conn.commit()
        conn.close()

        id_entry_1.delete(0, END)
        name_entry_1.delete(0, END)
        year_entry_1.delete(0, END)
        language_entry_1.delete(0, END)
        genre_entry_1.delete(0, END)
        rating_entry_1.delete(0, END)
        quality_entry_1.delete(0, END)
        messagebox.showinfo("Info", "Data Inserted Successfully!")
        save_and_refresh()
    except:
        print("error")

ADD = PhotoImage(
    file=relative_to_assets("ADD.png"))
add =tk.Button(
    frame2_add_movie,
    image=ADD,
    borderwidth=0,
    highlightthickness=0,
    command=press_add_button,
    relief="flat",
    bg="#13101D",
    activebackground="#13101D"

)
add.place(
    x=280.0,
    y=940.0,
    width=109.0,
    height=47.0
)

canvas.create_text(
    200.0,
    200.0,
    anchor="nw",
    text="ADD A NEW MOVIE",
    fill="#FF3A3E",
    font=("Sansita", 45 * -1)
)

canvas.create_text(
    170.0, #42
    276.0,
    anchor="nw",
    text="ID",
    fill="#FFFFFF",
    font=("Sawarabi Mincho", 40 * -1)
)

canvas.create_text(
    100.0, #45
    376.0,
    anchor="nw",
    text="Name",
    fill="#FFFFFF",
    font=("Sawarabi Mincho", 40 * -1)   
)

canvas.create_text(
    32.0,
    576.0, #276
    anchor="nw",
    text="Language",
    fill="#FFFFFF",
    font=("Sawarabi Mincho", 40 * -1)
)

canvas.create_text(
    90.0, #589
    776.0,
    anchor="nw",
    text="Rating",
    fill="#FFFFFF",
    font=("Sawarabi Mincho", 40 * -1)
)

canvas.create_text(
    98.0,
    676.0,
    anchor="nw",
    text="Genre",
    fill="#FFFFFF",
    font=("Sawarabi Mincho", 40 * -1)
)

canvas.create_text(
    122.0,
    476.0,
    anchor="nw",
    text="Year",
    fill="#FFFFFF",
    font=("Sawarabi Mincho", 40 * -1)
)

canvas.create_text(
    76.0,
    876.0,
    anchor="nw",
    text="Quality",
    fill="#FFFFFF",
    font=("Sawarabi Mincho", 40 * -1)
)

id_entry_1=tk.Entry(frame2_add_movie,borderwidth=0,font=("Sawarabi Mincho",15),bg="#CECEDD")
id_entry_1.place(x=230,y=289,height=30,width=300)

name_entry_1=tk.Entry(frame2_add_movie,borderwidth=0,font=("Sawarabi Mincho",15),bg="#CECEDD")
name_entry_1.place(x=230,y=389,height=30,width=300)

year_entry_1=tk.Entry(frame2_add_movie,borderwidth=0,font=("Sawarabi Mincho",15),bg="#CECEDD")
year_entry_1.place(x=231,y=490,height=30,width=300)

language_entry_1=tk.Entry(frame2_add_movie,borderwidth=0,font=("Sawarabi Mincho",15),bg="#CECEDD")
language_entry_1.place(x=230,y=589,height=30,width=300)

genre_entry_1=tk.Entry(frame2_add_movie,borderwidth=0,font=("Sawarabi Mincho",15),bg="#CECEDD")
genre_entry_1.place(x=230,y=689,height=30,width=300)

rating_entry_1=tk.Entry(frame2_add_movie,borderwidth=0,font=("Sawarabi Mincho",15),bg="#CECEDD")
rating_entry_1.place(x=230,y=788,height=30,width=300)

quality_entry_1=tk.Entry(frame2_add_movie,borderwidth=0,font=("Sawarabi Mincho",15),bg="#CECEDD")
quality_entry_1.place(x=230,y=888,height=30,width=300)

#Update Frame

frame3_Update_frame=tk.Frame(window)
frame3_Update_frame.place(relwidth=1,relheight=1)


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\course\tkinter proj\MMS\build\assets\frame3")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


canvas = Canvas(
    frame3_Update_frame,
    bg = "#13101D",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1920.0,
    146.0,
    fill="#251443",
    outline="")

canvas.create_text(
    625.0,
    15.0,
    anchor="nw",
    text="Cinema World",
    fill="#A2C496",
    font=("Irish Grover", 96 * -1),
    justify="center"
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    frame3_Update_frame,
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: gotoframes(frame1),
    relief="flat",
    bg="#13101D",
    activebackground="#13101D"
)
button_10.place(
    x=15.0,
    y=165.0,
    width=109.0,
    height=47.0
)

canvas.create_text(
    265.0,
    200.0,
    anchor="nw",
    text="Select Movie",
    fill="#FF3A3E",
    font=("Sansita", 45 * -1)
)

canvas.create_text(
    170.0, #42
    276.0,
    anchor="nw",
    text="ID",
    fill="#FFFFFF",
    font=("Sawarabi Mincho", 40 * -1)
)

canvas.create_text(
    100.0, #45
    356.0,
    anchor="nw",
    text="Name",
    fill="#FFFFFF",
    font=("Sawarabi Mincho", 40 * -1)   
)


id_entry_2=tk.Entry(frame3_Update_frame,borderwidth=0,font=("Sawarabi Mincho",15),bg="#CECEDD")
id_entry_2.place(x=230,y=289,height=30,width=300)

name_entry_2=tk.Entry(frame3_Update_frame,borderwidth=0,font=("Sawarabi Mincho",15),bg="#CECEDD")
name_entry_2.place(x=230,y=369,height=30,width=300)

id_entry_3=tk.Entry(frame3_Update_frame,borderwidth=0,font=("Sawarabi Mincho",15),bg="#CECEDD")
id_entry_3.place(x=230,y=642,height=30,width=300)

name_entry_3=tk.Entry(frame3_Update_frame,borderwidth=0,font=("Sawarabi Mincho",15),bg="#CECEDD")
name_entry_3.place(x=230,y=742,height=30,width=300)

year_entry_3=tk.Entry(frame3_Update_frame,borderwidth=0,font=("Sawarabi Mincho",15),bg="#CECEDD")
year_entry_3.place(x=231,y=842,height=30,width=300)

language_entry_3=tk.Entry(frame3_Update_frame,borderwidth=0,font=("Sawarabi Mincho",15),bg="#CECEDD")
language_entry_3.place(x=830,y=642,height=30,width=300)

genre_entry_3=tk.Entry(frame3_Update_frame,borderwidth=0,font=("Sawarabi Mincho",15),bg="#CECEDD")
genre_entry_3.place(x=830,y=742,height=30,width=300)

rating_entry_3=tk.Entry(frame3_Update_frame,borderwidth=0,font=("Sawarabi Mincho",15),bg="#CECEDD")
rating_entry_3.place(x=830,y=842,height=30,width=300)

quality_entry_3=tk.Entry(frame3_Update_frame,borderwidth=0,font=("Sawarabi Mincho",15),bg="#CECEDD")
quality_entry_3.place(x=1430,y=642,height=30,width=300)

movie_list_frame_update = tk.Frame(frame3_Update_frame)
movie_list_frame_update.place(width="1300",height="332",x="600",y="165")
movie_list_frame_update.configure(bg="#13101D")

table_1 = ttk.Treeview(movie_list_frame_update,columns=("col1","col2","col3","col4","col5","col6"),show="headings")
table_1.heading("col1",text="Name")
table_1.heading("col2",text="Year")
table_1.heading("col3",text="Language")
table_1.heading("col4",text="Genre")
table_1.heading("col5",text="Rating")
table_1.heading("col6",text="Quality")

table_1.pack(fill=tk.BOTH,side="right",expand=True)

style = ttk.Style()
style.theme_use("clam")

style.configure("Treeview",background="#13101D",foreground="White",fieldbackground = "#13101D",rowheight="45")

def press_select_button():
    for item in table_1.get_children():
        table_1.delete(item)
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "movielist"
        )
        cursor_select = connection.cursor()
        sql_4 = "select movie_name,movie_year,movie_language,movie_genre,movie_rating,movie_quality from moviedetails where movie_id = %s or movie_name = %s"

        movie_id_text = id_entry_2.get().strip() #convert to string
        movie_name_text = name_entry_2.get().strip() #convert to string

        if movie_id_text.isdigit(): #type karapu string eka number ekakda kiyala balanwa
            movie_id = int(movie_id_text) #convert to integer
        else:
            movie_id = None

        if movie_name_text:
            id_entry_3.insert(0,movie_id_text)

        select_data = (movie_id_text,movie_name_text)
        cursor_select.execute(sql_4,select_data)
        data_4 = cursor_select.fetchall()

        for record in data_4:

            id_entry_3.delete(0,END)
            name_entry_3.delete(0,END)
            year_entry_3.delete(0,END)
            language_entry_3.delete(0,END)
            genre_entry_3.delete(0,END)
            rating_entry_3.delete(0,END)
            quality_entry_3.delete(0,END)

            id_entry_3.insert(0, movie_id_text)
            name_entry_3.insert(0, record[0])
            year_entry_3.insert(0, record[1])
            language_entry_3.insert(0, record[2])
            genre_entry_3.insert(0, record[3])
            rating_entry_3.insert(0, record[4])
            quality_entry_3.insert(0, record[5])

        connection.close()

        try:
            for row in data_4:
                table_1.insert("","end",values=row)
        except:
            print("error")
    except:
        print("error")


def clear_entry():
    id_entry_2.delete(0, END)
    name_entry_2.delete(0, END)   

    for item in table_1.get_children():
            table_1.delete(item) 

def reset_update_details():
    id_entry_3.delete(0,END)
    name_entry_3.delete(0,END)
    year_entry_3.delete(0,END)
    language_entry_3.delete(0,END)
    genre_entry_3.delete(0,END)
    rating_entry_3.delete(0,END)
    quality_entry_3.delete(0,END)

select_11 = PhotoImage(
    file=relative_to_assets("select.png"))
select11 = Button(
    frame3_Update_frame,
    image=select_11,
    borderwidth=0,
    highlightthickness=0,
    command=press_select_button,
    relief="flat",
    bg="#13101D",
    activebackground="#13101D"
)
select11.place(
    x=240.0,
    y=450.0,
    width=109.0,
    height=47.0
)

clear_11 = PhotoImage(
    file=relative_to_assets("clear.png"))
clear11 = Button(
    frame3_Update_frame,
    image=clear_11,
    borderwidth=0,
    highlightthickness=0,
    command=clear_entry,
    relief="flat",
    bg="#13101D",
    activebackground="#13101D"
)
clear11.place(
    x=410.0,
    y=450.0,
    width=109.0,
    height=47.0
)
#update details

def update_database():
    try:
        connection_1 = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "movielist"
        )
        movieId = id_entry_2.get().strip()
        moviename = name_entry_2.get().strip()
        new_update_data = (
            name_entry_3.get().strip(),
            year_entry_3.get().strip(),
            language_entry_3.get().strip(),
            genre_entry_3.get().strip(),
            rating_entry_3.get().strip(),
            quality_entry_3.get().strip(),
            # movieId
        )
        cursor_update_database = connection_1.cursor()

        sql_get_data_from_db="""select movie_name,movie_year,movie_language,movie_genre,movie_rating,movie_quality from moviedetails
            where movie_id = %s"""
        

        cursor_update_database.execute(sql_get_data_from_db,(movieId,))
        current_data = cursor_update_database.fetchall()

        current_data_stripped = tuple(str(i).strip() for i in current_data) if current_data else None

        if current_data_stripped != new_update_data: 
            sql_4 = """update moviedetails set
                movie_name = %s,
                movie_year = %s,
                movie_language = %s,
                movie_genre = %s,
                movie_rating = %s,
                movie_quality = %s
                where movie_id = %s
            """
            cursor_update_database.execute(sql_4,(*new_update_data,movieId))
            connection_1.commit()
            

            # clear entries
            id_entry_3.delete(0,END)
            name_entry_3.delete(0,END)
            year_entry_3.delete(0,END)
            language_entry_3.delete(0,END)
            genre_entry_3.delete(0,END)
            rating_entry_3.delete(0,END)
            quality_entry_3.delete(0,END)

        cursor_fetch = connection_1.cursor()
        sql_data_fetch = """select movie_name,movie_year,movie_language,movie_genre,movie_rating,movie_quality from moviedetails
            where movie_id = %s"""
        movie__id = id_entry_2.get().strip()

        if movie__id.isdigit(): #type karapu string eka number ekakda kiyala balanwa
            movie_id = int(movie__id) #convert to integer
        else:
            movie_id = None

        select_fetch_data = (movie__id,)
        cursor_fetch.execute(sql_data_fetch,select_fetch_data)
        fetchall_data = cursor_fetch.fetchall()


        for item in table_1.get_children():
            table_1.delete(item)

        try:
            for row in fetchall_data:
                table_1.insert("","end",values=row)
        except:
            print("error")
        messagebox.showinfo("Info", "Data Updated Successfully!")
        connection_1.close()
    except:
         print("error")

canvas.create_text(
    202.0,
    550.0,
    anchor="nw",
    text="Update Movie Details",
    fill="#FF3A3E",
    font=("Sansita", 45 * -1)
)

canvas.create_text(
    170.0, #42
    630.0,
    anchor="nw",
    text="ID",
    fill="#FFFFFF",
    font=("Sawarabi Mincho", 40 * -1)
)

canvas.create_text(
    100.0, #45
    730.0,
    anchor="nw",
    text="Name",
    fill="#FFFFFF",
    font=("Sawarabi Mincho", 40 * -1)   
)

canvas.create_text(
    119.0, #45
    830.0,
    anchor="nw",
    text="Year",
    fill="#FFFFFF",
    font=("Sawarabi Mincho", 40 * -1)   
)

canvas.create_text(
    633.0, #45
    627.0,
    anchor="nw",
    text="Language",
    fill="#FFFFFF",
    font=("Sawarabi Mincho", 40 * -1)   
)

canvas.create_text(
    700.0, #45
    727.0,
    anchor="nw",
    text="Genre",
    fill="#FFFFFF",
    font=("Sawarabi Mincho", 40 * -1)   
)

canvas.create_text(
    690.0, #45
    827.0,
    anchor="nw",
    text="Rating",
    fill="#FFFFFF",
    font=("Sawarabi Mincho", 40 * -1)   
)

canvas.create_text(
    1275.0, #45
    627.0,
    anchor="nw",
    text="Quality",
    fill="#FFFFFF",
    font=("Sawarabi Mincho", 40 * -1)   
)
update_1 = PhotoImage(
    file=relative_to_assets("update.png"))
update = Button(
    frame3_Update_frame,
    image=update_1,
    borderwidth=0,
    highlightthickness=0,
    command=update_database,
    relief="flat",
    bg="#13101D",
    activebackground="#13101D"
)
update.place(
    x=1350.0,
    y=730.0,
    width=130.0,
    height=47.0
)

reset_1 = PhotoImage(
    file=relative_to_assets("reset.png"))
reset = Button(
    frame3_Update_frame,
    image=reset_1,
    borderwidth=0,
    highlightthickness=0,
    command=reset_update_details,
    relief="flat",
    bg="#13101D",
    activebackground="#13101D"
)
reset.place(
    x=1555.0,
    y=730.0,
    width=130.0,
    height=47.0
)

#Browse frames

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\course\tkinter proj\MMS\build\assets\frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

frame4_browse_frame = tk.Frame(window)
frame4_browse_frame.place(relwidth=1,relheight=1)



canvas = Canvas(
    frame4_browse_frame,
    bg = "#13101D",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1920.0,
    146.0,
    fill="#251443",
    outline="")

canvas.create_text(
    625.0,
    15.0,
    anchor="nw",
    text="Cinema World",
    fill="#A2C496",
    font=("Irish Grover", 96 * -1)
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    frame4_browse_frame,
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: gotoframes(frame1),
    relief="flat",
    bg="#13101D",
    activebackground="#13101D"
)
button_11.place(
    x=15.0,
    y=165.0,
    width=109.0,
    height=47.0
)

canvas.create_text(
    200.0,
    200.0,
    anchor="nw",
    text="Search Your Movie",
    fill="#FF3A3E",
    font=("Sansita", 48 * -1)
)

canvas.create_text(
    170.0, #42
    276.0,
    anchor="nw",
    text="ID",
    fill="#FFFFFF",
    font=("Sawarabi Mincho", 40 * -1)
)

canvas.create_text(
    100.0, #45
    376.0,
    anchor="nw",
    text="Name",
    fill="#FFFFFF",
    font=("Sawarabi Mincho", 40 * -1)   
)


id_entry_4=tk.Entry(frame4_browse_frame,borderwidth=0,font=("Sawarabi Mincho",15),bg="#CECEDD")
id_entry_4.place(x=230,y=289,height=30,width=300)

name_entry_4=tk.Entry(frame4_browse_frame,borderwidth=0,font=("Sawarabi Mincho",15),bg="#CECEDD")
name_entry_4.place(x=230,y=389,height=30,width=300)


movie_list_frame_search = tk.Frame(frame4_browse_frame)
movie_list_frame_search.place(width="1300",height="830",x="600",y="165")
movie_list_frame_search.configure(bg="#13101D")

table_2 = ttk.Treeview(movie_list_frame_search,columns=("col1","col2","col3","col4","col5","col6"),show="headings")
table_2.heading("col1",text="Name")
table_2.heading("col2",text="Year")
table_2.heading("col3",text="Language")
table_2.heading("col4",text="Genre")
table_2.heading("col5",text="Rating")
table_2.heading("col6",text="Quality")

table_2.pack(fill=tk.BOTH,side="right",expand=True)

style = ttk.Style()
style.theme_use("clam")

style.configure("Treeview",background="#13101D",foreground="White",fieldbackground = "#13101D",rowheight="45")

def press_search_button():

    for item in table_2.get_children():
        table_2.delete(item)
    try:
        conn_add = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "movielist"
            )

        cursor_3 = conn_add.cursor()
        sql_3 = "select movie_name,movie_year,movie_language,movie_genre,movie_rating,movie_quality from moviedetails where movie_id = %s or movie_name = %s"

        movie_id_text = id_entry_4.get().strip() #convert to string
        movie_name_text = name_entry_4.get().strip()
        if movie_id_text.isdigit(): #type karapu string eka number ekakda kiyala balanwa
                movie_id = int(movie_id_text) #convert to integer
        else:
                movie_id = None

        select_data = (movie_id_text,movie_name_text)

        cursor_3.execute(sql_3,select_data)
        data_5 = cursor_3.fetchall()
        conn_add.close()

        for item in table_2.get_children():
            table_2.delete(item)

        try:
            for row in data_5:
                table_2.insert("","end",values=row)
        except:
            print("error")
        messagebox.showinfo("Info", "Data Searched Successfully!")
    except:
         print("error")

def clear_searched_entry():
    for item in table_2.get_children():
        table_2.delete(item)

    id_entry_4.delete(0,END)
    name_entry_4.delete(0,END)

select_1 = PhotoImage(
    file=relative_to_assets("search_1.png"))
select = Button(
    frame4_browse_frame,
    image=select_1,
    borderwidth=0,
    highlightthickness=0,
    command=press_search_button,
    relief="flat",
    bg="#13101D",
    activebackground="#13101D"
)
select.place(
    x=240.0,
    y=450.0,
    width=109.0,
    height=47.0
)

clear_1 = PhotoImage(
    file=relative_to_assets("clear_1.png"))
clear = Button(
    frame4_browse_frame,
    image=clear_1,
    borderwidth=0,
    highlightthickness=0,
    command=clear_searched_entry,
    relief="flat",
    bg="#13101D",
    activebackground="#13101D"
)
clear.place(
    x=410.0,
    y=450.0,
    width=109.0,
    height=47.0
)

movie_list_frame_search = tk.Frame(frame4_browse_frame)
movie_list_frame_search.place(width="1300",height="830",x="600",y="165")
movie_list_frame_search.configure(bg="#13101D")

table_2 = ttk.Treeview(movie_list_frame_search,columns=("col1","col2","col3","col4","col5","col6"),show="headings")
table_2.heading("col1",text="Name")
table_2.heading("col2",text="Year")
table_2.heading("col3",text="Language")
table_2.heading("col4",text="Genre")
table_2.heading("col5",text="Rating")
table_2.heading("col6",text="Quality")

table_2.pack(fill=tk.BOTH,side="right",expand=True)

style = ttk.Style()
style.theme_use("clam")

style.configure("Treeview",background="#13101D",foreground="White",fieldbackground = "#13101D",rowheight="45")

def press_search_button():

    for item in table_2.get_children():
        table_2.delete(item)
    try:
        conn_add = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "movielist"
            )

        cursor_3 = conn_add.cursor()
        sql_3 = "select movie_name,movie_year,movie_language,movie_genre,movie_rating,movie_quality from moviedetails"
        cursor_3.execute(sql_3)
        data_5 = cursor_3.fetchall()
        conn_add.close()

        try:
            for row in data_5:
                table_2.insert("","end",values=row)
        except:
            print("error")
    except:
         print("error")

#Movie_List_Table

movie_list_frame_add = tk.Frame(frame2_add_movie)
movie_list_frame_add.place(width="1300",height="830",x="600",y="165")
movie_list_frame_add.configure(bg="#13101D")

scroll_y = ttk.Scrollbar(movie_list_frame_add, orient="vertical")
table = ttk.Treeview(movie_list_frame_add,columns=("col1","col2","col3","col4","col5","col6"),show="headings",yscrollcommand=scroll_y.set)
table.heading("col1",text="Name")
table.heading("col2",text="Year")
table.heading("col3",text="Language")
table.heading("col4",text="Genre")
table.heading("col5",text="Rating")
table.heading("col6",text="Quality")

style = ttk.Style()
style.theme_use("clam")
table.pack(fill=tk.BOTH,side="right",expand=True)

scroll_y.config(command=table.yview)
scroll_y.pack(side="right", fill="y")

style.configure("Treeview",background="#13101D",foreground="White",fieldbackground = "#13101D",rowheight="45")

def save_and_refresh():

    for item in table.get_children():
        table.delete(item)
    try:
        conn_add = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "movielist"
            )

        cursor_3 = conn_add.cursor()
        sql_3 = "select movie_name,movie_year,movie_language,movie_genre,movie_rating,movie_quality from moviedetails"
        cursor_3.execute(sql_3)
        data_3 = cursor_3.fetchall()
        conn_add.close()

        try:
            for row in data_3:
                table.insert("","end",values=row)
        except:
            print("error")
    except:
         print("error")

# start ui and load movielist
save_and_refresh()


#Delete frame

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\course\tkinter proj\MMS\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

frame5_delete_frame = tk.Frame(window)
frame5_delete_frame.place(relwidth=1,relheight=1)



canvas = Canvas(
    frame5_delete_frame,
    bg = "#13101D",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1920.0,
    146.0,
    fill="#251443",
    outline="")

canvas.create_text(
    625.0,
    15.0,
    anchor="nw",
    text="Cinema World",
    fill="#A2C496",
    font=("Irish Grover", 96 * -1)
)
button_image_delete = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_delete = Button(
    frame5_delete_frame,
    image=button_image_delete,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: gotoframes(frame1),
    relief="flat",
    bg="#13101D",
    activebackground="#13101D"
)
button_delete.place(
    x=15.0,
    y=165.0,
    width=109.0,
    height=47.0
)

canvas.create_text(
    200.0,
    200.0,
    anchor="nw",
    text="Delete Movie",
    fill="#FF3A3E",
    font=("Sansita", 48 * -1)
)

canvas.create_text(
    170.0, #42
    276.0,
    anchor="nw",
    text="ID",
    fill="#FFFFFF",
    font=("Sawarabi Mincho", 40 * -1)
)

canvas.create_text(
    100.0, #45
    376.0,
    anchor="nw",
    text="Name",
    fill="#FFFFFF",
    font=("Sawarabi Mincho", 40 * -1)   
)
id_entry_5=tk.Entry(frame5_delete_frame,borderwidth=0,font=("Sawarabi Mincho",15),bg="#CECEDD")
id_entry_5.place(x=230,y=289,height=30,width=300)

name_entry_5=tk.Entry(frame5_delete_frame,borderwidth=0,font=("Sawarabi Mincho",15),bg="#CECEDD")
name_entry_5.place(x=230,y=389,height=30,width=300)

movie_list_frame_delete = tk.Frame(frame5_delete_frame)
movie_list_frame_delete.place(width="1300",height="830",x="600",y="165")
movie_list_frame_delete.configure(bg="#13101D")

table_3 = ttk.Treeview(movie_list_frame_delete,columns=("col1","col2","col3","col4","col5","col6"),show="headings")
table_3.heading("col1",text="Name")
table_3.heading("col2",text="Year")
table_3.heading("col3",text="Language")
table_3.heading("col4",text="Genre")
table_3.heading("col5",text="Rating")
table_3.heading("col6",text="Quality")

table_3.pack(fill=tk.BOTH,side="right",expand=True)

style = ttk.Style()
style.theme_use("clam")

style.configure("Treeview",background="#13101D",foreground="White",fieldbackground = "#13101D",rowheight="45")

def press_search_for_delete_button():

    for item in table_3.get_children():
        table_3.delete(item)
    try:
        conn_delete = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "movielist"
            )

        cursor_delete = conn_delete.cursor()
        sql_delete = "select movie_name,movie_year,movie_language,movie_genre,movie_rating,movie_quality from moviedetails where movie_id = %s or movie_name = %s"

        movie_id_text = id_entry_5.get().strip() #convert to string
        movie_name_text = name_entry_5.get().strip()

        if movie_id_text.isdigit(): #type karapu string eka number ekakda kiyala balanwa
                movie_id = int(movie_id_text) #convert to integer
        else:
                movie_id = None

        select_data = (movie_id_text,movie_name_text)

        cursor_delete.execute(sql_delete,select_data)
        data_5 = cursor_delete.fetchall()
        conn_delete.close()

        try:
            for row in data_5:
                table_3.insert("","end",values=row)
        except:
            print("error")
    except:
         print("error")

def delete_entry_1():
    try:
        connection_delete = mysql.connector.connect(
            host= "localhost",
            user= "root",
            password = "",
            database = "movielist"
        )

        cursor_delete_1= connection_delete.cursor()
        del_sql = """delete from moviedetails where movie_id = %s"""

        movie_id_text = id_entry_5.get().strip() #convert to string

        if movie_id_text.isdigit(): #type karapu string eka number ekakda kiyala balanwa
                movie_id = int(movie_id_text) #convert to integer
        else:
                movie_id = None

        select_data = (movie_id_text,)

        cursor_delete_1.execute(del_sql,select_data)
        connection_delete.commit()
        connection_delete.close()

        id_entry_5.delete(0,END)

        for item in table_3.get_children():
            table_3.delete(item)
        name_entry_5.delete(0,END)
        messagebox.showinfo("Info", "Data Deleted Successfully!")
        save_and_refresh()
    except:
         print("error")

search3 = PhotoImage(
    file=relative_to_assets("search_3.png"))
search_3 = Button(
    frame5_delete_frame,
    image=search3,
    borderwidth=0,
    highlightthickness=0,
    command=press_search_for_delete_button,
    relief="flat",
    bg="#13101D",
    activebackground="#13101D"
)
search_3.place(
    x=130.0,
    y=450.0,
    width=109.0,
    height=47.0
)

delete = PhotoImage(
    file=relative_to_assets("button_2.png"))
delete_1 = Button(
    frame5_delete_frame,
    image=delete,
    borderwidth=0,
    highlightthickness=0,
    command=delete_entry_1,
    relief="flat",
    bg="#13101D",
    activebackground="#13101D"
)
delete_1.place(
    x=270.0,
    y=450.0,
    width=109.0,
    height=47.0
)

def clear_searched_entry_in_delete_frame():
    for item in table_3.get_children():
        table_3.delete(item)

    id_entry_5.delete(0,END)
    name_entry_5.delete(0,END)

clear_2 = PhotoImage(
    file=relative_to_assets("clear_2.png"))
clear__ = Button(
    frame5_delete_frame,
    image=clear_2,
    borderwidth=0,
    highlightthickness=0,
    command=clear_searched_entry_in_delete_frame,
    relief="flat",
    bg="#13101D",
    activebackground="#13101D"
)
clear__.place(
    x=410.0,
    y=450.0,
    width=109.0,
    height=47.0
)
frame1.tkraise()
window.resizable(True, False)
window.mainloop()
