#supposed original file
import os
from rich.console import Console

console = Console()

"""
written by: Paul Rhowen L. Cainong
"""

#============== music code blocks ============================


playlist = {
}

def show_playlist():
    if len(playlist) == 0:
        console.print("[black on red]\nno songs stored yet. please enter add a music to the list. [/]")
    else:
        print("\n>>>>>>>>>>>>> PlayList <<<<<<<<<<<<")
        for a, b in playlist.items():
            print(f"{b} by {a}") 
        return

def add_to_queue():
    print("\n>>>>>>>>>>>> Music Queueing Screen <<<<<<<<<<<<")
    artist_name = input("\nEnter music artist name: ").lower()
    music_title = input("\nEnter song title: ")
    playlist[artist_name] = music_title
    print(f"\n{playlist[artist_name]} successfully added to the list!")
    return

def play_music():
    artist_name = input("Enter the artist's name: ").lower()
    if artist_name not in playlist:
        console.print(f"[black on red] \ninvalid input. couldn't find {artist_name} from the list. [/]")
        console.print(f"[black on red] \nplease proceed to add_to_queue tab first [/]")
    else:
        print(f"\nplaying {playlist[artist_name]} by {artist_name}....")
        music_duration = 0
        print("\nmusic duration... ")
        for i in range(60):
            music_duration += 1
            print(f"{music_duration}s", end=" ")
        print("\nmusic finished playing.")

def music():
    console.print("[red on blue] \n<<<<<<<<<<<<< Nice Music Ver 2.71828 >>>>>>>>>>>> [/]")
    music_cond = True
    while music_cond:
        music_options = ["play_music", "add_to_queue","show_playlist", "exit_music"]
        print("\n>>>>>>>>> Music Menu Screen <<<<<<<<<<<<")
        for m in range(len(music_options)):
            print(music_options[m])
        music_choice = input("\nplease select from music tabs options: ")
        if music_choice == "play_music":
            play_music()
        elif music_choice == "add_to_queue":
            add_to_queue()
        elif music_choice == "show_playlist":
            show_playlist()
        elif music_choice == "exit_music":
            mus_confirm = input("\nExit Good Music? (yes/no) ").lower()
            if mus_confirm == "yes":
                music_cond = False
                break
        else:
            console.print("[black on red] \ninvalid input. choose from the tab options [/]")

#================= Notes Code Blocks ====================
def del_note():
    del_confirm = input("\ndelete note? (yes/no) ")
    if del_confirm == "yes":
        os.remove("notes_canvas.txt")
    else:
        console.print("[black on red] \noperation interrupted. [/]")

def view_note():
    try:
        with open("notes_canvas.txt", "r") as file:
            information = file.readlines()
            print("\n--------- Your Notes ---------")
            for info in information:
                print(info.strip())
            print("---------------------------------")
    except FileNotFoundError:
        console.print("[black on red] \nno notes located. append to your notes first. [/]")

def append_note():
    new_text = input("\nEnter your text: ")
    with open("notes_canvas.txt", "a") as file:
        file.write(new_text + "\n")
    print("Saved Successfully!")
    return

def notes():
    console.print("[red on blue] \n<<<<<<<<<<< Notes App Ver. 8.854E-12 >>>>>>>>>>> [/]")
    notes_cond = True
    while notes_cond:
        print("\n>>>>>>>>> Notes App Menu Screen <<<<<<<<<<<<<")
        notes_options = ["append_note", "view_note", "delete_note", "exit_note" ]
        for n in range(len(notes_options)):
            print(notes_options[n])
        notes_choice = input("Choose from notes tab: ")
        if notes_choice == "append_note":
            append_note()
        elif notes_choice == "view_note":
            view_note()
        elif notes_choice == "delete_note":
            del_note()
        elif notes_choice == "exit_note":
            notes_confirm = input("\nExit notes app? (yes/no) ").lower()
            if notes_confirm == "yes":
                notes_cond = False
                break
        else:
            console.print("[black on red] invalid input. please choose from the tab options [/]")

#================== Contacts Code Block =================================
#contact dictionary
store_contact = {
}

#contacts methods
def make_call():
    receiver_name = input("Enter a name to call: ").lower()
    if receiver_name not in store_contact:
        console.print(f"[black on red] \ninvalid input. couldn't find {receiver_name} from the list. [/]")
    else:
        print(f"calling {receiver_name}: {store_contact[receiver_name]}....")
        call_duration = 0
        print("call duration... ")
        for i in range(25):
            call_duration += 1
            print(f"{call_duration}s", end=" ")
        print("call ended.")

