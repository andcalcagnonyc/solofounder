import asyncio, json, sys, subprocess, time, re
from playwright.async_api import async_playwright
BASE="http://127.0.0.1:8765/index.html"
STUB = """
(() => {
  const KEY='__stubdb';
  const load=()=>JSON.parse(sessionStorage.getItem(KEY)||'{}'), save=o=>sessionStorage.setItem(KEY,JSON.stringify(o));
  window.__writes=0; window.__samplePrompts=[];
  const doc=path=>({id:path.split('/').pop(),path,
    async get(){const d=load()[path];return {exists:!!d,data:()=>d,metadata:{}}},
    async set(data){if(typeof data!=='object'||Array.isArray(data))throw {code:'invalid_argument'};JSON.stringify(data);const o=load();o[path]=JSON.parse(JSON.stringify(data));save(o);window.__writes++},
    collection(c){return coll(path+'/'+c)}});
  const coll=path=>({path,doc(id){return doc(path+'/'+id)}});
  const db={doc(p){if(p.split('/').length%2)throw new TypeError('odd');return doc(p)},collection(p){if(p.split('/').length%2===0)throw new TypeError('even');return coll(p)}};
  const user={id:async()=>'u_test1',isOwner:async()=>true};
  const sample=async(input,opts)=>{window.__samplePrompts.push(input);const full=window.__sampleText||'## Where this stands\\nDraft **ok**.\\n\\n- one\\n- two\\n\\n| a | b |\\n|---|---|\\n| 1 | 2 |\\n\\n<img src=x onerror="window.__xss=1">';
     opts&&opts.onText&&opts.onText({text:full.slice(0,10)});await new Promise(r=>setTimeout(r,30));opts&&opts.onText&&opts.onText({text:full});return {text:full,truncated:false}};
  window.claude={use:async n=>({db,user,sample}[n]||null)};
})();
"""
results=[]
def check(name, cond, detail=""):
    results.append((name,bool(cond),detail)); print(("PASS" if cond else "FAIL"), name, detail if not cond else "")

async def ready(page):
    await page.wait_for_function("window.__ready===true", timeout=15000)

