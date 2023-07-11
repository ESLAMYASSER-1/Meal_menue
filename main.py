import tkinter as tk
from PIL import ImageTk, Image
import io
import mysql.connector 
# Create a Tkinter window
root = tk.Tk()
root.geometry("700x900")

def createBD():
    conn= mysql.connector.connect(
        user="root",
        host="localhost",
        passwd="engeslam@8505611.mysql"
    )
    mycursor= conn.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS Ohmlatl")
createBD()
conn= mysql.connector.connect(
        user="root",
        host="localhost",
        passwd="engeslam@8505611.mysql",
        database="Ohmlatl"
    )
mycursor= conn.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Recipe(Meal_name varchar(255),Meal_ingredients TEXT,Meal_recipe TEXT )ENGINE = InnoDB;")

def insert_meal(meal_name,Meal_ingredient,meal_recipe):
    sql_statement="INSERT INTO Recipe VALUES('%s','%s')"%(meal_name,Meal_ingredient,meal_recipe)
    mycursor.execute(sql_statement)
    conn.commit()


# Create a frame to hold the canvas and scrollbar
class recipes:
    
    def __init__(self):
        
        xframe = tk.Frame(root,bg="#0c1015")
        xframe.pack(fill=tk.BOTH, expand=1)

        app_name = tk.Label(xframe,text="OHmlatL",bg="#0c1015",fg="white",font="Arial 40 bold")
        app_name.place(x=230,y=10)
        # Create a canvas to hold the inner frames
        canvas = tk.Canvas(xframe)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1,pady=(90,0))

        # Add a scrollbar to the frame
        scrollbar = tk.Scrollbar(xframe, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Attach the scrollbar to the canvas
        canvas.configure(yscrollcommand=scrollbar.set,bg="#0c1015",highlightthickness=0)#make it 0

        # Create a frame to hold the inner frames
        inner_frame = tk.Frame(canvas,bg="#0c1015",)

        # Add some inner frames to the inner frame
        def Create_frame(Recipe_name):
            if Recipe_name=="Mahshi":
                Recipe_image="res\mahshi.jpg"
            elif Recipe_name=="Kaware3":
                Recipe_image="res\kaware3.jpg"
            elif Recipe_name=="Hamam":
                Recipe_image="res\hamam.jpg"
            elif Recipe_name=="Mombar":
                Recipe_image="res\mombar.jpg"
            elif Recipe_name=="Seafood":
                Recipe_image="res\seafood.jpg"
            elif Recipe_name=="Makarona Bashamel":
                Recipe_image="res\makaronabechemel.webp"
            else:
                Recipe_image="res\defoult.png"
            image = Image.open(Recipe_image)
            image = image.resize((450,280),Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            frame = tk.Frame(inner_frame, bd=2, relief=tk.GROOVE, width=560,height=400,bg="#282828")
            frame.pack(fill=tk.BOTH, expand=1, pady=5, padx=60)
            frame.pack_propagate(0)
            label = tk.Label(frame, image=photo)
            label.photo = photo
            label.pack(pady=(10,0))
            recipe_namelbl=tk.Label(frame,text="NAME: ",fg="white",bg="#282828",font="Verdana 20 bold")
            recipe_namelbl.place(x=40,y=320)
            recipe_name=tk.Label(frame,text=Recipe_name,fg="white",bg="#282828",font="verdana 20")
            recipe_name.place(x=140,y=320)
            def open_Meal_detailes():
                childs=frame.winfo_children()
                Meal_name=childs[2].cget("text")
                xframe.destroy()
                mycursor = conn.cursor()
                
                mycursor.execute(f"SELECT Meal_ingredients,Meal_recipe FROM recipe where Meal_name = '{Meal_name}'")
                Meal_info=mycursor.fetchone()
                
                recipe_detailes(Meal_name,Meal_info[0],Meal_info[1])
            show_btn= tk.Button(frame, text="Show Recipe",relief="flat",font="verdana 12",bg="#282828",fg="white",command=open_Meal_detailes)
            show_btn.place(x=400,y=325)

        mycursor.execute("SELECT * FROM recipe ORDER BY Meal_name;")
        recipesarr=mycursor.fetchall()
        for recipe in recipesarr:
            Create_frame(recipe[0])
        # Create a window item for the inner frame
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        # Bind the canvas to a function that resizes the inner frame
        def resize_inner_frame(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
            
        inner_frame.bind("<Configure>", resize_inner_frame)

class recipe_detailes:
    def __init__(self,Recipe_name,Meal_ingredient,Meal_recipe):
        xframe = tk.Frame(root,bg="#0c1015")
        xframe.pack(fill=tk.BOTH, expand=1)

        app_name = tk.Label(xframe,text="OHmlatL",bg="#0c1015",fg="white",font="Arial 40 bold")
        app_name.place(x=230,y=10)
        def open_Meal_menue():
            xframe.destroy()
            recipes()
        backbtn=tk.Button(xframe,text="<<",font="Helvetica 20 bold",bg="#0c1015",fg="white",command=open_Meal_menue)
        backbtn.place(x=50,y=20)
        # Create a canvas to hold the inner frames
        canvas = tk.Canvas(xframe)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1,pady=(90,0))

        # Add a scrollbar to the frame
        scrollbar = tk.Scrollbar(xframe, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Attach the scrollbar to the canvas
        canvas.configure(yscrollcommand=scrollbar.set,bg="#0c1015",highlightthickness=0)#make it 0

        # Create a frame to hold the inner frames
        inner_frame = tk.Frame(canvas,bg="#0c1015",)
        if Recipe_name=="Mahshi":
            Recipe_image="res\mahshi.jpg"
        elif Recipe_name=="Kaware3":
            Recipe_image="res\kaware3.jpg"
        elif Recipe_name=="Hamam":
            Recipe_image="res\hamam.jpg"
        elif Recipe_name=="Mombar":
            Recipe_image="res\mombar.jpg"
        elif Recipe_name=="Seafood":
            Recipe_image="res\seafood.jpg"
        elif Recipe_name=="Makarona Bashamel":
            Recipe_image="res\makaronabechemel.webp"
        else:
            Recipe_image="res\defoult.png"
        image = Image.open(Recipe_image)
        image = image.resize((630,350),Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        frame = tk.Frame(inner_frame, width=650,height=2500 ,relief=tk.GROOVE,bg="#282828") 
        frame.pack(fill="x", expand=1,side="top",padx=15)
        frame.pack_propagate(0)
        label = tk.Label(frame, image=photo)
        label.photo = photo
        label.pack(pady=(10,0))
        namelbl=tk.Label(frame,text="Name:",font="Verdana 20 ",fg="white",bg="#282828")
        namelbl.place(x=20,y=400)
        nameLabel=tk.Label(frame,text=Recipe_name,font="Verdana 20 bold",fg="white",bg="#282828")
        nameLabel.place(x=120,y=400)

        ingred_lbl=tk.Label(frame,text="Ingredients:",font="Verdana 20 ",fg='white',bg="#282828")
        ingred_lbl.place(x=20,y=450)
        ingred_label=tk.Label(frame,text=Meal_ingredient,font="Verdana 20 bold",fg="white",bg="#282828",justify="left")
        ingred_label.place(x=70,y=500)

        recipe_lbl=tk.Label(frame,text='Recipe:',font="Verdana 20",bg="#282828",fg="white")
        recipe_lbl.place(x=20,y=1100)
        recipe_label=tk.Label(frame,text=Meal_recipe,bg="#282828",fg="white",justify="left",font="Verdana 17 bold")
        recipe_label.place(x=50,y=1150)
        canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

        # Bind the canvas to a function that resizes the inner frame
        def resize_inner_frame(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        inner_frame.bind("<Configure>", resize_inner_frame)
recipes()
# Start the Tkinter event loop
root.mainloop()
