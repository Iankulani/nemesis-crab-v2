#!/usr/bin/env bash
# ============================================================
# NEMESIS-CRAB-V2 - Bash Installer (Linux / macOS)
# ============================================================
set -e

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
BLUE='\033[0;34m'; MAGENTA='\033[0;35m'; CYAN='\033[0;36m'
BOLD='\033[1m'; RESET='\033[0m'

APP_NAME="NEMESIS-CRAB-V2"
INSTALL_DIR="${INSTALL_DIR:-$HOME/.nemesis-crab-v2}"
VENV_DIR="$INSTALL_DIR/venv"
SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

log()  { echo -e "${GREEN}[+]${RESET} $*"; }
warn() { echo -e "${YELLOW}[!]${RESET} $*"; }
err()  { echo -e "${RED}[x]${RESET} $*" >&2; }
info() { echo -e "${BLUE}[i]${RESET} $*"; }

banner() {
  echo -e "${MAGENTA}${BOLD}"
  cat <<'EOF'
╔══════════════════════════════════════════════════════════╗
║   🦀 NEMESIS-CRAB-V2 - Installer (Linux / macOS)         ║
╚══════════════════════════════════════════════════════════╝
EOF
  echo -e "${RESET}"
}

detect_os() {
  case "$(uname -s)" in
    Linux*)  OS="linux";;
    Darwin*) OS="macos";;
    *)       OS="unknown";;
  esac
  info "Detected OS: $OS"
}

detect_pkg_mgr() {
  if   command -v apt-get >/dev/null 2>&1; then PKG="apt"
  elif command -v dnf     >/dev/null 2>&1; then PKG="dnf"
  elif command -v yum     >/dev/null 2>&1; then PKG="yum"
  elif command -v pacman  >/dev/null 2>&1; then PKG="pacman"
  elif command -v brew    >/dev/null 2>&1; then PKG="brew"
  else PKG="none"; fi
  info "Package manager: $PKG"
}

need_sudo() {
  if [ "$(id -u)" -ne 0 ]; then echo "sudo"; else echo ""; fi
}

install_system_deps() {
  local SUDO; SUDO="$(need_sudo)"
  case "$PKG" in
    apt)
      log "Installing system packages via apt..."
      $SUDO apt-get update -y
      $SUDO apt-get install -y --no-install-recommends \
        python3 python3-pip python3-venv python3-dev \
        build-essential git curl wget \
        iputils-ping net-tools traceroute dnsutils \
        nmap netcat-openbsd whois \
        libpcap-dev libssl-dev libffi-dev \
        libjpeg-dev zlib1g-dev \
        libx11-dev libxtst-dev libxext-dev \
        chromium chromium-driver \
        docker.io docker-compose-plugin 2>/dev/null || true
      ;;
    dnf|yum)
      log "Installing system packages via $PKG..."
      $SUDO $PKG install -y \
        python3 python3-pip python3-devel \
        gcc make git curl wget \
        iputils traceroute bind-utils \
        nmap nc whois \
        libpcap-devel openssl-devel libffi-devel \
        libjpeg-turbo-devel zlib-devel \
        libX11-devel libXtst-devel libXext-devel \
        chromium chromedriver \
        docker docker-compose 2>/dev/null || true
      ;;
    pacman)
      log "Installing system packages via pacman..."
      $SUDO pacman -Sy --noconfirm \
        python python-pip base-devel git curl wget \
        iputils traceroute bind-tools \
        nmap gnu-netcat whois \
        libpcap openssl libffi \
        libjpeg-turbo zlib \
        libx11 libxtst libxext \
        chromium chromedriver \
        docker docker-compose 2>/dev/null || true
      ;;
    brew)
      log "Installing system packages via brew..."
      brew update || true
      brew install python@3.11 git curl wget \
        nmap whois \
        libpcap openssl@3 libffi \
        jpeg zlib \
        --quiet || true
      ;;
    *)
      warn "Unknown package manager — skipping system dependency installation."
      warn "Install manually: python3, pip, nmap, whois, curl, wget, netcat, docker"
      ;;
  esac
}

install_venv() {
  log "Creating installation directory: $INSTALL_DIR"
  mkdir -p "$INSTALL_DIR"
  log "Creating Python virtual environment..."
  python3 -m venv "$VENV_DIR"
  # shellcheck disable=SC1091
  source "$VENV_DIR/bin/activate"
  log "Upgrading pip / setuptools / wheel..."
  pip install --upgrade pip setuptools wheel
}

