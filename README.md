<div align="center">

# 💬 WhatsApp MCP Server

### Connect Claude AI to WhatsApp — Search, Read & Send Messages with AI

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Go 1.21+](https://img.shields.io/badge/Go-1.21+-00ADD8.svg)](https://golang.org/dl/)
[![MCP Protocol](https://img.shields.io/badge/MCP-Compatible-purple.svg)](https://modelcontextprotocol.io/)
[![Docker Ready](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)

<br />

**The most powerful open-source WhatsApp integration for Claude AI and other MCP-compatible assistants.**

Search conversations • Send messages • Share media • React to messages • All through natural language.

<br />

[**Quick Start**](#-quick-start) · [**Features**](#-features) · [**Documentation**](#-installation) · [**FAQ**](#-faq)

<br />

<img src="./example-use.png" alt="WhatsApp MCP Server Demo - Claude AI sending WhatsApp messages" width="700" />

<sub>*Example: Using Claude to interact with WhatsApp contacts naturally*</sub>

</div>

<br />

---

<br />

## 🎯 Why WhatsApp MCP Server?

| Problem | Solution |
|---------|----------|
| 🔒 **Privacy concerns** with cloud-based WhatsApp APIs | All data stored **locally** in SQLite — nothing leaves your machine unless you ask |
| 🤖 **No AI integration** with WhatsApp | Direct **Claude AI** integration via Model Context Protocol |
| 💰 **Expensive** third-party WhatsApp APIs | **100% free** and open-source, connects to your personal account |
| 🔧 **Complex setup** for WhatsApp automation | **Simple 3-step installation** — clone, run, connect |

<br />

> [!NOTE]
> This connects to your **personal WhatsApp account** via the official WhatsApp Web protocol. Your messages are stored locally and only sent to Claude when you explicitly request it through MCP tools.

<br />

---

<br />

## ✨ Features

<table>
<tr>
<td width="50%">

### 📱 Messaging
- ✅ Send text messages to contacts & groups
- ✅ Search message history with filters
- ✅ Get conversation context
- ✅ React to messages with emojis
- ✅ View chat metadata & info

</td>
<td width="50%">

### 📎 Media Support
- ✅ Send images, videos & documents
- ✅ Send voice messages (auto-converts audio)
- ✅ Download received media files
- ✅ FFmpeg auto-conversion for audio
- ✅ All major formats supported

</td>
</tr>
<tr>
<td width="50%">

### 🔍 Smart Search
- ✅ Search contacts by name or number
- ✅ Filter messages by date & sender
- ✅ Find specific conversations
- ✅ Get last interaction with contact
- ✅ Full-text message search

</td>
<td width="50%">

### 🔐 Privacy & Security
- ✅ Local SQLite database storage
- ✅ API key authentication
- ✅ No cloud dependencies
- ✅ You control what Claude sees
- ✅ Directory traversal protection

</td>
</tr>
</table>

<br />

---

<br />

## 🚀 Quick Start

Get up and running in under 5 minutes:

```bash
# 1. Clone the repository
git clone https://github.com/hemangjoshi37a/hjLabs.in-whatsapp-mcp-server.git
cd hjLabs.in-whatsapp-mcp-server

# 2. Start the WhatsApp bridge (scan QR code with your phone)
cd whatsapp-bridge && go run main.go

# 3. Configure Claude Desktop (see Installation section below)
```

<br />

---

<br />

## 📦 Installation

### Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| [Go](https://golang.org/dl/) | 1.21+ | WhatsApp bridge runtime |
| [Python](https://www.python.org/downloads/) | 3.11+ | MCP server runtime |
| [UV](https://github.com/astral-sh/uv) | Latest | Python package manager |
| [Claude Desktop](https://claude.ai/download) | Latest | Or Cursor IDE |
| [FFmpeg](https://ffmpeg.org/) | *Optional* | Audio format conversion |

<details>
<summary><strong>📥 Install UV (Python package manager)</strong></summary>

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

</details>

<details>
<summary><strong>🎵 Install FFmpeg (optional, for voice messages)</strong></summary>

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# Windows (with Chocolatey)
choco install ffmpeg
```

</details>

<br />

### Step 1: Clone & Start the Bridge

```bash
git clone https://github.com/hemangjoshi37a/hjLabs.in-whatsapp-mcp-server.git
cd hjLabs.in-whatsapp-mcp-server/whatsapp-bridge
go run main.go
```

**First run:** A QR code will appear in your terminal. Scan it with WhatsApp on your phone:
- Open WhatsApp → **Settings** → **Linked Devices** → **Link a Device**

<br />

### Step 2: Configure Claude Desktop

Add this to your Claude Desktop configuration file:

<table>
<tr>
<th>Operating System</th>
<th>Config File Location</th>
</tr>
<tr>
<td>macOS</td>
<td><code>~/Library/Application Support/Claude/claude_desktop_config.json</code></td>
</tr>
<tr>
<td>Windows</td>
<td><code>%APPDATA%\Claude\claude_desktop_config.json</code></td>
</tr>
<tr>
<td>Linux</td>
<td><code>~/.config/Claude/claude_desktop_config.json</code></td>
</tr>
</table>

```json
{
  "mcpServers": {
    "whatsapp": {
      "command": "/path/to/uv",
      "args": [
        "--directory",
        "/path/to/hjLabs.in-whatsapp-mcp-server/whatsapp-mcp-server",
        "run",
        "main.py"
      ]
    }
  }
}
```

> **💡 Tip:** Run `which uv` (macOS/Linux) or `where uv` (Windows) to find your UV path.

<br />

### Step 3: Restart & Connect

1. **Restart Claude Desktop** (or Cursor)
2. Look for the **WhatsApp** integration in the MCP tools panel
3. Start chatting! Try: *"Show me my recent WhatsApp conversations"*

<br />

<details>
<summary><strong>🪟 Windows-Specific Setup</strong></summary>

Windows requires CGO enabled for SQLite support:

```bash
# 1. Install MSYS2 from https://www.msys2.org/
# 2. Add ucrt64\bin to your PATH
# 3. Enable CGO and run:

cd whatsapp-bridge
go env -w CGO_ENABLED=1
go run main.go
```

See the [MinGW setup guide](https://code.visualstudio.com/docs/cpp/config-mingw) for detailed instructions.

</details>

<details>
<summary><strong>🐳 Docker Deployment</strong></summary>

```bash
# Using Docker Compose
docker-compose up -d

# Or build individually
docker build -t whatsapp-bridge ./whatsapp-bridge
docker build -t whatsapp-mcp ./whatsapp-mcp-server
```

Set the `WHATSAPP_API_KEY` environment variable for authentication.

</details>

<br />

---

<br />

## 🛠️ MCP Tools Reference

<table>
<tr>
<th>Tool</th>
<th>Description</th>
<th>Type</th>
</tr>
<tr>
<td><code>search_contacts</code></td>
<td>Search contacts by name or phone number</td>
<td>🔍 Read</td>
</tr>
<tr>
<td><code>list_chats</code></td>
<td>List all available chats with metadata</td>
<td>🔍 Read</td>
</tr>
<tr>
<td><code>get_chat</code></td>
<td>Get detailed information about a specific chat</td>
<td>🔍 Read</td>
</tr>
<tr>
<td><code>list_messages</code></td>
<td>Retrieve messages with filters (date, sender, etc.)</td>
<td>🔍 Read</td>
</tr>
<tr>
<td><code>get_message_context</code></td>
<td>Get surrounding context for a specific message</td>
<td>🔍 Read</td>
</tr>
<tr>
<td><code>get_direct_chat_by_contact</code></td>
<td>Find direct chat with a specific contact</td>
<td>🔍 Read</td>
</tr>
<tr>
<td><code>get_contact_chats</code></td>
<td>List all chats involving a specific contact</td>
<td>🔍 Read</td>
</tr>
<tr>
<td><code>get_last_interaction</code></td>
<td>Get the most recent message with a contact</td>
<td>🔍 Read</td>
</tr>
<tr>
<td><code>send_message</code></td>
<td>Send text message to contact or group</td>
<td>✏️ Write</td>
</tr>
<tr>
<td><code>send_file</code></td>
<td>Send image, video, or document</td>
<td>✏️ Write</td>
</tr>
<tr>
<td><code>send_audio_message</code></td>
<td>Send voice message (auto-converts to Opus)</td>
<td>✏️ Write</td>
</tr>
<tr>
<td><code>download_media</code></td>
<td>Download media from a message to local file</td>
<td>📥 Download</td>
</tr>
<tr>
<td><code>react_to_message</code></td>
<td>Add emoji reaction to a message</td>
<td>✏️ Write</td>
</tr>
</table>

<br />

---

<br />

## 🏗️ Architecture

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   Claude AI     │────▶│  Python MCP      │────▶│   Go Bridge     │
│   (or Cursor)   │◀────│  Server          │◀────│                 │
└─────────────────┘     └──────────────────┘     └─────────────────┘
                               │                        │
                               ▼                        ▼
                        ┌──────────────────┐     ┌─────────────────┐
                        │  SQLite DB       │     │  WhatsApp Web   │
                        │  (Local Storage) │     │  API            │
                        └──────────────────┘     └─────────────────┘
```

| Component | Directory | Purpose |
|-----------|-----------|---------|
| **Go Bridge** | `whatsapp-bridge/` | Connects to WhatsApp Web API, handles auth, stores messages |
| **Python MCP** | `whatsapp-mcp-server/` | Implements MCP protocol, exposes tools to Claude |
| **SQLite DB** | `whatsapp-bridge/store/` | Local storage for messages and chat history |

<br />

---

<br />

## ❓ FAQ

<details>
<summary><strong>Is my data safe? Where are messages stored?</strong></summary>

All messages are stored **locally** in a SQLite database on your machine (`whatsapp-bridge/store/`). Data is only sent to Claude when you explicitly use MCP tools to query it. No data is sent to any third-party servers.

</details>

<details>
<summary><strong>Will this get my WhatsApp account banned?</strong></summary>

This uses the official WhatsApp Web multi-device protocol (via [whatsmeow](https://github.com/tulir/whatsmeow)), the same protocol used by WhatsApp Web and Desktop apps. However, as with any automation, use responsibly and don't spam.

</details>

<details>
<summary><strong>How often do I need to re-authenticate?</strong></summary>

WhatsApp sessions typically last about **20 days** before requiring re-authentication. The bridge will automatically reconnect if your session is still valid.

</details>

<details>
<summary><strong>Can I use this with other MCP clients besides Claude?</strong></summary>

Yes! Any MCP-compatible client can use this server. The protocol is standardized, so it works with Cursor, and other tools implementing MCP.

</details>

<details>
<summary><strong>My messages aren't loading after authentication</strong></summary>

Initial sync can take several minutes, especially with many chats. Wait a few minutes and try again. If issues persist, check the bridge terminal for errors.

</details>

<details>
<summary><strong>Messages are out of sync with my phone</strong></summary>

Delete the database files and re-authenticate:
```bash
rm whatsapp-bridge/store/messages.db whatsapp-bridge/store/whatsapp.db
cd whatsapp-bridge && go run main.go
```

</details>

<details>
<summary><strong>QR code doesn't appear in terminal</strong></summary>

Ensure your terminal supports Unicode characters. Try a different terminal emulator, or check the bridge logs for the QR code URL if HTTP mode is enabled.

</details>

<br />

---

<br />

## 🔒 Security Considerations

> [!WARNING]
> As with many MCP servers, be aware of [the lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) — prompt injection could potentially lead to data exfiltration. Review Claude's tool usage carefully.

**Security features included:**
- 🔑 API key authentication (set `WHATSAPP_API_KEY` environment variable)
- 🛡️ Input sanitization and validation
- 📁 Directory traversal protection for media downloads
- 📝 Sanitized logging (phone numbers and JIDs are masked)

<br />

---

<br />

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

<br />

---

<br />

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

<br />

---

<br />

<div align="center">

### 📬 Stay Updated

Get notified about updates and new features:

[**Subscribe to Updates**](https://docs.google.com/forms/d/1rTF9wMBTN0vPfzWuQa2BjfGKdKIpTbyeKxhPMcEzgyI/preview)

<br />

**Built with ❤️ by [hjLabs](https://hjlabs.in)**

<br />

[![GitHub stars](https://img.shields.io/github/stars/hemangjoshi37a/hjLabs.in-whatsapp-mcp-server?style=social)](https://github.com/hemangjoshi37a/hjLabs.in-whatsapp-mcp-server)

<sub>If this project helped you, consider giving it a ⭐</sub>

</div>
