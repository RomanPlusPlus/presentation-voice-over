import sys

from utils.movies import build_video_segments, merge_segments
from utils.presentations import extract_notes_from_pptx, pdf_to_images
from utils.text_to_speech_gen import text_to_speech
from utils.files import recreate_directory

"""
How to use: 

1. place both the .pptx and its .pdf version into the script's directory
2. Name them input.pptx and input.pdf
3. Run the script

Note: unfortunately, an automatic conversion of the pptx to pdf is impractical.
I checked, there is no reliable way to convert .pptx to .pdf using python, so I will not implement it.
The possible solutions require either a windows with powerPoint, or Libreoffice (which may break the design), or 
a low-level handling of presentation objects, which likely will also break the design.
"""


def cleanup_notes(chunks):
    clean_chunks = []
    counter = 0
    for chunk in chunks:
        cleaned = chunk.strip()
        if len(cleaned) > 0:
            clean_chunks.append(cleaned)
        else:
            print(f"Empty notes for slide {counter}! Fill it out and then retry.")
            sys.exit(1)

        counter += 1

    return clean_chunks


def build_audios_by_slide(clean_chunks, mp3s_dir):
    counter = 0
    for chunk in clean_chunks:
        print(f"Voicing the notes for the slide {counter}:\n{chunk}\n")
        text_to_speech(chunk.strip(), counter, mp3s_dir)

        counter += 1



input_pptx_file_path = "input.pptx"
input_pdf_file_path = "input.pdf"

mp3s_dir = "temp_audio_by_slide"
slides_dir = "temp_pres_images"
segments_dir = "temp_video_segment_by_slide"
result_dir = "000_RESULT"

temp_dirs = [mp3s_dir, slides_dir, segments_dir, result_dir]
print("Recreating temp directories...")
for temp_dir in temp_dirs:
    recreate_directory(temp_dir)

pdf_to_images(input_pdf_file_path, slides_dir, dpi=150)
notes = extract_notes_from_pptx(input_pptx_file_path)

clean_notes = cleanup_notes(notes)

build_audios_by_slide(clean_notes, mp3s_dir)

build_video_segments(mp3s_dir, slides_dir, segments_dir)

merge_segments(segments_dir, result_dir)
