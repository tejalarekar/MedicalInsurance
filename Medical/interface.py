
from flask import Flask,jsonify,request,render_template
import config
from Project.utils import MedicalInsurance

app = Flask(__name__)


@app.route("/")
def home_api():
    return render_template("login.html")

@app.route("/predict_charges",methods = ["POST","GET"])
def get_medical_insurance_charges():
    if request.method == "POST":
        data = request.form
        age = int(data["age"])
        sex = data["sex"]
        bmi = eval(data["bmi"])
        children = int(data["children"])
        smoker = data["smoker"]
        region = data["region"]
        med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
        charges = med_ins.get_predicted_charges()
        return jsonify({"Result":f"Predicted Medical Insurance charges :{charges}"})
    else:
        age = int(request.args.get("age"))
        sex = request.args.get("sex")
        bmi = int(request.args.get("bmi"))
        children = int(request.args.get("children"))
        smoker = request.args.get("smoker")
        region = request.args.get("region")
        med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
        charges = med_ins.get_predicted_charges()
        return jsonify({"Result":f"Predicted Medical Insurance charges :{charges}"})



if __name__ == "__main__":
    app.run()