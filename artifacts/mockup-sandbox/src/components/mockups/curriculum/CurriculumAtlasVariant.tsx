import React, { useMemo, useState } from "react";

type IconName = "grid" | "library" | "calendar" | "building" | "nodes" | "settings" | "search" | "plus" | "arrow" | "close";

const iconPaths: Record<IconName, string> = {
  grid: "M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h6v6h-6z",
  library: "M4 5.5A2.5 2.5 0 0 1 6.5 3H20v16H6.5A2.5 2.5 0 0 0 4 21.5zM4 5.5v16M8 7h8M8 11h8",
  calendar: "M5 4v3M19 4v3M4 8h16M5 5h14a1 1 0 0 1 1 1v13H4V6a1 1 0 0 1 1-1zM8 12h3M13 12h3M8 16h3",
  building: "M5 21V5l7-2 7 2v16M3 21h18M8 8h1M15 8h1M8 12h1M15 12h1M8 16h1M15 16h1M11 21v-4h2v4",
  nodes: "M6 5a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm12 6a2 2 0 1 0 0 4 2 2 0 0 0 0-4zM6 15a2 2 0 1 0 0 4 2 2 0 0 0-4zm2-8 8 5M8 17l8-4",
  settings: "M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8zm0-5v2m0 10v2m7-5h2M3 12h2m12.95-4.95 1.4-1.4M4.65 17.35l1.4-1.4m11.9 0 1.4 1.4m-14.7-11.7 1.4 1.4",
  search: "m20 20-4.5-4.5M10.8 17a6.2 6.2 0 1 0 0-12.4 6.2 6.2 0 0 0 0 12.4z",
  plus: "M12 5v14M5 12h14",
  arrow: "M5 12h13M14 8l4 4-4 4",
  close: "M6 6l12 12M18 6 6 18",
};

function Icon({ name, size = 17 }: { name: IconName; size?: number }) {
  return <svg aria-hidden="true" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round"><path d={iconPaths[name]} /></svg>;
}

const nav = [
  { label: "Overview", icon: "grid" as IconName },
  { label: "Curriculum library", icon: "library" as IconName },
  { label: "180-day calendar", icon: "calendar" as IconName },
  { label: "School building", icon: "building" as IconName },
  { label: "Verb network", icon: "nodes" as IconName },
];

const domains = [
  { name: "Attention", count: 26, tone: "ochre" },
  { name: "Memory", count: 19, tone: "sage" },
  { name: "Executive functions", count: 15, tone: "coral" },
  { name: "Visuospatial processing", count: 11, tone: "blue" },
];

