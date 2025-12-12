package main

import (
	"errors"
	"fmt"
	"log"
	"os"
	"path/filepath"
)

func main() {
	// log.SetPrefix("greetings: ")
	// log.SetFlags(0)

	fmt.Println("--- Offline Text File to Audiobook Converter ---")
	inputName := "input_testfile.txt"
	outputName := "output_testfile.wav"
	inputFile := filepath.Join("INPUT", inputName)
	outputFile := filepath.Join("OUTPUT", outputName)
	result, err := create_offline_audiobook(inputFile, outputFile)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(result)
}

func create_offline_audiobook(input_txt_path string, output_audio_path string) (string, error) {
	/*
		Reads a .txt file and converts its content into an audio file using pyttsx3 (offline).

		:param input_txt_path: Path to the input text file (e.g., 'story.txt').
		:param output_audio_path: Path to save the output audio file (e.g., 'audiobook.mp3' or 'audiobook.wav').
	*/
	// 1. Initialize the TTS engine

	result := "success"

	if input_txt_path == "" {
		return input_txt_path, errors.New("Please provide input filename it can't be empty!")
	}
	if output_audio_path == "" {
		return output_audio_path, errors.New("Please provide output filename it can't be empty!")
	}

	data, err := os.ReadFile(input_txt_path)
	if err != nil {
		error_temp := fmt.Sprintf("Error reading file: %v\n", err)
		return "", errors.New(error_temp)
	}

	fmt.Printf(string(data))

	return result, nil
}

// import os
// import pyttsx3
// import time

// def create_offline_audiobook(input_txt_path, output_audio_path):
//     """
//     Reads a .txt file and converts its content into an audio file using pyttsx3 (offline).

//     :param input_txt_path: Path to the input text file (e.g., 'story.txt').
//     :param output_audio_path: Path to save the output audio file (e.g., 'audiobook.mp3' or 'audiobook.wav').
//     """
//     # 1. Initialize the TTS engine
//     try:
//         engine = pyttsx3.init()
//     except Exception as e:
//         print(f"Error initializing pyttsx3 engine. Ensure your system's native TTS engine is available. Details: {e}")
//         return

//     try:
//         # 2. Read the text from the input file
//         with open(input_txt_path, 'r', encoding='utf-8') as f:
//             text_to_speak = f.read()

//         if not text_to_speak.strip():
//             print(f"Error: The file '{input_txt_path}' is empty or contains only whitespace.")
//             return

//         print(f"Text read successfully. Length: {len(text_to_speak)} characters.")

//         # 3. Use pyttsx3 to save the speech to a file
//         # NOTE: pyttsx3 usually saves as WAV on Windows/Linux or AIFF on macOS.
//         # It's safest to use .wav, but some systems can handle .mp3 if the correct driver is installed.
//         print(f"Generating audio and saving to '{output_audio_path}'...")
//         engine.save_to_file(text_to_speak, output_audio_path)

//         # This line is crucial: it runs the speech synthesis process and saves the file.
//         engine.runAndWait()

//         print("Conversion complete!")
//         print(f"File saved at: {os.path.abspath(output_audio_path)}")

//     except FileNotFoundError:
//         print(f"Error: Input file not found at '{input_txt_path}'")
//     except Exception as e:
//         print(f"An unexpected error occurred: {e}")
//     finally:
//         # Stop the engine to free up resources
//         if 'engine' in locals():
//             engine.stop()

// # --- Interactive CLI Usage ---
// if __name__ == "__main__":
//     print("--- Offline Text File to Audiobook Converter ---")

//     # Get input and output filenames from the user
//     input_name = input("Enter the input text file name (e.g., story.txt): ").strip()

//     # Default output name will now be .wav for maximum pyttsx3 compatibility
//     default_output = os.path.splitext(input_name)[0] + ".wav"
//     output_name = input(f"Enter the output audio file name (default: {default_output}): ").strip() or default_output

//     input_file = os.path.join("INPUT", input_name)
//     outpu_file = os.path.join("OUTPUT", output_name)
//     create_offline_audiobook(input_file, outpu_file)
