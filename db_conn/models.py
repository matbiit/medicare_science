from sqlalchemy import Column, Float, Integer, Sequence, String

from .database import Base

TABLE_ID = Sequence('table_id_seq', start=1)

class Service(Base):
    __tablename__ = "service"

    id = Column(Integer, TABLE_ID, primary_key=True, server_default=TABLE_ID.next_value())
    rndrng_npi= Column(Integer)
    rndrng_prvdr_last_org_name= Column(String)
    rndrng_prvdr_first_name= Column(String)
    rndrng_prvdr_mi= Column(String)
    rndrng_prvdr_crdntls= Column(String) 
    rndrng_prvdr_gndr= Column(String)
    rndrng_prvdr_ent_cd= Column(String) 
    rndrng_prvdr_st1= Column(String) 
    rndrng_prvdr_st2= Column(String) 
    rndrng_prvdr_city= Column(String) 
    rndrng_prvdr_state_abrvtn= Column(String) 
    rndrng_prvdr_state_fips= Column(Float) 
    rndrng_prvdr_zip5= Column(String) 
    rndrng_prvdr_ruca= Column(Float) 
    rndrng_prvdr_ruca_desc= Column(String) 
    rndrng_prvdr_cntry= Column(String)
    rndrng_prvdr_type= Column(String) 
    rndrng_prvdr_mdcr_prtcptg_ind= Column(String) 
    hcpcs_cd= Column(String)
    hcpcs_desc= Column(String) 
    hcpcs_drug_ind= Column(String) 
    place_of_srvc= Column(String) 
    tot_benes= Column(Integer)
    tot_srvcs= Column(Float)
    tot_bene_day_srvcs= Column(Float) 
    avg_sbmtd_chrg= Column(Float) 
    avg_mdcr_alowd_amt= Column(Float) 
    avg_mdcr_pymt_aamt= Column(Float) 
    avg_mdcr_stdzd_amt= Column(Float)
