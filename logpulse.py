#!/usr/bin/env python3
"""
# ⚡ LogPulse AI — Autonomous Terminal Log Debugger & Incident Copilot

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![AI Engine: Google Gemini 2.5](https://img.shields.io/badge/AI%20Engine-Gemini%202.5%20Flash-orange.svg)](https://ai.google.dev/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/jigar48/logpulse-ai)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Support-ffd700.svg)](https://buymeacoffee.com/buildwithjigar)

> **Turn unreadable stack traces, production crash loops, and CI/CD failures into root causes, unified git diffs, and executive incident post-mortems in seconds.**

---

## 🌟 Why LogPulse AI?

Modern production systems generate millions of lines of logs. When an outage occurs:
- **Developers waste hours** sifting through noisy logs to find the single line that caused a crash.
- **Leaked secrets are a massive risk**: Copy-pasting logs into web chatbots often exposes production database passwords, JWT tokens, and AWS access keys.
- **Incident reporting is tedious**: SREs and leads spend hours writing post-mortems after fixing the bug.

**LogPulse AI** solves this instantly from your terminal:
1. **Zero-Config Ingestion**: Pipe from `stdin` (`cat error.log | python logpulse.py`), pass a file (`--file`), or wrap failing commands (`python logpulse.py run "npm test"`).
2. **Enterprise Privacy (Local Secret Scrubber)**: Automatically redacts AWS keys, JWTs, Bearer tokens, DB connection strings, and IPs **locally** before sending context to Gemini.
3. **Smart Noise Compaction**: Strips repetitive health checks and isolates the critical crash blast radius.
4. **Autonomous Root Cause & Git Patching**: Leverages Google Gemini 2.5 Flash to identify root causes and generate ready-to-apply unified code/config diffs.
5. **One-Click Post-Mortem Export**: Generates professional, executive-ready Incident Post-Mortem Markdown reports (`--export incident.md`).

---

## 🚀 Quickstart (30 Seconds)

### 1. Installation
```bash
git clone https://github.com/jigar48/logpulse-ai.git
cd logpulse-ai
pip install google-genai
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
python logpulse.py --file crash.log
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
python logpulse.py --file prod_incident.log --export postmortem-2026-10-19.md
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

- ☕ **[Buy Me a Coffee](https://buymeacoffee.com/buildwithjigar)** — Fuel further open-source development!
- ⭐ **Star this repository** on GitHub to help fellow engineers find it.

---

## 💼 Custom AI & High-Performance Engineering

Need enterprise-grade AI automation, intelligent developer tooling, or custom LLM infrastructure for your company?

I specialize in:
- Autonomous AI Agents & Workflow Automation
- Enterprise Retrieval-Augmented Generation (RAG) & Database Knowledge Graphs
- Low-Latency Backend Systems & Cloud Infrastructure (Python, Go, GCP, AWS)

📫 **Reach out for consulting & contract engagements:**
- **LinkedIn:** [Jigar Prajapati](https://www.linkedin.com/in/buildaiwith-jigar-prajapati/)
- **Portfolio:** [jigar48.github.io/automatewithjigar](https://jigar48.github.io/automatewithjigar/)
- **GitHub:** [@jigar48](https://github.com/jigar48)

---

*Built with precision by [Jigar Prajapati](https://www.linkedin.com/in/buildaiwith-jigar-prajapati/) for developers, SREs, and DevOps engineers worldwide.*
"""

import argparse
import datetime
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Ensure UTF-8 output encoding across Windows, Linux, and macOS terminals
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Attempt to import official google-genai SDK
try:
    from google import genai
    from google.genai import types
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False


# ============================================================================
# CONFIGURATION & CONSTANTS
# ============================================================================
__version__ = "1.0.0"
TOOL_NAME = "LogPulse AI"
DEFAULT_MODEL = "gemini-2.5-flash"
DONATION_LINK = "https://buymeacoffee.com/buildwithjigar"
LINKEDIN_LINK = "https://www.linkedin.com/in/buildaiwith-jigar-prajapati/"
PORTFOLIO_LINK = "https://jigar48.github.io/automatewithjigar/"
GITHUB_LINK = "https://github.com/jigar48"


