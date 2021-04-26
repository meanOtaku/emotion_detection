import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model('EmotionModel')
tflite_model = converter.convert()
open("LiteEmotionDetectionModel.tflite", "wb").write(tflite_model)