# Prompt Optimizer

Una app web para transformar cualquier prompt en uno más poderoso y preciso usando GPT-4.

## Cómo usar

1. Ingresá tu nombre, email y el prompt original.
2. La app lo optimiza usando OpenAI y te devuelve una mejor versión.

## Despliegue

Para correr localmente:

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=tu_clave
python app.py
```

Para producción, usar gunicorn:

```bash
gunicorn app:app
```