async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        # ---------- A: local-only (no claude object) ----------
        ctx=await b.new_context(viewport={"width":1280,"height":820})
        page=await ctx.new_page(); errs=[]
        page.on("console", lambda m: errs.append(m.text) if m.type=="error" else None)
        page.on("pageerror", lambda e: errs.append(str(e)))
        await page.goto(BASE); await ready(page)
        check("loads on Setup first", await page.locator(".form h1").inner_text()=="Location and legal")
        check("57 skills loaded", await page.evaluate("DATA.skills.length")==57)
        check("9 functions in sidebar", await page.locator(".nav a[href^='#area-']").count()==9)
        check("save indicator says browser", "this browser" in await page.locator("#save").inner_text())
        # validation
        await page.click("[data-a=setup-next]")
        check("HQ required: error shown", await page.locator(".f .err").count()==1 and await page.evaluate("S.setup.step")==0)
        await page.fill("#f-hq_country","Italy"); await page.fill("#f-hq_region","Milan")
        await page.click("[data-a=seg][data-k=incorporated][data-v=No]")
        check("conditional field appears", await page.locator("[data-k=open_abroad]").count()==3 and await page.locator("#f-legal_form").count()==0)
        check("typed values survive re-render", await page.input_value("#f-hq_country")=="Italy")
        await page.fill("#f-tax_residence","Italy"); await page.fill("#f-citizenship","Italian"); await page.fill("#f-customer_countries","Italy, Spain")
        await page.click("[data-a=setup-next]")
        await page.fill("#f-name","Contabil.ai <b>x</b>"); await page.fill("#f-one_liner","Month-end closings for small accounting firms")
        await page.click("[data-a=seg][data-v='Agentic AI']"); await page.click("[data-a=seg][data-v=Prototype]"); await page.click("[data-a=seg][data-v=Angels]")
        check("sidebar shows company name escaped", await page.locator(".ws b").inner_text()=="Contabil.ai <b>x</b>" and await page.locator(".ws b b").count()==0)
        await page.click("[data-a=setup-next]")
        await page.fill("#f-hours","20"); await page.fill("#f-budget","5,000 EUR")
        await page.click("[data-a=seg][data-v=Personal]")
        await page.click("[data-a=setup-next]")
        mdtxt=await page.locator("#profile-md").inner_text()
        check("profile has HQ and TBD", "HQ country (state / province / city): Italy (Milan)" in mdtxt and "Legal form: TBD" in mdtxt)
        flags=await page.locator(".flag").all_inner_texts()
        check("flags: not incorporated, personal data, hours", any("not incorporated" in f for f in flags) and any("personal data" in f for f in flags) and any("20 hours" in f for f in flags), str(flags))
        check("next skills recommended", await page.locator(".next .row").count()>=2 and "Entity Formation" in await page.locator(".next").inner_text())
        await page.click("[data-a=setup-finish]")
        check("setup done, decision logged, start in progress", await page.evaluate("S.setup.done && S.decisions.length===1 && S.runs.start.status==='progress'"))
        # sprint
        await page.click("a.btn.pri[href='#sprint']"); await page.wait_for_selector(".rail")
        check("rail has 14 days and 5 gates", await page.locator(".rail button").count()==14 and await page.locator(".rail .g").count()==5)
        nrows=await page.locator("#view a.row").count()
        check("sprint lists every skill once or more", nrows>=57, str(nrows))
        check("all 57 skills scheduled", await page.evaluate("new Set(DATA.days.flatMap(d=>d.skills).concat(DATA.later.flatMap(l=>l.skills))).size")==57)
        await page.click("[data-a=start-sprint]")
        check("sprint started day 1", await page.evaluate("sprintDay()")==1 and await page.locator(".rail .today").count()==1)
        await page.locator("[data-a=cycle][data-n=legal-entity-formation]").first.click()
        check("status cycle works without navigating", await page.evaluate("S.runs['legal-entity-formation'].status")=="todo" and "sprint" in page.url)
        # skill page
        await page.locator("a.row[href='#skill-legal-entity-formation']").first.click(); await page.wait_for_selector(".doc h1")
        check("skill page renders", await page.locator(".doc h1").inner_text()=="Entity Formation" and await page.locator(".steps").count()==3)
        check("no draft button without Claude", await page.locator("[data-a=draft]").count()==0 and await page.locator("[data-a=copy-prompt]").count()==1)
        await page.click("[data-a=begin]")
        check("begin sets in progress and marks current step", await page.locator(".step.cur").count()==1)
        await page.click("[data-a=next-step]"); await page.click("[data-a=next-step]")
        check("guided next-step completes steps in order", await page.evaluate("S.runs['legal-entity-formation'].steps.slice(0,3).join()")=="true,true,false")
        await page.locator(".steps").nth(1).locator(".step").first.click()
        await page.locator(".gates .step").first.click()
        check("approval adds a decision", await page.evaluate("S.decisions.some(d=>d.key==='legal-entity-formation:0')"))
        await page.locator(".gates .step").first.click()
        check("un-approving removes the decision", not await page.evaluate("S.decisions.some(d=>d.key==='legal-entity-formation:0')"))
        await page.fill("#notes","Notary booked for Tuesday")
        await page.click("[data-a=finish]")
        check("finish asks when items open", await page.locator(".confirm").count()==1 and await page.evaluate("S.runs['legal-entity-formation'].status")=="progress")
        await page.click("[data-a=finish-yes]")
        check("marked done", await page.evaluate("S.runs['legal-entity-formation'].status")=="done")
        check("function progress updated", "1/9" in await page.locator(".nav a[href='#area-legal']").inner_text())
        prompt=await page.evaluate("copyPrompt(SK['legal-entity-formation'])")
        check("copy prompt names plugin skill and profile", "solofounder-os plugin skill `legal-entity-formation`" in prompt and "Italy (Milan)" in prompt and "Notary booked" in prompt)
        # reload persistence (local)
        await page.reload(); await ready(page)
        check("reload restores state locally", await page.evaluate("S.runs['legal-entity-formation'].status==='done' && S.runs['legal-entity-formation'].notes==='Notary booked for Tuesday' && S.profile.hq_country==='Italy'"))
        check("reload keeps skill route", await page.locator(".doc h1").inner_text()=="Entity Formation")
        # palette
        await page.keyboard.press("Control+k"); await page.keyboard.type("bookkeep"); await page.keyboard.press("Enter")
        await page.wait_for_function("location.hash==='#skill-finance-bookkeeping-and-close'")
        check("command palette search navigates", True)
        check("jurisdiction note on finance skill", "locally licensed" in await page.locator(".doc").inner_text())
        # decisions manual
        await page.goto(BASE+"#decisions"); await ready(page)
        await page.fill("#dec-text","Bootstrap until pilot converts"); await page.fill("#dec-why","Keep control"); await page.keyboard.press("Enter")
        check("manual decision added", await page.locator(".declist .row").count()==2)
        # active view
        await page.goto(BASE+"#active"); await ready(page)
        check("active view lists in-progress and activity", "In progress" in await page.locator("#view").inner_text() and "Recent activity" in await page.locator("#view").inner_text())
        # themes & contrast
        def contrast_js(): return """
        (()=>{const c=document.createElement('canvas').getContext('2d',{willReadFrequently:true});const rgb=v=>{c.clearRect(0,0,1,1);c.fillStyle='#000';c.fillStyle=v;c.fillRect(0,0,1,1);return [...c.getImageData(0,0,1,1).data].slice(0,3)};
        const L=a=>{const f=a.map(x=>{x/=255;return x<=.03928?x/12.92:((x+.055)/1.055)**2.4});return .2126*f[0]+.7152*f[1]+.0722*f[2]};
        const cr=(a,b)=>{const x=L(rgb(a)),y=L(rgb(b));return (Math.max(x,y)+.05)/(Math.min(x,y)+.05)};
        const s=getComputedStyle(document.documentElement),g=n=>s.getPropertyValue(n).trim();
        const probe=document.createElement('div');document.body.appendChild(probe);const res=n=>{probe.style.color='var('+n+')';return getComputedStyle(probe).color};
        const o={tx:cr(res('--tx'),res('--bg')),tx2:cr(res('--tx2'),res('--bg')),tx3:cr(res('--tx3'),res('--bg')),tx2panel:cr(res('--tx2'),res('--panel')),accentTx:cr(res('--accent-tx'),res('--bg')),accentTxSoft:cr(res('--accent-tx'),res('--accent-soft')),onAccent:cr('#fff',res('--accent'))};probe.remove();return o})()"""
        worst={}
        for theme in ["light","dark"]:
            for pal in ["iris","ember","pine","tide","plum"]:
                await page.evaluate(f"S.prefs.theme='{theme}';S.prefs.palette='{pal}';applyPrefs()")
                c=await page.evaluate(contrast_js())
                for k,v in c.items(): worst[k]=min(worst.get(k,99),v)
                ok = c["tx"]>=7 and c["tx2"]>=4.5 and c["tx2panel"]>=4.5 and c["accentTx"]>=4.5 and c["accentTxSoft"]>=4.5 and c["onAccent"]>=4.5 and c["tx3"]>=3
                check(f"contrast {theme}/{pal}", ok, json.dumps({k:round(v,2) for k,v in c.items()}))
        print("worst contrast", {k:round(v,2) for k,v in worst.items()})
        await page.click("[data-a=pop]"); await page.click("[data-a=theme][data-v=dark]"); await page.click("[data-a=palette-set][data-v=pine]")
        check("appearance popover sets theme + palette", await page.evaluate("document.documentElement.dataset.theme==='dark' && document.documentElement.dataset.palette==='pine'"))
        await page.reload(); await ready(page)
        check("appearance persists after reload", await page.evaluate("document.documentElement.dataset.theme==='dark' && document.documentElement.dataset.palette==='pine'"))
        check("no console errors (local run)", not errs, str(errs[:3]))
        # screenshots
        await page.goto(BASE+"#sprint"); await ready(page); await page.screenshot(path="/home/claude/apptest/sprint-dark-pine.png")
        await page.evaluate("S.prefs.theme='light';S.prefs.palette='iris';applyPrefs()")
        await page.goto(BASE+"#skill-legal-commercial-contracts"); await ready(page); await page.click("[data-a=begin]"); await page.click("[data-a=next-step]"); await page.screenshot(path="/home/claude/apptest/skill-light-iris.png")
        await page.goto(BASE+"#setup"); await ready(page); await page.click("[data-a=setup-step][data-i='0']"); await page.screenshot(path="/home/claude/apptest/setup-light.png")
        await ctx.close()

        # ---------- B: with Claude capabilities ----------
        ctx=await b.new_context(viewport={"width":1280,"height":820}); await ctx.add_init_script(STUB)
        page=await ctx.new_page(); errs=[]
        page.on("console", lambda m: errs.append(m.text) if m.type=="error" else None); page.on("pageerror", lambda e: errs.append(str(e)))
        await page.goto(BASE); await ready(page)
        check("cloud: indicator says Claude account", "Claude account" in await page.locator("#save").inner_text())
        check("cloud: nothing written on load", await page.evaluate("window.__writes")==0)
        await page.fill("#f-hq_country","Singapore"); await page.fill("#f-hq_region","x"); await page.fill("#f-hq_region","")
        await page.wait_for_function("window.__writes>=1", timeout=5000)
        w=await page.evaluate("window.__writes")
        check("cloud: typing is batched into few writes", w<=2, str(w))
        doc=await page.evaluate("JSON.parse(sessionStorage.getItem('__stubdb'))['data/users/u_test1/workspace']")
        check("cloud: saved doc holds profile at private per-user path", doc and doc["profile"]["hq_country"]=="Singapore")
        await page.evaluate("localStorage.clear()"); await page.reload(); await ready(page)
        check("cloud: restores on a device with empty browser storage", await page.evaluate("S.profile.hq_country")=="Singapore" and await page.input_value("#f-hq_country")=="Singapore")
        await page.goto(BASE+"#skill-ops-incident-response"); await ready(page)
        check("cloud: draft button visible", await page.locator("[data-a=draft]").count()==1)
        await page.fill("#notes","61 refunds across 9 customers"); await page.click("[data-a=draft]")
        await page.wait_for_function("document.querySelector('#out table')!==null", timeout=5000)
        out=await page.locator("#out").inner_html()
        check("draft renders markdown", "<strong>ok</strong>" in out and "<li>one</li>" in out and "<th>a</th>" in out)
        check("draft output is escaped (no script injection)", await page.locator("#out img").count()==0 and not await page.evaluate("window.__xss"))
        pr=await page.evaluate("window.__samplePrompts[0]")
        check("draft prompt carries skill, profile, notes, guardrails", "Incident Response" in pr and "Singapore" in pr and "61 refunds" in pr and "do not invent" in pr and "no web access" in pr)
        await page.wait_for_function("!!JSON.parse(sessionStorage.getItem('__stubdb'))['data/users/u_test1/workspace/outputs/ops-incident-response']", timeout=5000)
        await page.evaluate("localStorage.clear()"); await page.reload(); await ready(page)
        await page.wait_for_selector("#out table", timeout=5000)
        check("draft is saved and restored", True)
        lp=await page.evaluate("draftPrompt(SK['legal-entity-formation'])")
        check("legal draft prompt forbids stating rules as fact", "Do not state jurisdiction-specific rules" in lp and "locally licensed lawyer" in lp)
        check("no console errors (cloud run)", not errs, str(errs[:3]))
        await ctx.close()

        # ---------- C: phone ----------
        ctx=await b.new_context(viewport={"width":390,"height":780}); page=await ctx.new_page(); errs=[]
        page.on("pageerror", lambda e: errs.append(str(e)))
        for h in ["setup","sprint","skill-legal-entity-formation","area-sales","decisions","profile","active"]:
            await page.goto(BASE+"#"+h); await ready(page)
            ov=await page.evaluate("document.documentElement.scrollWidth>document.documentElement.clientWidth || document.getElementById('scroll').scrollWidth>document.getElementById('scroll').clientWidth+1")
            check(f"phone: no sideways scroll on {h}", not ov)
        await page.click("[data-a=menu]"); await page.wait_for_timeout(300)
        check("phone: drawer opens", await page.evaluate("document.getElementById('side').getBoundingClientRect().left")>=0)
        await page.screenshot(path="/home/claude/apptest/phone-drawer.png")
        await page.click(".nav a[href='#sprint']"); await page.wait_for_timeout(300)
        check("phone: drawer closes on navigate", await page.evaluate("document.getElementById('side').getBoundingClientRect().right")<=0)
        await page.screenshot(path="/home/claude/apptest/phone-sprint.png")
        check("no page errors (phone)", not errs, str(errs[:3]))
        await b.close()
    fails=[r for r in results if not r[1]]
    json.dump({"total":len(results),"passed":len(results)-len(fails),"failed":[f[0]+" :: "+f[2] for f in fails]}, open("/home/claude/apptest/results.json","w"), indent=1)
    print(f"\n{len(results)-len(fails)}/{len(results)} passed")
asyncio.run(main())
