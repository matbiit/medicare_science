from fastapi import Depends, FastAPI, HTTPException
from typing import List
import pandas as pd
from sqlalchemy.orm import Session

from db_conn import crud, models, schemas
from db_conn.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/load")
async def load():
    # Create an iterable that will read "chunksize=100000" rows
    # at a time from the CSV file
    for df in pd.read_csv("medicare.csv",chunksize=100000,encoding='ISO-8859-1'):
        df.rename(columns = {'Rndrng_NPI': 'rndrng_npi', 'Rndrng_Prvdr_Last_Org_Name': 'rndrng_prvdr_last_org_name', 'Rndrng_Prvdr_First_Name': 'rndrng_prvdr_first_name', 'Rndrng_Prvdr_MI': 'rndrng_prvdr_mi', 'Rndrng_Prvdr_Crdntls': 'rndrng_prvdr_crdntls', 'Rndrng_Prvdr_Gndr': 'rndrng_prvdr_gndr', 'Rndrng_Prvdr_Ent_Cd': 'rndrng_prvdr_ent_cd', 'Rndrng_Prvdr_St1': 'rndrng_prvdr_st1', 'Rndrng_Prvdr_St2': 'rndrng_prvdr_st2', 'Rndrng_Prvdr_City': 'rndrng_prvdr_city', 'Rndrng_Prvdr_State_Abrvtn': 'rndrng_prvdr_state_abrvtn', 'Rndrng_Prvdr_State_FIPS': 'rndrng_prvdr_state_fips', 'Rndrng_Prvdr_Zip5': 'rndrng_prvdr_zip5', 'Rndrng_Prvdr_RUCA': 'rndrng_prvdr_ruca', 'Rndrng_Prvdr_RUCA_Desc': 'rndrng_prvdr_ruca_desc', 'Rndrng_Prvdr_Cntry': 'rndrng_prvdr_cntry', 'Rndrng_Prvdr_Type': 'rndrng_prvdr_type', 'Rndrng_Prvdr_Mdcr_Prtcptg_Ind': 'rndrng_prvdr_mdcr_prtcptg_ind', 'HCPCS_Cd': 'hcpcs_cd', 'HCPCS_Desc': 'hcpcs_desc', 'HCPCS_Drug_Ind': 'hcpcs_drug_ind', 'Place_Of_Srvc': 'place_of_srvc', 'Tot_Benes': 'tot_benes', 'Tot_Srvcs': 'tot_srvcs', 'Tot_Bene_Day_Srvcs': 'tot_bene_day_srvcs', 'Avg_Sbmtd_Chrg': 'avg_sbmtd_chrg', 'Avg_Mdcr_Alowd_Amt': 'avg_mdcr_alowd_amt', 'Avg_Mdcr_Pymt_Amt': 'avg_mdcr_pymt_aamt', 'Avg_Mdcr_Stdzd_Amt': 'avg_mdcr_stdzd_amt'}, inplace = True)
        df.to_sql(
            'service', 
            engine,
            index=False,
            if_exists='append' # if the table already exists, append this data
        )
    return {"message": "Load complete"}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/gender", response_model=List[schemas.ServiceByGender])
def retrieve_by_gender(db: Session = Depends(get_db)):
    db_services = crud.retrieve_by_gender(db)
    if db_services is None:
        raise HTTPException(status_code=404, detail="Error while retrieving data - by gender")
    return db_services

@app.get("/gender/country", response_model=List[schemas.ServiceGenderByCountry])
def retrieve_gender_by_country(db: Session = Depends(get_db)):
    db_services = crud.retrieve_gender_by_country(db)
    if db_services is None:
        raise HTTPException(status_code=404, detail="Error while retrieving gender data - by country")
    return db_services

@app.get("/gender/country/{country}/state", response_model=List[schemas.ServiceGenderByCountryState])
def retrieve_gender_by_country_state(country: str, db: Session = Depends(get_db)):
    db_services = crud.retrieve_gender_by_country_state(db, rndrng_prvdr_cntry=country.upper())
    if db_services is None:
        raise HTTPException(status_code=404, detail="Error while retrieving gender data - by country and state")
    return db_services

@app.get("/gender/country/{country}/state/{state}/city", response_model=List[schemas.ServiceGenderByCountryStateCity])
def retrieve_gender_by_country_state_city(country: str, state: str, db: Session = Depends(get_db)):
    db_services = crud.retrieve_gender_by_country_state_city(db, rndrng_prvdr_cntry=country.upper(), rndrng_prvdr_state_abrvtn=state.upper())
    if db_services is None:
        raise HTTPException(status_code=404, detail="Error while retrieving gender data - by country, state and city")
    return db_services


@app.get("/gender/provtype", response_model=List[schemas.ServiceGenderByProviderType])
def retrieve_gender_by_provider_type(db: Session = Depends(get_db)):
    db_services = crud.retrieve_gender_by_provider_type(db)
    if db_services is None:
        raise HTTPException(status_code=404, detail="Error while retrieving gender data - by provider")
    return db_services