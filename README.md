# Simple Whisper flask API

This repository contains a simple Flask API for transcribing audio files using the Whisper model.

# Whisper Transcribe CLI

`whisper-transcribe-cli.py` is a command-line interface (CLI) tool to transcribe audio files using the Whisper model. This script allows you to transcribe audio files and save the transcriptions in JSON format or print them to the console.

## Requirements

- Python 3.9+
- `whisper` library
- `argparse` library

## Installation

1. Install the required libraries:

```bash
pip install whisper
```

2. Clone this repository or download the script.

## Usage

The script can be run from the command line with various options to specify the input file, model size, transcription task, verbosity, and output format. Below are the details of the available arguments.

### Arguments

- `file_path` (required): Path to the audio file to be transcribed.
- `--model`: Size of the Whisper model to use (default: `tiny`).
- `--task`: Type of task (`translate` (default) | `transcribe`).
- `--verbose`: Enable verbose mode (default: `True`).
- `--output_format`: Format of the output (`json` (default)).
- `--output_path`: Path to save the output file. If not specified, the file will be saved in the `output_dir`.
- `--output_dir`: Directory to save the output file (default: `./res`).

### Example Commands

#### Basic Transcription

Transcribe an audio file and save the result in JSON format to the default directory.

```bash
python whisper-transcribe-cli.py samples/dragons.wav
```

#### Specify Model Size

Transcribe using a different model size.

```bash
python whisper-transcribe-cli.py samples/sofiavergaraspanish.clip.wav --model base
```

#### Change Task Type

Change the task to `transcribe`.

```bash
python whisper-transcribe-cli.py samples/interview_speech-analytics.wav --task transcribe
```

#### Disable Verbose Mode

Run the script without verbose output.

```bash
python whisper-transcribe-cli.py samples/dragons.wav --verbose False
```

#### Specify Output Format

Print the transcription text to the console instead of saving it as a JSON file.

```bash
python whisper-transcribe-cli.py samples/sofiavergaraspanish.clip.wav --output_format text
```

#### Custom Output Path

Save the transcription to a specific file path.

```bash
python whisper-transcribe-cli.py samples/interview_speech-analytics.wav --output_path ./results/interview_transcription.json
```

#### Custom Output Directory

Specify a different directory to save the transcription.

```bash
python whisper-transcribe-cli.py samples/dragons.wav --output_dir ./output
```

## Example Transcriptions

Here are some example commands using files from the `samples` directory:

```bash
python whisper-transcribe-cli.py samples/dragons.wav
python whisper-transcribe-cli.py samples/sofiavergaraspanish.clip.wav --model small --task transcribe
python whisper-transcribe-cli.py samples/interview_speech-analytics.wav --verbose False --output_format text
python whisper-transcribe-cli.py samples/dragons.wav --output_path ./results/dragons_transcription.json
python whisper-transcribe-cli.py samples/sofiavergaraspanish.clip.wav --output_dir ./transcriptions
```

Feel free to modify these commands as per your requirements.


# Flask API for Whisper Transcription

`app.py` is a Flask-based API that provides an interface to upload audio files and transcribe them using the Whisper model. This script allows you to interact with the Whisper transcription functionality via HTTP requests.

## Requirements

- Python 3.9+
- `flask` library
- `whisper` library (and its dependencies)
- `werkzeug` library (for secure file saving)

## Installation

1. Install the required libraries:

```bash
pip install flask whisper werkzeug
```

2. Clone this repository or download the script.

## Usage

The Flask API can be started from the command line and provides endpoints to interact with the Whisper transcription functionality.

### Running the API

To start the Flask API, run the following command:

```bash
python app.py
```

The API will be accessible at `http://0.0.0.0:5678`.

### Endpoints

#### GET /

This endpoint returns a simple message to verify that the API is running.

**Request:**

```http
GET /
```

**Response:**

```json
{
  "message": "Hello from API on port 5678!"
}
```

#### POST /upload

This endpoint allows you to upload an audio file for transcription. The file is saved to the `uploads` directory, and the transcription is performed using the Whisper model.

**Request:**

```http
POST /upload
Content-Type: multipart/form-data
```

**Form Data:**

- `file`: The audio file to be transcribed.

**Response:**

The transcription result is returned in the response. The format depends on the implementation of the `whisper_transcribe_fn`.

### Example Request

Here is an example using `curl` to upload a file for transcription:

```bash
curl -X POST -F "file=@path_to_your_audio_file.wav" http://0.0.0.0:5678/upload
```

## File Structure

- `app.py`: The main Flask application script.
- `whisper_transcribe_fn.py`: This script should contain the function `whisper_transcribe_fn` which handles the transcription logic using the Whisper model.
- `uploads/`: Directory where uploaded files are saved.

## Implementation Details

### app.py

This script sets up the Flask application with two endpoints: `/` for a simple health check and `/upload` for uploading files and performing transcriptions. It ensures the `uploads` directory exists and saves uploaded files securely.

### whisper_transcribe_fn.py

Ensure you have a `whisper_transcribe_fn.py` file with the following function defined:

```python
import whisper

def whisper_transcribe_fn(file_path):
    # Load the Whisper model
    model = whisper.load_model("tiny")

    # Perform the transcription
    result = model.transcribe(file_path)

    # Return the transcription result (modify as needed)
    return result["text"]
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.