from src.models.predict_model import Predict_label

### Argumentos com o caminho do datasets para predição

SUBMISSION_DATA_PATH = './data/raw/test_data.csv'
SAMPLE_SUBMISSION_PATH = './data/raw/sample_submission.csv'
OUTPUT_PATH = './Submissions/submission.csv'

### Iniciando a Predição

prediction = Predict_label(SUBMISSION_DATA_PATH,SAMPLE_SUBMISSION_PATH)
prediction.start(output_path=OUTPUT_PATH)
