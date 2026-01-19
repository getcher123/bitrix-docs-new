import json

import httpx
import respx

from bitrix_rag.clients.bge import BgeClient
from bitrix_rag.config import BgeEndpointsConfig


@respx.mock
def test_bge_deepinfra_embed_payload():
    cfg = BgeEndpointsConfig(
        base_url="https://api.deepinfra.com/v1/inference",
        embed_path="/BAAI/bge-m3",
        rerank_path="/Qwen/Qwen3-Reranker-0.6B",
        api_key="secret",
    )
    route = respx.post("https://api.deepinfra.com/v1/inference/BAAI/bge-m3").mock(
        return_value=httpx.Response(200, json={"embeddings": [[0.1, 0.2]]})
    )

    client = BgeClient(cfg)
    embeddings = client.embed(["Hello"])

    assert embeddings == [[0.1, 0.2]]
    assert route.called
    request = route.calls[0].request
    assert request.headers.get("Authorization") == "bearer secret"
    payload = json.loads(request.content)
    assert payload["inputs"] == ["Hello"]


@respx.mock
def test_bge_deepinfra_rerank_payload():
    cfg = BgeEndpointsConfig(
        base_url="https://api.deepinfra.com/v1/inference",
        embed_path="/BAAI/bge-m3",
        rerank_path="/Qwen/Qwen3-Reranker-0.6B",
        api_key="secret",
    )
    route = respx.post(
        "https://api.deepinfra.com/v1/inference/Qwen/Qwen3-Reranker-0.6B"
    ).mock(return_value=httpx.Response(200, json={"scores": [0.5, 0.2]}))

    client = BgeClient(cfg)
    scores = client.rerank("Q?", ["A", "B"])

    assert scores == [0.5, 0.2]
    payload = json.loads(route.calls[0].request.content)
    assert payload["queries"] == ["Q?"]
    assert payload["documents"] == ["A", "B"]


@respx.mock
def test_bge_colab_headers_and_payload():
    cfg = BgeEndpointsConfig(
        base_url="https://example.ngrok-free.app",
        embed_path="/embed",
        rerank_path="/rerank",
        api_key="token",
    )
    embed_route = respx.post("https://example.ngrok-free.app/embed").mock(
        return_value=httpx.Response(200, json={"embeddings": [[0.4]]})
    )
    rerank_route = respx.post("https://example.ngrok-free.app/rerank").mock(
        return_value=httpx.Response(200, json={"scores": [1.0]})
    )

    client = BgeClient(cfg)
    assert client.embed(["Hi"]) == [[0.4]]
    assert client.rerank("Q", ["D"]) == [1.0]

    embed_payload = json.loads(embed_route.calls[0].request.content)
    assert embed_payload["texts"] == ["Hi"]
    assert embed_route.calls[0].request.headers.get("X-API-Key") == "token"

    rerank_payload = json.loads(rerank_route.calls[0].request.content)
    assert rerank_payload["query"] == "Q"
