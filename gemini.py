import google.generativeai as genai
import os
import time
from dotenv import load_dotenv

# Classe que fornecerá todos os dados, por meio da comunicação com a api do Gemini
class Gemini:

    # Estrutura do objeto dos dados que será retornado para serem renderizados
    def __init__(self, prompt:str="", modelo:str="models/gemini-1.5-pro-latest", temperatura:float=0.8, top_k:int=20, top_p:float=0.8):
        self.prompt = prompt
        self.modelo = modelo
        self.temperatura = temperatura
        self.top_k = top_k
        self.top_p = top_p

    # Retorna a instância conigurada com minha chave de API do Gemini
    def config_gemeni(self):
        load_dotenv()
        chave = os.getenv("API_KEY")
        if chave is None:
            raise Exception("Chave de API não encontrada")
        genai.configure(
            api_key = chave
        )

        return genai
    
    # Realiza a requisição na API do Gemini enviando os parâmentros captados na interface e retorna a resposta gerada e os
    # outros dados que serão gerados
    def geracao_resposta(self) -> tuple[str, int, int, int]: 
        model = self.config_gemeni()
        inicio = time.time()
        gemini = model.GenerativeModel(
            model_name=self.modelo,
            generation_config={
                "temperature": self.temperatura,
                "top_k": self.top_k,
                "top_p": self.top_p
            }
        )
        response = gemini.generate_content(self.prompt)
        tokens_pergunta = str(gemini.count_tokens(self.prompt))
        qtd_tokens_perguntas = int(tokens_pergunta.split(" ")[1])

        tokens_resposta = str(gemini.count_tokens(response.text))
        qtd_tokens_resposta = int(tokens_resposta.split(" ")[1])

        fim = time.time()
        tempo = fim - inicio

        return response.text, qtd_tokens_perguntas, qtd_tokens_resposta, tempo



