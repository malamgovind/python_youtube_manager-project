import json 



def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []



def list_all_videos(videos):
    print("\n")
    print("-" * 70)

    if not videos:
        print("no videos found.")
    else:
        for index, video in enumerate(videos, start=1):
            print(f"{index}.video: {video['name']}, Duration: {video['time']}")
    print("-" * 70)



def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")

    videos.append({
        "name" : name,
        "time" : time
        })
    save_data_helper(videos)
    print("video added succesfully!!")



def update_video(videos):
    list_all_videos(videos)

    index = int(input("Enter the video number to update: "))

    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")

        videos[index-1] = {
            "name": name,
            "time": time
        }
        save_data_helper(videos)
        print("video updated successfully!")
    else:
        print("invalid index selected.")



def delete_video(videos):
    list_all_videos(videos)

    index = int(input("Enter the video number to delete: "))

    if 1 <= index <= len(videos):
        del videos[index - 1]

        save_data_helper(videos)
        print("Video deleted successfully!")
    else:
        print("Invalid video index selected.")



def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)




def main():
    videos = load_data()

    while True:
        print("\nYoutube Manager | Chose an option!")
        print("1. List all Youtube videos")
        print("2. Add a Youtube video")
        print("3. Update a Youtube video")
        print("4. Delete a Youtube video")
        print("5. Exit the app")

        choice = input("Enter your choice:")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("GoodBye!")
                break
            case _:
                print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()