import warnings
warnings.simplefilter('ignore')
import pickle

model=pickle.load(open(r"C:\sds\project\self_project\lr_final.pickle","rb"))

"""
def predict_species(SepalLengthCm,SepalWidthCm, PetalLengthCm, PetalWidthCm):
    x = np.zeros(4)
    x[0] = SepalLengthCm
    x[1] = SepalWidthCm
    x[2] = PetalLengthCm
    x[3] = PetalWidthCm
    species= Iris_model.predict([x])[0]
    return species

"""
def predict_species(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm):
    if model.predict([[SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]])==[0]:
        return "setosa"
    elif model.predict([[SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]])==[1]:
        return "versicolor"
    elif model.predict([[SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]])==[2]:
        return "verginica"
    
#print(predict_species(2,2,3,1))

