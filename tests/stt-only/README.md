#Start STT Service
docker-compose up -d stt

# Test your STT system
# Install test dependencies (if not already installed)
pip install -r tests/requirements.txt

# Run the audio test
python tests/audio_test.py