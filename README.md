# SkinAura - AI-Powered Skin Disease Classification

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.16-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

An intelligent web application that uses deep learning to classify skin diseases and provide personalized health recommendations using Convolutional Neural Networks (CNN) and Google Generative AI.

## Features

- **Image Upload**: Upload skin condition images in JPG, JPEG, or PNG format
- **Disease Prediction**: Get instant predictions with confidence scores using deep learning
- **Detailed Information**: Receive comprehensive details about symptoms, causes, and treatments
- **AI Chatbot**: Ask questions about your condition and get personalized responses powered by Google Gemini AI
- **User Feedback**: Rate your experience and provide feedback

## Technologies Used

- **Python** - Core programming language
- **Streamlit** - Web application framework
- **TensorFlow/Keras** - Deep learning framework
- **OpenCV** - Image processing
- **Google Generative AI** - Chatbot functionality
- **NumPy** - Numerical computing

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Google API Key ([Get one here](https://makersuite.google.com/app/apikey))
- Model file: `final_vgg1920epochs.h5`

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/bhavika2203/SkinAura.git
   cd SkinAura/skin_analyzer
   ```

2. **Create virtual environment (recommended)**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the `skin_analyzer` directory:
   ```bash
   GOOGLE_API_KEY=your_google_api_key_here
   HUGGINGFACE_TOKEN=your_huggingface_token_here  # Optional
   MODEL_PATH=final_vgg1920epochs.h5  # Optional
   ```
   
   > ⚠️ **Important**: Never commit your `.env` file! It's already in `.gitignore`.

5. **Add model file**
   
   Place your `final_vgg1920epochs.h5` model file in the `skin_analyzer` directory.

## Usage

### Running the Application

```bash
cd skin_analyzer
streamlit run app.py
```

The application will be accessible at: **http://localhost:8501**

### How to Use

1. Upload an image of a skin condition
2. Wait for AI analysis (usually takes a few seconds)
3. View the predicted disease with confidence score and detailed information
4. Ask questions using the chatbot for more information
5. Provide feedback on your experience

## Supported Diseases

The application can classify the following 8 categories of skin conditions:

1. Acne and Rosacea
2. Actinic Keratosis, Basal Cell Carcinoma, and other Malignant Lesions
3. Eczema
4. Melanoma, Nevi, and Moles
5. Psoriasis, Lichen Planus, and related diseases
6. Tinea, Ringworm, Candidiasis, and other Fungal Infections
7. Urticaria (Hives)
8. Nail Fungus and other Nail Diseases

## Project Structure

```
SkinAura/
├── skin_analyzer/
│   ├── app.py                 # Main Streamlit application
│   ├── hf.py                  # HuggingFace integration (optional)
│   ├── dat.json              # Disease information database
│   ├── requirements.txt      # Python dependencies
│   └── final_vgg1920epochs.h5 # Model file (not in repo)
├── .gitignore                # Git ignore rules
├── LICENSE                   # MIT License
└── README.md                 # This file
```

## Security

- All API keys are stored in `.env` (not committed to repository)
- Sensitive files are automatically excluded via `.gitignore`
- All credentials use environment variables
- HTTPS connections for all external services

> 🔐 **Remember**: Never share your API keys or commit them to version control!

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Bhavika**

- GitHub: [@bhavika2203](https://github.com/bhavika2203)

## Acknowledgments

- Special thanks to the open-source community and contributors
- The VGG19 model architecture for providing the base for our classifier
- Google's Gemini AI for powering our intelligent chatbot
- Medical resources and datasets that made this project possible

---

⭐ If you find this project helpful, please consider giving it a star!