def show_list():
    if len(store_contact) == 0:
        console.print(f"[black on red] \nno data stored yet. please enter add a contact. [/]")
    else:
        print("\n>>>>>>>>>>>>> Contact List <<<<<<<<<<<<")
        for a, b in store_contact.items():
            print(f"{a}: {b}") 
        return
        

def new_contact():
    print("\n>>>>>>>>>>>> New Contact Screen <<<<<<<<<<<<")
    contact_name = input("\nEnter new contact name: ").lower()
    contact_number = int(input("\nEnter phone number with no dash or spaces: "))
    store_contact[contact_name] = contact_number
    print("\nNew contact successfully added to the list!")
    print(store_contact[contact_name])
    return


def contacts():
    console.print("[red on blue] \n <<<<<<<<<<<<<<< CONTACTS Ver. 9.81 >>>>>>>>>>>>> [/]")
    contacts_cond = True
    contacts_options = ["new_contact", "show_list", "make_call", "exit_contacts"]
    while contacts_cond:
        console.print("[red on cyan]\n<<<<<<<<<<< Contacts Menu Screen >>>>>>>>>>>>>>>")
        for c in range(len(contacts_options)):
            print(contacts_options[c])
        contact_choice = input("\nChoose a tab from the menu screen: ").lower()
        if contact_choice == "new_contact":
            new_contact()
        elif contact_choice == "show_list":
            show_list()
        elif contact_choice == "make_call":
            make_call()
        elif contact_choice == "exit_contacts":
            cont_confirm = input("Exit contacts app? (yes/no): ").lower()
            if cont_confirm == "yes":
                contacts_cond = False
                break
        else:
            console.print("[black on red] \ninvalid tab choice. please select from the options only. [/]")

#================== Calculator Code Blocks ==========================

def power(x,y): 
    power_ans =  x ** y
    return float(power_ans)

def divide(x,y):
    quotient = x /y
    return float(quotient)

def multiply(x,y):
    product = x * y
    return float(product)

def subtract(x,y):
    difference = x - y
    return float(difference)

def add(x,y):
    sum = x + y
    return float(sum)


def calculator():
    console.print("[red on blue] \n<<<<<<<< Calcultor fx ver. 3.1415 >>>>>>>>> [/]")
    use_calc = True
    while use_calc == True:   
        try:
            x = float(input("\nEnter your first number: "))
            y = float(input("\nEnter your second number: "))
        except ValueError:
            console.print("[black on red] \nWarning! invalid datatype. please a number [/]")

        operations = ["add", "subtract", "multiply", "divide", "power","exit_calculator"]
        for i in range(len(operations)):
            print(operations[i])

        z = input("\nChoose an operation from above: ").lower()
        if z == "add":
            print(add(x,y))
        elif z == "subtract":
            print(subtract(x,y))
        elif z == "multiply":
            print(multiply(x,y))
        elif z == "divide":
            print(divide(x,y))
        elif z == "power":
            print(power(x,y))
        elif z == "exit_calculator":
            exit_calc = input("\nDo you want to exit calculator? (yes/no)").lower()
            if exit_calc == "yes":
                use_calc = False
                break
            else:
                use_calc = True
        else:
            console.print("[black on red] \ninvalid operation input. select from the choices [/]")

#=============== Greetings ============================
def greetings():
    for i in range (101):
        console.print(f"[green on black] loading... {i}% [/]")
    console.print("[green on black] Initializing Sequence.... [/]")
    console.print("[bold cyan] <<<<<<<<<<< SMARTPHONE >>>>>>>>> [/]")
    console.print("[bold white]\n Welcome, Dear User! [/]")

#================ Main Function =============================
def main():
    greetings()
    phone_use = "yes"

    while phone_use == "yes":
        console.print("[red on cyan]\n [bold red]>>>>>>>>>>>>> Apps Display Screen <<<<<<<<<<< [/]")
        apps = ["calculator", "contacts", "notes", "music", "exit"]
        for j in range(len(apps)):
            print(apps[j])
        app_selection = input("\nPlease choose a displayed app on the screen: ").lower()
        if app_selection == "calculator":
            calculator()
        elif app_selection == "contacts":
            contacts()
        elif app_selection == "notes":
            notes()
        elif app_selection == "music":
            music()
        elif (app_selection == "exit"):
            response = input("Exit console-based smartphone? (yes/no): ").lower()
            if response == "yes":
                phone_use = False
                break
        else:
            console.print("[black on red] \n invalid input. please choose from apps list [/]")

if __name__ == "__main__":
    main()