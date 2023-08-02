import codecs
import csv
import datetime
from app.api.database.db import database
from app.api.log.logger import logger,levels

def processCsvFile(file):
    csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
    IdsAdded = 0
    for rows in csvReader:
        Id = rows['VerificationCode']
        if database.read({"VerificationCode": Id}) != None:
            continue

        IdsAdded +=1

        date = datetime.datetime.now()
        date = date.strftime("%d/%m/%Y")
        rows["DateAdded"] = date
        database.writeRecords(rows)
    logger.log(levels.warning,f"Add Product Verification: {IdsAdded} more records added")
    return {"status":200,"records_added":IdsAdded}





