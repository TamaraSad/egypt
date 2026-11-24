/* Анимированные сцены игр на первом экране: <canvas data-scene="aviator|chicken-road|tower-rush">.
   Рисуется в логических координатах 560×420 и масштабируется под размер блока.
   Останавливается вне экрана; при prefers-reduced-motion показывает один статичный кадр. */
(function () {
  'use strict';

  var W = 560, H = 420;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function rand(a, b) { return a + Math.random() * (b - a); }
  function pick(arr) { return arr[Math.floor(Math.random() * arr.length)]; }
  function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }
  function rr(c, x, y, w, h, r) {
    r = Math.min(r, w / 2, h / 2);
    c.beginPath();
    c.moveTo(x + r, y);
    c.arcTo(x + w, y, x + w, y + h, r);
    c.arcTo(x + w, y + h, x, y + h, r);
    c.arcTo(x, y + h, x, y, r);
    c.arcTo(x, y, x + w, y, r);
    c.closePath();
  }
  function fmt(m) { return m.toFixed(2) + 'x'; }
  var FONT = '"Manrope", "Inter", "Segoe UI", Arial, sans-serif';

  /* ===================== AVIATOR ===================== */
  function Aviator() {
    var s = { phase: 'fly', t: 0, m: 1, crash: 3.2, cashed: false, toast: 9, stars: [], trail: [] };
    for (var i = 0; i < 46; i++) s.stars.push({ x: rand(0, W), y: rand(0, H), r: rand(0.4, 1.6), v: rand(8, 26) });

    function newRound() {
      s.phase = 'wait'; s.t = 0; s.m = 1; s.cashed = false; s.toast = 9;
      s.crash = Math.random() < 0.3 ? rand(1.25, 1.9) : rand(2.3, 7.5);
    }
    function px(t) { return 52 + clamp(t / 7, 0, 1) * 400; }
    function py(m) { return 330 - clamp(Math.log(m) / Math.log(7), 0, 1) * 220; }

    function update(dt) {
      var speed = s.phase === 'fly' ? 3 : 0.6;
      s.stars.forEach(function (st) { st.x -= st.v * speed * dt; if (st.x < -2) { st.x = W + 2; st.y = rand(0, H); } });
      s.t += dt; s.toast += dt;
      if (s.phase === 'wait') { if (s.t > 2.4) { s.phase = 'fly'; s.t = 0; } }
      else if (s.phase === 'fly') {
        s.m = Math.exp(0.24 * s.t);
        if (!s.cashed && s.m >= 2) { s.cashed = true; s.toast = 0; }
        if (s.m >= s.crash) { s.m = s.crash; s.phase = 'crash'; s.flyT = s.t; s.t = 0; }
      } else if (s.phase === 'crash') { if (s.t > 2) newRound(); }
    }

    function plane(c, x, y, a, alpha) {
      c.save(); c.globalAlpha = alpha; c.translate(x, y); c.rotate(a);
      c.fillStyle = 'rgba(22,183,122,.25)'; c.beginPath(); c.ellipse(-36, 0, 22, 4, 0, 0, Math.PI * 2); c.fill();
      c.fillStyle = '#e8eef7';
      c.beginPath(); c.moveTo(-14, -3); c.lineTo(-30, -26); c.lineTo(-20, -26); c.lineTo(4, -3); c.closePath(); c.fill();
      c.beginPath(); c.moveTo(-26, -2); c.lineTo(-36, -13); c.lineTo(-30, -13); c.lineTo(-18, -2); c.closePath(); c.fill();
      var g = c.createLinearGradient(0, -7, 0, 7); g.addColorStop(0, '#ffffff'); g.addColorStop(1, '#c4d0e0');
      c.fillStyle = g; c.beginPath(); c.moveTo(-34, -5); c.lineTo(16, -6); c.quadraticCurveTo(30, 0, 16, 6); c.lineTo(-34, 5); c.quadraticCurveTo(-40, 0, -34, -5); c.fill();
      c.fillStyle = '#16b77a'; c.fillRect(-26, -1.5, 34, 3);
      c.fillStyle = '#0b1d36'; c.beginPath(); c.ellipse(13, -2, 5, 2.6, 0, 0, Math.PI * 2); c.fill();
      c.fillStyle = '#c4d0e0';
      c.beginPath(); c.moveTo(-14, 3); c.lineTo(-30, 26); c.lineTo(-20, 26); c.lineTo(4, 3); c.closePath(); c.fill();
      c.restore();
    }

    function draw(c) {
      var bg = c.createLinearGradient(0, 0, 0, H); bg.addColorStop(0, '#102544'); bg.addColorStop(1, '#060f1f');
      c.fillStyle = bg; c.fillRect(0, 0, W, H);
      var glow = c.createRadialGradient(280, 190, 10, 280, 190, 260);
      glow.addColorStop(0, s.phase === 'crash' ? 'rgba(214,69,61,.22)' : 'rgba(22,183,122,.18)'); glow.addColorStop(1, 'rgba(0,0,0,0)');
      c.fillStyle = glow; c.fillRect(0, 0, W, H);
      s.stars.forEach(function (st) { c.fillStyle = 'rgba(255,255,255,' + (0.25 + st.r / 3) + ')'; c.beginPath(); c.arc(st.x, st.y, st.r, 0, 6.3); c.fill(); });
      c.strokeStyle = 'rgba(255,255,255,.05)'; c.lineWidth = 1;
      for (var gx = 52; gx < W; gx += 80) { c.beginPath(); c.moveTo(gx, 40); c.lineTo(gx, 330); c.stroke(); }
      for (var gy = 90; gy <= 330; gy += 60) { c.beginPath(); c.moveTo(52, gy); c.lineTo(W - 20, gy); c.stroke(); }

      if (s.phase !== 'wait') {
        var T = s.phase === 'fly' ? s.t : s.flyT;
        var pts = [];
        for (var k = 0; k <= 60; k++) { var tt = T * k / 60; pts.push([px(tt), py(Math.exp(0.24 * tt))]); }
        var fillG = c.createLinearGradient(0, 110, 0, 330);
        var col = s.phase === 'crash' ? '214,69,61' : '22,183,122';
        fillG.addColorStop(0, 'rgba(' + col + ',.45)'); fillG.addColorStop(1, 'rgba(' + col + ',0)');
        c.beginPath(); c.moveTo(pts[0][0], 330); pts.forEach(function (p) { c.lineTo(p[0], p[1]); }); c.lineTo(pts[pts.length - 1][0], 330); c.closePath();
        c.fillStyle = fillG; c.fill();
        c.beginPath(); pts.forEach(function (p, i) { if (i) c.lineTo(p[0], p[1]); else c.moveTo(p[0], p[1]); });
        c.strokeStyle = 'rgb(' + col + ')'; c.lineWidth = 4; c.lineCap = 'round'; c.stroke();
        var e = pts[pts.length - 1], b = pts[pts.length - 4] || pts[0];
        var ang = Math.atan2(e[1] - b[1], e[0] - b[0]);
        if (s.phase === 'fly') plane(c, e[0], e[1] + Math.sin(s.t * 6) * 1.5, ang, 1);
        else plane(c, e[0] + s.t * 420, e[1] - s.t * 260, -0.6, clamp(1 - s.t * 1.2, 0, 1));
      }

      c.textAlign = 'center'; c.textBaseline = 'middle';
      if (s.phase === 'wait') {
        c.fillStyle = 'rgba(255,255,255,.75)'; c.font = '700 18px ' + FONT; c.fillText('Next round in…', 280, 170);
        rr(c, 180, 196, 200, 8, 4); c.fillStyle = 'rgba(255,255,255,.12)'; c.fill();
        rr(c, 180, 196, 200 * clamp(1 - s.t / 2.4, 0, 1), 8, 4); c.fillStyle = '#16b77a'; c.fill();
      } else {
        if (s.phase === 'crash') { c.fillStyle = '#ff6b62'; c.font = '800 20px ' + FONT; c.fillText('FLEW AWAY!', 280, 128); }
        c.fillStyle = s.phase === 'crash' ? '#ff6b62' : '#ffffff';
        c.font = '800 66px ' + FONT; c.fillText(fmt(s.m), 280, 180);
      }

      // панели ставок
      [[40, 'Bet 1', 'Auto 2.00x', true], [292, 'Bet 2', 'Manual', false]].forEach(function (p) {
        var x = p[0];
        rr(c, x, 352, 228, 52, 12); c.fillStyle = 'rgba(255,255,255,.08)'; c.fill();
        c.strokeStyle = 'rgba(255,255,255,.1)'; c.lineWidth = 1; c.stroke();
        c.textAlign = 'left'; c.fillStyle = 'rgba(255,255,255,.6)'; c.font = '600 11px ' + FONT; c.fillText(p[1] + ' · ' + p[2], x + 14, 368);
        c.fillStyle = '#fff'; c.font = '800 15px ' + FONT; c.fillText('₦ 500', x + 14, 389);
        var done = p[3] && s.cashed;
        rr(c, x + 112, 362, 104, 32, 9); c.fillStyle = done ? '#ffffff' : (p[3] ? '#16b77a' : '#f4a62a'); c.fill();
        c.textAlign = 'center'; c.fillStyle = done ? '#0e8a5b' : '#0b1d36'; c.font = '800 12px ' + FONT;
        c.fillText(done ? 'WON 2.00x' : (s.phase === 'fly' ? 'CASH OUT' : 'BET'), x + 164, 378);
      });
      if (s.toast < 1.6) {
        var a = clamp(1.6 - s.toast, 0, 1), yy = 64 - Math.min(s.toast, 0.3) * 30;
        c.globalAlpha = a; rr(c, 180, yy, 200, 34, 17); c.fillStyle = '#16b77a'; c.fill();
        c.fillStyle = '#05261a'; c.font = '800 13px ' + FONT; c.textAlign = 'center'; c.fillText('Cashed out at 2.00x', 280, yy + 17); c.globalAlpha = 1;
      }
    }
    return { update: update, draw: draw, warm: 3.6 };
  }

  /* ===================== CHICKEN ROAD ===================== */
  function Chicken() {
    var LANES = 5, ROAD_X = 116, LANE_W = 84, CY = 236;
    var MULTS = [1.2, 1.5, 2.1, 3.0, 4.8];
    var COLORS = ['#f4a62a', '#d6453d', '#5aa3ff', '#e8eef7', '#9b6bff'];
    function laneX(i) { return i < 0 ? 64 : ROAD_X + LANE_W / 2 + LANE_W * i; }
    var cars = [];
    for (var i = 0; i < LANES; i++) cars.push({ lane: i, y: rand(-300, H), v: rand(200, 330), col: pick(COLORS) });
    var s = { lane: -1, from: -1, phase: 'idle', t: 0, target: 3, hit: false, feathers: [], flash: 0 };

    function reset() { s.lane = -1; s.from = -1; s.phase = 'idle'; s.t = 0; s.target = Math.floor(rand(2, 5.99)); s.hit = Math.random() < 0.35; s.feathers = []; }
    reset();

    function laneDanger(i) { var c = cars[i]; return c.y + 86 > CY - 110 && c.y < CY + 60; }

    function update(dt) {
      s.t += dt; s.flash = Math.max(0, s.flash - dt * 2);
      cars.forEach(function (c) {
        var occupied = s.lane === c.lane && s.phase !== 'hit' && !(s.hit && s.lane === s.target - 1 && s.phase === 'stand');
        var nv = c.v;
        if (occupied && c.y + 86 <= CY - 40 && c.y + 86 + c.v * dt > CY - 46) { c.y = CY - 46 - 86; nv = 0; }
        if (occupied && c.y + 86 > CY - 48 && c.y + 86 <= CY - 40) nv = 0;
        c.y += nv * dt;
        if (c.y > H + 20) { c.y = rand(-260, -110); c.v = rand(200, 330); c.col = pick(COLORS); }
      });
      if (s.phase === 'idle') { if (s.t > 0.9 && !laneDanger(0)) { s.from = -1; s.lane = 0; s.phase = 'hop'; s.t = 0; } }
      else if (s.phase === 'hop') { if (s.t > 0.36) { s.phase = 'stand'; s.t = 0; } }
      else if (s.phase === 'stand') {
        var last = s.lane === s.target - 1;
        if (last) {
          if (s.hit) {
            var car = cars[s.lane];
            if (car.y > CY + 10 || car.y < -100) { car.y = -100; car.v = 560; }
            if (car.y + 86 > CY - 18 && car.y < CY + 18) {
              s.phase = 'hit'; s.t = 0; s.flash = 1;
              for (var f = 0; f < 18; f++) s.feathers.push({ x: laneX(s.lane), y: CY - 10, vx: rand(-140, 140), vy: rand(-220, -40), r: rand(0, 6.3), vr: rand(-6, 6) });
            }
          } else if (s.t > 0.8) { s.phase = 'cash'; s.t = 0; }
        } else if (s.t > 0.75 && !laneDanger(s.lane + 1)) { s.from = s.lane; s.lane += 1; s.phase = 'hop'; s.t = 0; }
      } else if (s.phase === 'cash' || s.phase === 'hit') {
        s.feathers.forEach(function (p) { p.x += p.vx * dt; p.y += p.vy * dt; p.vy += 380 * dt; p.vx *= 0.98; p.r += p.vr * dt; });
        if (s.t > 2) reset();
      }
    }

    function car(c, x, y, col) {
      c.fillStyle = 'rgba(0,0,0,.28)'; rr(c, x - 22, y + 6, 46, 86, 12); c.fill();
      c.fillStyle = col; rr(c, x - 22, y, 44, 86, 12); c.fill();
      c.globalAlpha = 0.18; c.fillStyle = '#fff'; rr(c, x - 6, y + 4, 12, 78, 6); c.fill(); c.globalAlpha = 1;
      c.fillStyle = '#152234'; rr(c, x - 16, y + 50, 32, 20, 5); c.fill(); rr(c, x - 16, y + 14, 32, 14, 5); c.fill();
      c.fillStyle = '#fff6c9'; c.beginPath(); c.arc(x - 13, y + 83, 3.2, 0, 6.3); c.arc(x + 13, y + 83, 3.2, 0, 6.3); c.fill();
      var lg = c.createLinearGradient(0, y + 86, 0, y + 150); lg.addColorStop(0, 'rgba(255,246,201,.35)'); lg.addColorStop(1, 'rgba(255,246,201,0)');
      c.fillStyle = lg; c.beginPath(); c.moveTo(x - 18, y + 86); c.lineTo(x + 18, y + 86); c.lineTo(x + 30, y + 150); c.lineTo(x - 30, y + 150); c.closePath(); c.fill();
      c.fillStyle = '#d6453d'; c.fillRect(x - 17, y + 1, 7, 3); c.fillRect(x + 10, y + 1, 7, 3);
    }

    function chicken(c, x, y, sq, rot) {
      c.save(); c.translate(x, y); c.rotate(rot || 0); c.scale(1 + sq * 0.12, 1 - sq * 0.12);
      c.strokeStyle = '#f4a62a'; c.lineWidth = 3.5; c.lineCap = 'round';
      c.beginPath(); c.moveTo(-6, 16); c.lineTo(-7, 26); c.moveTo(6, 16); c.lineTo(7, 26); c.stroke();
      var g = c.createRadialGradient(-6, -6, 4, 0, 2, 26); g.addColorStop(0, '#ffffff'); g.addColorStop(1, '#d9e2ee');
      c.fillStyle = g; c.beginPath(); c.ellipse(0, 4, 21, 18, 0, 0, 6.3); c.fill();
      c.fillStyle = '#eef3f9'; c.beginPath(); c.ellipse(-10, 6, 10, 7, -0.5, 0, 6.3); c.fill();
      c.fillStyle = g; c.beginPath(); c.arc(7, -15, 12, 0, 6.3); c.fill();
      c.fillStyle = '#e8473f'; c.beginPath(); c.arc(2, -27, 4.5, 0, 6.3); c.arc(8, -29, 4.8, 0, 6.3); c.arc(13, -26, 4, 0, 6.3); c.fill();
      c.beginPath(); c.ellipse(17, -9, 3, 4.5, 0, 0, 6.3); c.fill();
      c.fillStyle = '#f4a62a'; c.beginPath(); c.moveTo(18, -16); c.lineTo(27, -13); c.lineTo(18, -10); c.closePath(); c.fill();
      c.fillStyle = '#0b1d36'; c.beginPath(); c.arc(11, -17, 2.4, 0, 6.3); c.fill();
      c.fillStyle = '#fff'; c.beginPath(); c.arc(11.8, -17.8, 0.8, 0, 6.3); c.fill();
      c.restore();
    }

    function draw(c) {
      c.fillStyle = '#2a323e'; c.fillRect(0, 0, W, H);
      var side = c.createLinearGradient(0, 0, ROAD_X, 0); side.addColorStop(0, '#8b97a7'); side.addColorStop(1, '#a9b4c2');
      c.fillStyle = side; c.fillRect(0, 0, ROAD_X, H);
      c.strokeStyle = 'rgba(0,0,0,.12)'; c.lineWidth = 1;
      for (var ty = 0; ty < H; ty += 36) { c.beginPath(); c.moveTo(0, ty); c.lineTo(ROAD_X, ty); c.stroke(); }
      c.fillStyle = '#d7dee8'; c.fillRect(ROAD_X - 6, 0, 6, H);
      var road = c.createLinearGradient(ROAD_X, 0, W, 0); road.addColorStop(0, '#2f3846'); road.addColorStop(1, '#262d38');
      c.fillStyle = road; c.fillRect(ROAD_X, 0, W - ROAD_X, H);
      c.strokeStyle = 'rgba(255,255,255,.65)'; c.lineWidth = 3; c.setLineDash([22, 20]);
      for (var l = 1; l < LANES; l++) { var lx = ROAD_X + LANE_W * l; c.beginPath(); c.moveTo(lx, 0); c.lineTo(lx, H); c.stroke(); }
      c.setLineDash([]);

      for (var i = 0; i < LANES; i++) {
        var x = laneX(i), passed = i < s.lane || (i === s.lane && s.phase !== 'hop'), cur = i === s.lane;
        c.fillStyle = 'rgba(0,0,0,.35)'; c.beginPath(); c.ellipse(x, CY + 30, 30, 10, 0, 0, 6.3); c.fill();
        c.fillStyle = passed ? (cur && s.phase === 'hit' ? '#d6453d' : '#16b77a') : '#3a4555';
        c.beginPath(); c.ellipse(x, CY + 26, 28, 9, 0, 0, 6.3); c.fill();
        c.fillStyle = passed ? '#05261a' : (i === LANES - 1 ? '#f4a62a' : '#cfd8e3');
        c.font = '800 13px ' + FONT; c.textAlign = 'center'; c.textBaseline = 'middle';
        c.fillText(MULTS[i].toFixed(1) + 'x', x, CY + 27);
      }
      cars.forEach(function (cr) { car(c, laneX(cr.lane), cr.y, cr.col); });

      // курица
      var cx, cy, sq = 0, rot = 0;
      if (s.phase === 'hop') {
        var p = clamp(s.t / 0.36, 0, 1);
        cx = laneX(s.from) + (laneX(s.lane) - laneX(s.from)) * p; cy = CY - Math.sin(p * Math.PI) * 42; sq = p > 0.85 ? 1 : 0;
      } else { cx = laneX(s.lane); cy = CY; if (s.phase === 'stand' && s.t < 0.12) sq = 1; }
      if (s.phase === 'hit') { rot = Math.min(s.t * 6, 1.6); cy = CY + Math.min(s.t * 30, 14); }
      c.fillStyle = 'rgba(0,0,0,.3)'; c.beginPath(); c.ellipse(cx, CY + 28, 18 - (CY - cy) * 0.15, 5, 0, 0, 6.3); c.fill();
      chicken(c, cx, cy - 2, sq, rot);
      s.feathers.forEach(function (f) { c.save(); c.translate(f.x, f.y); c.rotate(f.r); c.fillStyle = '#ffffff'; c.beginPath(); c.ellipse(0, 0, 6, 2.5, 0, 0, 6.3); c.fill(); c.restore(); });

      // интерфейс
      var curM = s.lane >= 0 && s.phase !== 'hop' ? MULTS[s.lane] : (s.lane > 0 ? MULTS[s.lane - 1] : 1);
      rr(c, 18, 16, 112, 30, 15); c.fillStyle = 'rgba(11,29,54,.85)'; c.fill();
      c.fillStyle = '#fff'; c.font = '700 12px ' + FONT; c.textAlign = 'center'; c.fillText('Medium', 74, 31);
      rr(c, W - 130, 16, 112, 40, 12); c.fillStyle = 'rgba(11,29,54,.9)'; c.fill();
      c.strokeStyle = '#16b77a'; c.lineWidth = 2; c.stroke();
      c.fillStyle = '#fff'; c.font = '800 20px ' + FONT; c.fillText('x' + curM.toFixed(2), W - 74, 36);
      var pulse = 1 + Math.sin(performance.now() / 260) * 0.03;
      c.save(); c.translate(64, 372); c.scale(pulse, pulse);
      rr(c, -52, -22, 104, 44, 12); c.fillStyle = s.lane >= 0 && s.phase !== 'hit' ? '#16b77a' : '#4a5566'; c.fill();
      c.fillStyle = '#05261a'; c.font = '800 13px ' + FONT; c.fillText('CASH OUT', 0, 1); c.restore();

      if (s.phase === 'cash' || s.phase === 'hit') {
        var a = clamp(s.t * 4, 0, 1) * clamp((2 - s.t) * 3, 0, 1);
        c.globalAlpha = a;
        rr(c, 190, 120, 260, 64, 16); c.fillStyle = s.phase === 'cash' ? '#16b77a' : '#d6453d'; c.fill();
        c.fillStyle = s.phase === 'cash' ? '#05261a' : '#fff'; c.font = '800 20px ' + FONT;
        c.fillText(s.phase === 'cash' ? 'Cashed out x' + MULTS[s.lane].toFixed(2) : 'Hit! Round over', 320, 152);
        c.globalAlpha = 1;
      }
      if (s.flash > 0) { c.fillStyle = 'rgba(214,69,61,' + (s.flash * 0.35) + ')'; c.fillRect(0, 0, W, H); }
    }
    return { update: update, draw: draw, warm: 2.2 };
  }

  /* ===================== TOWER RUSH ===================== */
  function Tower() {
    var FH = 34, FW = 128, GROUND = 372, BASEX = 240;
    var MULTS = [1, 1.25, 1.6, 2.0, 2.6, 3.2, 4.0, 5.0, 6.3, 8.0, 10.0];
    var s = { floors: [], phase: 'swing', t: 0, block: null, cam: 0, target: 5, cashOut: true, falling: [], clouds: [], time: 0 };
    for (var i = 0; i < 5; i++) s.clouds.push({ x: rand(0, W), y: rand(30, 220), w: rand(60, 120), v: rand(6, 16) });
    function windows() { var w = []; for (var k = 0; k < 4; k++) w.push(Math.random() < 0.55); return w; }
    function reset() { s.next = windows(); s.floors = []; s.phase = 'swing'; s.t = 0; s.block = null; s.target = Math.floor(rand(3, 8.99)); s.cashOut = Math.random() < 0.6; s.falling = []; }
    reset();
    function topY() { return GROUND - s.floors.length * FH; }
    function swingX() { return BASEX + Math.sin(s.time * 1.9) * 46; }
    function mastTop() { return Math.min(80, topY() - 150); }

    function update(dt) {
      s.time += dt; s.t += dt;
      s.clouds.forEach(function (cl) { cl.x += cl.v * dt; if (cl.x > W + 80) { cl.x = -cl.w; cl.y = rand(30, 220); } });
      var camTarget = Math.max(0, s.floors.length * FH - 170);
      if (s.phase === 'collapse' || s.phase === 'reset') camTarget = s.cam;
      s.cam += (camTarget - s.cam) * Math.min(1, dt * 3);
      if (s.phase === 'swing') {
        if (s.t > 1.1) { s.phase = 'drop'; s.t = 0; s.block = { x: swingX(), y: mastTop() + 36, vy: 0, tx: BASEX + rand(-7, 7), w: s.next }; }
      } else if (s.phase === 'drop') {
        var b = s.block; b.vy += 1300 * dt; b.y += b.vy * dt; b.x += (b.tx - b.x) * Math.min(1, dt * 7);
        if (b.y + FH >= topY()) {
          s.floors.push({ x: b.tx, w: b.w }); s.next = windows(); s.block = null; s.t = 0;
          s.phase = s.floors.length >= s.target ? (s.cashOut ? 'cash' : 'wobble') : 'swing';
        }
      } else if (s.phase === 'wobble') {
        if (s.t > 0.7) {
          s.phase = 'collapse'; s.t = 0;
          s.falling = s.floors.map(function (f, idx) { return { x: f.x, y: GROUND - (idx + 1) * FH, vx: rand(-60, 160) * (idx / s.floors.length + 0.2), vy: rand(-80, 0), r: 0, vr: rand(-2.5, 2.5) * (idx / s.floors.length + 0.3), w: f.w }; });
          s.floors = [];
        }
      } else if (s.phase === 'collapse') {
        s.falling.forEach(function (f) { f.vy += 900 * dt; f.x += f.vx * dt; f.y += f.vy * dt; f.r += f.vr * dt; });
        if (s.t > 1.8) { s.phase = 'reset'; s.t = 0; }
      } else if (s.phase === 'cash') { if (s.t > 2) { s.phase = 'reset'; s.t = 0; } }
      else if (s.phase === 'reset') { s.cam += (0 - s.cam) * Math.min(1, dt * 4); if (s.t > 0.6) { reset(); s.cam = 0; } }
    }

    function floor(c, x, y, w, rot) {
      c.save(); c.translate(x, y + FH / 2); if (rot) c.rotate(rot);
      var g = c.createLinearGradient(-FW / 2, 0, FW / 2, 0); g.addColorStop(0, '#f4f7fb'); g.addColorStop(1, '#c8d3e2');
      c.fillStyle = 'rgba(0,0,0,.18)'; c.fillRect(-FW / 2 + 4, -FH / 2 + 4, FW, FH);
      c.fillStyle = g; rr(c, -FW / 2, -FH / 2, FW, FH, 4); c.fill();
      c.fillStyle = '#9fb0c6'; c.fillRect(-FW / 2, -FH / 2, FW, 3);
      for (var k = 0; k < 4; k++) { c.fillStyle = w[k] ? '#ffd56b' : '#3b6fb5'; rr(c, -FW / 2 + 12 + k * 28, -FH / 2 + 10, 20, 15, 2); c.fill(); }
      c.restore();
    }

    function draw(c) {
      var sky = c.createLinearGradient(0, 0, 0, H); sky.addColorStop(0, '#3b6fb5'); sky.addColorStop(1, '#122c52');
      c.fillStyle = sky; c.fillRect(0, 0, W, H);
      var sun = c.createRadialGradient(470, 70, 5, 470, 70, 120); sun.addColorStop(0, 'rgba(255,214,107,.55)'); sun.addColorStop(1, 'rgba(255,214,107,0)');
      c.fillStyle = sun; c.fillRect(0, 0, W, H);
      s.clouds.forEach(function (cl) { c.fillStyle = 'rgba(255,255,255,.22)'; c.beginPath(); c.ellipse(cl.x, cl.y + s.cam * 0.3, cl.w / 2, 14, 0, 0, 6.3); c.ellipse(cl.x + cl.w * 0.2, cl.y - 10 + s.cam * 0.3, cl.w / 3, 14, 0, 0, 6.3); c.fill(); });

      c.save(); c.translate(0, s.cam);
      // город и земля
      c.fillStyle = 'rgba(11,29,54,.55)';
      [[20, 60], [70, 90], [130, 50], [380, 80], [440, 110], [500, 70]].forEach(function (b) { c.fillRect(b[0], GROUND - b[1], 46, b[1]); });
      c.fillStyle = '#0b1d36'; c.fillRect(0, GROUND, W, 200);
      c.fillStyle = '#16b77a'; c.fillRect(0, GROUND, W, 5);
      // кран (мачта в мире)
      var mt = mastTop();
      c.strokeStyle = '#f4a62a'; c.lineWidth = 5; c.lineCap = 'round';
      c.beginPath(); c.moveTo(460, GROUND); c.lineTo(460, mt); c.stroke();
      c.lineWidth = 1.5;
      for (var zy = GROUND; zy > mt + 20; zy -= 24) { c.beginPath(); c.moveTo(452, zy); c.lineTo(468, zy - 24); c.moveTo(468, zy); c.lineTo(452, zy - 24); c.stroke(); }
      c.lineWidth = 5; c.beginPath(); c.moveTo(150, mt + 6); c.lineTo(510, mt + 6); c.stroke();
      c.lineWidth = 2; c.beginPath(); c.moveTo(460, mt - 22); c.lineTo(200, mt + 6); c.moveTo(460, mt - 22); c.lineTo(505, mt + 6); c.stroke();
      c.fillStyle = '#5d6b7e'; c.fillRect(492, mt + 8, 22, 18);
      // крюк и блок
      if (s.phase === 'swing') {
        var hx = swingX(), hy = mt + 6;
        c.fillStyle = '#cfd8e3'; c.fillRect(hx - 8, hy - 4, 16, 8);
        c.strokeStyle = '#cfd8e3'; c.lineWidth = 2; c.beginPath(); c.moveTo(hx, hy); c.lineTo(hx, hy + 30); c.stroke();
        floor(c, hx, hy + 30, s.next, 0);
      }
      if (s.block) floor(c, s.block.x, s.block.y, s.block.w, 0);
      // башня
      var wob = s.phase === 'wobble' ? Math.sin(s.t * 40) * 0.03 * (s.t / 0.7) : 0;
      s.floors.forEach(function (f, idx) { var y = GROUND - (idx + 1) * FH; floor(c, f.x + wob * (GROUND - y), y, f.w, wob); });
      s.falling.forEach(function (f) { floor(c, f.x, f.y, f.w, f.r); });
      c.restore();

      // интерфейс
      var m = MULTS[Math.min(s.floors.length, MULTS.length - 1)];
      rr(c, 22, 20, 132, 64, 14); c.fillStyle = 'rgba(11,29,54,.88)'; c.fill(); c.strokeStyle = s.phase === 'collapse' ? '#d6453d' : '#16b77a'; c.lineWidth = 2; c.stroke();
      c.textAlign = 'center'; c.textBaseline = 'middle';
      c.fillStyle = 'rgba(255,255,255,.6)'; c.font = '600 11px ' + FONT; c.fillText('Floor ' + s.floors.length, 88, 38);
      c.fillStyle = '#fff'; c.font = '800 26px ' + FONT; c.fillText('x' + m.toFixed(2), 88, 64);
      rr(c, 22, 94, 132, 40, 12); c.fillStyle = s.floors.length && s.phase !== 'collapse' ? '#16b77a' : '#4a5566'; c.fill();
      c.fillStyle = '#05261a'; c.font = '800 13px ' + FONT; c.fillText('CASH OUT', 88, 115);
      if (s.phase === 'cash' || s.phase === 'collapse') {
        var a = clamp(s.t * 4, 0, 1) * clamp((1.9 - s.t) * 3, 0, 1);
        c.globalAlpha = a; rr(c, 170, 170, 240, 60, 16); c.fillStyle = s.phase === 'cash' ? '#16b77a' : '#d6453d'; c.fill();
        c.fillStyle = s.phase === 'cash' ? '#05261a' : '#fff'; c.font = '800 19px ' + FONT;
        c.fillText(s.phase === 'cash' ? 'Cashed out x' + MULTS[s.target].toFixed(2) : 'Tower collapsed!', 290, 200); c.globalAlpha = 1;
      }
    }
    return { update: update, draw: draw, warm: 4 };
  }

  var SCENES = { 'aviator': Aviator, 'chicken-road': Chicken, 'tower-rush': Tower };

  document.querySelectorAll('canvas[data-scene]').forEach(function (cv) {
    var make = SCENES[cv.getAttribute('data-scene')];
    if (!make || !cv.getContext) return;
    var ctx = cv.getContext('2d');
    var scene = make();
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var visible = true, raf = 0, last = 0;

    function size() {
      var r = cv.getBoundingClientRect();
      if (!r.width) return;
      cv.width = Math.round(r.width * dpr); cv.height = Math.round(r.width * 0.75 * dpr);
    }
    function render() { ctx.setTransform(cv.width / W, 0, 0, cv.height / H, 0, 0); scene.draw(ctx); }
    function frame(now) {
      var dt = Math.min(0.05, (now - last) / 1000); last = now;
      scene.update(dt); render();
      raf = (visible && !document.hidden) ? requestAnimationFrame(frame) : 0;
    }
    function start() { if (!raf && !reduce) { last = performance.now(); raf = requestAnimationFrame(frame); } }

    size();
    for (var w = 0; w < scene.warm * 30; w++) scene.update(1 / 30);
    render();
    var box = cv.closest('.game-screen'); if (box) box.classList.add('is-live');

    if ('ResizeObserver' in window) new ResizeObserver(function () { size(); render(); }).observe(cv);
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) { visible = es[0].isIntersecting; if (visible) start(); }).observe(cv);
    }
    document.addEventListener('visibilitychange', function () { if (!document.hidden && visible) start(); });
    start();
  });
})();
