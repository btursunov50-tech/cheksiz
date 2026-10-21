const path=require('path'),fs=require('fs');const {chromium}=require('playwright');
(async()=>{const[page,out,sec,fps='30',only]=process.argv.slice(2);fs.mkdirSync(out,{recursive:true});
const times=only?only.split(',').map(Number):[...Array(Math.round(sec*fps)).keys()].map(i=>i/fps);
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});await p.goto('file://'+path.resolve(page));await p.waitForTimeout(300);
for(let i=0;i<times.length;i++){await p.evaluate(t=>setT(t),times[i]);await p.screenshot({path:path.join(out,String(i).padStart(4,'0')+'.png'),omitBackground:true});}
await b.close();})();
