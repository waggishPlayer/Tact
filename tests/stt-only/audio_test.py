#!/usr/bin/env python3
import sounddevice as sd
import numpy as np
import wave
import requests
import tempfile
import os

def record_and_transcribe_explicit(duration=5, sample_rate=16000, language="hindi"):
    """Record audio and test with explicit language"""
    
    print(f"Recording for {duration} seconds for {language.upper()} transcription... Speak now!")
    
    # Record audio
    audio_data = sd.rec(int(duration * sample_rate), 
                       samplerate=sample_rate, 
                       channels=1, 
                       dtype=np.int16)
    sd.wait()  # Wait until recording is finished
    print("Recording finished!")
    
    # Create temporary WAV file
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_file:
        temp_filename = temp_file.name
        
        # Write to WAV file
        with wave.open(temp_filename, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)  # 16-bit = 2 bytes
            wf.setframerate(sample_rate)
            wf.writeframes(audio_data.tobytes())
    
    try:
        # Send to STT service with explicit language
        with open(temp_filename, 'rb') as audio_file:
            files = {'audio': audio_file}
            response = requests.post(f'http://localhost:5001/transcribe/{language}', files=files)
            
        if response.status_code == 200:
            result = response.json()
            print(f"Transcription ({language}): {result['text']}")
            print(f"Specified Language: {result['specified_language']}")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to STT service. Make sure it's running on localhost:5001")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Clean up temporary file
        os.unlink(temp_filename)

def record_and_transcribe(duration=5, sample_rate=16000):
    """Record audio for specified duration and send to STT service with automatic language detection"""
    
    print(f"Recording for {duration} seconds... Speak now (Hindi or English)!")
    
    # Record audio
    audio_data = sd.rec(int(duration * sample_rate), 
                       samplerate=sample_rate, 
                       channels=1, 
                       dtype=np.int16)
    sd.wait()  # Wait until recording is finished
    print("Recording finished!")
    
    # Create temporary WAV file
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_file:
        temp_filename = temp_file.name
        
        # Write to WAV file
        with wave.open(temp_filename, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)  # 16-bit = 2 bytes
            wf.setframerate(sample_rate)
            wf.writeframes(audio_data.tobytes())
    
    try:
        # Send to STT service with automatic language detection
        with open(temp_filename, 'rb') as audio_file:
            files = {'audio': audio_file}
            response = requests.post('http://localhost:5001/transcribe', files=files)
            
        if response.status_code == 200:
            result = response.json()
            print(f"Transcription: {result['text']}")
            print(f"Detected Language: {result['detected_language']}")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to STT service. Make sure it's running on localhost:5001")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Clean up temporary file
        os.unlink(temp_filename)

def main():
    print("Tact STT - Automatic Language Detection")
    print("=======================================")
    print("Speak in Hindi or English - the system will automatically detect and transcribe!")
    print()
    record_and_transcribe()

if __name__ == "__main__":
    main()
