# Vision Pro

## Description

This project utilizes Streamlit and Google's Generative AI to create a web application for extracting information from invoice images.

## Installation

Before running the application, make sure you have the necessary dependencies installed. You can install them using the following command:

    poetry install


This will install all the required dependencies specified in the `pyproject.toml` file.

## Usage

To run the application, execute the following command:

    poetry run streamlit run app.py 


This will start a local server where you can access the ML Invoice Extractor app in your web browser.

## Dependencies

- `dotenv`: For loading environment variables from a `.env` file.
- `streamlit`: A Python library for creating interactive web apps.
- `PIL`: The Python Imaging Library, used for working with images.
- `google.generativeai`: Google's Generative AI library for generating content.

## Configuration

Ensure that you have set up your environment variables correctly, particularly the `GOOGLE_API_KEY`, which is required for accessing Google's Generative AI models.

## Functionality

1. **Gemini App**: Allows users to input prompts and upload images of invoices.
2. **Image Processing**: Parses the uploaded image to extract relevant information.
3. **Response Generation**: Utilizes Google's Generative AI to generate a response based on the input prompt and uploaded image.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request to suggest improvements or report bugs.
