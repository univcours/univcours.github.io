/* UnivCours — network-first navigation worker.
   We deliberately never cache private documents, URLs containing access keys,
   or decrypted PDF data. Only static HTML can be kept for offline fallback. */
"use strict";
const CACHE_NAME="univcours-html-network-first-v1";
const ROOT="/econometrie-s5-2026/";

self.addEventListener("install",event=>{
 event.waitUntil(self.skipWaiting());
});

self.addEventListener("activate",event=>{
 event.waitUntil((async()=>{
  const keys=await caches.keys();
  await Promise.all(keys.filter(name=>name.startsWith("univcours-html-")&&name!==CACHE_NAME).map(name=>caches.delete(name)));
  await self.clients.claim();
 })());
});

self.addEventListener("fetch",event=>{
 const request=event.request;
 if(request.mode!=="navigate"||request.method!=="GET")return;
 const target=new URL(request.url);
 if(target.origin!==self.location.origin||!target.pathname.startsWith(ROOT))return;
 // PDF, media, encrypted files, API requests: not intercepted.
 if(!target.pathname.endsWith("/")&&!target.pathname.endsWith(".html"))return;
 event.respondWith((async()=>{
  try{
   const fresh=new URL(request.url);
   fresh.searchParams.set("_navfresh",String(Date.now()));
   const response=await fetch(new Request(fresh.toString(),{
    method:"GET",mode:"same-origin",credentials:"same-origin",
    redirect:"follow",cache:"no-store"
   }));
   if(!response.ok)throw new Error("HTTP "+response.status);
   const c=await caches.open(CACHE_NAME);
   // HTML only. The private access fragment never reaches the network.
   await c.put(ROOT+"index.html",response.clone());
   return response;
  }catch(error){
   const c=await caches.open(CACHE_NAME);
   const fallback=await c.match(ROOT+"index.html");
   if(fallback)return fallback;
   return new Response('<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>UnivCours — Hors ligne</title><p>Connexion indisponible. Veuillez réessayer une fois la connexion rétablie.</p>',{
     status:503,headers:{"Content-Type":"text/html; charset=utf-8","Cache-Control":"no-store"}
   });
  }
 })());
});
