import base64
import os
import aiofiles
import httpx
from fastapi import APIRouter, Response
from models import ImageBody

ai_image_router = APIRouter(tags=['AI-Images'])

@ai_image_router.post('/ai-image', status_code=201)
async def create_ai_image(response: Response, image_body: ImageBody):
    try:
        # Haetaan API avain .env tiedostosta. ks. Ympäristömuuttujat kohta.
        api_key = os.environ.get("API_KEY")

        # Request headerit
        headers: httpx.Headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

        # Request body
        payload = {
            "prompt": image_body.prompt,
            "n": image_body.n,
            "size": image_body.size
        }

        # Avataan asynkroninen httpx client, tämä mahdollistaa sen että ToDo API
        # voi suorittaa muuta koodia tai muita kyselyitä sillä välin kun vastausta odotellaan toisesta rajapinnasta.
        async with httpx.AsyncClient() as client:
            # POST Requestin tekeminen openai:n rajapintaan
            res = await client.post("https://api.openai.com/v1/images/generations", headers=headers, json=payload)

            if res.status_code != 200:
                response.status_code = res.status_code
                return {"err": "Error fetching image urls from openai API"}

            # JSON muotoisen datan parsiminen
            parsed_response = res.json()

            # Haetaan vastauksena saadun kuvan osoitteen perusteella itse kuva
            image_response = await client.get(parsed_response['data'][0]['url'])

            # Tallennetaan kuva tiedostojärjestelmään myös asynkronisesti käyttämällä id:tä osana kuvan nimeä
            async with aiofiles.open(f"image.png", "wb") as f:
                await f.write(image_response.content)

            # Muutetaan kuva BASE64 koodatuksi merkkijonoksi
            image_data_base64 = base64.b64encode(image_response.content).decode("utf-8")

            # Luodaan data_url jossa base64 merkkijonolle asetetaan sen MIME tyyppi.
            # Tämä mahdollistaa sen että data_url voidaan clientilla laittaa suoraan kuvana
            # esim. html img tägiin src:ksi
            image_url = f"data:image/png;base64,{image_data_base64}"

            # Palautetaan clientille JSON muotoinen vastaus joka sisältää BASE64 muotoisen data_url:n
            return {"data_url": image_url}
    except Exception as e:
        response.status_code = 500
        return {"err": str(e)}


@ai_image_router.get("/ai-image/")
async def get_ai_image(response: Response, id: int):
    try:
        # Luetaan kuva tiedostojärjestelmästä id:n perusteella asynkronisesti
        # hyödyntämällä aiofiles kirjastoa.
        async with aiofiles.open(f"image.png", "rb") as f:
            # Kuva luetaan binääridatana muuttujaan image_data
            image_data = await f.read()
            # Muutetaan binääridata BASE64 koodattuun muotoon
            image_data_base64 = base64.b64encode(image_data).decode("utf-8")

            # Luodaan data_url jossa base64 merkkijonolle asetetaan sen MIME tyyppi.
            # Tämä mahdollistaa sen että data_url voidaan clientilla laittaa suoraan kuvana
            # esim. html img tägiin src:ksi
            image_url = f"data:image/png;base64,{image_data_base64}"

            # Palautetaan clientille JSON muotoinen vastaus
            return {"data_url": image_url}

    except Exception as e:
        # Jos tiedostoa ei löydy annetulla id:llä, palautetaan statuskoodi 404
        response.status_code = 404
        return {"err": str(e)}
    
@ai_image_router.delete("/ai-image/")
def remove_ai_image(response: Response,id: int):
    try:
        # Käytetään os kirjaston remove metodia tiedoston poistamisessa 
        os.remove(f"image.png")

        # Voidaan palauttaa esim. seuraavanlainen viesti kun poisto onnistuu
        return {"msg": "AI generated image deleted successfully"}
    except Exception as e:
        response.status_code = 404
        return {"err": str(e)}