import json

import httpx
import respx

from bitrix_rag.clients.openai_client import OpenAIClient
from bitrix_rag.config import OpenAIConfig


@respx.mock
def test_openai_chat_completion():
    cfg = OpenAIConfig(
        api_key="test-key",
        model="gpt-4o-mini",
        base_url="https://api.openai.com/v1",
        max_output_tokens=123,
        timeout_s=5,
    )
    route = respx.post("https://api.openai.com/v1/chat/completions").mock(
        return_value=httpx.Response(
            200,
            json={
                "choices": [
                    {"message": {"content": "ok"}, "finish_reason": "stop"}
                ]
            },
        )
    )

    client = OpenAIClient(cfg)
    assert client.complete("hello") == "ok"

    assert route.called
    payload = json.loads(route.calls[0].request.content)
    assert payload["model"] == "gpt-4o-mini"
    assert payload["max_completion_tokens"] == 123


@respx.mock
def test_openai_responses_api():
    cfg = OpenAIConfig(
        api_key="test-key",
        model="gpt-5.2",
        base_url="https://api.openai.com/v1",
        max_output_tokens=321,
        timeout_s=5,
    )
    route = respx.post("https://api.openai.com/v1/responses").mock(
        return_value=httpx.Response(
            200,
            json={"output_text": "answer text"},
        )
    )

    client = OpenAIClient(cfg)
    assert client.complete("hello") == "answer text"

    assert route.called
    payload = json.loads(route.calls[0].request.content)
    assert payload["model"] == "gpt-5.2"
    assert payload["max_output_tokens"] == 321
