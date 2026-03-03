<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Secure Login Console — GUI</title>
  <meta name="description" content="A polished GUI for a simple username + password loop demo (default password: 1246)." />

  <!-- Distinct typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">

  <style>
    :root{
      /* Calm, security-console vibe (not neon cyberpunk) */
      --bg0:#070A10;
      --bg1:#0B1020;
      --ink:#EAF0FF;
      --muted:rgba(234,240,255,.72);
      --faint:rgba(234,240,255,.12);
      --fainter:rgba(234,240,255,.08);

      --accent:#89F7D0;     /* mint */
      --accent2:#E9C46A;    /* warm amber */
      --danger:#FF5D6C;
      --ok:#6EE7B7;

      --shadow: 0 18px 60px rgba(0,0,0,.55);
      --shadow2: 0 10px 30px rgba(0,0,0,.45);

      --radius-lg: 26px;
      --radius-md: 18px;
      --radius-sm: 12px;

      --grid-gap: clamp(14px, 2vw, 22px);

      --h1: clamp(2.1rem, 3.6vw, 3.3rem);
      --h2: clamp(1.2rem, 1.6vw, 1.55rem);
      --p:  clamp(1rem, 1.05vw, 1.05rem);
      --small: .9rem;
    }

    *{ box-sizing:border-box; }
    html,body{ height:100%; }
    body{
      margin:0;
      color:var(--ink);
      background:
        radial-gradient(1200px 700px at 18% 22%, rgba(137,247,208,.14), transparent 60%),
        radial-gradient(900px 700px at 78% 30%, rgba(233,196,106,.10), transparent 62%),
        radial-gradient(900px 900px at 50% 95%, rgba(137,247,208,.08), transparent 60%),
        linear-gradient(180deg, var(--bg0), var(--bg1));
      font-family:"IBM Plex Sans", system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
      overflow-x:hidden;
    }

    /* Subtle grain for richness */
    body::before{
      content:"";
      position:fixed; inset:0;
      pointer-events:none;
      opacity:.10;
      background-image:
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='180' height='180' filter='url(%23n)' opacity='.45'/%3E%3C/svg%3E");
      mix-blend-mode:overlay;
    }

    a{ color:inherit; text-decoration:none; }
    button, input { font:inherit; color:inherit; }
    ::selection{ background: rgba(137,247,208,.25); }

    /* Layout */
    .shell{
      min-height:100%;
      display:grid;
      grid-template-rows:auto 1fr auto;
    }

    header{
      position:sticky; top:0; z-index:20;
      backdrop-filter: blur(10px);
      background: linear-gradient(180deg, rgba(7,10,16,.78), rgba(7,10,16,.40));
      border-bottom:1px solid rgba(234,240,255,.08);
    }
    .nav{
      max-width:1120px;
      margin:0 auto;
      padding:16px clamp(16px, 3vw, 26px);
      display:flex;
      align-items:center;
      justify-content:space-between;
      gap:16px;
    }

    .brand{
      display:flex; align-items:center; gap:12px;
      letter-spacing:.2px;
      user-select:none;
    }
    .mark{
      width:38px; height:38px;
      border-radius:14px;
      background:
        radial-gradient(16px 16px at 30% 35%, rgba(255,255,255,.22), transparent 60%),
        linear-gradient(135deg, rgba(137,247,208,.95), rgba(233,196,106,.75));
      box-shadow: 0 10px 30px rgba(0,0,0,.35);
      position:relative;
    }
    .mark::after{
      content:"";
      position:absolute; inset:9px;
      border-radius:10px;
      border:1px solid rgba(0,0,0,.25);
      background: linear-gradient(180deg, rgba(7,10,16,.35), rgba(7,10,16,.10));
    }
    .brand strong{
      font-family:"Fraunces", serif;
      font-weight:700;
      font-size:1.05rem;
    }
    .brand span{
      display:block;
      font-size:.82rem;
      color:var(--muted);
      margin-top:1px;
    }

    .nav-actions{
      display:flex; align-items:center; gap:10px;
    }
    .pill{
      display:inline-flex; align-items:center; gap:10px;
      padding:10px 12px;
      border-radius:999px;
      border:1px solid rgba(234,240,255,.12);
      background: rgba(255,255,255,.04);
      box-shadow: 0 10px 20px rgba(0,0,0,.25);
      color:var(--muted);
      font-size:.92rem;
      white-space:nowrap;
    }
    .dot{
      width:8px; height:8px; border-radius:50%;
      background: rgba(110,231,183,.9);
      box-shadow: 0 0 0 4px rgba(110,231,183,.14);
    }

    main{
      max-width:1120px;
      margin:0 auto;
      padding: clamp(18px, 3.2vw, 34px) clamp(16px, 3vw, 26px) 34px;
      display:grid;
      gap: var(--grid-gap);
      align-items:start;
    }

    /* Hero grid: asymmetric, agency-like */
    .hero{
      display:grid;
      grid-template-columns: 1.08fr .92fr;
      gap: var(--grid-gap);
      align-items:stretch;
    }

    @media (max-width: 920px){
      .hero{ grid-template-columns: 1fr; }
    }

    .panel{
      border-radius: var(--radius-lg);
      border:1px solid rgba(234,240,255,.12);
      background:
        radial-gradient(1000px 500px at 20% 0%, rgba(137,247,208,.12), transparent 60%),
        radial-gradient(900px 600px at 110% 40%, rgba(233,196,106,.10), transparent 60%),
        rgba(255,255,255,.035);
      box-shadow: var(--shadow);
      overflow:hidden;
      position:relative;
    }

    .panel::before{
      content:"";
      position:absolute; inset:-2px;
      background:
        linear-gradient(135deg, rgba(137,247,208,.24), transparent 35%),
        linear-gradient(315deg, rgba(233,196,106,.18), transparent 45%);
      opacity:.8;
      pointer-events:none;
      mask: radial-gradient(260px 190px at 15% 15%, #000 35%, transparent 70%);
    }

    .hero-left{
      padding: clamp(18px, 3vw, 30px);
      display:grid;
      grid-template-rows:auto auto 1fr;
      gap: 14px;
    }

    .kicker{
      display:flex; align-items:center; gap:10px;
      color:var(--muted);
      font-size:.92rem;
    }
    .kicker .slash{
      width:18px; height:2px;
      background: linear-gradient(90deg, var(--accent), rgba(137,247,208,0));
      border-radius:99px;
    }

    h1{
      font-family:"Fraunces", serif;
      font-size:var(--h1);
      line-height:1.05;
      letter-spacing:-.02em;
      margin:0;
    }
    .sub{
      margin:0;
      font-size:var(--p);
      line-height:1.55;
      color:var(--muted);
      max-width:58ch;
    }

    .spec{
      margin-top:10px;
      display:grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      align-content:start;
    }
    @media (max-width: 520px){
      .spec{ grid-template-columns: 1fr; }
    }

    .spec-item{
      border-radius: var(--radius-md);
      border:1px solid rgba(234,240,255,.10);
      background: rgba(0,0,0,.16);
      padding: 12px 14px;
      box-shadow: var(--shadow2);
    }
    .spec-item b{
      display:block;
      font-weight:600;
      letter-spacing:.01em;
      margin-bottom:4px;
    }
    .spec-item small{
      display:block;
      color:var(--muted);
      font-size:.9rem;
      line-height:1.35;
    }

    /* Right: GUI */
    .gui{
      padding: 16px;
      display:grid;
      grid-template-rows:auto 1fr;
      gap: 12px;
    }

    .windowbar{
      display:flex; align-items:center; justify-content:space-between;
      gap:12px;
      padding: 12px 12px 10px;
      border-radius: 18px;
      border:1px solid rgba(234,240,255,.10);
      background: rgba(0,0,0,.18);
    }
    .lights{ display:flex; gap:8px; align-items:center; }
    .light{
      width:10px; height:10px; border-radius:50%;
      background: rgba(234,240,255,.25);
      box-shadow: inset 0 0 0 1px rgba(0,0,0,.25);
    }
    .light.red{ background: rgba(255,93,108,.8); }
    .light.amber{ background: rgba(233,196,106,.85); }
    .light.green{ background: rgba(110,231,183,.85); }

    .windowbar .title{
      display:flex; flex-direction:column;
      gap:2px;
      min-width: 0;
    }
    .windowbar .title strong{
      font-size:.95rem;
      letter-spacing:.01em;
      white-space:nowrap;
      overflow:hidden;
      text-overflow:ellipsis;
    }
    .windowbar .title span{
      font-size:.83rem;
      color:var(--muted);
    }

    .hint{
      display:inline-flex; align-items:center; gap:8px;
      padding:8px 10px;
      border-radius:999px;
      border:1px solid rgba(234,240,255,.12);
      background: rgba(255,255,255,.04);
      color: var(--muted);
      font-size:.86rem;
      white-space:nowrap;
    }
    .kbd{
      font-feature-settings:"tnum" 1, "ss01" 1;
      font-variant-numeric: tabular-nums;
      padding:2px 8px;
      border-radius: 999px;
      border:1px solid rgba(234,240,255,.16);
      background: rgba(0,0,0,.22);
      color: rgba(234,240,255,.86);
    }

    .gui-body{
      border-radius: 22px;
      border:1px solid rgba(234,240,255,.10);
      background:
        radial-gradient(500px 280px at 60% 0%, rgba(137,247,208,.10), transparent 62%),
        rgba(0,0,0,.18);
      overflow:hidden;
      display:grid;
      grid-template-rows:auto 1fr;
    }

    .form{
      padding: 16px 16px 14px;
      display:grid;
      gap: 12px;
    }

    .row{
      display:grid;
      gap: 8px;
    }
    label{
      font-size:.92rem;
      color: rgba(234,240,255,.82);
      letter-spacing:.01em;
    }

    .field{
      display:flex;
      align-items:center;
      gap:10px;
      padding: 12px 12px;
      border-radius: 16px;
      border:1px solid rgba(234,240,255,.12);
      background: rgba(255,255,255,.04);
      transition: transform .18s ease, border-color .18s ease, background .18s ease;
    }
    .field:focus-within{
      transform: translateY(-1px);
      border-color: rgba(137,247,208,.55);
      background: rgba(137,247,208,.05);
    }

    input{
      width:100%;
      border:0;
      outline:0;
      background: transparent;
      color: var(--ink);
      font-size: 1rem;
    }
    input::placeholder{ color: rgba(234,240,255,.40); }

    .icon{
      width:18px; height:18px;
      opacity:.9;
      flex:0 0 auto;
    }

    .actions{
      display:flex;
      gap:10px;
      align-items:center;
      flex-wrap:wrap;
      margin-top: 2px;
    }

    .btn{
      border:0;
      cursor:pointer;
      border-radius: 999px;
      padding: 11px 14px;
      font-weight:600;
      letter-spacing:.01em;
      transition: transform .16s ease, filter .16s ease, box-shadow .16s ease, background .16s ease;
      user-select:none;
    }
    .btn:active{ transform: translateY(1px) scale(.99); }

    .btn.primary{
      background: linear-gradient(135deg, rgba(137,247,208,.95), rgba(233,196,106,.86));
      color: rgba(7,10,16,.92);
      box-shadow: 0 16px 40px rgba(0,0,0,.45);
    }
    .btn.primary:hover{ filter: brightness(1.03) saturate(1.04); transform: translateY(-1px); }

    .btn.ghost{
      background: rgba(255,255,255,.05);
      border:1px solid rgba(234,240,255,.12);
      color: rgba(234,240,255,.9);
    }
    .btn.ghost:hover{
      background: rgba(255,255,255,.07);
      transform: translateY(-1px);
    }

    .inline{
      display:flex;
      align-items:center;
      gap:10px;
      color: var(--muted);
      font-size: .92rem;
      margin-left:auto;
    }
    .toggle{
      width:44px; height:26px;
      border-radius: 999px;
      border:1px solid rgba(234,240,255,.16);
      background: rgba(0,0,0,.24);
      position:relative;
      cursor:pointer;
      flex:0 0 auto;
      transition: background .18s ease, border-color .18s ease;
    }
    .toggle::after{
      content:"";
      position:absolute; top:3px; left:3px;
      width:20px; height:20px; border-radius:50%;
      background: rgba(234,240,255,.85);
      box-shadow: 0 10px 20px rgba(0,0,0,.35);
      transition: transform .18s ease, background .18s ease;
    }
    .toggle[aria-checked="true"]{
      background: rgba(137,247,208,.14);
      border-color: rgba(137,247,208,.45);
    }
    .toggle[aria-checked="true"]::after{
      transform: translateX(18px);
      background: rgba(137,247,208,.95);
    }

    /* Console output */
    .console{
      border-top:1px solid rgba(234,240,255,.10);
      padding: 14px 14px 16px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      font-size: .93rem;
      line-height: 1.45;
      color: rgba(234,240,255,.86);
      overflow:auto;
      max-height: 260px;
      background:
        linear-gradient(180deg, rgba(0,0,0,.10), rgba(0,0,0,.26));
    }
    .line{ display:flex; gap:10px; padding: 3px 0; }
    .caret{
      color: rgba(137,247,208,.9);
      opacity:.95;
      flex:0 0 auto;
    }
    .msg.muted{ color: rgba(234,240,255,.62); }
    .msg.bad{ color: rgba(255,93,108,.92); }
    .msg.ok{ color: rgba(110,231,183,.92); }
    .msg.warn{ color: rgba(233,196,106,.95); }

    .footer{
      max-width:1120px;
      margin:0 auto;
      padding: 18px clamp(16px, 3vw, 26px) 22px;
      color: rgba(234,240,255,.55);
      display:flex;
      justify-content:space-between;
      gap:14px;
      flex-wrap:wrap;
      border-top:1px solid rgba(234,240,255,.08);
    }

    /* Reveal animations */
    .reveal{
      opacity:0;
      transform: translateY(10px);
      animation: rise .7s cubic-bezier(.2,.85,.2,1) forwards;
    }
    .d1{ animation-delay:.08s; }
    .d2{ animation-delay:.18s; }
    .d3{ animation-delay:.28s; }
    .d4{ animation-delay:.38s; }

    @keyframes rise{
      to{ opacity:1; transform: translateY(0); }
    }

    /* Reduced motion */
    @media (prefers-reduced-motion: reduce){
      .reveal{ animation:none; opacity:1; transform:none; }
      .btn, .field, .toggle::after, .toggle{ transition:none; }
    }
  </style>
</head>

<body>
  <div class="shell">
    <header>
      <div class="nav">
        <div class="brand">
          <div class="mark" aria-hidden="true"></div>
          <div>
            <strong>Secure Login Console</strong>
            <span>GUI version of your Python password loop</span>
          </div>
        </div>

        <div class="nav-actions">
          <div class="pill" role="status" aria-live="polite">
            <span class="dot" aria-hidden="true"></span>
            Local demo • No network
          </div>
        </div>
      </div>
    </header>

    <main>
      <section class="hero">
        <article class="panel hero-left reveal d1">
          <div class="kicker">
            <span class="slash" aria-hidden="true"></span>
            <span>Reference logic: <code>while(password != default_password)</code></span>
          </div>

          <h1>Enter username, retry password, then log in.</h1>
          <p class="sub">
            This interface mirrors your script: it repeatedly asks for the password until it matches
            the default (<b>1246</b>), then prints <b>“Successful logged in:”</b>.
          </p>

          <div class="spec">
            <div class="spec-item reveal d2">
              <b>Default password</b>
              <small><code>1246</code> (stored locally in this demo)</small>
            </div>
            <div class="spec-item reveal d3">
              <b>Behavior</b>
              <small>Wrong password → prompt again; correct → success</small>
            </div>
            <div class="spec-item reveal d4">
              <b>Accessibility</b>
              <small>Keyboard-friendly, focus states, live status output</small>
            </div>
            <div class="spec-item reveal d4">
              <b>Tip</b>
              <small>Try a wrong password first to see the loop output</small>
            </div>
          </div>
        </article>

        <section class="panel gui reveal d2" aria-label="Login GUI">
          <div class="windowbar">
            <div class="lights" aria-hidden="true">
              <span class="light red"></span>
              <span class="light amber"></span>
              <span class="light green"></span>
            </div>
            <div class="title">
              <strong>login.py — Interactive GUI</strong>
              <span>Simulated console output</span>
            </div>
            <div class="hint">
              Press <span class="kbd">Enter</span> to submit
            </div>
          </div>

          <div class="gui-body">
            <form class="form" id="loginForm" autocomplete="off">
              <div class="row">
                <label for="username">User name</label>
                <div class="field">
                  <svg class="icon" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                    <path d="M12 12c2.761 0 5-2.239 5-5S14.761 2 12 2 7 4.239 7 7s2.239 5 5 5Z" stroke="currentColor" stroke-opacity=".95" stroke-width="1.6"/>
                    <path d="M20 22a8 8 0 0 0-16 0" stroke="currentColor" stroke-opacity=".75" stroke-width="1.6" stroke-linecap="round"/>
                  </svg>
                  <input id="username" name="username" placeholder="Enter username" required />
                </div>
              </div>

              <div class="row">
                <label for="password">Password</label>
                <div class="field">
                  <svg class="icon" viewBox="0 0 24 24" fill="none" aria-hidden="true">
                    <path d="M7 11V8a5 5 0 0 1 10 0v3" stroke="currentColor" stroke-opacity=".95" stroke-width="1.6" stroke-linecap="round"/>
                    <path d="M6.5 11h11A2.5 2.5 0 0 1 20 13.5v6A2.5 2.5 0 0 1 17.5 22h-11A2.5 2.5 0 0 1 4 19.5v-6A2.5 2.5 0 0 1 6.5 11Z" stroke="currentColor" stroke-opacity=".75" stroke-width="1.6"/>
                    <path d="M12 15v3" stroke="currentColor" stroke-opacity=".9" stroke-width="1.6" stroke-linecap="round"/>
                  </svg>
                  <input id="password" name="password" type="password" inputmode="numeric" placeholder="Enter password" required />
                </div>
              </div>

              <div class="actions">
                <button class="btn primary" type="submit">Login</button>
                <button class="btn ghost" type="button" id="resetBtn">Reset</button>

                <div class="inline">
                  <span>Show password</span>
                  <button class="toggle" id="showToggle" type="button" role="switch" aria-checked="false" aria-label="Show password"></button>
                </div>
              </div>
            </form>

            <div class="console" id="console" role="log" aria-live="polite" aria-relevant="additions text">
              <!-- lines injected by JS -->
            </div>
          </div>
        </section>
      </section>
    </main>

    <footer class="footer">
      <div>Built as a GUI interpretation of your loop-based login snippet.</div>
      <div><span style="color: rgba(234,240,255,.7)">Note:</span> This is a demo (not real authentication).</div>
    </footer>
  </div>

  <script>
    (() => {
      const DEFAULT_PASSWORD = 1246;

      const $ = (sel, root=document) => root.querySelector(sel);

      const form = $("#loginForm");
      const usernameEl = $("#username");
      const passwordEl = $("#password");
      const consoleEl = $("#console");
      const resetBtn = $("#resetBtn");
      const showToggle = $("#showToggle");

      let attempts = 0;

      function addLine(text, type="muted"){
        const line = document.createElement("div");
        line.className = "line";
        const caret = document.createElement("div");
        caret.className = "caret";
        caret.textContent = "›";

        const msg = document.createElement("div");
        msg.className = "msg " + type;
        msg.textContent = text;

        line.appendChild(caret);
        line.appendChild(msg);
        consoleEl.appendChild(line);
        consoleEl.scrollTop = consoleEl.scrollHeight;
      }

      function banner(){
        consoleEl.innerHTML = "";
        attempts = 0;
        addLine("default_password = 1246", "muted");
        addLine("user_name = input('Enter username:')", "muted");
        addLine("password = int(input('Enter password :'))", "muted");
      }

      function sanitizeName(name){
        return (name || "").trim().slice(0, 40);
      }

      // Initial output
      banner();
      addLine("Ready. Enter username and password in the form above.", "muted");

      // Toggle show/hide password
      showToggle.addEventListener("click", () => {
        const on = showToggle.getAttribute("aria-checked") === "true";
        const next = !on;
        showToggle.setAttribute("aria-checked", String(next));
        passwordEl.type = next ? "text" : "password";
        addLine(next ? "Password visibility: ON" : "Password visibility: OFF", "muted");
        passwordEl.focus();
      });

      // Reset
      resetBtn.addEventListener("click", () => {
        form.reset();
        passwordEl.type = (showToggle.getAttribute("aria-checked") === "true") ? "text" : "password";
        banner();
        addLine("Reset complete.", "muted");
        usernameEl.focus();
      });

      // Submit handling (mirrors while loop behavior)
      form.addEventListener("submit", (e) => {
        e.preventDefault();

        const username = sanitizeName(usernameEl.value);
        const raw = (passwordEl.value || "").trim();

        addLine(`Enter username: ${username || "(blank)"}`, "muted");

        // Mimic int(input()) behavior
        const entered = Number(raw);
        const isIntLike = raw !== "" && Number.isFinite(entered) && Number.isInteger(entered);

        if(!isIntLike){
          attempts++;
          addLine("Enter password : " + (raw === "" ? "(blank)" : raw), "muted");
          addLine("Enter correct password :", "bad");
          addLine("Hint: password must be a number (int).", "warn");
          passwordEl.select();
          passwordEl.focus();
          return;
        }

        addLine("Enter password : " + entered, "muted");

        if(entered !== DEFAULT_PASSWORD){
          attempts++;
          addLine("Enter correct password :", "bad");
          // Keep the loop going: do not clear username; just focus password.
          passwordEl.select();
          passwordEl.focus();
          return;
        }

        addLine("Successful logged in:", "ok");
        addLine(`Welcome, ${username ? username : "user"} (attempts: ${attempts}).`, "ok");

        // Lock inputs after success
        usernameEl.disabled = true;
        passwordEl.disabled = true;

        // Provide a clear next action
        resetBtn.focus();
      });

      // Scroll-trigger reveal (for future sections; safe no-op if already visible)
      const io = new IntersectionObserver((entries) => {
        for (const ent of entries){
          if(ent.isIntersecting){
            ent.target.style.animationPlayState = "running";
            io.unobserve(ent.target);
          }
        }
      }, { threshold: 0.12 });

      document.querySelectorAll(".reveal").forEach(el => {
        // ensure animation is ready
        el.style.animationPlayState = "running";
        io.observe(el);
      });
    })();
  </script>
</body>
</html>