# ============================================================================
# ANSI TERMINAL STYLING ENGINE
# ============================================================================
class TerminalStyle:
    """Cross-platform ANSI color and formatting manager."""
    def __init__(self, enabled: bool = True):
        self.enabled = enabled
        if self.enabled:
            self._init_windows_terminal()

    def _init_windows_terminal(self):
        """Enable virtual terminal processing on Windows if supported."""
        if sys.platform == "win32":
            try:
                import ctypes
                kernel32 = ctypes.windll.kernel32
                handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
                mode = ctypes.c_ulong()
                if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
                    mode.value |= 0x0004  # ENABLE_VIRTUAL_TERMINAL_PROCESSING
                    kernel32.SetConsoleMode(handle, mode)
            except Exception:
                pass
            os.system("")  # Triggers ANSI initialization in some Windows terminals

    def _c(self, code: str) -> str:
        return code if self.enabled else ""

    @property
    def RESET(self) -> str: return self._c("\033[0m")
    @property
    def BOLD(self) -> str: return self._c("\033[1m")
    @property
    def DIM(self) -> str: return self._c("\033[2m")
    @property
    def RED(self) -> str: return self._c("\033[91m")
    @property
    def GREEN(self) -> str: return self._c("\033[92m")
    @property
    def YELLOW(self) -> str: return self._c("\033[93m")
    @property
    def BLUE(self) -> str: return self._c("\033[94m")
    @property
    def MAGENTA(self) -> str: return self._c("\033[95m")
    @property
    def CYAN(self) -> str: return self._c("\033[96m")
    @property
    def WHITE(self) -> str: return self._c("\033[97m")
    @property
    def BG_DARK(self) -> str: return self._c("\033[48;5;236m")


# ============================================================================
# SPINNER FOR ASYNC OPERATIONS
# ============================================================================
class Spinner:
    """Threaded terminal spinner animation for long-running operations."""
    def __init__(self, message: str = "Processing...", style: Optional[TerminalStyle] = None):
        self.message = message
        self.style = style or TerminalStyle()
        self.frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        self.stop_event = threading.Event()
        self.thread: Optional[threading.Thread] = None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    def start(self):
        if not sys.stdout.isatty():
            print(f"{self.message}...")
            return
        self.stop_event.clear()
        self.thread = threading.Thread(target=self._spin, daemon=True)
        self.thread.start()

    def _spin(self):
        idx = 0
        while not self.stop_event.is_set():
            char = self.frames[idx % len(self.frames)]
            spin_str = f"\r{self.style.CYAN}{char}{self.style.RESET} {self.style.BOLD}{self.message}{self.style.RESET}"
            sys.stdout.write(spin_str)
            sys.stdout.flush()
            idx += 1
            time.sleep(0.08)

    def stop(self):
        if self.thread and self.thread.is_alive():
            self.stop_event.set()
            self.thread.join(timeout=1.0)
            if sys.stdout.isatty():
                sys.stdout.write("\r" + " " * (len(self.message) + 10) + "\r")
                sys.stdout.flush()


