import sqlite3
import requests

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

def fetch_username():

    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"]:
        username = data["data"]["name"]["first"]
        return username
    else:
        raise Exception("Failed to fetch username")

def list_video():
    print("\n")
    print("-" * 70)

    cursor.execute("SELECT * FROM videos")
    datas = cursor.fetchall()

    if len(datas) == 0:
        print("No videos Found")
    else:
        for data in datas:
            print(f"ID:{data[0]} | Username: {data[1]} | Video_Name: {data[2]} | Time: {data[3]}")

    print("-" * 70)

def add_video():
    try:
        username = fetch_username()
        print(f"\nUsername from API: {username}")

        name = input("Enter Video Name : ")
        time = input("Enter Video Duration : ")

        cursor.execute(""" INSERT INTO videos(username, name, time)
                       VALUES(?, ?, ?)""", (username, name, time)
                       )
        conn.commit()
        print("\nVideo added successfully!")

    except Exception as e:
        print(e)

def update_video():
    list_video()
    
    video_id = input("\nEnter Video ID To Update : ")

    name = input("Enter New Video Name : ")
    time = input("Enter New Duration : ")

    cursor.execute(""" 
    UPDATE videos
    SET name = ?, time = ?
    WHERE id = ?
    """, (name, time, video_id))
    conn.commit()

    print("\nVideo Updated Successfully!")

def delete_video():
    list_video()

    video_id = input("\nEnter Video ID To Delete : ")

    cursor.execute("""
    DELETE FROM videos
    WHERE id = ?
    """, (video_id,))

    conn.commit()

    print("\nVideo Deleted Successfully!")

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