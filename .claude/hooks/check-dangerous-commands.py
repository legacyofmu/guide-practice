#!/usr/bin/env python3
import json
import re
import sys

data = json.load(sys.stdin)
cmd = data.get("tool_input", {}).get("command", "")

# heredoc 내용 제거 (커밋 메시지 등 텍스트 안의 오탐 방지)
cmd_clean = re.sub(r"<<[\"']?(\w+)[\"']?\n.*?\n\1", "", cmd, flags=re.DOTALL)

_RM_PREFIX = r"(?:^|[\n;&|(]\s*)(?:sudo\s+|nohup\s+|nice\s+\S+\s+)*"
PATTERNS = [
    # rm -rf: 명령 경계 이후, sudo 등 프리픽스 허용
    (_RM_PREFIX + r"rm\s+(?:\S+\s+)*-\S*r\S*f\b"
     r"|" + _RM_PREFIX + r"rm\s+(?:\S+\s+)*-\S*f\S*r\b"
     r"|" + _RM_PREFIX + r"rm\s+--no-preserve-root\b",
     "rm -rf"),
    (r"\bDROP\s+TABLE\b|\bDROP\s+DATABASE\b|\bTRUNCATE\s+TABLE\b",
     "destructive SQL (DROP/TRUNCATE)"),
    (r"\bgit\s+push\b.*?(?:--force|-f)(?:\s|$)",
     "git push --force"),
]

for pattern, label in PATTERNS:
    if re.search(pattern, cmd_clean, re.IGNORECASE | re.MULTILINE):
        print(json.dumps({
            "decision": "block",
            "reason": f"[위험한 명령 차단] {label}: {cmd.splitlines()[0]}",
        }))
        sys.exit(0)
