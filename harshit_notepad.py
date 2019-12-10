import tkinter as tk
from tkinter import colorchooser,font,filedialog,messagebox
import os
from tkinter import ttk
import datetime

root=tk.Tk()
root.geometry("800x600+250+65")
root.title("Untitled - My Notepad")
root.wm_iconbitmap("main_icon.ico")  # Main icon of notepad

########################  Menu Bar ###################################

mainmenu=tk.Menu(root)

#file

#icons of file menu
new_icon=tk.PhotoImage(file="icons2\\new.png")
open_icon=tk.PhotoImage(file="icons2\\open.png")
save_icon=tk.PhotoImage(file="icons2\\save.png")
save_as_icon=tk.PhotoImage(file="icons2\\save_as.png")
new_icon=tk.PhotoImage(file="icons2\\new.png")
exit_icon=tk.PhotoImage(file="icons2\\exit.png")

# Creating file menu
filemenu=tk.Menu(mainmenu,tearoff=0)
mainmenu.add_cascade(label="File",menu=filemenu)


#edit

# icons of edit menu
cut_icon=tk.PhotoImage(file="icons2\\cut.png")
copy_icon=tk.PhotoImage(file="icons2\\copy.png")
paste_icon=tk.PhotoImage(file="icons2\\paste.png")
clear_all_icon=tk.PhotoImage(file="icons2\\clear_all.png")
find_icon=tk.PhotoImage(file="icons2\\find.png")
undo_icon=tk.PhotoImage(file="icons2\\undo.png")
redo_icon=tk.PhotoImage(file="icons2\\redo.png")
time_date_icon=tk.PhotoImage(file="icons2\\time_date.png")
select_all_icon=tk.PhotoImage(file="icons2\\select_all.png")

# Creating edit menu
edit=tk.Menu(mainmenu,tearoff=0)
mainmenu.add_cascade(label="Edit",menu=edit)


# View

# icons of Views menu
tool_bar_icon=tk.PhotoImage(file="icons2\\tool_bar.png")
status_bar_icon=tk.PhotoImage(file="icons2\\status_bar.png")

# creating view menu
view=tk.Menu(mainmenu,tearoff=0)
mainmenu.add_cascade(label="View",menu=view)


# Color Theme

# icons of color Theme menu
light_default_icon=tk.PhotoImage(file="icons2\\light_default.png")
light_plus_icon=tk.PhotoImage(file="icons2\\light_plus.png")
dark_icon=tk.PhotoImage(file="icons2\\dark.png")
monokai_icon=tk.PhotoImage(file="icons2\\monokai.png")
night_blue_icon=tk.PhotoImage(file="icons2\\night_blue.png")
flaunt_green_icon=tk.PhotoImage(file="icons2\\flaunt_green1.png")
red_icon=tk.PhotoImage(file="icons2\\red.png")

#Tuple which contain icons of color theme
color_icon_tuple=(light_default_icon,light_plus_icon,dark_icon,monokai_icon,night_blue_icon,night_blue_icon,flaunt_green_icon,red_icon)

#Creating Color Theme menu
color_theme=tk.Menu(mainmenu,tearoff=0)
color_selected=tk.StringVar()

# Dictionary which contains key as Color Name and value as tuple where first index is foreground and second is background
color_dictionary={
    "Light Default":("black","white"),
    "Light Plus":("#0000cc","#ffffcc"),
    "Dark":("white","#272822"),
    "Monokai":("#006600","#ffcc66"),
    "Night Blue":("white","#003366"),
    "Condensed Blue":("#00ffff","#666699"),
    "Flaunt Green":("yellow","#39ac39"),
    "Ruby Red":("black","#ff66cc")
}

mainmenu.add_cascade(label="Color Theme",menu=color_theme)


# About 

# Icon of About Menu
about_icon=tk.PhotoImage(file="icons2\\about.png")

about=tk.Menu(mainmenu,tearoff=0)
mainmenu.add_cascade(label="About",menu=about)

######################## End Menu Bar #####################################


######################### Toolbar #########################################

# Label over which toolbar elements reside 
toolbar_label=tk.Label(root)
toolbar_label.pack(side="top",fill="x")

font_selected=tk.StringVar()

