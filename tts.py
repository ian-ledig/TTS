from TTS.api import TTS

custom_model_path = "model/fichier.pth"

models = TTS().list_models()
model_name = TTS().load_model(custom_model_path)
tts = TTS(model_name=model_name, progress_bar=False, gpu=False)

tts.tts_to_file(text="Salut c'est moi tchoupi", file_path=OUTPUT_PATH)