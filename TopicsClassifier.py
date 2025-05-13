from LoadConfig import file_path
from simpletransformers.classification import ClassificationModel
from loguru import logger

reverse_label_mapping = {
    0 : "EKONOMI MAKRO",
    1 : "INOVASI DAN TEKNOLOGI",
    2 : "ISU DAN KONTROVERSI",
    3 : "KINERJA KEUANGAN",
    4 : "LAINNYA",
    5 : "PENGHARGAAN DAN PENGAKUAN",
    6 : "PROMOSI PRODUK",
    7 : "REKOMENDASI INVESTASI"
}

def classify_topics(df):
    logger.info('Classify Topics')
    MODEL_PATH = file_path['model_topics_classifier']
    loaded_model = ClassificationModel('bert', MODEL_PATH, use_cuda = False)
    texts = df['summarized'].tolist()
    predictions,_ = loaded_model.predict(texts)
    df['topics'] = predictions
    df['topics'] = df['topics'].map(reverse_label_mapping)
    return df