# Font family combo
font_combo=ttk.Combobox(toolbar_label,state="readonly",textvariable=font_selected,width=30)
font_combo["values"]=tk.font.families()   #Font has families method
font_tuple=tk.font.families()
font_combo.current(font_tuple.index("Arial"))
font_combo.grid(row=0,column=0,padx=5)


#Font Size combo
font_size=tk.IntVar()
font_size_combo=ttk.Combobox(toolbar_label,textvariable=font_size,width=14,state="readonly")
font_size_combo["values"]=tuple(range(8,81))
font_size_combo.current(4)   # current method takes index
font_size_combo.grid(row=0,column=1,padx=5)


# Bold ,italic, underline ,aligns ,color choose icons
bold_icon=tk.PhotoImage(file="icons2\\bold.png")
italic_icon=tk.PhotoImage(file="icons2\\italic.png")
underline_icon=tk.PhotoImage(file="icons2\\underline.png")
align_left_icon=tk.PhotoImage(file="icons2\\align_left.png")
align_center_icon=tk.PhotoImage(file="icons2\\align_center.png")
align_right_icon=tk.PhotoImage(file="icons2\\align_right.png")
font_color_icon=tk.PhotoImage(file="icons2\\font_color.png")


bold_button=ttk.Button(toolbar_label,image=bold_icon)
bold_button.grid(row=0,column=2,padx=5)

italic_button=ttk.Button(toolbar_label,image=italic_icon)
italic_button.grid(row=0,column=3,padx=5)

underline_button=ttk.Button(toolbar_label,image=underline_icon)
underline_button.grid(row=0,column=4,padx=5)

font_color_button=ttk.Button(toolbar_label,image=font_color_icon)
font_color_button.grid(row=0,column=5,padx=5)

align_left_button=ttk.Button(toolbar_label,image=align_left_icon)
align_left_button.grid(row=0,column=6,padx=5)

align_center_button=ttk.Button(toolbar_label,image=align_center_icon)
align_center_button.grid(row=0,column=7,padx=5)

align_right_button=ttk.Button(toolbar_label,image=align_right_icon)
align_right_button.grid(row=0,column=8,padx=4)

########################## End Toolbar #######################################


########################### Text Editor ######################################

# creating text editor using Text Class
texteditor=tk.Text(root,undo=True,maxundo=-1)       #undo=True starts undo-redo operations

# Scroll bar command configuration
scrollbar=tk.Scrollbar(root,command=texteditor.yview)
texteditor.config(wrap="word",yscrollcommand=scrollbar.set,relief="flat")

scrollbar.pack(side="right",fill="y")
texteditor.pack(fill="both",expand=True)
texteditor.focus()

# Font family and size functionality
current_font_selected="Arial"
current_font_size=12

# We make global variable so that the changes reflected in both functions
def font_family(event=None):
    '''Function for changing font family'''
    global current_font_selected
    current_font_selected=font_selected.get()
    texteditor.configure(font=(current_font_selected,current_font_size))

def font_size_func(event=None):
    '''Function for changing font size'''
    global current_font_size
    current_font_size=font_size.get()
    texteditor.configure(font=(current_font_selected,current_font_size))

# Binding of combobox so that items can be selected without using buttons
font_combo.bind("<<ComboboxSelected>>",font_family)
font_size_combo.bind("<<ComboboxSelected>>",font_size_func)
texteditor.configure(font="Arial 12")


# we make weight and slant; a global variable so that text can be bold and italic at the same time

weight="normal"
slant="roman"

# bold functionality

def change_bold(event=None):
    '''Function for making font bold'''
    global weight,slant
    text_property=tk.font.Font(font=texteditor['font'])
    # text_property=tk.font.Font(font=texteditor['font']) 
    # font class has Font method which takes input as font of texteditor
    # text_propery variable is font object 
    # actual() method return dictionary like object
    if text_property.actual()["weight"]=="bold":
        weight="normal"
        texteditor.configure(font=(current_font_selected,current_font_size,weight,slant))
    if text_property.actual()["weight"]=="normal":
        weight="bold"
        texteditor.configure(font=(current_font_selected,current_font_size,weight,slant))

