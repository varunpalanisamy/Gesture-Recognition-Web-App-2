from flask import Flask, request, jsonify, render_template
import base64
from PIL import Image
import io
import torch
from torchvision import models, transforms

model = models.resnet18(pretrained=False)
model.fc = torch.nn.Linear(model.fc.in_features, 18)

# Load the state dictionary for the model
checkpoint = torch.load('ResNet18.pth', map_location=torch.device('cpu'))
model.load_state_dict(checkpoint['MODEL_STATE'])
model.eval()  # Set the model to evaluation mode

# Define the image transformations for preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

app = Flask(__name__, template_folder='.')  # Initialize Flask app


@app.route('/')
def index():
    return render_template('index.html')  # Render the main HTML page


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json  # Get JSON data from the request
        print("Received data:", data)  # Debugging statement
        image_data = base64.b64decode(data['image'])  # Decode the base64 image data
        image = Image.open(io.BytesIO(image_data))  # Open the image using PIL

        # Convert image to RGB if it's in RGBA format
        if image.mode == 'RGBA':
            image = image.convert('RGB')

        # Apply transformations to the image
        image = transform(image).unsqueeze(0)

        # Predict the gesture using the model
        with torch.no_grad():
            output = model(image)
            _, predicted = torch.max(output, 1)
            prediction = predicted.item()

        # Mapping of gesture classes to their names
        gesture_map = {0: "call", 1: "dislike", 2: "fist", 3: "four", 4: "like",
                       5: "mute", 6: "ok", 7: "one", 8: "palm", 9: "peace",
                       10: "peace_inverted", 11: "rock", 12: "stop",
                       13: "stop_inverted", 14: "three", 15: "three2",
                       16: "two_up", 17: "two_up_inverted"}

        predicted_gesture = gesture_map.get(prediction, "Unknown gesture")  # Get gesture name

        print("Predicted gesture:", predicted_gesture)  # Debugging statement

        return jsonify({'gesture': predicted_gesture})  # Return predicted gesture as JSON
    except Exception as e:
        print("Error during prediction:", e)  # Debugging statement
        return jsonify({'error': str(e)}), 500  # Return error as JSON



if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