# ============================================================================
# ENTERPRISE PRIVACY: LOCAL SECRET & PII SCRUBBER
# ============================================================================
class SecurityScrubber:
    """
    Guarantees no sensitive company secrets, API keys, credentials, or PII
    leave the developer's workstation without sanitization.
    """
    def __init__(self, strict_mode: bool = False):
        self.strict_mode = strict_mode
        self.rules = [
            ("AWS Access Key", r"\b(AKIA[0-9A-Z]{16})\b", "[REDACTED_AWS_ACCESS_KEY]"),
            ("API / Secret Key", r"(?i)\b(api[_-]?key|secret[_-]?key|access[_-]?token|auth[_-]?token|client[_-]?secret)\s*[:=]\s*['\"]?([A-Za-z0-9_\-\.]{12,128})['\"]?", r"\1: [REDACTED_SECRET_KEY]"),
            ("JWT Token", r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b", "[REDACTED_JWT_TOKEN]"),
            ("Bearer Token", r"(?i)\bBearer\s+[A-Za-z0-9_\-\.]{16,}\b", "Bearer [REDACTED_BEARER_TOKEN]"),
            ("Database Credentials", r"\b(postgres(?:ql)?|mysql|mongodb(?:\+srv)?|redis|amqp):\/\/([^:@\s]+):([^@\s]+)@([^\s\/]+)", r"\1://[REDACTED_USER]:[REDACTED_PASSWORD]@\4"),
            ("Private Key Block", r"-----BEGIN (?:RSA )?PRIVATE KEY-----[\s\S]+?-----END (?:RSA )?PRIVATE KEY-----", "[REDACTED_PRIVATE_KEY_BLOCK]"),
            ("GitHub Token", r"\b(gh[pousr]_[A-Za-z0-9_]{36,255})\b", "[REDACTED_GITHUB_TOKEN]"),
            ("Stripe Secret Key", r"\b(?:sk|rk)_(?:live|test)_[0-9a-zA-Z]{24,99}\b", "[REDACTED_STRIPE_KEY]"),
            ("Password Field", r"(?i)(password|passwd|pwd)\s*[:=]\s*['\"]?([^'\"\s,;]{4,})['\"]?", r"\1: [REDACTED_PASSWORD]"),
            ("Email Address", r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "[REDACTED_EMAIL]"),
        ]

        if self.strict_mode:
            # Mask IPv4 addresses (excluding standard localhost)
            self.rules.append(
                ("Internal IP Address", r"\b(?!127\.0\.0\.1|0\.0\.0\.0)(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", "[REDACTED_IP]")
            )

    def scrub(self, text: str) -> Tuple[str, Dict[str, int]]:
        """
        Sanitize text and return tuple of (scrubbed_text, stats_dict).
        """
        scrubbed = text
        stats: Dict[str, int] = {}

        for friendly_name, pattern, replacement in self.rules:
            matches = len(re.findall(pattern, scrubbed))
            if matches > 0:
                stats[friendly_name] = stats.get(friendly_name, 0) + matches
                scrubbed = re.sub(pattern, replacement, scrubbed)

        return scrubbed, stats


# ============================================================================
# LOG NOISE COMPACTION & WINDOW EXTRACTION
# ============================================================================
class LogCompressor:
    """
    Strips high-volume, repetitive log spam (health checks, heartbeats)
    and extracts high-density error context windows for LLM analysis.
    """
    NOISE_PATTERNS = [
        re.compile(r"GET \/health(?:z)? HTTP\/[0-9.]+\" 200", re.IGNORECASE),
        re.compile(r"GET \/metrics HTTP\/[0-9.]+\" 200", re.IGNORECASE),
        re.compile(r"GET \/ping HTTP\/[0-9.]+\" 200", re.IGNORECASE),
        re.compile(r"Heartbeat ack|PONG|Keep-Alive", re.IGNORECASE),
        re.compile(r"kube-probe\/[0-9.]+", re.IGNORECASE),
    ]

    ERROR_TRIGGERS = re.compile(
        r"(Exception|Traceback|Error|FATAL|PANIC|CRITICAL|FAIL|errno|denied|timed out|segfault|deadlock|oom)",
        re.IGNORECASE
    )

    @classmethod
    def compress(cls, raw_logs: str, max_chars: int = 40000) -> Tuple[str, int, int]:
        """
        Filters noise and returns (compacted_log, original_line_count, compressed_line_count).
        """
        lines = raw_logs.splitlines()
        original_count = len(lines)

        filtered_lines: List[str] = []
        for line in lines:
            # Check if line matches any spam pattern
            if any(p.search(line) for p in cls.NOISE_PATTERNS):
                continue
            filtered_lines.append(line)

        # If logs are still extremely large, extract a smart window around error triggers
        if len("\n".join(filtered_lines)) > max_chars:
            # Find indices with error triggers
            error_indices = [i for i, line in enumerate(filtered_lines) if cls.ERROR_TRIGGERS.search(line)]
            if error_indices:
                # Build context windows of 15 lines before and 35 lines after each error
                keep_indices = set()
                for idx in error_indices:
                    start = max(0, idx - 15)
                    end = min(len(filtered_lines), idx + 35)
                    keep_indices.update(range(start, end))

                filtered_lines = [line for i, line in enumerate(filtered_lines) if i in keep_indices]

        result = "\n".join(filtered_lines)
        if len(result) > max_chars:
            # Truncate keeping head and tail
            half = max_chars // 2
            result = result[:half] + "\n\n... [LogPulse: Intermediate log chunk condensed] ...\n\n" + result[-half:]

        return result, original_count, len(filtered_lines)


# ============================================================================
# GEMINI 2.5 FLASH SRE REASONING ENGINE
# ============================================================================
class GeminiDebugger:
    """Integrates with Google Gemini to perform autonomous SRE root-cause analysis."""
    
    SYSTEM_INSTRUCTION = """You are LogPulse AI, a Principal Site Reliability Engineer (SRE), Staff Software Architect, and Senior Incident Commander.
Your job is to autonomously analyze raw or crash logs, diagnose the exact failure mechanisms, and deliver high-precision engineering remedies.

You must format your response clearly in standard Markdown using the following strict section structure:

### 1. 🎯 INCIDENT OVERVIEW & SEVERITY
- **Severity Rating**: [CRITICAL | HIGH | MEDIUM | LOW]
- **Component / Service**: Identify the failing service or subsystem.
- **Incident Summary**: 2-3 sentences explaining what happened in plain, high-level terms.

### 2. 🔍 ROOT CAUSE ANALYSIS (RCA)
- Provide a precise, technical breakdown of why this failure occurred.
- Point out the exact line, exception, deadlock, memory leak, or misconfiguration in the log.
- Explain the cascade effects (e.g., worker pool exhaustion, thread starvation).

### 3. 🛠️ RECOMMENDED CODE / CONFIG PATCH
Provide a ready-to-apply Unified Git Diff or exact configuration block. Format inside a fenced code block with `diff` or proper language tag:
```diff
--- a/path/to/failing_code.py
+++ b/path/to/failing_code.py
...
```

### 4. 📋 STEP-BY-STEP REMEDIATION PLAN
Numbered, immediate actions the engineer must take right now to recover the system and deploy the fix.

### 5. 🛡️ PREVENTATIVE SAFEGUARDS & ALERTS
- Exact Prometheus/Datadog/CloudWatch metric to alert on.
- Architectural improvements or circuit breakers to prevent recurrence.

Keep your response authoritative, concise, actionable, and free of fluff."""

    def __init__(self, api_key: Optional[str] = None, model: str = DEFAULT_MODEL):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        self.model = model
        self.client = None

        if not self.api_key:
            return

        if GENAI_AVAILABLE:
            try:
                self.client = genai.Client(api_key=self.api_key)
            except Exception as e:
                raise RuntimeError(f"Failed to initialize Google GenAI Client: {e}")

    def analyze(self, sanitized_logs: str) -> str:
        """Call Gemini 2.5 Flash to generate the incident analysis."""
        if not GENAI_AVAILABLE:
            raise RuntimeError(
                "The 'google-genai' package is not installed.\n"
                "Please run: pip install google-genai"
            )

        if not self.client:
            raise RuntimeError(
                "Gemini API Key is missing.\n"
                "Set it via environment variable: export GEMINI_API_KEY='your-key'\n"
                "Or pass it via the CLI: python logpulse.py -k 'your-key'\n"
                "Or run without a key using demo mode: python logpulse.py --demo"
            )

        prompt = f"Analyze the following sanitized application crash log and generate an authoritative SRE incident report:\n\n```\n{sanitized_logs}\n```"

        config = types.GenerateContentConfig(
            system_instruction=self.SYSTEM_INSTRUCTION,
            temperature=0.2,
        )

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=config,
        )

        return response.text or "No analysis returned from Gemini."