function CurriculumAtlasVariant() {
  const [active, setActive] = useState("Overview");
  const [query, setQuery] = useState("");
  const [showModal, setShowModal] = useState(false);
  const [activeVariable, setActiveVariable] = useState("Math");
  const [toast, setToast] = useState("");

  const objectives = useMemo(() => [
    { code: "K.O.014", title: "Trace and name the circle", domain: "Visuospatial processing", level: "D1a", variable: "Math" },
    { code: "2.O.031", title: "Compare border motifs across cultures", domain: "Attention", level: "D2", variable: "Arts" },
    { code: "4.O.008", title: "Explain why a city builds monuments", domain: "Executive functions", level: "D3", variable: "Power" },
  ].filter(item => `${item.code} ${item.title} ${item.domain}`.toLowerCase().includes(query.toLowerCase())), [query]);

  const flash = (message: string) => {
    setToast(message);
    window.setTimeout(() => setToast(""), 2200);
  };

  return (
    <div className="atlas-shell">
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap');
        .atlas-shell{--ink:#172e3a;--muted:#6b7777;--paper:#f7f3ea;--card:#fffdf8;--line:#dedbd2;--ochre:#d79035;--coral:#c75e4c;--sage:#718c79;--blue:#64869b;background:var(--paper);color:var(--ink);font-family:Manrope,sans-serif;min-height:100dvh;display:flex;overflow:hidden}
        .atlas-shell *{box-sizing:border-box}.atlas-sidebar{width:220px;min-width:220px;padding:28px 16px 22px;border-right:1px solid var(--line);background:#f0eee5;display:flex;flex-direction:column;justify-content:space-between}
        .atlas-mark{display:flex;align-items:center;gap:10px;padding:0 10px 34px}.atlas-seal{width:30px;height:30px;border-radius:50%;background:var(--ink);color:var(--paper);display:grid;place-items:center;font-family:Georgia,serif;font-size:16px}.atlas-brand{font-size:12px;line-height:1.1;font-weight:800;letter-spacing:.08em;text-transform:uppercase}
        .atlas-brand span{display:block;color:var(--ochre);font-family:"DM Mono",monospace;font-size:8px;letter-spacing:.16em;margin-top:4px}
        .atlas-kicker{font:500 9px "DM Mono",monospace;letter-spacing:.13em;text-transform:uppercase;color:#8a8d83;padding:0 12px 10px}.atlas-nav{display:grid;gap:4px}.atlas-nav button{border:0;background:transparent;color:#667171;text-align:left;width:100%;display:flex;gap:11px;align-items:center;padding:11px 12px;border-radius:7px;font:600 11px Manrope;cursor:pointer}.atlas-nav button:hover{background:#e6e4db;color:var(--ink)}.atlas-nav button.active{background:var(--ink);color:var(--paper);box-shadow:4px 4px 0 #d4cfc3}.atlas-rail-note{border-top:1px solid var(--line);padding:18px 11px 0;color:#7b817b;font-size:10px;line-height:1.6}.atlas-rail-note strong{display:block;color:var(--ink);font-size:11px;margin-bottom:5px}
        .atlas-main{flex:1;min-width:0;overflow:auto;padding:35px clamp(22px,4vw,64px) 44px}.atlas-top{display:flex;align-items:flex-start;justify-content:space-between;gap:22px;margin-bottom:35px}.atlas-eyebrow{font:500 10px "DM Mono",monospace;letter-spacing:.14em;text-transform:uppercase;color:var(--coral);margin-bottom:10px}.atlas-title{font:700 clamp(28px,4vw,44px) "Playfair Display",Georgia,serif;letter-spacing:-.03em;line-height:1.04;margin:0}.atlas-subtitle{font-size:12px;color:var(--muted);margin:11px 0 0;max-width:520px}.atlas-actions{display:flex;gap:8px;align-items:center}.atlas-button{border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:5px;padding:10px 13px;display:flex;align-items:center;gap:8px;font:700 10px Manrope;cursor:pointer}.atlas-button:hover{border-color:var(--ink);transform:translateY(-1px)}.atlas-button.primary{background:var(--ochre);border-color:var(--ochre);color:#fffaf0}
        .atlas-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:31px}.atlas-stat{background:var(--card);border:1px solid var(--line);border-top:3px solid var(--ochre);padding:15px 17px 16px;min-height:90px}.atlas-stat:nth-child(2){border-top-color:var(--sage)}.atlas-stat:nth-child(3){border-top-color:var(--coral)}.atlas-stat:nth-child(4){border-top-color:var(--blue)}.atlas-stat-label{font:500 9px "DM Mono",monospace;text-transform:uppercase;letter-spacing:.08em;color:#88908a}.atlas-stat-value{font:700 27px "Playfair Display",serif;margin:8px 0 1px}.atlas-stat-note{font-size:9px;color:var(--muted)}
        .atlas-grid{display:grid;grid-template-columns:minmax(0,1.28fr) minmax(270px,.72fr);gap:14px}.atlas-panel{background:var(--card);border:1px solid var(--line);padding:22px}.atlas-panel-head{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:19px}.atlas-panel h2{font:700 18px "Playfair Display",serif;margin:0}.atlas-panel-caption{font-size:10px;color:var(--muted);margin-top:5px}.atlas-link{border:0;background:transparent;color:var(--coral);font:700 10px Manrope;cursor:pointer;padding:3px 0}.atlas-link:hover{text-decoration:underline}
        .atlas-search{display:flex;align-items:center;gap:8px;border-bottom:1px solid var(--line);padding:0 0 10px;color:#8c9690;margin-bottom:14px}.atlas-search input{border:0;outline:0;background:transparent;width:100%;font:500 11px Manrope;color:var(--ink)}.atlas-objective{display:grid;grid-template-columns:66px 1fr auto;gap:12px;align-items:center;padding:13px 0;border-bottom:1px solid #ebe8df}.atlas-objective:last-child{border-bottom:0}.atlas-code{font:500 10px "DM Mono",monospace;color:var(--coral)}.atlas-objective-title{font-size:11px;font-weight:700}.atlas-objective-meta{font-size:9px;color:var(--muted);margin-top:4px}.atlas-level{font:500 9px "DM Mono",monospace;color:var(--ink);background:#e5ede5;padding:5px 6px;border-radius:3px}.atlas-empty{font-size:11px;color:var(--muted);padding:20px 0}
        .atlas-domain{display:grid;grid-template-columns:1fr 45px;gap:8px;align-items:center;margin:17px 0}.atlas-domain-top{display:flex;justify-content:space-between;font-size:10px;font-weight:700;margin-bottom:7px}.atlas-domain-top span:last-child{font:500 10px "DM Mono",monospace;color:var(--muted)}.atlas-bar{height:5px;background:#e8e5dc;border-radius:3px;overflow:hidden}.atlas-bar i{display:block;height:100%;border-radius:3px}.atlas-domain-count{text-align:right;font:500 18px "Playfair Display",serif}.atlas-variable-panel{grid-column:1/-1;display:grid;grid-template-columns:1fr 1.5fr;gap:26px;margin-top:0}.atlas-tabs{display:flex;gap:6px;flex-wrap:wrap;margin-top:16px}.atlas-tab{border:1px solid var(--line);border-radius:20px;background:transparent;padding:8px 11px;font:600 10px Manrope;color:var(--muted);cursor:pointer}.atlas-tab.selected{background:var(--ink);border-color:var(--ink);color:var(--paper)}.atlas-insight{background:#f0e9da;border-left:3px solid var(--ochre);padding:17px 18px;margin-top:10px}.atlas-insight-label{font:500 9px "DM Mono",monospace;letter-spacing:.1em;text-transform:uppercase;color:var(--ochre)}.atlas-insight p{font:700 14px "Playfair Display",serif;line-height:1.35;margin:7px 0 0}.atlas-modal-backdrop{position:fixed;inset:0;background:rgba(23,46,58,.35);display:grid;place-items:center;padding:20px;z-index:3}.atlas-modal{width:min(420px,100%);background:var(--card);border:1px solid var(--line);box-shadow:10px 10px 0 rgba(23,46,58,.15);padding:24px}.atlas-modal h3{font:700 22px "Playfair Display",serif;margin:0 0 18px}.atlas-modal label{display:block;font:500 10px "DM Mono",monospace;text-transform:uppercase;color:var(--muted);margin:13px 0 6px}.atlas-modal input,.atlas-modal select{width:100%;padding:10px;border:1px solid var(--line);background:#faf8f1;font:500 11px Manrope;color:var(--ink)}.atlas-modal-actions{display:flex;justify-content:flex-end;gap:8px;margin-top:21px}.atlas-toast{position:fixed;right:24px;bottom:24px;background:var(--ink);color:var(--paper);padding:11px 15px;font-size:11px;border-radius:4px;box-shadow:5px 5px 0 var(--ochre);z-index:4}
        @media(max-width:800px){.atlas-shell{display:block;overflow:auto}.atlas-sidebar{width:100%;min-width:0;padding:16px 14px;border-right:0;border-bottom:1px solid var(--line);display:block}.atlas-mark{padding:0 4px 15px}.atlas-rail-note{display:none}.atlas-kicker{display:none}.atlas-nav{display:flex;overflow:auto;gap:4px}.atlas-nav button{white-space:nowrap;padding:9px 10px}.atlas-main{padding:27px 16px 35px}.atlas-top{display:block;margin-bottom:25px}.atlas-actions{margin-top:18px}.atlas-stats{grid-template-columns:repeat(2,1fr)}.atlas-grid{grid-template-columns:1fr}.atlas-variable-panel{grid-column:auto;grid-template-columns:1fr}.atlas-panel{padding:17px}.atlas-objective{grid-template-columns:57px 1fr auto}}
      `}</style>
      <aside className="atlas-sidebar">
        <div>
          <div className="atlas-mark"><div className="atlas-seal">S</div><div className="atlas-brand">Mesa / Phoenix<span>Curriculum atlas</span></div></div>
          <div className="atlas-kicker">Workspace</div>
          <nav className="atlas-nav">{nav.map(item => <button key={item.label} className={active === item.label ? "active" : ""} onClick={() => { setActive(item.label); flash(`${item.label} view selected`); }}><Icon name={item.icon} />{item.label}</button>)}</nav>
        </div>
        <div className="atlas-rail-note"><strong>2025—26 school year</strong>Twice weekly SDA practice<br />Arizona Common Core, every day</div>
      </aside>
      <main className="atlas-main">
        <header className="atlas-top"><div><div className="atlas-eyebrow">Field notes / 01</div><h1 className="atlas-title">{active === "Overview" ? "The curriculum at a glance." : active}</h1><p className="atlas-subtitle">A living map of cultural innovation across K–8 — standards, stories, and the hands that make things.</p></div><div className="atlas-actions"><button className="atlas-button" onClick={() => flash("Export prepared for download")}><Icon name="arrow" size={15} /> Export map</button><button className="atlas-button primary" onClick={() => setShowModal(true)}><Icon name="plus" size={15} /> Add objective</button></div></header>
        <section className="atlas-stats"><div className="atlas-stat"><div className="atlas-stat-label">Total nodes</div><div className="atlas-stat-value">184</div><div className="atlas-stat-note">+12 since last review</div></div><div className="atlas-stat"><div className="atlas-stat-label">Relationships</div><div className="atlas-stat-value">327</div><div className="atlas-stat-note">Across 9 cognitive domains</div></div><div className="atlas-stat"><div className="atlas-stat-label">Node types</div><div className="atlas-stat-value">14</div><div className="atlas-stat-note">Standards to story prompts</div></div><div className="atlas-stat"><div className="atlas-stat-label">Objectives</div><div className="atlas-stat-value">71</div><div className="atlas-stat-note">Mapped to grade + week</div></div></section>
        <section className="atlas-grid">
          <div className="atlas-panel"><div className="atlas-panel-head"><div><h2>Recent objectives</h2><div className="atlas-panel-caption">The newest entries in the working library</div></div><button className="atlas-link" onClick={() => { setActive("Curriculum library"); flash("Library view selected"); }}>View library <Icon name="arrow" size={12} /></button></div><div className="atlas-search"><Icon name="search" size={15} /><input value={query} onChange={e => setQuery(e.target.value)} placeholder="Search objectives, eras, or concepts" /></div>{objectives.map(o => <div className="atlas-objective" key={o.code}><div className="atlas-code">{o.code}</div><div><div className="atlas-objective-title">{o.title}</div><div className="atlas-objective-meta">{o.domain} · {o.variable}</div></div><div className="atlas-level">{o.level}</div></div>)}{objectives.length === 0 && <div className="atlas-empty">No objectives match that search.</div>}</div>
          <div className="atlas-panel"><div className="atlas-panel-head"><div><h2>Cognitive domains</h2><div className="atlas-panel-caption">Where attention is landing</div></div><button className="atlas-link" onClick={() => flash("Domain report opened")}>Full report <Icon name="arrow" size={12} /></button></div>{domains.map((d, i) => <div className="atlas-domain" key={d.name}><div><div className="atlas-domain-top"><span>{d.name}</span><span>{[41, 30, 23, 17][i]}%</span></div><div className="atlas-bar"><i style={{ width: `${[82, 60, 46, 34][i]}%`, background: `var(--${d.tone})` }} /></div></div><div className="atlas-domain-count">{d.count}</div></div>)}</div>
          <div className="atlas-panel atlas-variable-panel"><div><div className="atlas-eyebrow">The four forces</div><h2>Variables in conversation</h2><div className="atlas-panel-caption">Two variables make a work square. Four make an invention moment.</div><div className="atlas-tabs">{["Math", "Arts", "Mythology", "Power"].map(v => <button key={v} className={`atlas-tab ${activeVariable === v ? "selected" : ""}`} onClick={() => setActiveVariable(v)}>{v}</button>)}</div></div><div className="atlas-insight"><div className="atlas-insight-label">Current lens / {activeVariable}</div><p>{activeVariable === "Math" ? "Patterns become rules, then predictions." : activeVariable === "Arts" ? "Beauty is a record of what a culture values." : activeVariable === "Mythology" ? "Stories give a structure to the unknown." : "Every object has a maker, a funder, and a gatekeeper."}</p></div></div>
        </section>
      </main>
      {showModal && <div className="atlas-modal-backdrop" onClick={() => setShowModal(false)}><div className="atlas-modal" onClick={e => e.stopPropagation()}><div style={{display:"flex",justifyContent:"space-between",alignItems:"start"}}><h3>Add an objective</h3><button className="atlas-link" onClick={() => setShowModal(false)}><Icon name="close" /></button></div><label>Objective code</label><input placeholder="e.g. 3.O.042" /><label>What will students do?</label><input placeholder="Write a clear, observable action" /><label>Dimensional level</label><select defaultValue="D2"><option>D1a — atomic</option><option>D2 — how</option><option>D3 — why</option><option>D4 — what-if</option></select><div className="atlas-modal-actions"><button className="atlas-button" onClick={() => setShowModal(false)}>Cancel</button><button className="atlas-button primary" onClick={() => { setShowModal(false); flash("Objective added to the atlas"); }}>Save objective</button></div></div></div>}
      {toast && <div className="atlas-toast">{toast}</div>}
    </div>
  );
}

export default CurriculumAtlasVariant;