import joblib
import pandas as pd
import json

from django.shortcuts import render
from django.http import JsonResponse


model = joblib.load('house_price_model.pkl')


def home(request):

    prediction = None

    if request.method == 'POST':

        bedrooms = float(request.POST['bedrooms'])
        bathrooms = float(request.POST['bathrooms'])
        sqft_living = float(request.POST['sqft_living'])
        sqft_lot = float(request.POST['sqft_lot'])
        floors = float(request.POST['floors'])
        waterfront = int(request.POST['waterfront'])
        view = int(request.POST['view'])
        condition = int(request.POST['condition'])
        sqft_above = float(request.POST['sqft_above'])
        sqft_basement = float(request.POST['sqft_basement'])
        yr_built = int(request.POST['yr_built'])

        new_house = pd.DataFrame([{
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'sqft_living': sqft_living,
            'sqft_lot': sqft_lot,
            'floors': floors,
            'waterfront': waterfront,
            'view': view,
            'condition': condition,
            'sqft_above': sqft_above,
            'sqft_basement': sqft_basement,
            'yr_built': yr_built
        }])

        prediction = model.predict(new_house)[0]

        # Check if it's an AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'prediction': float(prediction)})

    return render(
        request,
        'predictor/index.html',
        {'prediction': prediction}
    )