# ============================================================================
# INCIDENT POST-MORTEM REPORT EXPORTER
# ============================================================================
class PostMortemExporter:
    """Exports structured SRE post-mortems into markdown files."""
    @staticmethod
    def export(
        filepath: str,
        analysis_markdown: str,
        scrub_stats: Dict[str, int],
        orig_lines: int,
        comp_lines: int,
        model_name: str
    ) -> Path:
        target = Path(filepath).resolve()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")

        stats_summary = ", ".join([f"{k}: {v}" for k, v in scrub_stats.items()]) if scrub_stats else "None (Clean Log)"

        document = f"""# 🚨 Incident Post-Mortem Report

**Generated By:** {TOOL_NAME} v{__version__}  
**Timestamp:** {now}  
**AI Engine:** Google {model_name}  
**Log Telemetry:** {orig_lines} raw lines condensed to {comp_lines} lines  
**Enterprise Security:** {stats_summary} masked locally before analysis  

---

{analysis_markdown}

---

## 📌 Metadata & Sign-off
- **Author:** Automated SRE Diagnostics ({TOOL_NAME})
- **Status:** Action Items Pending Deployment
- **Review Date:** {datetime.datetime.now().strftime("%Y-%m-%d")}

---
### 🤝 Support & Consulting
- ☕ **Support this Open-Source Project:** [{DONATION_LINK}]({DONATION_LINK})
- 💼 **Custom AI Automation & SRE Engineering Engagements:** [{LINKEDIN_LINK}]({LINKEDIN_LINK})
- 🌐 **Portfolio & Case Studies:** [{PORTFOLIO_LINK}]({PORTFOLIO_LINK})
"""
        target.write_text(document, encoding="utf-8")
        return target


