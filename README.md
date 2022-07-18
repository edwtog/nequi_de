[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

# nequi_de
## 1. Datasets
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

## 2. Exploración datos

Se realiza una exploración sencilla sobre los datos transformados a **Pandas DataFrames** con el uso del script `utils/eda.py` con el fin de generar reporte con estadisticas basicas sobre cada tabla incluyen numero de faltantes y tipo da dato por columna. Los reporte se ubican en la carpeta `profiling_reports` para cada tabla generada y lista para ser llevada a la zona processed (Diagrama de arquitectura).

## 3. Modelo de datos

![Alt text](img/diagram_01.jpg "Architecre Overview")

## 4. 


### Pruebas unitarias

Se utiliza Unittest

`python -m unittest discover -v`


## 5. Consideraciones finales

1. Desarrollar las ingestiones de las fuentes de datos al data lake  
   * Conservando su formato original
   * Transformalas a un formato estandar
   * Almacenar con propósito de consulta ágil (Particionamiento y compresión)
2. 
3. Modelo elegido
   * Organizacion de las fuentes y conservación de los datos originales (Raw, processed)
   * Optimizar uso de recursos (Consultas)
   * Facilitar la conexión con otras herramientas del proveedor de servicios en la nube
4. Aspectoss de escalabilidad
   * Incremento 100X
      * Migrar a metodos de ingestion por streaming (AWS Kinesis Streams o Firhose, Kafka) [Alta frecuencia]
      * Ingestión a través de lambdas (frecuencia baja)
      * Uso de glue jobs [Alto tamaño]
   * Frecuencia de ejecucion
      * Configurar contrab para ejecucion de procesos
      * Utilizar un orquestador (para todo el flujo): Airflow, AWS step functions
   *
   



