
#!/usr/bin/env python3
import os, sys
from dotenv import load_dotenv
load_dotenv()
from rich.console import Console
from aas.engine import Engine
from aas.orchestrator import Orchestrator
from aas.safety import Safety

console = Console()

def banner():
    console.print("""
    [bold green]
     ___       __     __          _       _
    /   | ____/ /__  / /_  ____  (_)___  (_)___  ___
   / /| |/ __  / _ \/ __ \/ __ \/ / __ \/ / __ \/ _ \
  / ___ / /_/ /  __/ /_/ / /_/ / / / / / / /  __/
 /_/  |_\__,_/\___/_.___/\____/_/_/ /_/_/_/ /_/\___/
    [/bold green]
    """)
def main():
    banner()
    token = os.getenv('AAS_AUTH_TOKEN')
    if not token:
        console.print('[red]AAS_AUTH_TOKEN missing. Create .env with token or use .env.example[/red]')
        sys.exit(1)
    args = sys.argv[1:]
    if not args:
        console.print('[yellow]Usage: python aas_cli.py <target1> [target2 ...][/yellow]')
        sys.exit(1)
    targets = args
    safe = Safety(token)
    if not safe.is_authorized():
        console.print('[red]Unauthorized token[/red]')
        sys.exit(1)
    engine = Engine(targets, config=safe.config)
    orchestrator = Orchestrator(engine, safe)
    orchestrator.run_all()
    console.print('[green]Scan complete. Reports in reports/[/green]')
if __name__ == '__main__':
    main()
