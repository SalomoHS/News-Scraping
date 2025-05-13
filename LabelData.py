from LoadConfig import file_path
from simpletransformers.classification import ClassificationModel
from loguru import logger

reverse_label_mapping = {
    0 : "Positive",
    1 : "Neutral",
    2 : "Negative"
}

def call_model():
    logger.info('Call Sentiment Labeling Model')
    MODEL_PATH = file_path['model_sentiment_labeling']
    loaded_model = ClassificationModel('bert', MODEL_PATH, use_cuda = False)
    return loaded_model

def classify_sentiment(df):
    loaded_model = call_model()
    summarized = df['summarized'].tolist()
    logger.info('Classify Sentiment')
    predictions,_ = loaded_model.predict(summarized)
    df['sentiment'] = predictions
    df['sentiment'] = df['sentiment'].map(reverse_label_mapping)
    return df