bold_button.configure(command=change_bold) # Button to activate bold function

#italic functionality
def change_italic(event=None):
    '''Function for making font italic'''
    global slant,weight
    text_property=tk.font.Font(font=texteditor['font'])
    if text_property.actual()["slant"]=="roman":
        slant="italic"
        texteditor.configure(font=(current_font_selected,current_font_size,weight,slant))
    if text_property.actual()["slant"]=="italic":
        slant="roman"
        texteditor.configure(font=(current_font_selected,current_font_size,weight,slant))

italic_button.configure(command=change_italic) # Button to activate Italic function

# underline functionality
def change_underline(event=None):
    '''Function for making font underline'''
    global slant,weight
    text_property=tk.font.Font(font=texteditor['font'])
    if text_property.actual()["underline"]==0:
        texteditor.configure(font=(current_font_selected,current_font_size,weight,slant,"underline"))
    if text_property.actual()["underline"]==1:
        texteditor.configure(font=(current_font_selected,current_font_size,weight,slant))
underline_button.configure(command=change_underline) # Button to activate Underline function


# change font_color functionality
def color_font():
    '''Function for changing font color'''
    color=tk.colorchooser.askcolor()  # tkinter has colorchooser class
    # colorchooser class has askcolor method which shows color dialog box
    texteditor.configure(fg=color[1])  
    # askcolor return tuple where index 0 has rgb values and index 1 has hex values
font_color_button.configure(command=color_font)


#align functionality
def align_left(event=None):
    '''Function for left align text'''
    text_content=texteditor.get(1.0,"end")
    # text has get method which takes start,stop index
    # Here start index is 1.0 which means first line and 0 character
    # Stop index is end, which means end of text editor
    texteditor.tag_config("left",justify=tk.LEFT)
    # tag_config method of text accepts first input as tag name which is "left"
    # second argument is justify to left 
    texteditor.delete(1.0,tk.END)
    # delete method deletes element from 1.0 to end which means all text is deleted
    texteditor.insert(tk.INSERT,text_content,"left")
    # insert method first argument is index,second is content and third is tag name. It inserts content at index. tk.INSERT means insert at that index where the mouse cursor is.

align_left_button.configure(command=align_left) # Button for left alignment.

def align_center(event=None):
    '''Function for center align text'''
    text_content=texteditor.get(1.0,"end")
    texteditor.tag_config("center",justify=tk.CENTER)
    texteditor.delete(1.0,tk.END)
    texteditor.insert(tk.INSERT,text_content,"center")

align_center_button.configure(command=align_center) # Button for center alignment.

def align_right(event=None):
    '''Function for right align text'''
    text_content=texteditor.get(1.0,"end")
    texteditor.tag_config("right",justify=tk.RIGHT)
    texteditor.delete(1.0,tk.END)
    texteditor.insert(tk.INSERT,text_content,"right")

align_right_button.configure(command=align_right) # Button for right alignment.


# Hovering Effects on Buttons #

child=None  # Toplevel global variable 

def bold_events(event=None):
    '''Function to display bold hovering effect when mouse enters bold button'''
    global child
    child=tk.Toplevel()
    child.overrideredirect(1)  # Removes title bar of Toplevel window
    child.geometry("100x50+500+100")
    child.configure(bg="skyblue")
    label=tk.Label(child,text="Bold the text\nCtrl+B",bg="skyblue",font="arial 10 bold")
    label.pack(pady=5)
    def destroy_at_2sec():
        '''Function for destroying child bold hover window after 2 seconds'''
        child.destroy()  # destroy Toplevel window at <Leave> event
    child.after(2000,destroy_at_2sec)

def bold_destroy(event=None):
    '''Function for destroying child bold hover window when mouse leave bold button'''
    global child
    child.destroy()

# Binding bold_button for hovering effect
bold_button.bind("<Enter>",bold_events)  # Activate when mouse enter the widget
bold_button.bind("<Leave>",bold_destroy) # Activate when mouse leave the widget