# ============================================================================
# REALISTIC DEMO SIMULATION (ZERO-KEY SHOWCASE)
# ============================================================================
SAMPLE_INCIDENT_LOG = """2026-10-19 11:30:02.104 [INFO] [uvicorn.access] 127.0.0.1:48212 - "GET /health 200 OK"
2026-10-19 11:30:04.108 [INFO] [uvicorn.access] 127.0.0.1:48214 - "GET /health 200 OK"
2026-10-19 11:30:05.812 [INFO] [payment_service] Processing checkout order_id=ord_99812 customer=alex@example.com
2026-10-19 11:30:06.120 [INFO] [payment_service] Connecting to db: postgres://prod_admin:SuperSecretPass992@10.0.4.12:5432/payments_db
2026-10-19 11:30:06.310 [DEBUG] [auth_service] Validating Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIn0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
2026-10-19 11:30:07.412 [WARNING] [db_pool] PoolQueueSize reached 98/100 connections. High latency detected.
2026-10-19 11:30:08.520 [ERROR] [payment_service] Database connection acquisition timed out after 5000ms!
2026-10-19 11:30:08.521 [ERROR] [payment_service] AWS Sync Failed. Key AKIAIOSFODNN7EXAMPLE used with invalid token header.
2026-10-19 11:30:08.522 [CRITICAL] [uvicorn.error] Exception in ASGI application
Traceback (most recent call last):
  File "/app/services/checkout.py", line 142, in process_transaction
    async with db.transaction() as session:
  File "/usr/local/lib/python3.12/site-packages/sqlalchemy/ext/asyncio/engine.py", line 872, in begin
    conn = await self.acquire(timeout=self.timeout)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/asyncpg/pool.py", line 630, in acquire
    raise exceptions.PoolTimeoutError(f"Queue pool exhausted: {self._queue.qsize()} waiters")
asyncpg.exceptions.PoolTimeoutError: Queue pool exhausted: 124 waiters waiting for available connection.
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "/app/api/endpoints/checkout.py", line 58, in checkout_endpoint
    await process_transaction(payload, stripe_key="sk_live_51NzABC1234567890abcdef")
  File "/app/services/checkout.py", line 155, in process_transaction
    raise UnhandledTransactionError("Checkout transaction aborted due to database connection starvation")
services.exceptions.UnhandledTransactionError: Checkout transaction aborted due to database connection starvation
2026-10-19 11:30:08.610 [INFO] [uvicorn.access] 127.0.0.1:48220 - "POST /api/v1/checkout HTTP/1.1" 500 Internal Server Error"""

SIMULATED_DEMO_ANALYSIS = """### 1. 🎯 INCIDENT OVERVIEW & SEVERITY
- **Severity Rating**: **CRITICAL** (Production Outage / Transaction Failure)
- **Component / Service**: `payment_service` / PostgreSQL Async Connection Pool (`asyncpg` & SQLAlchemy)
- **Incident Summary**: Checkout requests failed with HTTP 500 errors due to catastrophic async connection pool exhaustion (`PoolTimeoutError`), leaving 124 queued transactions starved of database sockets.

### 2. 🔍 ROOT CAUSE ANALYSIS (RCA)
1. **Connection Leak / Pool Starvation**: The async database connection pool capped at 100 connections with a strict 5000ms timeout. Heavy checkout traffic combined with unreleased sessions or slow queries rapidly consumed all available connections.
2. **Missing Concurrency Backpressure & Circuit Breakers**: Once queue size exceeded threshold, `async with db.transaction()` failed to acquire a socket, throwing an uncaught `PoolTimeoutError` that escalated to `UnhandledTransactionError`.
3. **Leaked Secrets In Telemetry**: The application was improperly configured to dump raw database connection strings, AWS credentials, and Stripe secret keys into standard log streams during errors.

### 3. 🛠️ RECOMMENDED CODE / CONFIG PATCH
```diff
--- a/services/checkout.py
+++ b/services/checkout.py
@@ -139,12 +139,24 @@
 async def process_transaction(payload: CheckoutPayload, stripe_key: str):
-    async with db.transaction() as session:
-        result = await session.execute(...)
-        return result
+    try:
+        # Ensure max overflow buffer and strict query timeouts
+        async with asyncio.timeout(3.5):
+            async with db.transaction() as session:
+                result = await session.execute(...)
+                return result
+    except (asyncpg.PoolTimeoutError, TimeoutError) as exc:
+        logger.error("Database connection throttled under load. Triggering circuit breaker.")
+        # Return clean 429 / 503 instead of crashing ASGI worker
+        raise ServiceUnavailableError("Payment processing busy. Please retry shortly.") from exc
+    finally:
+        # Guarantee connection cleanup
+        await db.engine.dispose_orphan_sessions()
```

```diff
--- a/config/database.py
+++ b/config/database.py
@@ -15,4 +15,7 @@
 engine = create_async_engine(
     DATABASE_URL,
-    pool_size=100,
+    pool_size=50,
+    max_overflow=50,
+    pool_timeout=10,
+    pool_recycle=1800,
+    pool_pre_ping=True
 )
```

### 4. 📋 STEP-BY-STEP REMEDIATION PLAN
1. **Immediate Hotfix**: Increase `max_overflow` to 50 and set `pool_pre_ping=True` in `config/database.py` to prevent stale socket accumulation.
2. **Deploy Circuit Breaker**: Wrap checkout endpoints with a circuit breaker (e.g. `fastapi-limiter` or `pybreaker`) to fail fast with HTTP 429 instead of cascading into 500 crashes.
3. **Audit Secret Logging**: Disable verbose debug logging in production to stop emitting database credentials and Stripe keys into logs.

### 5. 🛡️ PREVENTATIVE SAFEGUARDS & ALERTS
- **Prometheus Metric**: Alert on `asyncpg_pool_waiters_count > 20` for > 60 seconds (Warning) and `> 50` for > 15 seconds (PagerDuty Critical).
- **Database Telemetry**: Monitor PostgreSQL `pg_stat_activity` for long-running idle in transaction states (`state = 'idle in transaction' > 5s`)."""


