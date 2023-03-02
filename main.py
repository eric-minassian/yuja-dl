import os
import time

from seleniumwire import webdriver


def main():
    link = input("Enter the link: \n")
    get_dependencies()
    print("Dependencies Successfully Downloaded!")
    print("Downloading the video...")
    print("DO NOT CLOSE THE WINDOW!")
    print("Please be patient, this may take a while...")
    video_list = get_video_link(link)
    download_videos(video_list)
    print("Video Successfully Downloaded!")


def get_dependencies():
    if os.system("./dependencies.sh") != 0:
        print("Error in downloading the dependencies")
        exit()


def download_videos(video_list):
    if os.path.exists("output1.mp4"):
        os.system("rm output1.mp4")
    if os.path.exists("output2.mp4"):
        os.system("rm output2.mp4")

    # Download the videos
    os.system(
        f"ffmpeg -i '{video_list[0]}' -c copy 'output1.mp4' -hide_banner -loglevel error -nostats"
    )
    os.system(
        f"ffmpeg -i '{video_list[1]}' -c copy 'output2.mp4' -hide_banner -loglevel error -nostats"
    )

    # Check output directory and get next filename for output
    count = 0
    if not os.path.exists("output"):
        os.makedirs("output")
    else:
        while True:
            if not os.path.exists(f"output/output{count}.mp4"):
                break
            count += 1

    # Merge the videos
    os.system(f"ffmpeg -i output1.mp4 -i output2.mp4 -c copy output/output{count}.mp4")

    # Delete the temporary files
    os.system("rm output1.mp4")
    os.system("rm output2.mp4")


def get_video_link(link):
    # Initialize the driver
    driver = webdriver.Chrome()

    # Capture requests
    driver.get(link)
    time.sleep(10)
    video_list = []

    # Get audio and video links
    count = 0
    for request in driver.requests:
        if count == 2:
            break

        # If the request is a m3u8 file add it to the list
        if (
            request.response
            and request.response.headers["content-type"]
            == "application/x-mpegURL; charset=UTF-8"
        ):
            count += 1
            video_list.append(str(request.response.headers["yuja-url"]))
    driver.quit()

    return video_list


if __name__ == "__main__":
    main()
