const {chromium}=require('playwright');
// node frames.js query outdir fps [onlyT]
(async()=>{const [q,out,fps,only]=process.argv.slice(2);const fs=require('fs');fs.mkdirSync(out,{recursive:true});
const b=await chromium.launch({args:['--disable-gpu','--disable-accelerated-2d-canvas','--disable-gpu-compositing']});const p=await b.newPage({viewport:{width:1080,height:1080}});
await p.goto('file://'+__dirname+'/anim.html?'+q);p.on('pageerror',e=>console.log('ERR',e.message));await p.waitForFunction(()=>window.ready===1,null,{timeout:120000});
const T=await p.evaluate('T');const n=only!==undefined?1:Math.round(T*fps);
for(let i=0;i<n;i++){const t=only!==undefined?+only:i/fps;await p.evaluate(t=>draw(t),t);
 await (await p.$('canvas')).screenshot({path:`${out}/f${String(i).padStart(4,'0')}.jpg`,type:'jpeg',quality:92});}
await b.close();})();