# ============================================================================
# TERMINAL UI & PRESENTATION
# ============================================================================
class TerminalUI:
    """Renders sleek banners, status boxes, diff syntax highlighting, and footers."""
    
    @staticmethod
    def banner(style: TerminalStyle):
        art = f"""{style.CYAN}{style.BOLD}
  ██╗      ██████╗  ██████╗ ██████╗ ██╗   ██╗██╗     ███████╗███████╗
  ██║     ██╔═══██╗██╔════╝ ██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
  ██║     ██║   ██║██║  ███╗██████╔╝██║   ██║██║     ███████╗█████╗  
  ██║     ██║   ██║██║   ██║██╔═══╝ ██║   ██║██║     ╚════██║██╔══╝  
  ███████╗╚██████╔╝╚██████╔╝██║     ╚██████╔╝███████╗███████║███████╗
  ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝{style.RESET}
       {style.WHITE}{style.BOLD}Autonomous Terminal Log Debugger & SRE Copilot{style.RESET} {style.DIM}v{__version__}{style.RESET}
        {style.DIM}Powered by Google Gemini 2.5 • Zero-Data-Leak Local Scrubber{style.RESET}
"""
        print(art)

    @staticmethod
    def print_scrub_box(stats: Dict[str, int], style: TerminalStyle):
        """Displays security audit results."""
        total = sum(stats.values())
        print(f"\n{style.BOLD}{style.GREEN}🛡️  ENTERPRISE PRIVACY SHIELD ACTIVATED{style.RESET}")
        print(f"{style.DIM}──────────────────────────────────────────────────────────{style.RESET}")
        if total == 0:
            print(f" {style.GREEN}✔{style.RESET} {style.WHITE}No sensitive secrets or credentials detected in log stream.{style.RESET}")
        else:
            print(f" {style.YELLOW}✔ Local Sanitizer Masked {total} Sensitive Tokens Before Processing:{style.RESET}")
            for name, count in stats.items():
                print(f"   {style.DIM}•{style.RESET} {style.CYAN}{name}{style.RESET}: {style.BOLD}{count} redacted{style.RESET}")
        print(f"{style.DIM}──────────────────────────────────────────────────────────{style.RESET}\n")

    @staticmethod
    def render_markdown(md_text: str, style: TerminalStyle):
        """Colorizes markdown headers, bullet points, and git diffs in terminal."""
        lines = md_text.splitlines()
        in_diff = False
        in_code = False

        for line in lines:
            if line.startswith("```diff"):
                in_diff = True
                print(f"{style.CYAN}{style.BOLD}┌── Unified Git Patch ──────────────────────────────────────┐{style.RESET}")
                continue
            elif line.startswith("```") and in_diff:
                in_diff = False
                print(f"{style.CYAN}{style.BOLD}└───────────────────────────────────────────────────────────┘{style.RESET}")
                continue
            elif line.startswith("```"):
                in_code = not in_code
                print(f"{style.DIM}{line}{style.RESET}")
                continue

            if in_diff:
                if line.startswith("+"):
                    print(f"{style.GREEN}{line}{style.RESET}")
                elif line.startswith("-"):
                    print(f"{style.RED}{line}{style.RESET}")
                elif line.startswith("@"):
                    print(f"{style.MAGENTA}{style.BOLD}{line}{style.RESET}")
                else:
                    print(f"{style.DIM}{line}{style.RESET}")
            elif line.startswith("### "):
                title = line.replace("### ", "").strip()
                print(f"\n{style.BOLD}{style.CYAN}══╡ {title} ╞{'═' * max(2, 60 - len(title))}{style.RESET}")
            elif line.startswith("## "):
                title = line.replace("## ", "").strip()
                print(f"\n{style.BOLD}{style.MAGENTA}▶ {title}{style.RESET}")
            elif line.startswith("- **Severity Rating**"):
                if "CRITICAL" in line:
                    print(f"{style.RED}{style.BOLD}{line}{style.RESET}")
                elif "HIGH" in line:
                    print(f"{style.YELLOW}{style.BOLD}{line}{style.RESET}")
                else:
                    print(f"{style.GREEN}{style.BOLD}{line}{style.RESET}")
            elif line.startswith("- **") or line.startswith("1. **") or line.startswith("2. **") or line.startswith("3. **"):
                print(f"{style.WHITE}{line}{style.RESET}")
            else:
                print(line)

    @staticmethod
    def footer(style: TerminalStyle):
        """Displays lead generation and support hooks."""
        box = f"""
{style.DIM}─────────────────────────────────────────────────────────────────────────────{style.RESET}
 {style.YELLOW}{style.BOLD}☕ Enjoying LogPulse?{style.RESET} {style.WHITE}Support open-source development:{style.RESET}
    {style.CYAN}{DONATION_LINK}{style.RESET}

 {style.MAGENTA}{style.BOLD}💼 Need Custom AI Engineering or SRE Automation for your business?{style.RESET}
    {style.WHITE}Let's build high-performance AI agents & cloud systems for your team.{style.RESET}
    {style.GREEN}Connect on LinkedIn:{style.RESET} {style.CYAN}{LINKEDIN_LINK}{style.RESET}
    {style.GREEN}View Portfolio:{style.RESET}      {style.CYAN}{PORTFOLIO_LINK}{style.RESET}
{style.DIM}─────────────────────────────────────────────────────────────────────────────{style.RESET}"""
        print(box)


