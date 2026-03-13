from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(title="霸王大陆2 配置查询器 API", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/items/search")
def search_items(q: str) -> dict[str, object]:
    return {
        "query": q,
        "status": "stub",
        "message": "待接入 SQLite 与聚合查询逻辑。",
        "results": [],
    }
