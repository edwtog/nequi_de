[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

# nequi_de
## Datasets
Las fuentes de los datos se toman de [Kaggle Datasets](https://www.kaggle.com/datasets "Kaggle Datasets") y son ingestados con el uso de la [API](https://www.kaggle.com/docs/api "Kaggle API") pública expuesta por Kaggle mediante el script `src/load_data.py` .
1. [Credit risk analysis](https://www.kaggle.com/datasets/ranadeep/credit-risk-dataset "CreditRisk")  
   Caso de uso: Análisis de mora, PD, uso, reportes de estado de cartera y/o cosechas  
   Requerimiento: acceso a datos en zona de data procesada  
   Formato: CSV
2. [Electric Motor Temperature](https://www.kaggle.com/datasets/wkirgsn/electric-motor-temperature "ElectrinMotorTemperature")  
   Caso de uso: Análisis de series de tiempo, pronóstico de fallas  
   Requerimiento: acceso a datos en zona de data procesada  
   Formato: CSV
3. [CiteSum](https://www.kaggle.com/datasets/nbroad/cite-sum "CiteSum")  
   Caso de uso: NLP (generacion automatica de resumenes), análisis de publicaciones y journals  
   Requerimiento: acceso a datos en zona de data procesada con tablas relacionadas  
   Formato: json



![Alt text](img/diagram_01.jpg "Architecre Overview")


## Unittest

python -m unittest discover -v