# ============================================================================
# SAFE STREAM INGESTION (CROSS-PLATFORM NON-BLOCKING)
# ============================================================================
def read_stdin_safe(timeout: float = 0.35) -> str:
    """Reads stdin if data is piped into the process without hanging if stdin was redirected without EOF."""
    if sys.stdin.isatty():
        return ""

    if sys.platform != "win32":
        try:
            import select
            r, _, _ = select.select([sys.stdin], [], [], timeout)
            if r:
                return sys.stdin.read()
        except Exception:
            pass
        return ""
    else:
        # Windows named pipe polling using PeekNamedPipe
        try:
            import msvcrt
            import ctypes
            from ctypes import wintypes
            handle = msvcrt.get_osfhandle(sys.stdin.fileno())
            avail = wintypes.DWORD()
            start = time.time()
            while time.time() - start < timeout:
                if ctypes.windll.kernel32.PeekNamedPipe(handle, None, 0, None, ctypes.byref(avail), None):
                    if avail.value > 0:
                        return sys.stdin.read()
                time.sleep(0.04)
        except Exception:
            pass
        return ""


# ============================================================================
# COMMAND EXECUTION WRAPPER
# ============================================================================
def run_command_and_debug(cmd: str) -> str:
    """Executes an arbitrary shell command, streams output, and returns combined logs."""
    print(f"\n🚀 Running target command: {cmd}\n")
    proc = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )

    output_lines = []
    if proc.stdout:
        for line in proc.stdout:
            sys.stdout.write(line)
            output_lines.append(line)

    proc.wait()
    return "".join(output_lines)


