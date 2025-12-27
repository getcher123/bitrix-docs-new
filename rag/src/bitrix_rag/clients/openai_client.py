from __future__ import annotations

from dataclasses import dataclass

import httpx

from ..config import OpenAIConfig


@dataclass(frozen=True)
class OpenAIClient:
    cfg: OpenAIConfig

    def complete(self, prompt: str, timeout_s: int | None = None) -> str:
        url = "https://api.openai.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {self.cfg.api_key}"}
        payload = {
            "model": self.cfg.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
            "top_p": 0.9,
            "max_completion_tokens": 800,
        }
        with httpx.Client(timeout=timeout_s or self.cfg.timeout_s) as client:
            resp = client.post(url, headers=headers, json=payload)
            if resp.status_code >= 400:
                detail = resp.text[:800]
                raise RuntimeError(f"OpenAI API error {resp.status_code}: {detail}")
            data = resp.json()
        return data["choices"][0]["message"]["content"].strip()
