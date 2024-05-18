## Overview
The script creates a narrated video from your presentation. 

It uses the impressively human-like text-to-speech model from OpenAI to generate the narration.

As inputs, it takes a pptx file and the pdf version of the same presentation. 
You have to provide both. 

As the output, it generates a video with your slides and the narration of the notes.

Don't forget to write the narration text into the notes of each slide. 

## Sample output:

<video width="600" controls>
  <source src="000_RESULT/output_concatenated_video.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- OpenAI API key

It works in MacOS. It should work in Linux, but it has not been tested.
Not sure about Windows.

### Installation
1. Clone the repository and cd into it.

2. Create and activate the virtual environment:
    ```bash
    python -m venv venv

    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip3 install -r requirements.txt
    ```

### Usage
1. Place your input files (both PDF and PowerPoint) in the root directory of the project.

Name them `input.pdf` and `input.pptx`.

2. In the terminal, set the API key:

```bash
export OPENAI_API_KEY='your_key'
```

2. Run the main script:
    ```bash
    python3 main.py
    ```
   
If it complains about "The api_key client option", this means you forgot to set the OpenAI API key. 

3. The output video will be generated and placed into the `000_RESULT` directory.

## How it works:

The main script coordinates the process by:
- Converting PDF to an image for each slide.
- Extracting notes from the PowerPoint file.
- A light cleaning of the extracted notes.
- Generating audio for each notes text, using text-to-speech.
- Creating a video segment for each slide, from the image and the audio.
- Merging video segments into the final video.

## License
This project is licensed under the MIT License.