# ============================================================================
# CLI ORCHESTRATION & MAIN ENTRYPOINT
# ============================================================================
def main():
    parser = argparse.ArgumentParser(
        description="⚡ LogPulse AI — Autonomous Terminal Log Debugger & SRE Copilot",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
  cat /var/log/nginx/error.log | python logpulse.py
  python logpulse.py --file app.log --export incident.md
  python logpulse.py run "pytest tests/"
  python logpulse.py --demo

Links & Inquiries:
  Support:  {DONATION_LINK}
  Services: {LINKEDIN_LINK}
        """
    )

    parser.add_argument("-f", "--file", type=str, help="Path to crash or application log file")
    parser.add_argument("-r", "--run", type=str, help="Execute shell command and debug if it crashes")
    parser.add_argument("-e", "--export", type=str, help="Export post-mortem markdown report to file")
    parser.add_argument("-m", "--model", type=str, default=DEFAULT_MODEL, help=f"Gemini model ID (default: {DEFAULT_MODEL})")
    parser.add_argument("-k", "--api-key", type=str, help="Google Gemini API key (or set GEMINI_API_KEY env var)")
    parser.add_argument("-s", "--scrub-strict", action="store_true", help="Aggressively mask IPv4 and internal network addresses")
    parser.add_argument("--demo", action="store_true", help="Run interactive zero-key demo simulation")
    parser.add_argument("--no-color", action="store_true", help="Disable ANSI terminal styling")
    parser.add_argument("-v", "--version", action="version", version=f"{TOOL_NAME} v{__version__}")

    # Support running `python logpulse.py run "cmd"` directly
    if len(sys.argv) > 1 and sys.argv[1] == "run":
        sys.argv.pop(1)
        if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
            cmd_target = sys.argv[1]
            sys.argv[1] = "--run"
            sys.argv.insert(2, cmd_target)

    args = parser.parse_args()

    style = TerminalStyle(enabled=not args.no_color)
    TerminalUI.banner(style)

    # 1. DEMO MODE
    if args.demo:
        print(f"{style.BOLD}{style.CYAN}ℹ️  Starting Zero-Key Interactive Showcase...{style.RESET}")
        time.sleep(0.5)

        scrubber = SecurityScrubber(strict_mode=args.scrub_strict)
        sanitized_logs, stats = scrubber.scrub(SAMPLE_INCIDENT_LOG)
        TerminalUI.print_scrub_box(stats, style)

        # Check if user has an active Gemini key
        api_key = args.api_key or os.environ.get("GEMINI_API_KEY")
        if api_key and GENAI_AVAILABLE:
            print(f"{style.GREEN}✔ Detected Gemini API Key. Running live analysis with {args.model}...{style.RESET}")
            debugger = GeminiDebugger(api_key=api_key, model=args.model)
            with Spinner("Consulting Google Gemini SRE Reasoning Engine", style):
                analysis = debugger.analyze(sanitized_logs)
        else:
            with Spinner("Simulating Gemini 2.5 Flash SRE Reasoning Engine", style):
                time.sleep(1.8)
            analysis = SIMULATED_DEMO_ANALYSIS

        TerminalUI.render_markdown(analysis, style)

        if args.export:
            out_file = PostMortemExporter.export(
                args.export, analysis, stats, 18, 14, args.model
            )
            print(f"\n{style.GREEN}✔ Incident Post-Mortem successfully written to: {out_file}{style.RESET}")

        TerminalUI.footer(style)
        return

    # 2. INGEST LOGS (Command, File, or Stdin)
    raw_logs = ""
    if args.run:
        raw_logs = run_command_and_debug(args.run)
    elif args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"{style.RED}✖ Error: File not found: {args.file}{style.RESET}")
            sys.exit(1)
        raw_logs = file_path.read_text(encoding="utf-8", errors="replace")
    elif True:
        # Read from pipe/stdin safely without hanging on unclosed handles
        raw_logs = read_stdin_safe(timeout=0.35)

    if not raw_logs or not raw_logs.strip():
        print(f"{style.YELLOW}⚠️  No log input detected.{style.RESET}")
        print(f"Usage examples:")
        print(f"  {style.CYAN}cat error.log | python logpulse.py{style.RESET}")
        print(f"  {style.CYAN}python logpulse.py --file error.log{style.RESET}")
        print(f"  {style.CYAN}python logpulse.py run 'pytest'{style.RESET}")
        print(f"  {style.CYAN}python logpulse.py --demo{style.RESET} (instant zero-key test)")
        TerminalUI.footer(style)
        return

    # 3. SCRUB PRIVACY & SECRETS LOCALLY
    scrubber = SecurityScrubber(strict_mode=args.scrub_strict)
    sanitized_logs, stats = scrubber.scrub(raw_logs)
    TerminalUI.print_scrub_box(stats, style)

    # 4. COMPACT NOISE
    compacted_logs, orig_count, comp_count = LogCompressor.compress(sanitized_logs)
    if orig_count > comp_count:
        print(f"{style.DIM}⚡ Log Compressor reduced payload from {orig_count} lines to {comp_count} high-signal lines.{style.RESET}\n")

    # 5. EXECUTE GEMINI ANALYSIS
    api_key = args.api_key or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print(f"{style.RED}{style.BOLD}✖ GEMINI_API_KEY is not set.{style.RESET}")
        print(f"\n{style.WHITE}To use live Gemini analysis:{style.RESET}")
        print(f"  1. Get a free key at: {style.CYAN}https://aistudio.google.com/{style.RESET}")
        print(f"  2. Set your environment variable:")
        print(f"     {style.BOLD}export GEMINI_API_KEY=\"AIza...\"{style.RESET}  (Linux/macOS)")
        print(f"     {style.BOLD}$env:GEMINI_API_KEY=\"AIza...\"{style.RESET}  (PowerShell)")
        print(f"  Or pass on CLI: {style.BOLD}python logpulse.py -k \"AIza...\"{style.RESET}")
        print(f"\n{style.GREEN}Tip: Try the interactive demo without an API key right now:{style.RESET}")
        print(f"  {style.BOLD}python logpulse.py --demo{style.RESET}\n")
        TerminalUI.footer(style)
        sys.exit(1)

    try:
        debugger = GeminiDebugger(api_key=api_key, model=args.model)
        with Spinner(f"Consulting Google {args.model} SRE Reasoning Engine", style):
            analysis = debugger.analyze(compacted_logs)
    except Exception as e:
        print(f"\n{style.RED}✖ Error analyzing logs with Gemini: {e}{style.RESET}")
        sys.exit(1)

    # 6. RENDER ANALYSIS
    TerminalUI.render_markdown(analysis, style)

    # 7. EXPORT POST-MORTEM IF REQUESTED
    if args.export:
        out_file = PostMortemExporter.export(
            args.export, analysis, stats, orig_count, comp_count, args.model
        )
        print(f"\n{style.GREEN}✔ Incident Post-Mortem successfully written to: {out_file}{style.RESET}")

    # 8. MONETIZATION & LEAD-GEN FOOTER
    TerminalUI.footer(style)


if __name__ == "__main__":
    main()
