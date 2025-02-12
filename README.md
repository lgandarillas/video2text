# Video to Text Converter

## Project Description
This project provides a tool to convert MP4 video files to MP3 audio files and transcribe the audio to text using the Whisper library. It is designed to run on macOS, Linux and Windows systems, facilitating the easy conversion and transcription of video content.
<br><br>
<img src="assets/diagram.webp" width="600" alt="Conversion Process Diagram">

## Features
- Convert MP4 video files to MP3 audio.
- Transcribe audio from MP3 files to text using OpenAI's Whisper model.

## Prerequisites
Ensure you have Python installed on your system (Python 3.8 or later is recommended). You can check your Python version by running:
```bash
python3 --version
```
## Setup and Installation

### 1. Clone the repository
First, clone this repository to your local machine using:
```bash
git clone https://github.com/lgandarillas/video2text-lgand.git
cd video2text-lgand
```

### 2. Create a Python Virtual Environment
To avoid any conflicts with existing Python packages, it is advisable to set up a virtual environment. Run the following command in the project directory:

```bash
python3 -m venv venv
```
Activate the virtual environment.<br>
On macOS and Linux:
```
source venv/bin/activate
```
On Windows:
```
.\venv\Scripts\activate
```

### 3. Install Required Packages
Install all required packages listed in the requirements.txt file:
```bash
pip install -r requirements.txt
```

## Usage
To use the converter, you need an MP4 file. Place your MP4 file in the same directory as the converter.py script or specify the path to the file when running the script.
Run the script using the following command:
```bash
python3 converter.py example_video.mp4
```
For example:
```bash
python3 converter.py Make_Your_Bed-McRaven.mp4
```

## Conclusion
This tool simplifies the process of converting videos to text, which can be useful for generating transcripts, analyzing spoken content, or simply extracting audio from video files.