def italic_events(event=None):
    '''Function to display italic hovering effect when mouse enters italic button'''
    global child
    child=tk.Toplevel()
    child.overrideredirect(1)
    child.geometry("100x50+500+100")
    child.configure(bg="skyblue")
    label=tk.Label(child,text="Italic the text\nCtrl+I",bg="skyblue",font="arial 10 italic")
    label.pack(pady=5)
    def destroy_at_2sec():
        '''Function for destroying child italic hover window after 2 seconds'''
        child.destroy()
    child.after(2000,destroy_at_2sec)

def italic_destroy(event=None):
    '''Function for destroying child italic hover window when mouse leave italic button'''
    global child
    child.destroy()

# Binding italic_button for hovering effect 
italic_button.bind("<Enter>",italic_events)
italic_button.bind("<Leave>",italic_destroy)


def underline_events(event=None):
    '''Function to display underline hovering effect when mouse enters underline button'''
    global child
    child=tk.Toplevel()
    child.overrideredirect(1)
    child.geometry("120x50+500+100")
    child.configure(bg="skyblue")
    label=tk.Label(child,text="Underline the text\nCtrl+U",bg="skyblue",font="arial 10 underline")
    label.pack(pady=5)
    def destroy_at_2sec():
        '''Function for destroying child underline hover window after 2 seconds'''
        child.destroy()
    child.after(2000,destroy_at_2sec)

def underline_destroy(event=None):
    '''Function for destroying child underline hover window when mouse leave underline button'''
    global child
    child.destroy()

# Binding underline_button for hovering effect
underline_button.bind("<Enter>",underline_events)
underline_button.bind("<Leave>",underline_destroy)


def align_left_events(event=None):
    '''Function to display left alignment hovering effect when mouse enters align_left button'''
    global child
    child=tk.Toplevel()
    child.overrideredirect(1)
    child.geometry("120x50+500+100")
    child.configure(bg="skyblue")
    label=tk.Label(child,text="Left Align the text\nCtrl+L",bg="skyblue",font="arial 10",justify="left")
    label.pack(pady=5)
    def destroy_at_2sec():
        '''Function for destroying child align_left hover window after 2 seconds'''
        child.destroy()
    child.after(2000,destroy_at_2sec)

def align_left_destroy(event=None):
    '''Function for destroying child align_left hover window when mouse leave align_left button'''
    global child
    child.destroy()

# Binding align_left_button for hovering effect
align_left_button.bind("<Enter>",align_left_events)
align_left_button.bind("<Leave>",align_left_destroy)


def align_center_events(event=None):
    '''Function to display center alignment hovering effect when mouse enters align_center button'''
    global child
    child=tk.Toplevel()
    child.overrideredirect(1)
    child.geometry("130x50+500+100")
    child.configure(bg="skyblue")
    label=tk.Label(child,text="Center Align the text\nCtrl+E",bg="skyblue",font="arial 10",justify="center")
    label.pack(pady=5)
    def destroy_at_2sec():
        '''Function for destroying child align_center hover window after 2 seconds'''
        child.destroy()
    child.after(2000,destroy_at_2sec)

def align_center_destroy(event=None):
    '''Function for destroying child align_center hover window when mouse leave align_center button'''
    global child
    child.destroy()

# Binding align_center_button for hovering effect
align_center_button.bind("<Enter>",align_center_events)
align_center_button.bind("<Leave>",align_center_destroy)


def align_right_events(event=None):
    '''Function to display right alignment hovering effect when mouse enters align_right button'''
    global child
    child=tk.Toplevel()
    child.overrideredirect(1)
    child.geometry("130x50+500+100")
    child.configure(bg="skyblue")
    label=tk.Label(child,text="Right Align the text\nCtrl+R",bg="skyblue",font="arial 10",justify="right")
    label.pack(pady=5)
    def destroy_at_2sec():
        '''Function for destroying child align_right hover window after 2 seconds'''
        child.destroy()
    child.after(2000,destroy_at_2sec)

def align_right_destroy(event=None):
    '''Function for destroying child align_right hover window when mouse leave align_right button'''
    global child
    child.destroy()

# Binding align_right_button for hovering effect
align_right_button.bind("<Enter>",align_right_events)
align_right_button.bind("<Leave>",align_right_destroy)


