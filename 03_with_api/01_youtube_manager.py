import sqlite3

conn = sqlite3.connect("03_with_api/youtube.db")
cursor = conn.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS videos
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT NOT NULL,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
""")
conn.commit()

def list_video():
    pass

def add_video():
    pass

def update_video():
    pass

def delete_video():
    pass


def main():

    while True:

        print("\n")
        print("=" * 50)
        print("     YouTube Manager With API + SQLite")
        print("=" * 50)

        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")

        choice = input("\nEnter Your Choice : ")

        if choice == "1":
            list_video()

        elif choice == "2":
            add_video()

        elif choice == "3":
            update_video()

        elif choice == "4":
            delete_video()

        elif choice == "5":
            print("\nThank You!")
            break

        else:
            print("\nInvalid Choice! Try Again.")

    conn.close()


if __name__ == "__main__":
    main()