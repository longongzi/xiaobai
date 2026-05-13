#!/usr/bin/env python3
"""
小白 — 零成本终端 AI 助手
有问题？找小白。

Usage:
    pip install xiaobai
    小白 帮我写个Python爬虫
    小白 今天天气怎么样？
    小白 --voice   # 语音模式
"""

import json
import sys
import os
import platform
from datetime import datetime

__version__ = "0.1.0"

# ── 配置 ──────────────────────────────────────────────
CONFIG_PATH = os.path.expanduser("~/.xiaobai_config.json")

DEFAULT_CONFIG = {
    "api_url": "http://localhost:8081/v1/chat/completions",
    "model": "deepseek-chat",
    "temperature": 0.7,
    "enable_voice": False,
    "system_prompt": "你叫小白，是一个友好的AI助手。回答简洁、实用、亲切。",
}

# ── 配置管理 ───────────────────────────────────────────

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            cfg = json.load(f)
            return {**DEFAULT_CONFIG, **cfg}
    return dict(DEFAULT_CONFIG)

def save_config(cfg):
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)

def show_config():
    cfg = load_config()
    print("小白配置：")
    for k, v in cfg.items():
        print(f"  {k}: {v}")

def set_config(key, value):
    cfg = load_config()
    cfg[key] = value
    save_config(cfg)
    print(f"✓ 已设置 {key} = {value}")


# ── API 调用 ───────────────────────────────────────────

def chat(prompt, cfg=None):
    if cfg is None:
        cfg = load_config()

    messages = [
        {"role": "system", "content": cfg["system_prompt"]},
        {"role": "user", "content": prompt},
    ]

    body = json.dumps({
        "model": cfg["model"],
        "messages": messages,
        "temperature": cfg["temperature"],
        "stream": True,
    }, ensure_ascii=False)

    try:
        import urllib.request

        req = urllib.request.Request(
            cfg["api_url"],
            data=body.encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "User-Agent": f"xiaobai/{__version__}",
            },
            method="POST",
        )

        resp = urllib.request.urlopen(req, timeout=60)
        content_type = resp.headers.get("Content-Type", "")

        # ── SSE 流式响应 ──
        if "text/event-stream" in content_type or "text/plain" in content_type:
            result = ""
            buffer = b""
            while True:
                chunk = resp.read(1)
                if not chunk:
                    break
                buffer += chunk
                if b"\n" in buffer:
                    lines = buffer.split(b"\n")
                    buffer = lines.pop()
                    for line in lines:
                        line = line.decode("utf-8", errors="replace").strip()
                        if not line or line.startswith(":"):
                            continue
                        if line.startswith("data: "):
                            data_str = line[6:]
                            if data_str == "[DONE]":
                                break
                            try:
                                data = json.loads(data_str)
                                delta = (
                                    data.get("choices", [{}])[0]
                                    .get("delta", {})
                                    .get("content", "")
                                )
                                result += delta
                                print(delta, end="", flush=True)
                            except json.JSONDecodeError:
                                pass
                    if data_str == "[DONE]":
                        break
            print()
            return result

        # ── JSON 响应 ──
        result_text = resp.read().decode("utf-8")
        data = json.loads(result_text)
        content = (
            data.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "")
        )
        print(content)
        return content

    except urllib.error.URLError as e:
        print(f"\n✗ 连不上小白了… 检查一下 API 地址对不对？")
        print(f"  错误: {e.reason}")
        print(f"  当前 API: {cfg['api_url']}")
        print(f"  提示: xiaobai config set api_url <你的地址>")
        return None
    except Exception as e:
        print(f"\n✗ 出错了: {e}")
        return None


# ── 语音模式（预览版） ─────────────────────────────────

def voice_mode():
    """语音对话模式 — 使用系统 TTS + 录音"""
    cfg = load_config()

    # Windows TTS
    if platform.system() == "Windows":
        try:
            import win32com.client
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
        except ImportError:
            speaker = None
            print("提示: pip install pywin32 开启语音朗读")
    else:
        speaker = None
        print("语音模式暂不支持当前系统")

    print("小白语音模式（按 Ctrl+C 退出）")
    print("-" * 30)

    try:
        while True:
            text = input("\n你说: ").strip()
            if not text:
                continue
            if text.lower() in ("exit", "quit", "退出"):
                break

            result = chat(text, cfg)
            if result and speaker:
                speaker.Speak(result)
    except KeyboardInterrupt:
        print("\n拜拜~")


# ── 主入口 ─────────────────────────────────────────────

def main():
    args = sys.argv[1:]

    if not args:
        print("小白 — 零成本终端 AI 助手 v" + __version__)
        print()
        print("用法:")
        print("  小白 <你的问题>      直接问")
        print("  小白 --voice         语音对话模式")
        print("  小白 config          查看配置")
        print("  小白 config set <k> <v>  修改配置")
        print("  小白 --version       查看版本")
        print()
        print("例子:")
        print("  小白 帮我写一个Python爬虫")
        print("  小白 今天深圳天气怎么样？")
        return

    if args[0] in ("--version", "-v"):
        print(f"小白 v{__version__}")
        return

    if args[0] == "config":
        if len(args) >= 4 and args[1] == "set":
            set_config(args[2], " ".join(args[3:]))
        else:
            show_config()
        return

    if args[0] in ("--voice", "-V"):
        voice_mode()
        return

    # 非空参数：当作问题
    prompt = " ".join(args)
    chat(prompt)


if __name__ == "__main__":
    main()