def font_color_events(event=None):
    '''Function to display font color hovering effect when mouse enters font_color button'''
    global child
    child=tk.Toplevel()
    child.overrideredirect(1)
    child.geometry("150x50+500+100")
    child.configure(bg="skyblue")
    label=tk.Label(child,text="Changes the Font color",bg="skyblue",font="arial 10")
    label.pack(pady=5)
    def destroy_at_2sec():
        '''Function for destroying child font_color hover window after 2 seconds'''
        child.destroy()
    child.after(2000,destroy_at_2sec)

def font_color_destroy(event=None):
    '''Function for destroying child font_color hover window when mouse leave font_color button'''
    global child
    child.destroy()

# Binding font_color_button for hovering effect
font_color_button.bind("<Enter>",font_color_events)
font_color_button.bind("<Leave>",font_color_destroy)


########################### End Text Editor ##################################

############################ Status Bar ####################################

status_bar=tk.Label(texteditor,text="Status Bar",font="timesnewroman 8 bold")
status_bar.pack(side="bottom",fill="x")

# Global variable which keeps record of any change made in text editor
text_change=False  


def change_status(root):
    '''Function to display changing effect to status bar (Counting words and character)'''
    global text_change
    if texteditor.edit_modified():  # method which activate when any change reflected in text editor
        text_change=True
        words=len(texteditor.get(1.0,"end-1c").split())
        # words variable contain length of word in text editor 
        character=len(texteditor.get(1.0,"end-1c"))
        # character variable contain length of each character in text editor 
        status_bar.config(text=f"Character {character} Words {words}")
    texteditor.edit_modified(False)  # Deactivate the method so that method can be called again when changes made, Otherwise method is called only one time.

# Binding of text editor for any reflecting any modification
texteditor.bind("<<Modified>>",change_status)

####################### End Status bar ######################################


# ########################### main menu bar functionality ####################


'''File Menu'''

# Functions of file menu ####

url=""  # global variable for keeping record of filepath during save

def new_file(event=None):
    '''Function for creating new text editor window'''
    global url
    global text_change
    try:
        if url=="":
            if len(texteditor.get("1.0","end-1c"))==0:
                # if there is no text in text editor, it states that there is no change in text editor.
                text_change=False
            if text_change==False:
                texteditor.delete(1.0,tk.END)
                root.title("Untitled - My Notepad")
            else:
                value=messagebox.askyesnocancel("My Notepad","Do You Want to save changes to Untitled")
                if value==True:
                    url=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save File",defaultextension=".txt",filetypes=(("Text Files","*.txt"),("All Files","*.*")))
                    # tkinter has filedialog class which has asksaveasfilename() method which opens dialog box for saving file.
                    with open(url,"w",encoding='utf-8')as f:
                        f.write(str(texteditor.get(1.0,"end")))
                    root.title(os.path.basename(url)+ " - My Notepad")
                    text_change=False
                elif value==False:
                    texteditor.delete(1.0,tk.END)
                    root.title("Untitled - My Notepad")
                    url=""
                elif value==None:
                    pass
        else:
            if text_change==False:
                texteditor.delete(1.0,tk.END)
                root.title("Untitled - My Notepad")
                url=""
            else:
                value=messagebox.askyesnocancel("My Notepad",f"Do You Want to save changes to {os.path.basename(url)}")
                if value==True:
                    with open(url,"w",encoding='utf-8')as f:
                        f.write(texteditor.get(1.0,"end"))
                        url=""
                        text_change=False
                elif value==False:
                    texteditor.delete(1.0,tk.END)
                    root.title("Untitled - My Notepad")
                    url=""
                elif value==None:
                    pass
    except Exception as err:
        return
        
def open_file(event=None):
    '''Function for opening already saved file'''
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select file",filetypes=(("Text Files","*.txt"),("All Files","*.*")))
    # filedialog class which has askopenfilename() method which opens dialog box for opening file.
    try:
        with open(url,"r")as f:
            texteditor.delete(1.0,tk.END)
            texteditor.insert(1.0,f.read())
    except:
        return
    root.title(os.path.basename(url)+ " - My Notepad")
