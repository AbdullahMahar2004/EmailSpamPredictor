# Email Spam Predictor

A machine learning web application that classifies emails as spam or not spam using Flask and scikit-learn.

## Features

- **Web Interface**: Simple and intuitive web interface for email classification
- **Machine Learning**: Uses pre-trained machine learning models for accurate spam detection
- **Real-time Prediction**: Instant classification of email content
- **Flask Web Framework**: Lightweight and responsive web application

## Project Structure

```
EmailSpamPredictor/
├── app.py                     # Main Flask application
├── requirements.txt           # Python dependencies
├── models/
│   ├── clf.pkl               # Pre-trained classifier model
│   └── cv.pkl                # CountVectorizer for text preprocessing
└── templates/
    └── spam_classifier.html  # HTML template for the web interface
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AbdullahMahar2004/EmailSpamPredictor.git
   cd EmailSpamPredictor
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Access the web interface**
   - Open your browser and navigate to `http://localhost:8080`
   - Enter email content in the text area
   - Click the "Button" to classify the email
   - View the prediction result (Spam/Not Spam)

## Dependencies

- **Flask 3.1.1** - Web framework
- **scikit-learn 1.7.1** - Machine learning library
- **numpy 2.3.1** - Numerical computing
- **scipy 1.16.0** - Scientific computing
- **joblib 1.5.1** - Model serialization

See `requirements.txt` for the complete list of dependencies.

## How It Works

1. **Text Preprocessing**: The input email text is processed using a pre-trained CountVectorizer (`cv.pkl`)
2. **Classification**: The processed text is fed to a trained classifier model (`clf.pkl`)
3. **Prediction**: The model returns a prediction (1 for spam, -1 for not spam)
4. **Display**: The result is displayed on the web interface with color coding (red for spam, green for not spam)

## Model Information

The application uses pre-trained models stored in the `models/` directory:
- `clf.pkl`: The main classification model
- `cv.pkl`: CountVectorizer for text tokenization and feature extraction

## Configuration

The Flask application runs with the following default settings:
- **Host**: 0.0.0.0 (accessible from all network interfaces)
- **Port**: 8080
- **Debug Mode**: Enabled

You can modify these settings in the `app.py` file.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions or suggestions, please contact:
- **GitHub**: [@AbdullahMahar2004](https://github.com/AbdullahMahar2004)

## Future Enhancements

- [ ] Add model training pipeline
- [ ] Implement email file upload functionality
- [ ] Add batch processing capabilities
- [ ] Improve UI/UX design
- [ ] Add confidence scores for predictions
- [ ] Implement API endpoints for programmatic access
