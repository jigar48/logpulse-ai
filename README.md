# ⚡ LogPulse AI — Autonomous Terminal Log Debugger & SRE Copilot

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![AI Engine: Google Gemini 2.5](https://img.shields.io/badge/AI%20Engine-Gemini%202.5%20Flash-orange.svg)](https://ai.google.dev/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/jigar48/logpulse-ai)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Support-ffd700.svg)](https://buymeacoffee.com/YOUR_LINK)

> **Turn unreadable stack traces, production crash loops, and CI/CD failures into root causes, unified git diffs, and executive incident post-mortems in seconds.**

---

```
  ██╗      ██████╗  ██████╗ ██████╗ ██╗   ██╗██╗     ███████╗███████╗
  ██║     ██╔═══██╗██╔════╝ ██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
  ██║     ██║   ██║██║  ███╗██████╔╝██║   ██║██║     ███████╗█████╗  
  ██║     ██║   ██║██║   ██║██╔═══╝ ██║   ██║██║     ╚════██║██╔══╝  
  ███████╗╚██████╔╝╚██████╔╝██║     ╚██████╔╝███████╗███████║███████╗
  ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝
       Autonomous Terminal Log Debugger & SRE Copilot v1.0.0
        Powered by Google Gemini 2.5 • Zero-Data-Leak Local Scrubber
```

---

## 🌟 Why LogPulse AI?

Modern production systems generate millions of lines of logs. When an outage occurs:
- **Developers waste hours** sifting through noisy logs to find the single line that caused a crash.
- **Leaked secrets are a catastrophic risk**: Copy-pasting logs into web chatbots often leaks production database passwords, JWT tokens, customer emails, and AWS access keys.
- **Incident reporting is tedious**: SREs and tech leads spend hours writing post-mortems after fixing the bug.

**LogPulse AI** solves this instantly right inside your terminal:
1. **Zero-Config Ingestion**: Pipe from `stdin` (`cat error.log | python logpulse.py`), pass a file (`--file`), or wrap failing commands (`python logpulse.py run "npm test"`).
2. **Enterprise Privacy (Local Secret Scrubber)**: Automatically redacts AWS keys, JWTs, Bearer tokens, DB connection strings, and IPs **locally** before sending context to Gemini.
3. **Smart Noise Compaction**: Strips repetitive health checks (`/health`, `/metrics`) and extracts the exact crash blast radius.
4. **Autonomous Root Cause & Git Patching**: Leverages Google Gemini 2.5 Flash to identify root causes and generate ready-to-apply unified code/config diffs.
5. **One-Click Post-Mortem Export**: Generates professional, executive-ready Incident Post-Mortem Markdown reports (`--export incident.md`).

---

## 🚀 Quickstart (30 Seconds)

### 1. Installation
```bash
git clone https://github.com/jigar48/logpulse-ai.git
cd logpulse-ai
pip install -r requirements.txt
```

### 2. Configure Gemini API Key
Get your free API key at [Google AI Studio](https://aistudio.google.com/):
```bash
# Linux / macOS
export GEMINI_API_KEY="AIzaSyYourKeyHere..."

# Windows PowerShell
$env:GEMINI_API_KEY="AIzaSyYourKeyHere..."

# Windows CMD
set GEMINI_API_KEY=AIzaSyYourKeyHere...
```

### 3. Run the Zero-Key Demo
Test the scrubber, root-cause engine, and diff generator instantly:
```bash
python logpulse.py --demo
```

---

## 🛠️ Usage Examples

### A. Pipe Directly from Logs or CI/CD
```bash
# Debug a live docker container crash
docker logs backend --tail 300 | python logpulse.py

# Debug a Kubernetes pod crash
kubectl logs pod/api-service-xyz --previous | python logpulse.py

# Debug any log file
cat /var/log/nginx/error.log | python logpulse.py
```

### B. Analyze a Specific Log File
```bash
python logpulse.py --file sample_crash.log
```

### C. Wrap and Auto-Debug Failing Commands
```bash
# Runs the command, captures crash output, and auto-debugs if non-zero exit code:
python logpulse.py run "pytest tests/unit/"
python logpulse.py run "npm run build"
python logpulse.py run "go test ./..."
```

### D. Generate an Incident Post-Mortem Report
```bash
python logpulse.py --file sample_crash.log --export incident-report.md
```

---

## 🛡️ Enterprise Security & Secret Scrubbing

LogPulse AI guarantees zero credential leaks. Before any byte is transmitted to the AI engine, the built-in regex scrubber masks:
- **Cloud Credentials**: AWS Access Keys (`AKIA...`), AWS Secret Keys
- **Authentication**: JWT tokens, OAuth Bearer tokens, GitHub PATs (`ghp_...`), Stripe Secret Keys (`sk_live_...`)
- **Databases**: PostgreSQL, MySQL, MongoDB, Redis connection strings (`postgres://user:pass@host...`)
- **Cryptographic Keys**: RSA / OpenSSH Private Keys
- **PII**: IPv4 / IPv6 addresses, Email addresses

Run with `--scrub-strict` for aggressive masking.

---

## 📋 CLI Reference

| Flag / Option | Description | Example |
|---|---|---|
| `-f, --file PATH` | Path to log file to analyze | `python logpulse.py -f app.log` |
| `-r, --run "CMD"` | Execute command and auto-debug on failure | `python logpulse.py -r "pytest"` |
| `-e, --export PATH`| Export analysis to an Incident Post-Mortem Markdown file | `python logpulse.py -f app.log -e rca.md` |
| `-m, --model MODEL`| Gemini model ID (default: `gemini-2.5-flash`) | `python logpulse.py --model gemini-2.5-pro` |
| `-k, --api-key KEY`| Pass Gemini API key directly via CLI | `python logpulse.py -k "AIza..."` |
| `-s, --scrub-strict`| Enable aggressive IP and identifier masking | `python logpulse.py --demo -s` |
| `--demo` | Run interactive showcase with simulated deadlock | `python logpulse.py --demo` |
| `--no-color` | Disable ANSI terminal colors | `python logpulse.py -f app.log --no-color` |
| `-v, --version` | Display version information | `python logpulse.py -v` |

---

## ☕ Support & Community

LogPulse AI is completely free and open-source under the MIT license. If this tool saved you hours of debugging outages or downtime:

- ☕ **[Buy Me a Coffee](https://buymeacoffee.com/YOUR_LINK)** — Fuel further open-source development!
- ⭐ **Star this repository** on GitHub to help fellow engineers find it.

---

## 💼 Custom AI & High-Performance Engineering

Need enterprise-grade AI automation, intelligent developer tooling, or custom LLM infrastructure for your company?

I specialize in:
- Autonomous AI Agents & Workflow Automation
- Enterprise Retrieval-Augmented Generation (RAG) & Database Knowledge Graphs
- Low-Latency Backend Systems & Cloud Infrastructure (Python, Go, GCP, AWS)

📫 **Reach out for consulting & contract engagements:**
- **LinkedIn:** [linkedin.com/in/YOUR_LINK](https://linkedin.com/in/YOUR_LINK)
- **Portfolio / Inquiries:** [YOUR_WEBSITE_OR_EMAIL](mailto:your_email@example.com)

---

*Built with precision for developers, SREs, and DevOps engineers worldwide.*
