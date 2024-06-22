# Hybrid Recommendation System

## Project Overview

This project implements an advanced hybrid recommendation system that combines Amazon Personalize, TensorFlow Lite, and Firebase ML Kit. The system aims to provide more accurate and personalized recommendations by integrating multiple approaches.

## Key Components

1. **Data Collection and Preprocessing** (`src/data_processing/`)
   - Collect user data from Firebase
   - Data preprocessing and normalization

2. **Amazon Personalize Integration** (`src/recommenders/personalize_recommender.py`)
   - Generate recommendations using Amazon Personalize

3. **TensorFlow Lite Model** (`src/models/tf_lite_model.py`)
   - Create and use custom TensorFlow Lite models

4. **Firebase ML Kit Integration** (`src/ml_kit/firebase_ml_kit.py`)
   - On-device inference using Firebase ML Kit

5. **Hybrid Recommender** (`src/recommenders/hybrid_recommender.py`)
   - Generate final recommendations by combining multiple recommendation sources

## Setup Instructions

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set up credentials for Firebase, Amazon Personalize, and TensorFlow Lite.

3. Create the TensorFlow Lite model and save it as `model.tflite`.

4. Deploy the model to Firebase ML Kit.

## Usage

1. Data Collection:
   ```python
   from src.data_processing.data_collector import collect_user_data, preprocess_data

   raw_data = collect_user_data()
   processed_data = preprocess_data(raw_data)
   ```

2. Get Recommendations:
   ```python
   from src.recommenders.hybrid_recommender import HybridRecommender

   recommender = HybridRecommender()
   recommendations = recommender.get_recommendations(user_id, user_data)
   ```

## Development Guidelines

1. Code Style: Follow PEP 8 guidelines.
2. Testing: Add corresponding unit tests in the `tests/` directory when adding new features.
3. Documentation: Add appropriate docstrings to functions and classes.

## Future Improvements

1. Model performance evaluation and optimization
2. Implementation of more advanced recommendation fusion algorithms
3. Integration of real-time feedback
4. Scalability improvements

## License

This project is licensed under the [MIT License](LICENSE).
