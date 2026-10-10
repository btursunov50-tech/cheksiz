const path=require('path'),fs=require('fs'),{chromium}=require('playwright');
(async()=>{const [page,out,secs,fps='30',only]=process.argv.slice(2);fs.mkdirSync(out,{recursive:true});
const times=only?only.split(',').map(Number):[...Array(Math.round(+secs*+fps)).keys()].map(i=>i/+fps);
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+path.resolve(page));await p.waitForTimeout(1200);
for(let i=0;i<times.length;i++){await p.evaluate(t=>setT(t),times[i]);
 await p.screenshot({path:path.join(out,(only?'p':'f')+String(i).padStart(5,'0')+'.jpg'),type:'jpeg',quality:90});}
await b.close();})();
