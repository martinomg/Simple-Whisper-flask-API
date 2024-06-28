import whisper
import sys
import os
import json
import argparse

def whisper_transcribe_fn(
    file_path,
    model="small",
    task="transcribe",
    verbose=True,
    output_format="json",
    output_dir="./res",
    output_path=None
):
    # Load model
    model = whisper.load_model(model)

    print(f"Transcribing {file_path}")

    result = model.transcribe(
        file_path,
        verbose=verbose,
        fp16=True,
        task=task
    )

    # Output transcription
    if output_format == 'json':
        if output_path is None:
            output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(file_path))[0] + '.json')
        else:
            output_file = output_path
        
        # Create directories if they don't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'w') as f:
            json.dump(result, f)
            print(f"Transcription saved to {output_file}")
    else:
        print(result["text"])

    return result