def save_file(event=None):
    '''Function for saving a new file or currently working file'''
    global url,text_change
    try:
        if url=="":
            url=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save File",defaultextension=".txt",filetypes=(("Text Files","*.txt"),("All Files","*.*")))
            with open(url,"w",encoding='utf-8')as f:
                f.write(str(texteditor.get(1.0,"end")))
            root.title(os.path.basename(url)+ " - My Notepad")
        else:
            with open(url,"w",encoding='utf-8')as f:
                f.write(str(texteditor.get(1.0,"end")))
            root.title(os.path.basename(url)+ " - My Notepad")
        text_change=False  # After saving file, text editor has no changes 
    except:
        return

def save_as(event=None):
    '''Function for saving a file with new name'''
    global url,text_change
    try:
        content=texteditor.get(1.0,"end")
        url=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save As",defaultextension=".txt",filetypes=(("Text Files","*.txt"),("All Files","*.*")))
        with open(url,"w",encoding='utf-8')as f:
            f.write(content)
        root.title(os.path.basename(url)+ " - My Notepad")
        text_change=False
    except :
        return

def exit_file(event=None):
    '''Function for exitting the text editor'''
    global url,text_change
    try:
        if url=="":  # if no file is opened
            if len(texteditor.get("1.0","end-1c"))==0:
                text_change=False
            if text_change==False:
                root.destroy()    # close the text editor
            else:
                value=messagebox.askyesnocancel("My Notepad","Do You Want to save changes to Untitled")
                if value==True:
                    url=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save File",defaultextension=".txt",filetypes=(("Text Files","*.txt"),("All Files","*.*")))
                    with open(url,"w",encoding='utf-8')as f:
                        f.write(str(texteditor.get(1.0,"end")))
                        text_change=False
                    root.title(os.path.basename(url)+ " - My Notepad")
                    root.destroy()
                elif value==False:
                    root.destroy()
                elif value==None:
                    pass
        else:
            if text_change==False:
                root.destroy() 
            else:
                value=messagebox.askyesnocancel("My Notepad",f"Do You Want to save changes to {os.path.basename(url)}")
                if value==True:
                    with open(url,"w",encoding='utf-8')as f:
                        f.write(texteditor.get(1.0,"end"))
                        text_change=False
                        root.destroy()
                elif value==False:
                    root.destroy()
                elif value==None:
                    pass
    except:
        return

# if user closes window by clicking on X button, the protocol method activates
root.protocol("WM_DELETE_WINDOW",exit_file)  

# file menu command 

filemenu.add_command(label="New",image=new_icon,compound=tk.LEFT,accelerator="Ctrl+N",command=new_file)
filemenu.add_command(label="Open",image=open_icon,compound=tk.LEFT,accelerator="Ctrl+O",command=open_file)
filemenu.add_separator()
filemenu.add_command(label="Save",image=save_icon,compound=tk.LEFT,accelerator="Ctrl+S",command=save_file)
filemenu.add_command(label="Save_as",image=save_as_icon,compound=tk.LEFT,accelerator="Alt+S",command=save_as)
filemenu.add_separator()
filemenu.add_command(label="Exit",image=exit_icon,compound=tk.LEFT,accelerator="Ctrl+Q",command=exit_file)

'''Edit Menu'''

# Edit menu Functions

def clear_all(event=None):
    '''Function for clearing all text'''
    texteditor.delete(1.0,tk.END)

