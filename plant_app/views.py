from django.shortcuts import render
import numpy as np
from PIL import Image
import base64

from .deeplearning import model, output_list, graph, session


def index(request):
    if request.method == 'POST' and request.FILES.get('myfile'):
        myfile = request.FILES['myfile']

        # Convert image to base64 (preview)
        file_bytes = myfile.read()
        b64_img = base64.b64encode(file_bytes).decode('ascii')
        myfile.seek(0)

        # Process image
        img = Image.open(myfile).convert('RGB')
        img = img.resize((224, 224))
        img = np.array(img)

        # ✅ NORMALIZATION (important for model)
        img = img / 255.0

        img = np.expand_dims(img, axis=0)

        print("Image Shape:", img.shape)

        # Prediction
        with graph.as_default():
            with session.as_default():
                prediction = model.predict(img)

        print("Raw Prediction:", prediction)

        # ✅ BEST RESULT
        max_index = np.argmax(prediction)
        best_disease = output_list[max_index]
        confidence = float(prediction[0][max_index]) * 100

        # Clean name
        best_disease = best_disease.replace("___", " - ")

        # ✅ WARNING SYSTEM (instead of hiding result)
        if confidence < 40:
            warning = "⚠ Low confidence prediction"
        else:
            warning = ""

        print("BEST:", best_disease, confidence)

        return render(request, "plant_app/index.html", {
            'result': best_disease,
            'confidence': round(confidence, 2),
            'warning': warning,
            'file_url': b64_img
        })

    return render(request, "plant_app/index.html")