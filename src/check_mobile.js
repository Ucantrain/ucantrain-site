// Phone-layout check. Serve the repo root first:  python3 -m http.server 8765
// then: node src/check_mobile.js [url] [--shots]
// Prints, per width, any element wider than the screen ('wide') and any word split across lines ('broken'). Both should be empty.
const {chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch();
 for (const w of [360,390,430,768]){
  const p=await b.newPage({viewport:{width:w,height:800},deviceScaleFactor:1});
  await p.goto('process.argv[2] || 'http://127.0.0.1:8765/''); await p.waitForTimeout(800);
  const r=await p.evaluate(()=>{
    const out={docW:document.documentElement.scrollWidth, wide:[], broken:[]};
    document.querySelectorAll('body *').forEach(e=>{const rc=e.getBoundingClientRect(); if(rc.right>innerWidth+1 && rc.width>0) out.wide.push(e.tagName+'.'+e.className+' '+Math.round(rc.right));});
    // detect words split across lines
    const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
    let n; while(n=walker.nextNode()){ const t=n.textContent; const re=/\S+/g; let m;
      while(m=re.exec(t)){ if(m[0].length<4) continue; const rg=document.createRange(); rg.setStart(n,m.index); rg.setEnd(n,m.index+m[0].length); const rs=[...rg.getClientRects()].filter(x=>x.width>0); const tops=new Set(rs.map(x=>Math.round(x.top))); if(tops.size>1) out.broken.push(m[0]); } }
    return out;});
  console.log(w, JSON.stringify(r).slice(0,1500));
  if (process.argv.includes('--shots')) await p.screenshot({path:`m${w}.png`,fullPage:true});
 }
 await b.close();})();
