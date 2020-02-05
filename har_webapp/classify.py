from app import app
import pandas as pd
import numpy as np
from scipy import stats
from keras.models import model_from_json

COLUMNS = ['x-axis', 'y-axis', 'z-axis']
LABELS = ['Downstairs', 'Jogging', 'Sitting', 'Standing', 'Upstairs', 'Walking']
MODEL_PATH = "app/model/model.json"
WEIGHTS_PATH = "app/model/model.h5"


def process_raw_data(data):
    df = pd.read_csv(data, header=None, names=COLUMNS)
    return df


def create_data_segmentation(dataset, window, increment):
    segmented_dataset = []

    for i in range(0, len(dataset) - window, increment):
        x_axis = dataset['x-axis'].values[i: i + window]
        y_axis = dataset['y-axis'].values[i: i + window]
        z_axis = dataset['z-axis'].values[i: i + window]
        segmented_dataset.append([x_axis, y_axis, z_axis])
    
    segmented_dataset = np.asarray(segmented_dataset, dtype=np.float32)
    transposed_segments = segmented_dataset.reshape(-1, window, 3)
    return transposed_segments


def load_model(model_path, weights_path):
    json_file = open(model_path, 'r')
    loaded_model = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model)
    loaded_model.load_weights(weights_path)
    return loaded_model


def classify_activity(model, processed_data):
    keras_prediction = np.argmax(model.predict(processed_data), axis=1)
    return LABELS[keras_prediction[0]]


def perform_har_classification(data):
    model = load_model(MODEL_PATH, WEIGHTS_PATH)
    raw_data = process_raw_data(data)
    segmented_data = create_data_segmentation(raw_data, 200, 20)
    output = classify_activity(model, segmented_data)
    return output