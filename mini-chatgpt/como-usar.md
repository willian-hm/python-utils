# Como usar o Mini GPT

## 1. Clone o repositório

```bash
git clone https://github.com/willian-hm/python-utils.git
```

---

## 2. Entre na pasta do projeto

```bash
cd python-utils/mini-gpt
```

---

## 3. Instale as bibliotecas Python

```bash
pip install flask ollama
```

---

## 4. Instale o Ollama

Baixe e instale o Ollama no site oficial:

* Windows / Linux / Mac:
  https://ollama.com

Depois de instalar, verifique se ele funciona:

```bash
ollama
```

---

## 5. Baixe o modelo llama3

```bash
ollama pull llama3
```

Isso pode demorar um pouco dependendo da internet e do hardware.

---

## 6. Rode o projeto

```bash
python app.py
```

---

## 7. Abra no navegador

Acesse:

```text
http://localhost:5000
```

---

## Como funciona?

O projeto usa:

* Flask → backend/web server
* HTML/CSS/JS → interface
* Ollama → roda IA localmente
* Llama3 → modelo de linguagem

Fluxo:

```text
Usuário → JS → Flask → Ollama/Llama3 → Flask → Navegador
```

---

## Requisitos

* Python 3 instalado
* Ollama instalado
* Modelo llama3 baixado

---

## Observações

Se der erro relacionado ao Ollama:

* confira se o Ollama está instalado
* confira se o modelo llama3 foi baixado
* tente rodar:

```bash
ollama run llama3
```

para verificar se o modelo está funcionando corretamente.
