# 🎬 Video Editing Orchestration Agent

An agentic video editing system powered by LLaMA 3 + LangChain.

This project converts high-level editing instructions into structured execution plans and deterministically applies video transformations using FFmpeg and MoviePy.

It demonstrates how to build a production-safe AI orchestration layer for video workflows.

---

## 🚀 Features

- 🧠 LLaMA 3 planner (via Ollama)
- 📐 Structured JSON plan generation using Pydantic
- 🔒 Schema validation to prevent tool hallucination
- ⚙️ Deterministic execution layer
- 🎥 FFmpeg + MoviePy video processing
- 📊 Metadata-aware planning (duration, resolution, fps)

---

## 🏗 Architecture
┌──────────────────────────┐
│       User Request       │
└──────────────────────────┘
              │
              ▼
┌──────────────────────────┐
│  LLaMA 3 Planner         │
│  (LangChain + Ollama)    │
└──────────────────────────┘
              │
              ▼
┌──────────────────────────┐
│  Structured Plan         │
│  (Pydantic Schema)       │
└──────────────────────────┘
              │
              ▼
┌──────────────────────────┐
│     Validation Layer     │
│  - Tool Allowlist        │
│  - Param Validation      │
└──────────────────────────┘
              │
              ▼
┌──────────────────────────┐
│    Execution Engine      │
│  - Sequential Execution  │
│  - Artifact Tracking     │
└──────────────────────────┘
              │
              ▼
┌──────────────────────────┐
│     Video Tools Layer    │
│  FFmpeg / MoviePy        │
└──────────────────────────┘
              │
              ▼
┌──────────────────────────┐
│    Final Output Video    │
└──────────────────────────┘


The system separates:

- Probabilistic planning (LLM)
- Deterministic execution (tool layer)

This prevents unsafe command generation and improves reliability.

---

## 🧠 Available Tools

- `trim_video(start: float, end: float)`
- `remove_silence()`
- `add_subtitles(subtitle_file: str)`

Tools are strictly validated before execution.

---

## 🛠 Tech Stack

- Python 3.10+
- LangChain
- Ollama (LLaMA 3)
- FFmpeg
- MoviePy
- Pydantic

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone git@github.com:pankajmi/video-editor-agent.git
cd video-agent
```

### 2. Create virtual environment & Install deps
```
uv sync
```

### 3. Install FFmpeg
```
brew install ffmpeg
```

### 4. Install and run LLaMA 3 with Ollama
```
ollama pull llama3
```

### 5. Run agent
```
python main.py
```

The agent will:
Extract video metadata
Generate structured editing plan
Validate tool usage
Execute tools sequentially
Produce final edited video


🚀 Future Improvements
LangGraph state machine orchestration
Parallel DAG execution
Highlight detection via transcript
Silence detection pre-analysis
GPU accelerated encoding
Cloud worker support
Object storage integration (S3)
