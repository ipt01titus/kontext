/* Pure model helpers shared by the UI and migration checks. */
(function(root){
"use strict";
const collections={project:"projects",object:"objects",person:"people",task:"tasks",goal:"goals",event:"events"};
function ancestors(items,id){const chain=[],seen=new Set();let item=items.find(x=>x.id===id);while(item&&!seen.has(item.id)){seen.add(item.id);chain.unshift(item);item=items.find(x=>x.id===item.parent);}return chain;}
function within(items,id,parent){return ancestors(items,id).some(x=>x.id===parent);}
function ordered(items){const result=[],seen=new Set();function visit(x){if(seen.has(x.id))return;seen.add(x.id);result.push(x);items.filter(c=>c.parent===x.id).forEach(visit);}items.filter(x=>!x.parent||!items.some(p=>p.id===x.parent)).forEach(visit);items.forEach(visit);return result;}
function numberRecords(data){const records=Object.values(collections).flatMap(k=>data[k]||[]),seen=new Set();let next=Math.max(1,Number.isSafeInteger(data.nextNumber)?data.nextNumber:1,...records.map(x=>Number.isSafeInteger(x.number)&&x.number>0?x.number+1:1));for(const x of records){if(!Number.isSafeInteger(x.number)||x.number<1||seen.has(x.number))x.number=next++;seen.add(x.number);}data.nextNumber=next;}
function migrate(data){
 if(!data.hierarchyVersion){
  const add=p=>{if(!data.projects.some(x=>x.id===p.id))data.projects.push(p);};
  add({id:"mge",name:"MGE",color:"#6684a0",parent:null});
  add({id:"personal",name:"Mein Leben",color:"#7c98a2",parent:null});
  [["family","Meine Familie"],["finance","Meine Finanzen"],["investments","Meine Investments"],["friends","Meine Freunde"],["learning","Mein Lernen"],["travel","Meine Reisen und Events"],["dreams","Meine Träume"],["organisation","Meine Orga"],["purchases","Meine Einkäufe"],["sales","Meine Verkäufe"],["health","Meine Gesundheit"],["it","Meine IT"]].forEach(([id,name])=>add({id:"life-"+id,name,color:"#7c98a2",parent:"personal"}));
  const garden=data.projects.find(p=>p.id==="garten");if(garden&&!Object.hasOwn(garden,"parent"))garden.parent="personal";
  data.hierarchyVersion=1;
 }
 for(const p of data.projects){if(!Object.hasOwn(p,"parent"))p.parent=null;if(!p.description)p.description="";}
 numberRecords(data);return data;
}
root.KontextModel={collections,ancestors,within,ordered,numberRecords,migrate};
})(globalThis);
