from sqlalchemy.orm import Session
from sqlalchemy import func, distinct

from . import models

END_CD = 'I'

def retrieve_by_state(db: Session, rndrng_prvdr_state_fips: int):
    return db.query(models.Service).filter(models.Service.rndrng_prvdr_state_fips == rndrng_prvdr_state_fips).all()

def retrieve_by_gender(db: Session):
    list_query = db.query(distinct(models.Service.rndrng_prvdr_gndr)).add_columns(func.count(models.Service.rndrng_prvdr_gndr)).filter(models.Service.rndrng_prvdr_ent_cd == END_CD).group_by(models.Service.rndrng_prvdr_gndr).all()
    result = []
    for item_query in list_query:
        item = {}
        item['gender'] = item_query[0]
        item['count'] = item_query[1]
        result.append(item)
    return result 

def retrieve_gender_by_country(db: Session):
    list_query = db.query(distinct(models.Service.rndrng_prvdr_cntry)).add_columns( models.Service.rndrng_prvdr_gndr, func.count(models.Service.rndrng_prvdr_gndr)).filter(models.Service.rndrng_prvdr_ent_cd == END_CD).group_by(models.Service.rndrng_prvdr_cntry, models.Service.rndrng_prvdr_gndr).all()
    result = []
    for item_query in list_query:
        item = {}
        item['country'] = item_query[0]
        item['gender'] = item_query[1]
        item['count'] = item_query[2]
        result.append(item)
    return result 

def retrieve_gender_by_country_state(db: Session, rndrng_prvdr_cntry: str):
    list_query = db.query(distinct(models.Service.rndrng_prvdr_cntry)).add_columns(models.Service.rndrng_prvdr_state_abrvtn, models.Service.rndrng_prvdr_gndr, func.count(models.Service.rndrng_prvdr_gndr)).filter(models.Service.rndrng_prvdr_ent_cd == END_CD, models.Service.rndrng_prvdr_cntry == rndrng_prvdr_cntry).group_by(models.Service.rndrng_prvdr_cntry, models.Service.rndrng_prvdr_state_abrvtn, models.Service.rndrng_prvdr_gndr).all()
    result = []
    for item_query in list_query:
        item = {}
        item['country'] = item_query[0]
        item['state'] = item_query[1]
        item['gender'] = item_query[2]
        item['count'] = item_query[3]
        result.append(item)
    return result 

def retrieve_gender_by_country_state_city(db: Session, rndrng_prvdr_cntry: str, rndrng_prvdr_state_abrvtn: str):
    list_query = db.query(distinct(models.Service.rndrng_prvdr_cntry)).add_columns(models.Service.rndrng_prvdr_state_abrvtn, models.Service.rndrng_prvdr_city, models.Service.rndrng_prvdr_gndr, func.count(models.Service.rndrng_prvdr_gndr)).filter(models.Service.rndrng_prvdr_ent_cd == END_CD, models.Service.rndrng_prvdr_cntry == rndrng_prvdr_cntry, models.Service.rndrng_prvdr_state_abrvtn == rndrng_prvdr_state_abrvtn).group_by(models.Service.rndrng_prvdr_cntry, models.Service.rndrng_prvdr_state_abrvtn, models.Service.rndrng_prvdr_city, models.Service.rndrng_prvdr_gndr).all()
    result = []
    for item_query in list_query:
        item = {}
        item['country'] = item_query[0]
        item['state'] = item_query[1]
        item['city'] = item_query[2]
        item['gender'] = item_query[3]
        item['count'] = item_query[4]
        result.append(item)
    return result 

def retrieve_gender_by_provider_type(db: Session):
    list_query = db.query(distinct(models.Service.rndrng_prvdr_type)).add_columns( models.Service.rndrng_prvdr_gndr, func.count(models.Service.rndrng_prvdr_gndr)).filter(models.Service.rndrng_prvdr_ent_cd == END_CD).group_by(models.Service.rndrng_prvdr_type, models.Service.rndrng_prvdr_gndr).all()
    result = []
    for item_query in list_query:
        item = {}
        item['provider_type'] = item_query[0]
        item['gender'] = item_query[1]
        item['count'] = item_query[2]
        result.append(item)
    return result 