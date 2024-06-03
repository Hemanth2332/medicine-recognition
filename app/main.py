from fastapi import FastAPI, File, UploadFile, Request
import additionals, time

app = FastAPI()

UPLOAD_FOLDER = 'images'


@app.post("/api/image", tags=['api'])
async def process_image(user_id: str, file: UploadFile = File(...)):

    if additionals.check_user_id(user_id):
        ext = additionals.get_ext(file.filename)

        if ext in additionals.ALLOWED_EXT:
            file_contents = await file.read()
            with open(f"{UPLOAD_FOLDER}/{file.filename}", "wb") as f:
                f.write(file_contents)

            output = additionals.process_image()
            data = additionals.print_med_time(user_id, output)

        else:
            data = None

        print(output)
        print(data)
            
        return {
            "user_id": user_id,
            "time": int(time.time()),
            "result" : data
        }
        
    else:
        return {
            "user_id": user_id,
            "time": int(time.time()),
            "result" : None
        }


@app.post("/api/update_med_data", tags=['api'])
async def update_med_data(user_id: str, jsonData: Request) -> dict:

    data = await jsonData.json()
    result = additionals.update_med(user_id, data["data"])

    return {
        "time": int(time.time()),
        "user_id": user_id,
        "result": result
    }



@app.post("/api/delete_med_data", tags=['api'])
async def del_med_data(user_id: str, jsonData: Request) -> dict:

    data = await jsonData.json()
    result = additionals.delete_med(user_id, data["data"])

    return {
        "time": int(time.time()),
        "user_id": user_id,
        "result": result
    }


@app.post("/api/create_user", tags=['api'])
async def create_user(user_id:str):

    result = additionals.create_user(user_id)

    return {
        "time": int(time.time()),
        "user_id": user_id,
        "result": result
    }


@app.post("/api/delete_user", tags=['api'])
async def delete_user(user_id:str):

    result = additionals.del_user(user_id)

    return {
        "time": int(time.time()),
        "user_id": user_id,
        "result": result
    }

