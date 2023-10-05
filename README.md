<h1 align="center">
  Entity Recognition
</h1>
<p align="center">
Implementación de API en FastAPI para el reconocimiento de entidades nombradas en oraciones escritas en español
</p>

## 🛠 Instrucciones

1. Instalación de Dependencias y el modelo 'es_core_news_sm' para el idioma español

   ```
   pip install fastapi uvicorn spacy
   python -m spacy download es_core_news_sm
   ```

2. Para ejecutar la API, se puede usar uvicorn:

  ```
  uvicorn entity_recognition:app --reload
  ```
 Una vez ejecutado el comando de uvicorn, ya se pueden enviar solicitudes POST a http://127.0.0.1:8000/ner/ con un JSON que contenga oraciones escritas en español.

 Ejemplo de prueba:

 ```
{
  "oraciones": [
   "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
   "San Francisco considera prohibir los robots de entrega en la acera.",
   "Google ha inaugurado una nueva oficina en Madrid.",
   "El Amazonas es el río más largo del mundo.",
   "Barack Obama fue el 44º presidente de Estados Unidos.",
   "La Torre Eiffel es un símbolo icónico de París.",
   "El Real Madrid y el FC Barcelona son equipos de fútbol famosos.",
   "El Monte Everest es la montaña más alta de la Tierra."
  ]
}
```


3. Para probar la API manualmente, se accede a: http://127.0.0.1:8000/docs
   Aparecera esta seccion que corresponde a la peticion POST hacia la API:
![image](https://github.com/SleepWalKer09/Entity_recognition/assets/44912298/b9a34129-ac86-49ca-a25a-2a5d0974ba92)

  3.1. Clic en "try it out" y se desplegara una seccion donde se debera colocar el JSON que se requiera analizar, por ejemplo:
   ![image](https://github.com/SleepWalKer09/Entity_recognition/assets/44912298/c645f9f8-ff67-4a1a-8c21-832913a04a46)
 
   y clic en "Execute"

4. Respuesta de la API:
Con la API funcionando correctamente este sera el resultado:
![image](https://github.com/SleepWalKer09/Entity_recognition/assets/44912298/b5047a8a-8489-4db9-adf2-8dc86f61bbf6)

  En caso que exista algun error, la API se encarga de indicarlo.

   
