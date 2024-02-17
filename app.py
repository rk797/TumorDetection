from flask import Flask, render_template, request, jsonify, send_from_directory, url_for, redirect
from ultralytics import YOLO
import cv2
import os

app = Flask(__name__)

model = YOLO('./models/best.pt', task='detect')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        #some logic to handle file upload
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)

        result = inference(file_path)
        
        return send_from_directory('uploads', os.path.basename(result['data']['output_image_path']))
    
    
def inference(image_path):
    # inference
    results = model(image_path, conf=0.5)

    boxes = results[0].boxes
    #extract box coords and confidence
    info = boxes[0].data[0]
    xmin = info[0].item()
    ymin = info[1].item()
    xmax = info[2].item()
    ymax = info[3].item()
    confidence = info[4].item()

    original_image = cv2.imread(image_path)

    cv2.rectangle(original_image, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 0, 255), 2)

    text = f"Confidence: {confidence:.2f}"
    cv2.putText(original_image, text, (int(xmin), int(ymin) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    output_image_path = os.path.join('uploads', 'output_' + os.path.basename(image_path))
    cv2.imwrite(output_image_path, original_image)

    return {'success': True, 'data': {'output_image_path': output_image_path, 'confidence': confidence}}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)