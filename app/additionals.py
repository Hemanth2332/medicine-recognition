import json
import os,easyocr
from PIL import Image
from fuzzywuzzy import fuzz
# from paddleocr import PaddleOCR


ocr = easyocr.Reader(['en'], gpu=False)
# ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)

ALLOWED_EXT = {'jpg', 'jpeg', 'png'}

################################################################
def get_ext(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower()

################################################################
def check_user_id(user_id:str):
    with open("database.json", "r") as f:
        con = json.load(f)

    if user_id in con.keys():
        return True
    
    else:
        return False
    
#################################################################
def process_image()-> list:

    if len(os.listdir("images")) != 0:
        img_path = f"images/{os.listdir('images')[-1]}"
        img = Image.open(img_path)
        
        if img.size != (600,600):
            reimg = img.resize((600,600))
            reimg.save(img_path)
        result = ocr.readtext(img_path, detail=False)
        os.remove(img_path)
        return result
    else:
        return []

##################################################################  
def print_med_time(user_id:str, ocrlist):
    with open("database.json", "r") as f:
        data = json.load(f)

    meds_key = data[user_id]
    for meds in meds_key:
            for ocr_out in ocrlist:
                if fuzz.partial_ratio(meds, ocr_out.lower()) > 60:
                # if meds == ocr_out.lower():
                    return {"medicine": meds,
                        "period": data[user_id][meds]
                        }

######################################################################
def update_med(user_id:str, med_data:dict) -> dict:
    try:
        with open("database.json", "r") as jsonFile:
            data = json.load(jsonFile)

        data[user_id].update(med_data)

        with open("database.json", "w") as jsonFile:
            json.dump(data, jsonFile, indent=4) 

        data = "success"
    
    except:
        data = "failed to update"

    return {"data": data}
    
################################################################# 
def delete_med(user_id: str, med_name:str) -> dict:
    try:
        with open("database.json", "r") as f:
            data = json.load(f)

        del data[user_id][med_name]

        with open("database.json", "w") as f:
            json.dump(data, f, indent=4)

        data = "success"

    except:
        data = "failed to update"
    
    return {"data": data}

#########################################################
def create_user(user_id:str) -> dict:
    try:
        with open("database.json", "r") as jsonFile:
                data = json.load(jsonFile)

        if user_id not in data.keys():
            data[user_id] = {}

        with open("database.json", "w") as jsonFile:
            json.dump(data, jsonFile, indent=4) 
        
        out = "success"
    
    except:
        out = "failed to create"

    return {"data":out}


####################################################
def get_content(result:list):
  contents = []
  for i in range(len(result)):
      res = result[i]
      for j in res:
          for k in j:
            if type(k) is tuple:
              contents.append(k[0])
  return contents

######################################################
def del_user(user_id:str) -> dict:
    try:
        with open("database.json", "r") as f:
            data = json.load(f)

        del data[user_id]

        with open("database.json", "w") as f:
            json.dump(data, f, indent=4)

        data = "success"

    except:
        data = "failed to update"
    
    return {"data": data}