def find(event=None):
    '''Function for finding and replacing word'''
    find_box=tk.Toplevel()  # creates toplevel window
    def find_text_func():
        '''Function for finding word in the text editor'''
        word=find_text.get()
        texteditor.tag_remove("match","1.0",tk.END)
        # tag_remove method remove tag from text editor where first argument is tag name which is "match" . match tag finds matching word.
        matches=0
        if word:
            replace_button.configure(state="normal")
            replace_entry.configure(state="normal")
            start_pos="1.0"
            while True:
                start_pos=texteditor.search(word,start_pos,stopindex=tk.END)
                # search method search for the pattern passed at first argumnent. This method returns index of first character of the pattern. 
                if not start_pos:  # if no more words found ,loop break
                    break
                end_pos=f"{start_pos}+{len(word)}c"
                texteditor.tag_add("match",start_pos,end_pos)
                # add the tag with tag name
                matches+=1
                start_pos=end_pos
                texteditor.tag_config("match",foreground="red",background="yellow")
            if matches==0:
                messagebox.showinfo("My Notepad",f"Cannot find the text {word}")
        else:
            messagebox.showerror("Not Found","Cannot find the Word")
    def replace_text_func():
        '''Function for replacing a text with new text'''
        word=find_text.get()
        replace_word=replace_text.get()
        content=texteditor.get(1.0,tk.END)
        texteditor.delete(1.0,tk.END)
        new_content=content.replace(word,replace_word)
        texteditor.insert(1.0,new_content)
        replace_entry.delete(0,tk.END)
        find_entry.delete(0,tk.END)
        find_entry.focus()
        replace_button.configure(state="disabled")

    find_box.configure(bg="lightblue")
    find_box.geometry("400x300+200+200")
    find_box.wm_iconbitmap("icons2\\find.ico")
    find_box.resizable(0,0)   # window cannot be minimize or maximize
    find_box.title("Find and Replace")
    main_frame=tk.LabelFrame(find_box,text="Find and Replace",pady=10,padx=20,font="arial 10 bold",relief="raised")
    main_frame.pack(pady=50,padx=10)

    tk.Label(main_frame,text="Find Text",font="arial 10 bold").grid(row=0,column=0,padx=10)
    tk.Label(main_frame,text="Replace",font="arial 10 bold").grid(row=1,column=0,pady=10)

    find_text=tk.StringVar()
    replace_text=tk.StringVar()
    find_entry=tk.Entry(main_frame,textvariable=find_text,width=20,font="arial 10 bold")
    find_entry.grid(row=0,column=1,padx=5)
    find_entry.focus()
    replace_entry=tk.Entry(main_frame,textvariable=replace_text,width=20,font="arial 10 bold",state="disabled")
    replace_entry.grid(row=1,column=1,padx=5)

    tk.Button(main_frame,text="Find",command=find_text_func,width=10,font="arial 10 bold",relief="raised",bg="pink").grid(row=3,column=0,pady=20,padx=15)
    replace_button=tk.Button(main_frame,text="Replace",command=replace_text_func,state="disabled",width=10,font="arial 10 bold",relief="raised",bg="lightgreen")
    replace_button.grid(row=3,column=1,pady=10)
    find_box.mainloop()


def add_time_date(event=None):
    '''Function for adding current time and date in text editor'''
    time_date=time_date=datetime.datetime.now().strftime("%d/%m/%y , %H:%M:%S")
    texteditor.insert(tk.INSERT,time_date)


def select_all(event=None): 
    '''Function for selecting all texts in the text editor'''  
    texteditor.tag_add("sel",1.0,tk.END)
    # sel is tag name for selecting the text
    return "break"


# Edit menu command add

edit.add_command(label="Undo",image=undo_icon,compound=tk.LEFT,accelerator="Ctrl+Z",state="disabled")
edit.add_command(label="Redo",image=redo_icon,compound=tk.LEFT,accelerator="Ctrl+Y",state="disabled")
edit.add_separator()
edit.add_command(label="Cut",image=cut_icon,compound=tk.LEFT,accelerator="Ctrl+X",command=lambda : texteditor.event_generate("<Control x>"))
edit.add_command(label="Copy",image=copy_icon,compound=tk.LEFT,accelerator="Ctrl+C",command=lambda : texteditor.event_generate("<Control c>"))
edit.add_command(label="Paste",image=paste_icon,compound=tk.LEFT,accelerator="Ctrl+V",command=lambda : texteditor.event_generate("<Control v>"))
edit.add_separator()
edit.add_command(label="Clear All",image=clear_all_icon,compound=tk.LEFT,accelerator="Ctrl+Alt+C",command=clear_all)
edit.add_command(label="Find",image=find_icon,compound=tk.LEFT,accelerator="Ctrl+F",command=find)
edit.add_separator()
edit.add_command(label="Select All",image=select_all_icon,compound=tk.LEFT,accelerator="Ctrl+A",command=select_all)
edit.add_command(label="Time/Date",image=time_date_icon,compound=tk.LEFT,accelerator="Alt+T",command=add_time_date)


'''View Menu'''

# View menu functions

show_toolbar=True  # global variable for showing toolbar
show_statusbar=True  # global variable for showing statusbar

