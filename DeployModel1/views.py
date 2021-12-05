
from django.http import HttpResponse

from django.shortcuts import render

# import joblib


# import librosa

# import keras

# from keras.models import load_model
# import h5py

# from sklearn.externals import joblib

def home(request):
    # return HttpResponse(" my ML model is working")
    return render(request, 'home.html' )


# def result(request):

#     saveBestModel = keras.callbacks.ModelCheckpoint('/audio_classification',
#     monitor='val_acc', verbose=0, save_best_only=True, save_weights_only=False, mode='auto', period=1)

#     # from keras.models import load_model
#     # import h5py
#     prd_model = load_model('audio_classification.hdf5')




    # model = joblib.load('audio_classification.hdf5')
    # D:\DeployModel1-project\audio_classification.hdf5
    #  getting the keyerror at this step again and again........

    #  now take the user imputs here and put the model to work
    # lis = []
    # lis.append(request.GET['audio1'])

    # ans = cls.predict([lis])


    
    # filename = "audio1"
    # audio, sample_rate = librosa.load(filename, res_type = 'kaiser_fast')
    # mfcc_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)

    # mfcc_scaled_features = np.mean(mfcc_features.T, axis=0)

    # mfcc_scaled_features = mfcc_scaled_features.reshape(1,-1)

    # # predicted_label = model.predict_classes(mfcc_scaled_features)
    # predicted_label = model.predict(mfcc_scaled_features)

    # prediction_class = labelencoder.inverse_transform(predicted_label)

    # print(prediction_class, " is our result")

    # return render(request, 'result.html', {'class': prediction_class })

    # import keras
    # print(keras.__version__)

    # return render(request, 'result.html')

def audio_store(request):
    if request.method == 'POST':
        form = AudoForm(request.POST, request.FILES or None)

        if(form.is_valid()):
            form.save()
            return HttpResponse(" Successfully Uploaded the file")

    else:
        form=AudioForm()
    
    return render(request, 'aud.html', {'form': form})
