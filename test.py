import mysql.connector
import tkinter as tk
from tkinter import messagebox

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",       # Promjeni ako koristiš drugi host
        user="root",            # Korisničko ime MySQL korisnika
        password="",            # Lozinka MySQL korisnika
        database="sara"         # Ime baze podataka
    )

def validate_user(username, password):
    try:
        db = connect_to_database()
        cursor = db.cursor()
        query = "SELECT * FROM user WHERE user = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        db.close()
        return result is not None
    except mysql.connector.Error as err:
        messagebox.showerror("Greška", f"Greška prilikom povezivanja sa bazom: {err}")
        return False

def register_user(username, password):
    try:
        db = connect_to_database()
        cursor = db.cursor()
        query = "INSERT INTO user (user, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        db.commit()
        db.close()
        return True
    except mysql.connector.Error as err:
        messagebox.showerror("Greška", f"Greška prilikom registracije: {err}")
        return False

def login_action(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()

    if validate_user(username, password):
        messagebox.showinfo("Uspeh", f"Prijava uspešna! Dobrodošli, {username}.")
    else:
        messagebox.showerror("Greška", "Pogrešno korisničko ime ili password. Pokušajte ponovo.")

def register_action(username_entry, password_entry, root):
    username = username_entry.get()
    password = password_entry.get()

    if register_user(username, password):
        messagebox.showinfo("Uspeh", "Registracija uspešna! Možete se prijaviti.")
        root.destroy()
    else:
        messagebox.showerror("Greška", "Registracija nije uspela.")

def create_registration_screen():
    reg_root = tk.Toplevel()
    reg_root.title("Register Screen")

    # Postavljanje manjeg prozora centriranog na ekranu
    window_width, window_height = 300, 200
    screen_width = reg_root.winfo_screenwidth()
    screen_height = reg_root.winfo_screenheight()
    position_x = (screen_width - window_width) // 2
    position_y = (screen_height - window_height) // 2
    reg_root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
    
    # Postavljanje always on top atributa
    reg_root.attributes('-topmost', True)

    tk.Label(reg_root, text="Korisničko ime:").pack(pady=5)
    username_entry = tk.Entry(reg_root)
    username_entry.pack(pady=5)

    tk.Label(reg_root, text="Password:").pack(pady=5)
    password_entry = tk.Entry(reg_root, show="*")
    password_entry.pack(pady=5)

    tk.Button(reg_root, text="Registriraj se", command=lambda: register_action(username_entry, password_entry, reg_root)).pack(pady=10)

    reg_root.mainloop()

def create_login_screen():
    root = tk.Tk()
    root.title("Login Screen")

    # Postavljanje prozora na skoro fullscreen (sa kontrolama)
    window_width, window_height = root.winfo_screenwidth() - 100, root.winfo_screenheight() - 100
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_x = (screen_width - window_width) // 2
    position_y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    tk.Label(root, text="Korisničko ime:", font=("Arial", 14)).pack(pady=20)
    username_entry = tk.Entry(root, font=("Arial", 14))
    username_entry.pack(pady=10)

    tk.Label(root, text="Password:", font=("Arial", 14)).pack(pady=10)
    password_entry = tk.Entry(root, show="*", font=("Arial", 14))
    password_entry.pack(pady=10)

    tk.Button(root, text="Prijavi se", font=("Arial", 14), command=lambda: login_action(username_entry, password_entry)).pack(pady=20)
    tk.Button(root, text="Registracija", font=("Arial", 14), command=create_registration_screen).pack(pady=10)

    root.mainloop()

def create_users_table():
    try:
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user VARCHAR(50) NOT NULL,
                password VARCHAR(50) NOT NULL
            )
        """)
        cursor.execute("""
            INSERT INTO user (user, password)
            VALUES
            ('test', '123'),
            ('admin', 'admin123')
            ON DUPLICATE KEY UPDATE user=user
        """)
        db.commit()
        db.close()
        print("Tabela `user` kreirana i testni korisnici dodati.")
    except mysql.connector.Error as err:
        print(f"Greška: {err}")

if __name__ == "__main__":
    # Opciono: Pokrenuti samo jednom za kreiranje tabele
    # create_users_table()

    # Pokreni login ekran
    create_login_screen()
