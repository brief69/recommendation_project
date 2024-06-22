import tensorflow as tf

def create_tf_lite_model(model):
    # TensorFlowモデルをTensorFlow Liteモデルに変換
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()
    
    # モデルをファイルに保存
    with open('model.tflite', 'wb') as f:
        f.write(tflite_model)

def load_tf_lite_model():
    # TensorFlow Liteモデルをロード
    interpreter = tf.lite.Interpreter(model_path="model.tflite")
    interpreter.allocate_tensors()
    return interpreter

def predict_with_tf_lite(interpreter, input_data):
    # TensorFlow Liteモデルで予測を実行
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    return output_data
