from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import joblib

def home(request):
    return render(request, 'index.html')

def detect_fraud(request):
    if request.method == 'POST':
        # Get input from the form
        transaction_data = {
            
            
            'type': int(request.POST['type']),
            'amount': float(request.POST['amount']),
            
            'oldbalanceOrg': float(request.POST['oldbalanceOrg']),
            'newbalanceOrig': float(request.POST['newbalanceOrig']),
            
            'oldbalanceDest': float(request.POST['oldbalanceDest']),
            'newbalanceDest': float(request.POST['newbalanceDest']),
            
        }

        # Convert the input data to a DataFrame
        input_data = pd.DataFrame([transaction_data])

        # Load the pre-trained Random Forest model
        model = joblib.load(r'model.pkl')

        # Make a prediction
        is_fraud = model.predict(input_data)[0]

        # Return the result as JSON
        return JsonResponse({'is_fraud': bool(is_fraud)})

    return JsonResponse({'error': 'Invalid request method'})


