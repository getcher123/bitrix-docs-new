from __future__ import annotations

from dataclasses import dataclass

import httpx

from ..config import OpenAIConfig


@dataclass(frozen=True)
class OpenAIClient:
    cfg: OpenAIConfig

    def complete(self, prompt: str, timeout_s: int | None = None) -> str:
        if _use_responses_api(self.cfg.model):
            return _complete_responses(self.cfg, prompt, timeout_s)
        return _complete_chat(self.cfg, prompt, timeout_s)


def _supports_sampling_params(model: str) -> bool:
    return not model.startswith("gpt-5")


def _use_responses_api(model: str) -> bool:
    return model.startswith("gpt-5")


def _complete_chat(cfg: OpenAIConfig, prompt: str, timeout_s: int | None = None) -> str:
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {cfg.api_key}"}
    payload = {
        "model": cfg.model,
        "messages": [{"role": "user", "content": prompt}],
        "max_completion_tokens": cfg.max_output_tokens,
    }
    if _supports_sampling_params(cfg.model):
        payload["temperature"] = 0.2
        payload["top_p"] = 0.9
    with httpx.Client(timeout=timeout_s or cfg.timeout_s) as client:
        resp = client.post(url, headers=headers, json=payload)
        if resp.status_code >= 400:
            detail = resp.text[:800]
            raise RuntimeError(f"OpenAI API error {resp.status_code}: {detail}")
        data = resp.json()
    choice = (data.get("choices") or [{}])[0]
    finish_reason = choice.get("finish_reason")
    message = choice.get("message") or {}
    content = message.get("content")
    content_text = (content or "").strip() if isinstance(content, str) else ""
    if not content_text:
        usage = data.get("usage") or {}
        prompt_tokens = usage.get("prompt_tokens")
        completion_tokens = usage.get("completion_tokens")
        model = data.get("model", cfg.model)
        print(
            "OpenAI empty content",
            f"model={model}",
            f"finish_reason={finish_reason}",
            f"prompt_tokens={prompt_tokens}",
            f"completion_tokens={completion_tokens}",
            f"content_type={type(content).__name__}",
        )
        return ""
    return content_text


def _complete_responses(cfg: OpenAIConfig, prompt: str, timeout_s: int | None = None) -> str:
    url = "https://api.openai.com/v1/responses"
    headers = {"Authorization": f"Bearer {cfg.api_key}"}
    payload = {
        "model": cfg.model,
        "input": prompt,
        "max_output_tokens": cfg.max_output_tokens,
    }
    with httpx.Client(timeout=timeout_s or cfg.timeout_s) as client:
        resp = client.post(url, headers=headers, json=payload)
        if resp.status_code >= 400:
            detail = resp.text[:800]
            raise RuntimeError(f"OpenAI API error {resp.status_code}: {detail}")
        data = resp.json()
    text = _extract_responses_text(data)
    if text:
        return text
    usage = data.get("usage") or {}
    prompt_tokens = usage.get("input_tokens")
    completion_tokens = usage.get("output_tokens")
    model = data.get("model", cfg.model)
    print(
        "OpenAI empty content",
        f"model={model}",
        "endpoint=responses",
        f"prompt_tokens={prompt_tokens}",
        f"completion_tokens={completion_tokens}",
    )
    return ""


def _extract_responses_text(data: dict) -> str:
    output_text = data.get("output_text")
    if isinstance(output_text, str) and output_text.strip():
        return output_text.strip()
    output = data.get("output") or []
    parts: list[str] = []
    for item in output:
        content = item.get("content") if isinstance(item, dict) else None
        if not content:
            continue
        for block in content:
            if isinstance(block, dict):
                if block.get("type") in {"output_text", "text"} and isinstance(block.get("text"), str):
                    parts.append(block["text"])
            elif isinstance(block, str):
                parts.append(block)
    return "\n".join(part.strip() for part in parts if part and part.strip()).strip()
