# 小白 — 零成本终端 AI 助手 🚀

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/zero--cost-🎯-orange" alt="Zero Cost">
  <img src="https://img.shields.io/github/stars/longongzi/xiaobai?style=social" alt="Stars">
</p>

**小白**是一个零成本、零配置的终端 AI 助手。只需一行命令，即可在终端中与 AI 对话，无需注册、无需 API Key、无需付费。

```bash
pip install xiaobai
小白 "什么是量子计算？"
```

## ✨ 特性

- 🆓 **完全免费** — 基于 Zero Token 网关，零成本使用
- 🚀 **即装即用** — `pip install xiaobai`，无需配置
- 💬 **三种模式** — 单次问答、连续对话、语音输入
- 🌐 **纯 Python** — 零依赖，轻量快速
- 🏠 **本地运行** — 数据不上云，隐私安全

## 📦 安装

```bash
pip install xiaobai
```

或直接运行脚本：

```bash
git clone https://github.com/longongzi/xiaobai.git
cd xiaobai
python xiaobai.py
```

## 🎯 使用方法

### 快速问答
```bash
小白 "Python 如何读取 CSV 文件？"
```

### 连续对话
```bash
小白 --chat
```

### 语音输入
```bash
小白 --voice
```

### 指定模型
```bash
小白 "写一首诗" --model gpt-4o-mini
```

## 🧠 原理

小白通过 Zero Token 免费 AI 网关（`localhost:8081`）与 AI 模型通信。网关由 [OpenClaw Zero Token](https://github.com/openclaw-zero/zerotoken) 提供支持。

## 🤝 赞助

如果你觉得小白对你有帮助，欢迎赞助支持我继续开发：

- **[GitHub Sponsors](https://github.com/sponsors/longongzi)** — 每月赞助
- **微信** — 扫码赞助（建设中）

## 📄 开源协议

MIT License © 2024 [longongzi](https://github.com/longongzi)
