# Tact - Accessibility Platform

Tact is a comprehensive accessibility platform that provides speech-to-text, text-to-speech, and braille conversion services. The platform is designed to help individuals with visual and hearing impairments interact with digital content more effectively.

## 🚀 Features

- **Speech-to-Text (STT)**: Real-time audio transcription with support for English and Hindi
- **Text-to-Speech (TTS)**: Convert text to natural-sounding speech
- **Braille Conversion**: Transform text into braille format
- **Multi-language Support**: Currently supports English and Hindi
- **Docker-based Architecture**: Easy deployment and scaling

## 🏗️ Architecture

The project consists of multiple microservices:

- **STT Service**: Handles speech recognition and transcription
- **TTS Service**: Manages text-to-speech conversion
- **Braille Service**: Converts text to braille format
- **Shared Components**: Common utilities and models

## 📋 Prerequisites

- Docker and Docker Compose
- Python 3.8+
- Vosk speech recognition models

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/tact.git
   cd tact
   ```

2. **Download Vosk Models**
   The project requires Vosk speech recognition models. Download them to the `models/vosk/` directory:
   - English model: `vosk-model-small-en-us-0.15`
   - Hindi model: `vosk-model-small-hi-0.22`

3. **Start the services**
   ```bash
   docker-compose up --build
   ```

## 🚀 Usage

### Speech-to-Text Service

The STT service runs on port 5001 and provides the following endpoints:

- `POST /transcribe` - Auto-detect language and transcribe
- `POST /transcribe/<lang>` - Transcribe with specified language (english/hindi)

Example usage:
```bash
curl -X POST http://localhost:5001/transcribe \
  -H "Content-Type: multipart/form-data" \
  -F "audio=@your_audio_file.wav"
```

### Text-to-Speech Service

The TTS service provides text-to-speech conversion capabilities.

### Braille Service

The Braille service converts text to braille format.

## 🧪 Testing

Run the test suite:
```bash
cd tests/stt-only
python audio_test.py
```

## 📁 Project Structure

```
tact/
├── stt/                 # Speech-to-Text service
│   ├── app.py          # Flask application
│   ├── requirements.txt # Python dependencies
│   └── dockerfile      # Docker configuration
├── tts/                # Text-to-Speech service
├── braille/            # Braille conversion service
├── models/             # Vosk speech recognition models
├── shared/             # Shared utilities
├── tests/              # Test suite
└── docker-compose.yml  # Service orchestration
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Vosk](https://alphacephei.com/vosk/) for speech recognition models
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Docker](https://www.docker.com/) for containerization

## 📞 Support

For support and questions, please open an issue on GitHub or contact the development team.

---

**Note**: This project is designed for accessibility and inclusivity. We welcome contributions that improve the user experience for individuals with disabilities.
