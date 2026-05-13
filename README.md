# 小白 🐣

> **有问题？找小白。** 零成本终端 AI 助手，不需要 API Key，不需要注册，不需要付费。

```
小白 帮我写一个Python爬虫
小白 今天深圳天气怎么样？
小白 帮我翻译成英文
```

---

## 它能做什么？

小白是一个跑在终端的 AI 助手，你问什么它答什么。和 ChatGPT 一样聪明，**但完全免费**。

- ✅ **写代码** — `小白 写一个 Flask 登录页面`
- ✅ **翻译** — `小白 把这段话翻译成日语`
- ✅ **查资料** — `小白 Python 的装饰器是什么`
- ✅ **写文案** — `小白 帮我写一段产品介绍`
- ✅ **语音对话** — `小白 --voice`
- 🔜 图片识别
- 🔜 多轮对话历史
- 🔜 浏览器插件

## 一分钟上手

### 1. 安装

```bash
pip install xiaobai
```

### 2. 启动 Zero Token 网关（免费 AI 引擎）

小白默认连接本地的 Zero Token 网关，这是它能免费的原因。

在另一个终端启动：

```bash
# 从项目仓库下载网关
git clone https://github.com/longongzi/zero-token-gateway.git
cd zero-token-gateway
python zerotoken_gateway.py
```

或者用你喜欢的任何 OpenAI 兼容 API。

### 3. 开聊！

```bash
小白 你好，你叫什么名字？
```

小白会回答你。就这么简单。

## 自定义

小白的配置保存在 `~/.xiaobai_config.json`，你可以改：

```bash
小白 config                # 查看当前配置
小白 config set api_url http://你的地址/v1/chat/completions
小白 config set model gpt-4o
小白 config set temperature 0.5
```

## 语音模式

```bash
小白 --voice
```

Windows 下自动朗读回复内容（需要 `pip install pywin32`）。

## 为什么免费？

小白后端连接的是 [Zero Token Gateway](https://github.com/longongzi/zero-token-gateway)，它通过浏览器复用在 AI 网站的登录态，实现零成本调用。

**原理**：你登录一次 ChatGPT/DeepSeek 等网站后，网关复用这个会话，你问问题它回答，不消耗任何 API 额度。

## 小白的哲学

- **零门槛** — pip install 就能用
- **零成本** — 不需要一分钱 API 费
- **零配置** — 装上就能问
- **中文优先** — 对中文用户友好

## 📢 赞助

小白是完全免费的开源项目。如果你觉得它有用，请考虑赞助支持：

**[☕ 赞助小白](https://github.com/sponsors/longongzi)**

每一分钱都会用来：
- 升级服务器让小白更快
- 支持更多免费 AI 模型
- 开发新功能（图片、文件、插件系统）

或者给我点个 ⭐，也是最大的支持！

## License

MIT
