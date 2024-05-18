import os

from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips


def video_from_image_and_mp3(image_path, audio_path, output_path):
    # Create a video clip from the image
    clip = ImageClip(image_path)

    # Load the audio file
    audio = AudioFileClip(audio_path)

    # Set the duration of the image clip to the duration of the audio clip
    audio_duration = audio.duration

    clip = clip.set_duration(audio_duration)

    # Set the audio of the image clip to be the audio clip
    clip = clip.set_audio(audio)

    fps = 6  # Frames per second

    # Write the result to a file
    clip.write_videofile(output_path, fps=fps, codec="libx264")


def build_video_segments(mp3s_dir, slides_dir, segments_dir):

    mp3s = os.listdir(mp3s_dir)
    slides = os.listdir(slides_dir)

    # keep only the paths of the mp3 files:
    mp3s = [file for file in mp3s if file.endswith(".mp3")]

    # keep only the paths of the png slides:
    slides = [file for file in slides if file.endswith(".png")]

    # stop script if the number of mp3s and slides are not the same
    if len(mp3s) != len(slides):
        print("Number of mp3s and slides are not the same")
        return None

    # create a list of tuples with the slide and mp3 file paths
    for i in range(len(mp3s)):
        slide = os.path.join(slides_dir, f"slide_{i}.png")
        mp3 = os.path.join(mp3s_dir, f"speech_{i}.mp3")

        print(f"Creating video segment for slide {i}...")
        video_from_image_and_mp3(
            slide, mp3, os.path.join(segments_dir, f"segment_{i}.mp4")
        )


def merge_segments(video_dir, result_dir):
    import os
    from moviepy.editor import VideoFileClip, concatenate_videoclips

    # List all files in the directory and filter out the video files
    video_files = [
        file
        for file in os.listdir(video_dir)
        if file.startswith("segment_") and file.endswith(".mp4")
    ]

    # Sort the files by the segment number
    video_files.sort(key=lambda x: int(x.split("_")[1].split(".")[0]))

    # Load the videos in order
    videos = [VideoFileClip(os.path.join(video_dir, file)) for file in video_files]

    print("concatenating videos")
    final_clip = concatenate_videoclips(videos)

    # Write the result to a file
    output_path = os.path.join(result_dir, "output_concatenated_video.mp4")
    final_clip.write_videofile(output_path, codec="libx264")

    # Close all clips to free resources
    for clip in videos:
        clip.close()