install_python_deps() {
  log "Installing Python dependencies..."
  if [ -f "$SRC_DIR/requirements.txt" ]; then
    pip install -r "$SRC_DIR/requirements.txt"
  else
    warn "requirements.txt not found — installing from PyPI list"
    pip install requests psutil colorama cryptography paramiko \
                scapy python-whois dnspython pyyaml pyperclip \
                reportlab matplotlib seaborn numpy pandas \
                pyinstaller tqdm tabulate
  fi
}

copy_sources() {
  log "Copying source files to $INSTALL_DIR"
  cp -f "$SRC_DIR/nemesis_crab_v2.py" "$INSTALL_DIR/" 2>/dev/null || \
    warn "nemesis_crab_v2.py not found in $SRC_DIR"
  for f in requirements.txt requirements-check.py test-command.py health.py; do
    [ -f "$SRC_DIR/$f" ] && cp -f "$SRC_DIR/$f" "$INSTALL_DIR/"
  done
  mkdir -p "$INSTALL_DIR/.nemesis_crab_v2"
}

create_launcher() {
  log "Creating launcher: /usr/local/bin/nemesis-crab"
  local SUDO; SUDO="$(need_sudo)"
  cat > /tmp/nemesis-crab <<EOF
#!/usr/bin/env bash
source "$VENV_DIR/bin/activate"
cd "$INSTALL_DIR"
exec python3 "$INSTALL_DIR/nemesis_crab_v2.py" "\$@"
EOF
  chmod +x /tmp/nemesis-crab
  $SUDO mv /tmp/nemesis-crab /usr/local/bin/nemesis-crab 2>/dev/null || \
    { mkdir -p "$HOME/.local/bin"; mv /tmp/nemesis-crab "$HOME/.local/bin/nemesis-crab"; \
      warn "Installed to ~/.local/bin — ensure it is on your PATH"; }
}

create_health_launcher() {
  cat > /tmp/nemesis-health <<EOF
#!/usr/bin/env bash
source "$VENV_DIR/bin/activate"
exec python3 "$INSTALL_DIR/health.py" "\$@"
EOF
  chmod +x /tmp/nemesis-health
  local SUDO; SUDO="$(need_sudo)"
  $SUDO mv /tmp/nemesis-health /usr/local/bin/nemesis-health 2>/dev/null || \
    mv /tmp/nemesis-health "$HOME/.local/bin/nemesis-health"
}

create_systemd_service() {
  if [ "$OS" != "linux" ]; then return; fi
  if ! command -v systemctl >/dev/null 2>&1; then return; fi
  local SUDO; SUDO="$(need_sudo)"
  cat > /tmp/nemesis-crab.service <<EOF
[Unit]
Description=NEMESIS-CRAB-V2 Cybersecurity Platform
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$INSTALL_DIR
ExecStart=$VENV_DIR/bin/python $INSTALL_DIR/nemesis_crab_v2.py
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF
  $SUDO mv /tmp/nemesis-crab.service /etc/systemd/system/nemesis-crab.service
  $SUDO systemctl daemon-reload
  info "systemd unit installed (enable with: sudo systemctl enable --now nemesis-crab)"
}

verify() {
  log "Verifying installation..."
  # shellcheck disable=SC1091
  source "$VENV_DIR/bin/activate"
  python3 "$INSTALL_DIR/requirements-check.py" || true
  echo
  log "Running health check..."
  python3 "$INSTALL_DIR/health.py" --json || true
}

summary() {
  echo
  echo -e "${GREEN}${BOLD}════════════════════════════════════════════${RESET}"
  echo -e "${GREEN}${BOLD}  🎉 Installation Complete!${RESET}"
  echo -e "${GREEN}${BOLD}════════════════════════════════════════════${RESET}"
  echo -e "  Install dir : ${CYAN}$INSTALL_DIR${RESET}"
  echo -e "  Venv        : ${CYAN}$VENV_DIR${RESET}"
  echo -e "  Launcher    : ${CYAN}nemesis-crab${RESET}"
  echo -e "  Health      : ${CYAN}nemesis-health${RESET}"
  echo
  echo -e "  Run: ${BOLD}nemesis-crab${RESET}"
  echo -e "  Web: ${BOLD}http://localhost:5000${RESET}"
  echo -e "  Help: ${BOLD}nemesis-crab${RESET} then type ${BOLD}help${RESET}"
  echo
}

main() {
  banner
  detect_os
  detect_pkg_mgr
  install_system_deps || warn "Some system deps failed — continuing"
  install_venv
  install_python_deps
  copy_sources
  create_launcher
  create_health_launcher
  create_systemd_service
  verify
  summary
}

main "$@"
