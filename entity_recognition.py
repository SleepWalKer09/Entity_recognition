from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List
import spacy

#carga el modelo solicitado ('es_core_news_sm)
nlp = spacy.load("es_core_news_sm")

app=FastAPI()

#define el modelo de entrada de datos que la API espera recibir
class InputData(BaseModel):
    oraciones: List[str]

#define el modelo de la respuesta de la API (oracion y entidades)
class ResponseData(BaseModel):
    oracion: str
    entidades: dict

#define el modelo completo de la respuesta de la API 
class NERResponse(BaseModel):
    resultado: List[ResponseData]

#endopoint para el reconomiento de entidades
@app.post("/ner", response_model=NERResponse, summary="Reconocimiento de Entidades Nombradas", description="Este endpoint identifica y devuelve las entidades nombradas presentes en las oraciones proporcionadas.")
async def recognize_entities(data: InputData):

    """
    Dado un conjunto de oraciones en español, identifica y devuelve las entidades nombradas en cada oracion.

    """

    sentences = data.oraciones
    results= []

    for sentence in sentences:
        doc = nlp(sentence)
        #toma las entidades reconocidas de la oracion y las convierte en un diccionario de palabrras y sus categorias
        #label_ = en spacy, devolvera la etqiqueta en formato string
        entities = {ent.text: ent.label_ for ent in doc.ents}

        results.append({
            "oracion": sentence,
            "entidades": entities
        })

    return{"resultado":results}
    