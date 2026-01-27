import os
import shutil
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService

if browser_kind == "edge":
    opts = EdgeOptions()

    # ✅ Force 64-bit Edge if installed (prevents many crashes)
    edge64 = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
    if os.path.exists(edge64):
        opts.binary_location = edge64

    # ✅ Create a UNIQUE profile dir per run (avoid "profile in use" / locks)
    base = os.environ.get("TEMP", r"C:\Windows\Temp")
    profile_dir = os.path.join(base, f"edge_profile_{os.getpid()}")
    if os.path.exists(profile_dir):
        shutil.rmtree(profile_dir, ignore_errors=True)
    os.makedirs(profile_dir, exist_ok=True)

    opts.add_argument(f"--user-data-dir={profile_dir}")
    opts.add_argument("--no-first-run")
    opts.add_argument("--no-default-browser-check")
    opts.add_argument("--disable-extensions")
    opts.add_argument("--disable-background-networking")
    opts.add_argument("--disable-background-timer-throttling")
    opts.add_argument("--disable-renderer-backgrounding")
    opts.add_argument("--disable-features=Translate,BackForwardCache,AcceptCHFrame,MediaRouter")
    opts.add_argument("--remote-debugging-port=0")  # let it choose a free port

    if headless:
        opts.add_argument("--headless=new")
        opts.add_argument("--window-size=1920,1080")

    opts.add_argument("--disable-gpu")

    # Windows only; harmless if ignored
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--no-sandbox")

    # ✅ turn on driver logs (will print into Jenkins console)
    service = EdgeService(log_output=os.path.join(base, "msedgedriver.log"))

    return webdriver.Edge(service=service, options=opts)
