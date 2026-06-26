import sqlite3

conn = sqlite3.connect("02_with_sqlite3/youtube.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')


def list_video():
    print("\n")
    print("-" * 70)
    cursor.execute("SELECT * FROM videos")
    datas = cursor.fetchall()
    for data in datas:
        print(f"ID: {data[0]} | Name: {data[1]} | Time: {data[2]}")
    print("-" * 70)

def add_video():
    name = input("Enter the video name: ")
    time = input("Enter the video time: ")
    cursor.execute("""INSERT INTO videos(name, time)
                   VALUES(?, ?)
                   """,(name, time))
    conn.commit()
    print("video succesfully added$")

def update_video():
    list_video()
    video_id = input("Enter video ID to update: ")
    name = input("Enter new video name: ")
    time = input("Enter new video time: ")

    cursor.execute("UPDATE videos SET name = ? , time = ? WHERE id = ?",(name,time,video_id))
    conn.commit()
    print("video succesfully updated!")
    
def delete_video():
    list_video()
    video_id = input("Enter video ID to delete: ")
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    conn.commit()
    print("video succesfully deleted@")

def main():
    while True:
        print("\nYouTube Manager App with DB")
        print("1. List videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_video()
        elif choice == '2':
            add_video()
        elif choice == '3':
            update_video()
        elif choice == '4':
            delete_video()
        elif choice == '5':
            break
        else:
            print("Invalid number!!, Try again.")

    conn.close()

if __name__ == "__main__":
    main()