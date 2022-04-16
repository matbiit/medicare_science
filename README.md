# Medicare - Science

This project has as its main objective to analyze the gender distribution of providers in the Medicare system to determine whether incentive policies for better parity can be carried out.

### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Python ^3.9](https://www.python.org/downloads/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [PostgreSQL Docker Image](https://hub.docker.com/_/postgres?tab=description)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Anaconda - Jupyter Notebook](https://www.anaconda.com/products/distribution)
* [GeoPandas](https://geopandas.org/en/stable/getting_started/install.html)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Download [Public Dataset from Centers for Medicare and Medicaid Services, CMS](https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider-and-service) and put the file in the root folder with the name:
```sh
  medicare.csv
```
The data in the file only have information for Medicare beneficiaries with Part B FFS coverage 

* Start the Docker Image of PostgreSQL. Example:
```sh
docker run --name postgres-db -e POSTGRES_PASSWORD=your_password -p 5432:5432 -d postgres
```

* Change the database url inside the file db_conn/database.py
```sh
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
```

* Install Python3, pip3, Ananconda and GeoPandas

### Installation

Once with all prerequisites done, you need install the dependencies:
```sh
pip3 install -r requirements.txt
```
Run the server with:
```sh
uvicorn main:app --reload
```
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

Now go to http://127.0.0.1:8000/docs to verify all the routes.
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Matheus Bitencourt - [@matbiit](https://www.linkedin.com/in/matbiit/)

Project Link: [https://github.com/matbiit/medicare_science](https://github.com/matbiit/medicare_science)

<p align="right">(<a href="#top">back to top</a>)</p>


