import whisper
import sys
import os
import json
import argparse

def main(args):
    # Load model
    model = whisper.load_model(args.model)

    print(f"Transcribing {args.file_path}")

    result = model.transcribe(
        args.file_path,
        verbose=args.verbose,
        fp16=False,
        task=args.task
    )

    # Output transcription
    if args.output_format == 'json':
        if args.output_path is None:
            output_file = os.path.join(args.output_dir, os.path.splitext(os.path.basename(args.file_path))[0] + '.json')
        else:
            output_file = args.output_path
        
        # Create directories if they don't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'w') as f:
            json.dump(result, f)
            print(f"Transcription saved to {output_file}")
    else:
        print(result["text"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe audio files.")
    parser.add_argument("file_path", help="Path to the audio file.")
    parser.add_argument("--model", default="tiny", help="Model size (default: tiny).")
    parser.add_argument("--task", default="translate", help="Type of task: translate (default)|transcribe")
    parser.add_argument("--verbose", default=True, action="store_true", help="Verbose mode.")
    parser.add_argument("--output_format", default="json", help="Output format (default: json).")
    parser.add_argument("--output_path", help="Output file path.")
    parser.add_argument("--output_dir", default="./res", help="Output directory (default: ./res).")

    args = parser.parse_args()
    main(args)
