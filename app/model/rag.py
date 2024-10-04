"""Arquivo `app/model/rag.py` no repositório. Modulo com a pipeline RAG. """

import os

import chromadb
import openai
from openai.types.chat.chat_completion import ChatCompletion

CONTEXT_PATH = os.path.join(os.path.dirname(__file__), "context")


class RagPipeline:
    """Pipeline RAG.

    O método principal é o `answer`, que responde à pergunta do usuário com
    o LLM.
    """

    def __init__(self):
        self.openai_client = openai.OpenAI()
        chroma_client = chromadb.PersistentClient(path=CONTEXT_PATH)
        self.collection = chroma_client.get_collection(name="context")

    def answer(self, question: str, stream: bool = False) -> ChatCompletion:
        """Método principal.

        Implementa cada uma das etapas do RAG.
        """
        context = self.retrieve_context(question)
        prompt = self.prepare_prompt(question, context)
        answer = self.generate_answer(prompt, stream)
        return answer

    def retrieve_context(self, question: str) -> str:
        """Retriever de contexto.

        Dada uma pergunta (`question`), retorna o contexto mais similar
        do banco de vetores.
        """
        return self.collection.query(query_texts=[question], n_results=1)["documents"][
            0
        ]

    def prepare_prompt(self, question: str, context: str) -> str:
        """Combina a pergunta do usuário com o contexto recuperado,
        preenchendo o template de prompt.
        """
        prompt = f"""
        Você é um assistente que responde perguntas sobre o iafluente,
        um site educativo com tutoriais sobre inteligência artificial (IA).

        Você deve responder à pergunta do usuário utilizando apenas o contexto
        fornecido. Caso o contexto não seja relevante para responder à pergunta,
        responda com "O iafluente não tem a resposta para essa pergunta.".

        Pergunta:
        {question}

        Contexto:
        {context}
        """
        return prompt

    def generate_answer(self, prompt: str, stream: bool) -> ChatCompletion:
        """Envia a instrução ao LLM e retorna a resposta."""
        response = self.openai_client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="gpt-4o",
            stream=stream,
        )
        return response
