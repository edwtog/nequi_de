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
2. Necesidad de los datos  
   Las preguntas surgen del entendimiento del caso de uso y las conversaciones con el usuario que adelanta generalmente un científico de datos. A partir de estas se generan requeriminetos asociados a los datos. Requerimeintos que el equipo de ingeniería de datos atenderá haciendo uso de los mecanismos de ingesta, estandarizacion y disponibiliación de datos disponibles.    
   Es importante considerar el propósito de uso de los datos para generar valor al negocio y que no esten relacionados exclusivamente con la opreación y que será abordado por alguna técnica de ciencia de datos:
      * Business intelligence - BI: Métricas, indicadores, KPI
      * Business analytics - BA: Entendimineto del cliente, interacción y comportamineto con la App, CLTV, segmentos, analítica digital
      * Advanced analytics - AA: Exploración de datos crudos, integracion de multiples fuentes, desarrollo de bases para entrenamiento de modelos

3. Modelo elegido
   * Tablas relacionales (para llevar a una BD)
   * Organizacion de las fuentes y conservación de los datos originales (Raw, processed)
   * Optimizar uso de recursos (particionamineto, compresion -> Consultas)
   * Facilitar la conexión con otras herramientas del proveedor de servicios en la nube

4. Aspectos de escalabilidad
   * Incremento 100X
      * Migrar a metodos de ingestion por streaming (AWS Kinesis Streams o Firhose, Kafka) [Alta frecuencia]
      * Ingestión a través de lambdas [Baja frecuencia]
      * Uso de glue jobs [Alto tamaño]
      * Consultas a través de RedShift [Gran volumen]
   * Frecuencia de ejecución ingestiones
      * Configurar contrab para ejecución de procesos
      * Utilizar un orquestador (para todo el flujo): Airflow, AWS step functions
   * Volumen número de consultas
      *
   