def toolbar():
    '''Function for showing or hiding toolbar'''
    global show_toolbar
    if show_toolbar==True:
        toolbar_label.pack_forget()
        show_toolbar=False
    else:
        texteditor.pack_forget()
        status_bar.pack_forget()
        toolbar_label.pack(side="top",fill="x")
        status_bar.pack(side="bottom",fill="x")
        texteditor.pack(fill="both",expand=True)
        show_toolbar=True

def statusbar():
    '''Function for showing or hiding statusbar'''
    global show_statusbar
    if show_statusbar==True:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side="bottom",fill="x")
        show_statusbar=True

# view menu command add
view.add_checkbutton(label="Hide Toolbar",image=tool_bar_icon,compound=tk.LEFT,command=toolbar)
view.add_checkbutton(label="Hide Status Bar",image=status_bar_icon,compound=tk.LEFT,command=statusbar)


'''Color Theme Menu'''

# Color Theme Functions

def change_theme():
    '''Function for configuring background and foreground color of text editor and statusbar'''
    color_tuple=color_dictionary[color_selected.get()]
    fg,bg=color_tuple
    texteditor.configure(fg=fg,bg=bg)
    status_bar.configure(fg=fg,bg=bg)

count=0  # variable for counting index of color_icon_tuple
for i in color_dictionary:
    color_theme.add_radiobutton(label=i,image=color_icon_tuple[count],compound=tk.LEFT,variable=color_selected,command=change_theme)
    count+=1


'''About Menu'''

# About menu function

def about_notepad():
    '''Function for displaying information about notepad'''
    child=tk.Toplevel()
    child.grab_set()         # only enable child window and disable root window
    child.title("About Notepad")
    child.wm_iconbitmap("icons2\\about_icon.ico")
    child.geometry("500x400")
    child.resizable(0,0)
    notepad_about_icon=tk.PhotoImage(file="icons2\\notepad_about.png")
    tk.Label(child,image=notepad_about_icon).pack(side="left",anchor="nw")
    tk.Label(child,text="Notepad - Version 1.0",font="Arial 12 bold").pack(pady=20)
    tk.Label(child,text="This Notepad contains almost all features required for text editor.\n\nThe version 1.0 of Notepad is compatiable in all Windows Version",font="comicsansms 10 bold",wraplength=300).pack(pady=20)
    message_var=tk.StringVar()
    message_var.set("For any help,please communicate me on")
    email_var=tk.StringVar()
    email_var.set("harshitraj4839@gmail.com")
    tk.Entry(child,textvariable=message_var,font="timesnewroman 10 bold",state="readonly",bd=0,width=200).pack(padx=50,pady=10)
    tk.Entry(child,textvariable=email_var,font="timesnewroman 10 bold",state="readonly",bd=0,width=50,bg="yellow").pack(padx=90)
    tk.Label(child,text="Designed and Programmed by -- Harshit Raj",font="arial 8 bold").pack(side="bottom",fill="x",padx=30)
    tk.Button(child,text="OK",command=child.destroy,font="arial 10 bold",width=10,bg="grey").pack(pady=40)
    child.mainloop()

# About menu command add

about.add_command(label="About Notepad/Help",image=about_icon,compound=tk.LEFT,command=about_notepad)

########################### end main menu functionality #####################

###################### Shortcut Key Binding ################################

root.bind("<Control-Alt-c>",clear_all)
root.bind("<Control-n>",new_file)
root.bind("<Control-o>",open_file)
root.bind("<Control-s>",save_file)
root.bind("<Alt-s>",save_as)
root.bind("<Control-f>",find)
root.bind("<Control-q>",exit_file)
root.bind("<Control-b>",change_bold)
root.bind("<Control-i>",change_italic)
root.bind("<Control-u>",change_underline)
root.bind("<Control-l>",align_left)
root.bind("<Control-e>",align_center)
root.bind("<Control-r>",align_right)
root.bind("<Control-a>",select_all)
root.bind("<Alt-t>",add_time_date)

######################## End Shortcut Key Binding #######################

############################### Undo ################################

root.config(menu=mainmenu)  # adding main menu bar to root window
root.mainloop()