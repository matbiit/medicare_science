from pydantic import BaseModel
from typing import Optional

class Service(BaseModel):
    id: int
    rndrng_npi: int
    rndrng_prvdr_last_org_name: Optional[str]
    rndrng_prvdr_first_name: Optional[str]
    rndrng_prvdr_mi: Optional[str]
    rndrng_prvdr_crdntls: Optional[str] 
    rndrng_prvdr_gndr: Optional[str]
    rndrng_prvdr_ent_cd: Optional[str] 
    rndrng_prvdr_st1: Optional[str] 
    rndrng_prvdr_st2: Optional[Optional[str]]
    rndrng_prvdr_city: Optional[str] 
    rndrng_prvdr_state_abrvtn: Optional[str] 
    rndrng_prvdr_state_fips: float 
    rndrng_prvdr_zip5: Optional[str] 
    rndrng_prvdr_ruca: float 
    rndrng_prvdr_ruca_desc: Optional[str] 
    rndrng_prvdr_cntry: Optional[str]
    rndrng_prvdr_type: Optional[str] 
    rndrng_prvdr_mdcr_prtcptg_ind: Optional[str] 
    hcpcs_cd: Optional[str]
    hcpcs_desc: Optional[str] 
    hcpcs_drug_ind: Optional[str] 
    place_of_srvc: Optional[str] 
    tot_benes: int
    tot_srvcs: float
    tot_bene_day_srvcs: float 
    avg_sbmtd_chrg: float 
    avg_mdcr_alowd_amt: float 
    avg_mdcr_pymt_aamt: float 
    avg_mdcr_stdzd_amt: float
    class Config:
        orm_mode = True

class ServiceByGender(BaseModel):
    gender: Optional[str]
    count: int

class ServiceGenderByCountry(ServiceByGender):
    country: Optional[str]

class ServiceGenderByCountryState(ServiceGenderByCountry):
    state: Optional[str]

class ServiceGenderByCountryStateCity(ServiceGenderByCountryState):
    city: Optional[str]

class ServiceGenderByProviderType(ServiceByGender):
    provider_type: Optional[str]