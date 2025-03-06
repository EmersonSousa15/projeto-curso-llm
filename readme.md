
---

# Projeto final curso AI Generativa

Este é o projeto final da aplicação de um curso de AI Generativa, que permite interagir com a **API Gemini** para gerar respostas de linguagem natural com base em um prompt fornecido pelo usuário. O usuário pode configurar parâmetros como o modelo, temperatura, top_k e top_p para controlar a geração do texto.

## Funcionalidades

- **Configuração do Modelo e Parâmetros**: O usuário pode escolher o modelo e ajustar parâmetros como temperatura, top_k e top_p para personalizar o comportamento da resposta.
- **Entrada de Prompt**: O usuário pode inserir um texto (prompt) para gerar uma resposta.
- **Exibição de Métricas**: Após gerar a resposta, o site exibe métricas como o número de tokens usados para a pergunta e para a resposta, bem como o tempo total para gerar a resposta.
- **Resposta Gerada**: A resposta gerada pela API Gemini será exibida.

## Tecnologias Utilizadas

- **Streamlit**: Para a criação da interface de usuário.
- **Gemini (Google Generative AI)**: API de linguagem natural utilizada para gerar as respostas.
- **Dotenv**: Para gerenciar a chave de API do Gemini de forma segura.
- **Python**: Linguagem de programação utilizada para a implementação do back-end da aplicação.

## Pré-requisitos
Antes de executar este projeto, você precisará ter o seguinte instalado:

- Python
- Streamlit
- Biblioteca `gemini` (para integração com a API Gemini)
- Biblioteca `google-generativeai` (para integração com o Gemini)
- Biblioteca `dotenv` (para carregar variáveis de ambiente de forma segura)

## Instalação

1. Clone este repositório para o seu ambiente local:

   ```bash
   git clone https://github.com/EmersonSousa15/projeto-curso-llm.git
   ```

2. Navegue até a pasta do projeto:

   ```bash
   cd projeto-curso-llm
   ```

3. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/MacOS
   venv\Scripts\activate     # Para Windows
   ```

4. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

   O arquivo `requirements.txt` deve conter as seguintes dependências:

   ```
   streamlit
   gemini
   google-generativeai
   python-dotenv
   ```

5. Adicione a sua chave da API do Gemini em um arquivo `.env` na raiz do projeto:

   ```
   API_KEY=your_gemini_api_key
   ```

6. Execute o aplicativo Streamlit:

   ```bash
   streamlit run app.py
   ```

7. O aplicativo estará acessível em `http://localhost:8501`.

## Como Usar

1. **Configuração do Modelo**: Na barra lateral, selecione o modelo que deseja utilizar entre as opções disponíveis, como `models/gemini-1.5-pro-latest` ou `lm-studio`.
   
2. **Ajuste dos Parâmetros**:
   - **Temperatura**: Controle a criatividade da resposta gerada.
   - **Top K**: Limita a quantidade de tokens (palavras) a serem considerados durante a geração da resposta.
   - **Top P**: Controla a probabilidade cumulativa dos tokens a serem escolhidos para a próxima palavra.

3. **Entrada de Prompt**: Insira um prompt (texto) na caixa de texto para a geração da resposta.

4. **Gerar Resposta**: Após preencher o prompt e configurar os parâmetros, clique no botão "Gerar resposta" para obter a resposta gerada pelo modelo.

5. **Visualização dos Resultados**:
   - **Tokens de Pergunta**: O número de tokens utilizados no seu prompt.
   - **Tokens de Resposta**: O número de tokens utilizados na resposta gerada.
   - **Tempo de Resposta**: O tempo total de execução para gerar a resposta.

6. **Resposta Gerada**: A resposta gerada será exibida abaixo das métricas. Você pode visualizar o código da resposta gerada.

## Estrutura do Código

### `app.py`

Este é o arquivo principal onde a interface de usuário é configurada usando Streamlit. Ele contém os seguintes blocos principais:

- **Sidebar**: A sidebar permite que o usuário selecione o modelo e ajuste os parâmetros como temperatura, top_k e top_p.
- **Entrada de Prompt**: Campo de texto para o usuário digitar o prompt.
- **Botão de Geração**: Um botão para disparar a geração da resposta.
- **Exibição de Resultados**: Após a resposta ser gerada, o app exibe a resposta e as métricas (tokens e tempo).

### `gemini.py`

Este arquivo contém a classe `Gemini`, que é responsável por interagir com a API Gemini para gerar a resposta. A classe possui dois métodos principais:

- **`config_gemini`**: Configura a chave da API e inicializa a conexão com a API Gemini.
- **`geracao_resposta`**: Envia o prompt para a API Gemini, processa a resposta e retorna a resposta gerada junto com as métricas de tokens e tempo.

---