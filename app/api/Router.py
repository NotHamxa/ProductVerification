from fastapi import APIRouter,UploadFile
from fastapi.responses import RedirectResponse
from app.api.log.logger import Log,levels
import csv
import codecs
from app.api.database.db import Database
import datetime
from app.core.Config import settings,AdminData
logger = Log(settings.logKey)
router = APIRouter()
database =Database(settings.dbPassword,settings.dbDatabase)

@router.get("/")
def redirect():
    return RedirectResponse("/docs")

@router.get("/verify/{productID}")
def verify(productID:str):
    response = database.read({"VerificationCode":productID})
    if response==None:
        return {"detail":False}
    else:
        return {"detail":True}


@router.post("/addproducts/")
async def AddProducts(LogInData:AdminData,file:UploadFile):
    state,query = database.checkAdmin(LogInData.Username, LogInData.Password)
    if not state:
        if query==1:
            logger.log(levels.warning,"Add Product Verification:Admin username does not exist")
        elif query==2:
            logger.log(levels.warning,f"Add Product Verification:Password for username '{LogInData.Username}' is incorrect")
        return {"detail":query}
    csvReader =csv.DictReader(codecs.iterdecode(file.file,'utf-8'))
    IdsAdded=[]
    for rows in csvReader:
        Id = rows['VerificationCode']
        if database.read({"VerificationCode":Id}) !=None:
            continue

        IdsAdded.append(rows["VerificationCode"])

        date = datetime.datetime.now()
        date = date.strftime("%d/%m/%Y")
        rows["DateAdded"] = date
        database.writeRecords(rows)

    if len(IdsAdded)!=0:
        logger.log(levels.warning,f"Admin '{LogInData.Username}' added {len(IdsAdded)} records")
        return "added records for",IdsAdded
    return "No new records detected"
