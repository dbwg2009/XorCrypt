<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SecureVault — Encrypted Messaging & Storage</title>
<style>
  :root {
    --bg: #1a1a2e;
    --surface: #252540;
    --surface-hi: #2d2d4d;
    --surface-hover: #313157;
    --border: rgba(108, 99, 255, 0.18);
    --border-soft: rgba(255, 255, 255, 0.06);
    --accent: #6c63ff;
    --accent-hi: #8a83ff;
    --accent-dim: rgba(108, 99, 255, 0.15);
    --accent2: #43c9a0;
    --accent2-hi: #5fdcb6;
    --warn: #e05c5c;
    --warn-hi: #f07878;
    --gold: #e0a030;
    --fg: #e8e8f0;
    --fg-dim: #7a7a99;
    --fg-hi: #ffffff;
    --mono: ui-monospace, "SF Mono", "Cascadia Mono", "JetBrains Mono", Consolas, "Liberation Mono", monospace;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { height: 100%; }
  body {
    background:
      radial-gradient(circle at 18% -10%, rgba(108, 99, 255, 0.18), transparent 45%),
      radial-gradient(circle at 90% 110%, rgba(67, 201, 160, 0.12), transparent 45%),
      var(--bg);
    color: var(--fg);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Inter", system-ui, sans-serif;
    font-size: 14px;
    -webkit-font-smoothing: antialiased;
    min-height: 100vh;
    overflow: hidden;
  }

  button, input, textarea, select { font-family: inherit; color: inherit; }
  textarea { resize: none; }

  .container {
    display: flex;
    height: 100vh;
  }

  /* ── Sidebar ── */
  .sidebar {
    width: 280px;
    background: var(--surface);
    border-right: 1px solid var(--border-soft);
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  .sidebar-header {
    padding: 16px;
    border-bottom: 1px solid var(--border-soft);
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .logo-mini {
    display: flex;
    align-items: center;
    gap: 10px;
    font-weight: 600;
    font-size: 15px;
  }

  .logo-icon {
    width: 28px;
    height: 28px;
    border-radius: 7px;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    display: grid;
    place-items: center;
    font-size: 14px;
  }

  .user-btn {
    width: 32px;
    height: 32px;
    border-radius: 8px;
    background: var(--surface-hi);
    border: 1px solid var(--border-soft);
    cursor: pointer;
    display: grid;
    place-items: center;
    font-weight: 600;
    font-size: 12px;
    transition: all 0.15s;
  }

  .user-btn:hover {
    background: var(--surface-hover);
  }

  .tabs {
    display: flex;
    gap: 0;
    padding: 8px;
    border-bottom: 1px solid var(--border-soft);
  }

  .tab-btn {
    flex: 1;
    padding: 8px 12px;
    border: none;
    background: transparent;
    color: var(--fg-dim);
    cursor: pointer;
    font-size: 12px;
    border-radius: 6px;
    transition: all 0.15s;
  }

  .tab-btn:hover {
    background: var(--surface-hi);
  }

  .tab-btn.active {
    background: var(--accent-dim);
    color: var(--accent-hi);
    font-weight: 600;
  }

  .sidebar-content {
    flex: 1;
    overflow-y: auto;
    padding: 8px;
  }

  .list-item {
    padding: 10px 12px;
    margin-bottom: 6px;
    background: var(--surface-hi);
    border: 1px solid transparent;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.15s;
    font-size: 13px;
  }

  .list-item:hover {
    background: var(--surface-hover);
    border-color: var(--border-soft);
  }

  .list-item.active {
    background: var(--accent-dim);
    color: var(--accent-hi);
    border-color: var(--accent);
  }

  .list-empty {
    padding: 24px 12px;
    text-align: center;
    color: var(--fg-dim);
    font-size: 12px;
  }

  /* ── Main content ── */
  .main {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  .auth-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: var(--bg);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
  }

  .auth-card {
    background: var(--surface);
    border: 1px solid var(--border-soft);
    border-radius: 14px;
    padding: 32px;
    max-width: 420px;
    width: 90%;
  }

  .auth-card h2 {
    font-size: 24px;
    margin-bottom: 8px;
  }

  .auth-card p {
    color: var(--fg-dim);
    font-size: 13px;
    margin-bottom: 24px;
  }

  .auth-form input {
    width: 100%;
    padding: 10px 12px;
    background: var(--surface-hi);
    border: 1px solid var(--border-soft);
    border-radius: 8px;
    color: var(--fg);
    margin-bottom: 12px;
    font-size: 14px;
  }

  .auth-form input:focus {
    outline: none;
    border-color: var(--accent);
    box-shadow: 0 0 0 3px var(--accent-dim);
  }

  .auth-tabs {
    display: flex;
    gap: 12px;
    margin-bottom: 20px;
  }

  .auth-tab {
    flex: 1;
    padding: 10px;
    background: var(--surface-hi);
    border: 1px solid transparent;
    border-radius: 8px;
    cursor: pointer;
    color: var(--fg-dim);
    font-weight: 500;
    transition: all 0.15s;
  }

  .auth-tab.active {
    background: var(--accent);
    color: white;
  }

  .auth-submit {
    width: 100%;
    padding: 12px;
    background: linear-gradient(135deg, var(--accent), var(--accent-hi));
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-weight: 600;
    transition: all 0.15s;
  }

  .auth-submit:hover {
    box-shadow: 0 0 12px rgba(108, 99, 255, 0.5);
  }

  .auth-submit:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  .hidden {
    display: none !important;
  }

  /* ── Content panels ── */
  .panel {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  .panel-header {
    padding: 16px;
    border-bottom: 1px solid var(--border-soft);
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .panel-title {
    font-size: 15px;
    font-weight: 600;
  }

  .panel-content {
    flex: 1;
    overflow-y: auto;
    padding: 16px;
  }

  .panel-footer {
    padding: 16px;
    border-top: 1px solid var(--border-soft);
  }

  .input-group {
    display: flex;
    gap: 8px;
    margin-bottom: 12px;
  }

  .input-group input,
  .input-group textarea {
    flex: 1;
    padding: 10px 12px;
    background: var(--surface-hi);
    border: 1px solid var(--border-soft);
    border-radius: 8px;
    color: var(--fg);
    font-size: 13px;
  }

  .input-group input:focus,
  .input-group textarea:focus {
    outline: none;
    border-color: var(--accent);
    box-shadow: 0 0 0 3px var(--accent-dim);
  }

  .btn {
    padding: 10px 16px;
    background: var(--accent);
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-weight: 600;
    transition: all 0.15s;
    font-size: 13px;
  }

  .btn:hover {
    box-shadow: 0 0 12px rgba(108, 99, 255, 0.5);
  }

  .btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  .btn.secondary {
    background: var(--surface-hi);
    color: var(--fg);
    border: 1px solid var(--border-soft);
  }

  .btn.secondary:hover {
    background: var(--surface-hover);
  }

  /* ── Vault items ── */
  .vault-item {
    padding: 12px;
    background: var(--surface-hi);
    border: 1px solid var(--border-soft);
    border-radius: 8px;
    margin-bottom: 8px;
    cursor: pointer;
    transition: all 0.15s;
  }

  .vault-item:hover {
    border-color: var(--accent);
    background: var(--surface-hover);
  }

  .vault-item-label {
    font-weight: 600;
    font-size: 13px;
    margin-bottom: 4px;
  }

  .vault-item-meta {
    font-size: 11px;
    color: var(--fg-dim);
  }

  .vault-item.pinned {
    border-color: var(--gold);
    background: rgba(224, 160, 48, 0.1);
  }

  /* ── Messages ── */
  .message {
    margin-bottom: 12px;
    padding: 12px;
    border-radius: 8px;
    background: var(--surface-hi);
    border-left: 3px solid var(--accent);
  }

  .message.other {
    border-left-color: var(--accent2);
  }

  .message-sender {
    font-size: 11px;
    color: var(--fg-dim);
    margin-bottom: 4px;
    font-weight: 600;
  }

  .message-text {
    font-size: 13px;
    line-height: 1.4;
    word-break: break-word;
  }

  .message-time {
    font-size: 10px;
    color: var(--fg-dim);
    margin-top: 6px;
  }

  /* ── History ── */
  .history-item {
    padding: 10px;
    background: var(--surface-hi);
    border-radius: 8px;
    margin-bottom: 6px;
    font-size: 12px;
  }

  .history-item-type {
    color: var(--accent2);
    font-weight: 600;
    margin-bottom: 2px;
  }

  .history-item-text {
    color: var(--fg-dim);
    font-family: var(--mono);
    word-break: break-all;
  }

  .history-item-time {
    font-size: 10px;
    color: var(--fg-dim);
    margin-top: 4px;
  }

  /* ── Toasts ── */
  #toasts {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 999;
    max-width: 380px;
  }

  .toast {
    background: var(--surface);
    border: 1px solid var(--border-soft);
    border-radius: 10px;
    padding: 14px 16px;
    margin-bottom: 10px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
    animation: toast-in 0.3s ease;
  }

  .toast.info {
    border-color: var(--accent);
  }

  .toast.error {
    border-color: var(--warn);
  }

  .toast.success {
    border-color: var(--accent2);
  }

  .toast.fade-out {
    animation: toast-out 0.4s ease forwards;
  }

  .t-title {
    color: var(--fg-hi);
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 4px;
  }

  .t-body {
    color: var(--fg-dim);
    font-size: 12px;
    line-height: 1.4;
  }

  @keyframes toast-in {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }

  @keyframes toast-out {
    from { opacity: 1; transform: translateY(0); }
    to { opacity: 0; transform: translateY(20px); }
  }

  @media (max-width: 768px) {
    .sidebar {
      width: 100%;
      max-height: 40vh;
    }
    .container {
      flex-direction: column;
    }
  }
</style>
</head>
<body>

<div id="auth-overlay" class="auth-overlay">
  <div class="auth-card">
    <h2>SecureVault</h2>
    <p>Encrypted messaging & storage</p>
    <div class="auth-tabs">
      <div class="auth-tab active" id="tab-login" onclick="setAuthMode('login')">Sign In</div>
      <div class="auth-tab" id="tab-register" onclick="setAuthMode('register')">Register</div>
    </div>
    <div class="auth-form">
      <input type="email" id="auth-email" placeholder="Email address" autocomplete="email">
      <input type="password" id="auth-pass" placeholder="Passphrase" autocomplete="current-password">
      <div id="reg-token-field" style="display:none;">
        <input type="text" id="auth-token" placeholder="Registration token (optional)" autocomplete="off">
      </div>
      <button class="auth-submit" id="auth-submit">Sign in</button>
    </div>
  </div>
</div>

<div id="app" class="hidden">
  <div class="container">
    <div class="sidebar">
      <div class="sidebar-header">
        <div class="logo-mini">
          <div class="logo-icon">🔐</div>
          <span>SecureVault</span>
        </div>
        <button class="user-btn" id="user-avatar" onclick="showLogout()" title="Logout"></button>
      </div>

      <div class="tabs">
        <button class="tab-btn active" onclick="switchSidebarTab('vault')">Vault</button>
        <button class="tab-btn" onclick="switchSidebarTab('messages')">Messages</button>
        <button class="tab-btn" onclick="switchSidebarTab('history')">History</button>
      </div>

      <div class="sidebar-content">
        <div id="vault-list-panel">
          <input type="text" id="vault-search" placeholder="Search vault..." style="width:100%; padding:8px; background:var(--surface-hi); border:1px solid var(--border-soft); border-radius:6px; color:var(--fg); margin-bottom:8px;" oninput="renderVault()">
          <div id="vault-list" class="list-empty">Loading vault...</div>
        </div>
        <div id="messages-list-panel" style="display:none;">
          <div id="thread-list" class="list-empty">Loading messages...</div>
        </div>
        <div id="history-list-panel" style="display:none;">
          <div id="history-list" class="list-empty">No history yet</div>
        </div>
      </div>
    </div>

    <div class="main">
      <div id="vault-panel" class="panel">
        <div class="panel-header">
          <div class="panel-title">Vault</div>
          <button class="btn secondary" onclick="showNewVaultForm()">+ New</button>
        </div>
        <div class="panel-content">
          <div id="vault-detail"></div>
        </div>
      </div>

      <div id="messages-panel" class="panel hidden">
        <div class="panel-header">
          <div class="panel-title" id="thread-title">Messages</div>
        </div>
        <div class="panel-content">
          <div id="message-list"></div>
        </div>
        <div class="panel-footer">
          <div class="input-group">
            <input type="text" id="recipient-lookup" placeholder="Find user by email..." onkeypress="handleLookupKeypress(event)" style="margin-bottom:0;">
            <button class="btn" onclick="lookupUser()" style="width:auto;">Find</button>
          </div>
          <div class="input-group">
            <input type="text" id="message-input" placeholder="Type a message..." onkeypress="handleMessageKeypress(event)" style="margin-bottom:0;">
            <button class="btn" onclick="sendMessage()" style="width:auto;">Send</button>
          </div>
        </div>
      </div>

      <div id="cipher-panel" class="panel hidden">
        <div class="panel-header">
          <div class="panel-title">Cipher Tool</div>
        </div>
        <div class="panel-content">
          <div style="margin-bottom:16px;">
            <label style="display:block; margin-bottom:8px; color:var(--fg-dim); font-size:12px;">Key</label>
            <input type="password" id="cipher-key" placeholder="Enter encryption key" style="width:100%; padding:10px; background:var(--surface-hi); border:1px solid var(--border-soft); border-radius:6px; color:var(--fg);">
          </div>
          <div style="margin-bottom:16px;">
            <label style="display:block; margin-bottom:8px; color:var(--fg-dim); font-size:12px;">Input</label>
            <textarea id="cipher-input" placeholder="Text to encrypt/decrypt" style="width:100%; height:100px; padding:10px; background:var(--surface-hi); border:1px solid var(--border-soft); border-radius:6px; color:var(--fg); font-family:var(--mono);"></textarea>
          </div>
          <div class="input-group">
            <button class="btn" onclick="cipherEncrypt()" style="flex:1;">🔒 Encrypt</button>
            <button class="btn secondary" onclick="cipherDecrypt()" style="flex:1;">🔓 Decrypt</button>
          </div>
          <div style="margin-top:16px;">
            <label style="display:block; margin-bottom:8px; color:var(--fg-dim); font-size:12px;">Output</label>
            <textarea id="cipher-output" placeholder="Result will appear here" readonly style="width:100%; height:100px; padding:10px; background:var(--surface-hi); border:1px solid var(--border-soft); border-radius:6px; color:var(--fg); font-family:var(--mono);"></textarea>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div id="toasts"></div>

<script>
"use strict";

/* ─────────────────────────────────────────────────────────────
   CRYPTO CORE
   ───────────────────────────────────────────────────────────── */
const SALT_LEN = 16;
const ITERATIONS = 200_000;
const KEY_LEN = 32;
const subtle = crypto.subtle;

async function deriveKeys(password, salt) {
  const baseKey = await subtle.importKey(
    "raw",
    new TextEncoder().encode(password),
    { name: "PBKDF2" },
    false,
    ["deriveBits"]
  );
  const bits = await subtle.deriveBits(
    { name: "PBKDF2", salt, iterations: ITERATIONS, hash: "SHA-256" },
    baseKey,
    KEY_LEN * 2 * 8
  );
  const km = new Uint8Array(bits);
  return [km.slice(0, KEY_LEN), km.slice(KEY_LEN)];
}

async function deriveAuthHash(password, salt) {
  // Derive a 64-byte key from password+salt using PBKDF2
  // The first 32 bytes will be used as the authHash
  const baseKey = await subtle.importKey(
    "raw",
    new TextEncoder().encode(password),
    { name: "PBKDF2" },
    false,
    ["deriveBits"]
  );
  const bits = await subtle.deriveBits(
    { name: "PBKDF2", salt, iterations: ITERATIONS, hash: "SHA-256" },
    baseKey,
    KEY_LEN * 8  // 32 bytes
  );
  return bytesToHex(new Uint8Array(bits));
}

async function keystream(encKey, salt, length) {
  const out = new Uint8Array(length);
  const buf = new Uint8Array(encKey.length + salt.length + 4);
  buf.set(encKey, 0);
  buf.set(salt, encKey.length);
  const counterView = new DataView(buf.buffer, encKey.length + salt.length, 4);
  let counter = 0;
  let off = 0;
  while (off < length) {
    counterView.setUint32(0, counter, false);
    const digest = new Uint8Array(await subtle.digest("SHA-256", buf));
    const take = Math.min(digest.length, length - off);
    out.set(digest.subarray(0, take), off);
    off += take;
    counter += 1;
  }
  return out;
}

async function hmacSha256(key, data) {
  const k = await subtle.importKey(
    "raw", key, { name: "HMAC", hash: "SHA-256" }, false, ["sign"]
  );
  return new Uint8Array(await subtle.sign("HMAC", k, data));
}

function bytesToHex(b) {
  let s = "";
  for (let i = 0; i < b.length; i++) s += b[i].toString(16).padStart(2, "0");
  return s;
}

function hexToBytes(hex) {
  if (hex.length % 2) throw new Error("bad hex");
  const out = new Uint8Array(hex.length / 2);
  for (let i = 0; i < out.length; i++) {
    const v = parseInt(hex.substr(i * 2, 2), 16);
    if (Number.isNaN(v)) throw new Error("bad hex");
    out[i] = v;
  }
  return out;
}

function ctEqual(a, b) {
  if (a.length !== b.length) return false;
  let r = 0;
  for (let i = 0; i < a.length; i++) r |= a[i] ^ b[i];
  return r === 0;
}

async function encryptText(plaintext, password) {
  const data = new TextEncoder().encode(plaintext);
  const salt = crypto.getRandomValues(new Uint8Array(SALT_LEN));
  const [encKey, macKey] = await deriveKeys(password, salt);
  const ks = await keystream(encKey, salt, data.length);
  const ct = new Uint8Array(data.length);
  for (let i = 0; i < data.length; i++) ct[i] = data[i] ^ ks[i];
  const macInput = new Uint8Array(salt.length + ct.length);
  macInput.set(salt, 0);
  macInput.set(ct, salt.length);
  const tag = await hmacSha256(macKey, macInput);
  return `${bytesToHex(salt)}:${bytesToHex(ct)}:${bytesToHex(tag)}`;
}

async function decryptToken(token, password) {
  const parts = token.trim().split(":");
  if (parts.length !== 3) return { ok: false, err: "invalid format" };
  let salt, ct, tag;
  try {
    salt = hexToBytes(parts[0]);
    ct = hexToBytes(parts[1]);
    tag = hexToBytes(parts[2]);
  } catch {
    return { ok: false, err: "decryption failed" };
  }
  if (salt.length !== SALT_LEN) return { ok: false, err: "invalid format" };
  const [encKey, macKey] = await deriveKeys(password, salt);
  const macInput = new Uint8Array(salt.length + ct.length);
  macInput.set(salt, 0);
  macInput.set(ct, salt.length);
  const expected = await hmacSha256(macKey, macInput);
  if (!ctEqual(tag, expected)) return { ok: false, err: "wrong key or tampered" };
  const ks = await keystream(encKey, salt, ct.length);
  const pt = new Uint8Array(ct.length);
  for (let i = 0; i < ct.length; i++) pt[i] = ct[i] ^ ks[i];
  try {
    return { ok: true, text: new TextDecoder("utf-8", { fatal: false }).decode(pt) };
  } catch {
    return { ok: false, err: "decryption failed" };
  }
}

/* ─────────────────────────────────────────────────────────────
   STATE & GLOBALS
   ───────────────────────────────────────────────────────────── */
let currentUser = null;
let masterPass = null;
let authMode = "login";
let vaultItems = [];
let threads = [];
let history = [];
let currentThreadId = null;
let currentPeerId = null;
let currentVaultItemId = null;

/* ─────────────────────────────────────────────────────────────
   UTILITY FUNCTIONS
   ───────────────────────────────────────────────────────────── */
function toast(body, kind = "info", title = null) {
  const el = document.createElement("div");
  el.className = `toast ${kind}`;
  el.innerHTML = `${title ? `<div class="t-title">${title}</div>` : ""}<div class="t-body"></div>`;
  el.querySelector(".t-body").textContent = body;
  document.getElementById("toasts").appendChild(el);
  setTimeout(() => {
    el.classList.add("fade-out");
    el.addEventListener("animationend", () => el.remove(), { once: true });
  }, 2400);
}

function escHtml(str) {
  const div = document.createElement("div");
  div.textContent = str;
  return div.innerHTML;
}

function relTime(ts) {
  if (!ts) return "now";
  const now = Math.floor(Date.now() / 1000);
  const diff = now - ts;
  if (diff < 60) return "now";
  if (diff < 3600) return Math.floor(diff / 60) + "m ago";
  if (diff < 86400) return Math.floor(diff / 3600) + "h ago";
  return Math.floor(diff / 86400) + "d ago";
}

async function api(method, path, body = null) {
  const opts = {
    method,
    credentials: "include",
    headers: { "Content-Type": "application/json" },
  };
  if (body !== null) opts.body = JSON.stringify(body);
  const res = await fetch(path, opts);
  
  const contentType = res.headers.get("content-type") || "";
  if (res.status === 204) return null;
  
  if (!contentType.includes("application/json")) {
    const text = await res.text();
    throw new Error(`Server error: ${res.status}`);
  }
  
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(data.detail || data.error || `Error: ${res.status}`);
  return data;
}

/* ─────────────────────────────────────────────────────────────
   AUTH FUNCTIONS
   ───────────────────────────────────────────────────────────── */
function setAuthMode(mode) {
  authMode = mode;
  document.getElementById("tab-login").classList.toggle("active", mode === "login");
  document.getElementById("tab-register").classList.toggle("active", mode === "register");
  document.getElementById("auth-submit").textContent = mode === "login" ? "Sign in" : "Create account";
  document.getElementById("reg-token-field").style.display = mode === "register" ? "block" : "none";
  document.getElementById("auth-pass").autocomplete = mode === "login" ? "current-password" : "new-password";
}

async function doAuth() {
  const email = document.getElementById("auth-email").value.trim();
  const pass = document.getElementById("auth-pass").value;
  
  if (!email || !pass) {
    toast("Email and passphrase required", "error");
    return;
  }

  const btn = document.getElementById("auth-submit");
  btn.disabled = true;
  btn.textContent = "Working…";

  try {
    // Step 1: Get salt from preflight
    const preflight = await api("POST", "/api/auth/preflight", { email });
    const saltHex = preflight.authSalt;
    const salt = hexToBytes(saltHex);
    
    // Step 2: Derive authHash from password
    const authHash = await deriveAuthHash(pass, salt);

    let result;
    
    if (authMode === "login") {
      result = await api("POST", "/api/auth/login", {
        email,
        authHash
      });
    } else {
      const token = document.getElementById("auth-token").value;
      result = await api("POST", "/api/auth/register", {
        email,
        authSalt: saltHex,
        authHash,
        registrationToken: token || null
      });
    }

    masterPass = pass;
    currentUser = result;
    
    document.getElementById("auth-overlay").style.display = "none";
    document.getElementById("app").classList.remove("hidden");
    document.getElementById("user-avatar").textContent = (currentUser.email || "?")[0].toUpperCase();
    
    loadVault();
    loadHistory();
    loadThreads();
    toast("Logged in successfully", "success", "✓");
  } catch (e) {
    toast(e.message, "error", "Auth failed");
  } finally {
    btn.disabled = false;
    btn.textContent = authMode === "login" ? "Sign in" : "Create account";
  }
}

function doLogout() {
  // Clear all decrypted data from DOM
  document.getElementById("vault-list").innerHTML = "";
  document.getElementById("thread-list").innerHTML = "";
  document.getElementById("message-list").innerHTML = "";
  document.getElementById("history-list").innerHTML = "";
  document.getElementById("vault-detail").innerHTML = "";
  
  currentUser = null;
  masterPass = null;
  vaultItems = [];
  threads = [];
  history = [];
  currentThreadId = null;
  currentPeerId = null;
  currentVaultItemId = null;
  
  api("POST", "/api/auth/logout").catch(console.error);
  
  document.getElementById("auth-overlay").style.display = "flex";
  document.getElementById("app").classList.add("hidden");
  document.getElementById("auth-email").value = "";
  document.getElementById("auth-pass").value = "";
  toast("Logged out", "info");
}

function showLogout() {
  if (confirm("Logout?")) {
    doLogout();
  }
}

/* ─────────────────────────────────────────────────────────────
   VAULT FUNCTIONS
   ───────────────────────────────────────────────────────────── */
async function loadVault() {
  if (!currentUser) return;
  try {
    const items = await api("GET", "/api/vault");
    vaultItems = items || [];
    renderVault();
  } catch (e) {
    toast(e.message, "error", "Vault");
  }
}

async function renderVault() {
  const query = document.getElementById("vault-search")?.value.toLowerCase() || "";
  const list = document.getElementById("vault-list");
  
  if (!vaultItems.length) {
    list.innerHTML = '<div class="list-empty">No items in vault</div>';
    return;
  }

  // Decrypt labels
  const rendered = await Promise.all(vaultItems.map(async item => {
    let label = "[encrypted]";
    try {
      const res = await decryptToken(item.labelCt, masterPass);
      if (res.ok) label = res.text;
    } catch {
      // Use default
    }
    return { ...item, label };
  }));

  const filtered = query
    ? rendered.filter(i => i.label.toLowerCase().includes(query))
    : rendered;

  if (!filtered.length) {
    list.innerHTML = '<div class="list-empty">No matches</div>';
    return;
  }

  list.innerHTML = filtered.map(item => `
    <div class="list-item ${item.pinned ? "pinned" : ""}" onclick="viewVaultItem(${item.id})">
      <div class="vault-item-label">${escHtml(item.label)}</div>
      <div class="vault-item-meta">${item.pinned ? "📌 " : ""}${relTime(item.updatedAt)}</div>
    </div>
  `).join("");
}

async function viewVaultItem(id) {
  currentVaultItemId = id;
  const item = vaultItems.find(i => i.id === id);
  if (!item) return;

  let decrypted = "[Unable to decrypt]";
  try {
    const res = await decryptToken(item.payloadCt, masterPass);
    if (res.ok) decrypted = res.text;
  } catch (e) {
    console.error(e);
  }

  document.querySelector(".list-item.active")?.classList.remove("active");
  event.currentTarget?.classList.add("active");

  let label = "[encrypted]";
  try {
    const res = await decryptToken(item.labelCt, masterPass);
    if (res.ok) label = res.text;
  } catch {
    // Use default
  }

  document.getElementById("vault-detail").innerHTML = `
    <div style="margin-bottom:20px;">
      <h3 style="margin-bottom:8px;">${escHtml(label)}</h3>
      <p style="color:var(--fg-dim); font-size:12px;">Updated ${relTime(item.updatedAt)}</p>
    </div>
    <textarea readonly style="width:100%; height:300px; padding:12px; background:var(--surface-hi); border:1px solid var(--border-soft); border-radius:8px; color:var(--fg); font-family:var(--mono); font-size:12px; resize:none;">${escHtml(decrypted)}</textarea>
    <div style="margin-top:12px; display:flex; gap:8px;">
      <button class="btn secondary" onclick="deleteVaultItem(${item.id})" style="flex:1;">Delete</button>
    </div>
  `;
}

function showNewVaultForm() {
  document.getElementById("vault-detail").innerHTML = `
    <h3 style="margin-bottom:16px;">New Vault Item</h3>
    <div style="margin-bottom:12px;">
      <label style="display:block; margin-bottom:6px; color:var(--fg-dim); font-size:12px;">Label</label>
      <input type="text" id="vault-label" placeholder="Item name" style="width:100%; padding:10px; background:var(--surface-hi); border:1px solid var(--border-soft); border-radius:6px; color:var(--fg);">
    </div>
    <div style="margin-bottom:12px;">
      <label style="display:block; margin-bottom:6px; color:var(--fg-dim); font-size:12px;">Content</label>
      <textarea id="vault-content" placeholder="Item content" style="width:100%; height:200px; padding:10px; background:var(--surface-hi); border:1px solid var(--border-soft); border-radius:6px; color:var(--fg); resize:none;"></textarea>
    </div>
    <button class="btn" onclick="saveVaultItem()" style="width:100%;">Save Item</button>
  `;
}

async function saveVaultItem() {
  const label = document.getElementById("vault-label")?.value.trim();
  const content = document.getElementById("vault-content")?.value.trim();

  if (!label) {
    toast("Label required", "error");
    return;
  }
  if (!content) {
    toast("Content required", "error");
    return;
  }

  try {
    const labelCt = await encryptText(label, masterPass);
    const payloadCt = await encryptText(content, masterPass);
    
    const item = await api("POST", "/api/vault", {
      labelCt,
      payloadCt,
      pinned: false
    });

    vaultItems.push(item);
    renderVault();
    showNewVaultForm();
    toast("Item saved", "success", "✓");
  } catch (e) {
    toast(e.message, "error");
  }
}

async function deleteVaultItem(id) {
  if (!confirm("Delete this item?")) return;
  try {
    await api("DELETE", `/api/vault/${id}`);
    vaultItems = vaultItems.filter(i => i.id !== id);
    renderVault();
    document.getElementById("vault-detail").innerHTML = "";
    toast("Item deleted", "success", "✓");
  } catch (e) {
    toast(e.message, "error");
  }
}

/* ─────────────────────────────────────────────────────────────
   HISTORY FUNCTIONS
   ───────────────────────────────────────────────────────────── */
async function saveHistory(op, preview) {
  if (!currentUser) return;
  try {
    // Encrypt preview
    const previewCt = await encryptText(preview, masterPass);
    const item = await api("POST", "/api/history", {
      op,
      previewCt
    });
    history.unshift(item);
    if (history.length > 50) history = history.slice(0, 50);
    renderHistory();
  } catch (e) {
    console.error("History save failed:", e);
  }
}

async function loadHistory() {
  if (!currentUser) return;
  try {
    history = await api("GET", "/api/history") || [];
    renderHistory();
  } catch (e) {
    toast(e.message, "error", "History");
  }
}

async function renderHistory() {
  const list = document.getElementById("history-list");
  if (!history.length) {
    list.innerHTML = '<div class="list-empty">No history</div>';
    return;
  }

  // Decrypt previews
  const rendered = await Promise.all(history.map(async item => {
    let preview = "[encrypted]";
    try {
      const res = await decryptToken(item.previewCt, masterPass);
      if (res.ok) preview = res.text.substring(0, 100);
    } catch {
      // Use default
    }
    return { ...item, preview };
  }));

  list.innerHTML = rendered.map(item => `
    <div class="history-item">
      <div class="history-item-type">${item.op.toUpperCase()}</div>
      <div class="history-item-text">${escHtml(item.preview)}</div>
      <div class="history-item-time">${relTime(item.createdAt)}</div>
    </div>
  `).join("");
}

/* ─────────────────────────────────────────────────────────────
   MESSAGING FUNCTIONS
   ───────────────────────────────────────────────────────────── */
async function loadThreads() {
  if (!currentUser) return;
  try {
    threads = await api("GET", "/api/messages/threads") || [];
    renderThreads();
  } catch (e) {
    toast(e.message, "error", "Threads");
  }
}

function renderThreads() {
  const list = document.getElementById("thread-list");
  if (!threads.length) {
    list.innerHTML = '<div class="list-empty">No conversations</div>';
    return;
  }
  list.innerHTML = threads.map(thread => `
    <div class="list-item ${currentPeerId === thread.peerId ? "active" : ""}" onclick="openThread(${thread.peerId}, '${escHtml(thread.peerEmail)}')">
      <div style="font-weight:600; font-size:13px; margin-bottom:4px;">${escHtml(thread.peerEmail)}</div>
      <div style="font-size:11px; color:var(--fg-dim);">${thread.unread ? `${thread.unread} unread` : 'No new'}</div>
    </div>
  `).join("");
}

async function lookupUser() {
  const email = document.getElementById("recipient-lookup").value.trim();
  if (!email) {
    toast("Enter an email", "error");
    return;
  }
  try {
    const user = await api("POST", "/api/messages/lookup", { email });
    currentPeerId = user.id;
    openThread(user.id, user.email);
    document.getElementById("recipient-lookup").value = "";
  } catch (e) {
    toast(e.message, "error");
  }
}

async function openThread(peerId, peerEmail) {
  currentPeerId = peerId;
  document.getElementById("thread-title").textContent = peerEmail;
  document.querySelectorAll("#thread-list .list-item").forEach(el => el.classList.remove("active"));
  document.querySelector(`[onclick*="openThread(${peerId}"]`)?.classList.add("active");

  try {
    const messages = await api("GET", `/api/messages?peer=${peerId}`);
    renderMessages(messages || []);
    document.getElementById("message-input").focus();
  } catch (e) {
    toast(e.message, "error");
  }
}

function renderMessages(messages) {
  const list = document.getElementById("message-list");
  list.innerHTML = messages.reverse().map(msg => `
    <div class="message ${msg.fromMe ? "" : "other"}">
      <div class="message-sender">${msg.fromMe ? "You" : "Them"}</div>
      <div class="message-text">${escHtml(msg.ciphertext.substring(0, 100))}</div>
      <div class="message-time">${relTime(msg.createdAt)}</div>
    </div>
  `).join("");
  list.scrollTop = list.scrollHeight;
}

async function sendMessage() {
  if (!currentPeerId) {
    toast("Select a conversation", "error");
    return;
  }
  
  const input = document.getElementById("message-input");
  const text = input.value.trim();
  if (!text) return;

  try {
    // Encrypt the message
    const ciphertext = await encryptText(text, masterPass);
    
    await api("POST", "/api/messages", {
      recipientId: currentPeerId,
      ciphertext,
      hint: text.substring(0, 50)
    });
    input.value = "";
    
    // Reload messages
    const messages = await api("GET", `/api/messages?peer=${currentPeerId}`);
    renderMessages(messages || []);
    
    saveHistory("message", text);
  } catch (e) {
    toast(e.message, "error");
  }
}

function handleMessageKeypress(event) {
  if (event.key === "Enter" && !event.shiftKey) {
    event.preventDefault();
    sendMessage();
  }
}

function handleLookupKeypress(event) {
  if (event.key === "Enter") {
    event.preventDefault();
    lookupUser();
  }
}

/* ─────────────────────────────────────────────────────────────
   CIPHER TOOL
   ───────────────────────────────────────────────────────────── */
async function cipherEncrypt() {
  const key = document.getElementById("cipher-key").value;
  const input = document.getElementById("cipher-input").value;
  
  if (!key || !input) {
    toast("Enter key and text", "error");
    return;
  }

  try {
    const output = await encryptText(input, key);
    document.getElementById("cipher-output").value = output;
    toast("Encrypted", "success", "✓");
  } catch (e) {
    toast(e.message, "error");
  }
}

async function cipherDecrypt() {
  const key = document.getElementById("cipher-key").value;
  const input = document.getElementById("cipher-input").value;
  
  if (!key || !input) {
    toast("Enter key and token", "error");
    return;
  }

  try {
    const res = await decryptToken(input, key);
    if (!res.ok) {
      toast(res.err || "Decryption failed", "error");
      return;
    }
    document.getElementById("cipher-output").value = res.text;
    toast("Decrypted", "success", "✓");
  } catch (e) {
    toast(e.message, "error");
  }
}

/* ─────────────────────────────────────────────────────────────
   UI SWITCHING
   ───────────────────────────────────────────────────────────── */
function switchSidebarTab(tab) {
  document.querySelectorAll(".tab-btn").forEach(el => el.classList.remove("active"));
  event.currentTarget?.classList.add("active");

  document.getElementById("vault-list-panel").style.display = tab === "vault" ? "block" : "none";
  document.getElementById("messages-list-panel").style.display = tab === "messages" ? "block" : "none";
  document.getElementById("history-list-panel").style.display = tab === "history" ? "block" : "none";

  document.getElementById("vault-panel").style.display = tab === "vault" ? "flex" : "none";
  document.getElementById("messages-panel").classList.toggle("hidden", tab !== "messages");
  document.getElementById("cipher-panel").classList.toggle("hidden", tab !== "cipher");
}

/* ─────────────────────────────────────────────────────────────
   EVENT LISTENERS
   ───────────────────────────────────────────────────────────── */
document.getElementById("auth-submit").addEventListener("click", doAuth);
document.getElementById("auth-email").addEventListener("keypress", (e) => {
  if (e.key === "Enter") doAuth();
});
document.getElementById("auth-pass").addEventListener("keypress", (e) => {
  if (e.key === "Enter") doAuth();
});

setAuthMode("login");
</script>
</body>
</html>
