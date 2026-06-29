from rest_framework import generics
from rest_framework.response import Response
from .serializers import ImageSerializer

import numpy as np
from PIL import Image

from plant_app.deeplearning import graph, model, output_list


class Predict(generics.CreateAPIView):
    serializer_class = ImageSerializer

    def post(self, request):
        data = ImageSerializer(data=request.data)

        if data.is_valid():
            photo = request.FILES['photo']

            # ✅ FIXED SIZE (224, 224)
            img = Image.open(photo).convert('RGB')
            img = img.resize((224, 224))

            img = np.array(img)
            img = img / 255.0
            img = np.expand_dims(img, axis=0)

            print("Shape:", img.shape)  # (1, 224, 224, 3)

            with graph.as_default():
                prediction = model.predict(img)

            prediction_flatten = prediction.flatten()
            max_val_index = np.argmax(prediction_flatten)
            result = output_list[max_val_index]

            return Response({'result': result})

        return Response({'error': 'Invalid input'})