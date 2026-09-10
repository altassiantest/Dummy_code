import os
import requests

def list_published_usecases(base_url: str, token: str | None = None, timeout: int = 15):
    """
    Returns a list of dicts: [{id, name, description}, ...] for Published usecases.
    """
    base_url = (base_url or "").rstrip("/")
    usecase_base = f"{base_url}/aes"
    url = f"{usecase_base}/usecases"
    params = {
        "publish_status": "Published",
        "page_size": 1000,
        "page": 1,
    }
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    resp = requests.get(url, headers=headers, params=params, timeout=timeout)
    if resp.status_code in (401, 403):
        raise RuntimeError(
            "AUTH_EXPIRED: Your auth token has expired or is invalid. Re-authenticate and try again."
        )

    # Parse JSON (and surface errors clearly)
    try:
        data = resp.json()
    except Exception:
        resp.raise_for_status()
        raise RuntimeError(f"Usecase list response was not valid JSON: {resp.text[:500]}")

    if not resp.ok:
        raise RuntimeError(data.get("message") or f"Usecase list failed with {resp.status_code}.")

    if not data.get("status"):
        raise RuntimeError(data.get("message") or "Usecase list request failed.")

    items = data.get("data") or []
    # Map to a simple summary
    results = []
    for item in items:
        usecase_id = int(item.get("id") or 0)
        name = (item.get("name") or "").strip()
        if usecase_id > 0 and name:
            results.append(
                {
                    "id": usecase_id,
                    "name": name,
                    "description": (item.get("description") or "").strip() or None,
                }
            )
    # Sort by name for convenience
    results.sort(key=lambda x: x["name"])
    return results

if __name__ == "__main__":
    # Configure these:
    AIFORCE_BASE_URL = os.getenv("AIFORCE_BASE_URL", "https://example")  # e.g. https://your-host
    # Token can come from TOOL_API_KEY or USECASE_AUTH_TOKEN (mirrors the extension behavior)
    TOKEN = os.getenv("TOOL_API_KEY") or os.getenv("USECASE_AUTH_TOKEN")

    usecases = list_published_usecases(AIFORCE_BASE_URL, TOKEN)
    for u in usecases[:25]:
        print(f"{u['id']}: {u['name']}")
    if len(usecases) > 25:
        print(f"... and {len(usecases) - 25} more") 