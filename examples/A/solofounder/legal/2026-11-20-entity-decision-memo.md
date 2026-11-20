# Entity Decision Memo: Contabil.ai

_Date: 2026-11-20. DRAFT for review by a locally licensed lawyer and tax adviser in each jurisdiction named. Not legal or tax advice. Nothing here has been filed, signed, or paid._

## 1. Facts relied on (from `company-profile.md`)

- Founder: Italian citizen, tax resident in Italy, lives and works in Milan, sole founder (assumption: no other shareholders).
- Not incorporated; open to incorporating abroad. HQ still marked TBD in the profile.
- Funding plan: 500k pre-seed (currency TBD), mostly US angels, in about four months.
- Customers: Italy, then Spain. One freelance developer in Poland. No employees.
- Budget: 5,000 EUR for 90 days.

Unanswered and material: whether the US angels require a particular vehicle or instrument (profile Open question 3).

## 2. Which jurisdiction governs what

| Matter | Governing jurisdiction | Why |
| --- | --- | --- |
| Company law (formation, shares, directors) | Country of incorporation | The registry and company statute of that place |
| Corporate tax residence of any company you manage | Italy, potentially in addition to the country of incorporation | Italian law tests where the company is actually managed, and you manage from Milan |
| Your personal tax on shares, salary, and any restructuring | Italy | Your tax residence |
| Sale of securities to US angels | United States (federal and state securities rules), whatever the issuer's country | Location of the investors |
| Customer contracts, VAT, privacy | Italy and Spain, EU rules | Location of customers |
| Developer relationship and IP assignment | Poland and the contract's chosen law | Location of the worker |

## 3. Current rules checked (sources and dates)

**Italy: company tax residence.** Since the 2023 reform a company is Italian tax resident if, for most of the tax period, any one of three alternative tests is met in Italy: registered office, place of effective management, or main place of ordinary day-to-day management. The tests apply from 1 January 2024 for calendar-year companies. Source: Agenzia delle Entrate press release on Circolare 20/E of 4 November 2024 (agenziaentrate.gov.it), read 2026-11-20. Consequence: a foreign company run by you alone from Milan would very likely meet at least one test. Not checked: how the Italy-US tax treaty resolves dual residence, and Italian reporting duties for foreign shareholdings.

**Italy: innovative startup status.** Requirements after Law 193/2024 include: incorporated no more than five years ago; a micro, small, or medium enterprise; no prevalent agency or consulting activity; production value up to 5 million EUR from year two; no profit distribution; and at least one of R&D spending of at least 15%, qualified staff ratios, or a patent or registered software. Staying registered beyond year three needs additional conditions. Italian-taxpayer investors can get a 30% deduction, or 65% under de minimis for startups in their first three years of registration. Source: Camera dei deputati, "Start-up e PMI innovative", page dated 10 June 2025 (temi.camera.it), read 2026-11-20. The ministry page (mimit.gov.it) could not be reached today; confirm there. Consequence: these deductions are against Italian tax, so they are of little use to US angels (assumption to confirm with the tax adviser).

**Delaware: annual cost.** A Delaware corporation files an annual report (50 USD) and pays franchise tax by 1 March each year. Minimum tax is 175 USD under the authorized-shares method and 400 USD under the assumed-par-value method; the penalty for a late report is 200 USD plus 1.5% monthly interest. Source: Delaware Division of Corporations, corp.delaware.gov/frtax, read 2026-11-20. The two methods can give very different results for a startup with many authorized shares; have the lawyer compute both.

**United States: beneficial-ownership reporting.** FinCEN's final rule, announced 11 August 2026 and effective 14 August 2026, permanently exempts companies formed in the United States from beneficial-ownership reporting; companies formed abroad and registered to do business in a US state still report. Source: Morrison Foerster client note of 20 August 2026 (a secondary source), read 2026-11-20. Confirm against the rule text at fincen.gov.

**Not researched (search limit reached). Consult the primary source before relying on any figure:**
- S.r.l. and S.r.l. semplificata minimum capital, notary or online formation route, registry and chamber fees, timeline: Registro Imprese (registroimprese.it), Consiglio Nazionale del Notariato, MIMIT.
- Italian beneficial-owner register status: Registro Imprese, MEF.
- Delaware incorporation filing fee and registered-agent requirement: corp.delaware.gov fee schedule.
- US federal tax ID for a non-US founder, federal corporate filings for a foreign-owned corporation, founder stock election deadline: irs.gov.
- US securities exemption and notice filing for angel investments: sec.gov.
- Italian tax on contributing S.r.l. shares to a foreign parent (cost of a later flip): Agenzia delle Entrate, TUIR.
- Polish contractor classification and copyright assignment formalities: Polish Labour Code and Copyright Act via isap.sejm.gov.pl.

## 4. Shortlist

- **Option A: Italian S.r.l. only**, applying for innovative startup status if the requirements are met.
- **Option B: Delaware C-Corporation parent with a wholly owned Italian S.r.l.** The parent takes the investment; the S.r.l. contracts with Italian and Spanish customers and with the developer.
- **Option C: Italian S.r.l. now, restructure under a US parent later** only if investors require it.

Not shortlisted: a Delaware company alone with no Italian entity. Managed from Milan, it would likely be Italian tax resident or have a taxable presence in Italy anyway, while giving customers a non-EU counterparty.

## 5. Comparison

| Criterion | A: S.r.l. only | B: Delaware parent + S.r.l. | C: S.r.l. now, flip later |
| --- | --- | --- | --- |
| Investor familiarity (US angels) | Low. Unfamiliar law and documents; standard US instruments do not map directly (assumption) | High. The vehicle and instruments US angels normally use | Low now, high after the flip |
| Founder tax exposure | Simplest. One Italian company, Italian rules only | Most complex. Parent probably Italian tax resident as well as US-incorporated; dual residence, intercompany pricing, Italian reporting of foreign shares | Simple now; the flip is a taxable-event risk for you personally, growing with company value (to verify) |
| Administrative load | One set of books and filings | Two sets, in two languages and two legal systems, plus intercompany agreements | One now, two later, plus the restructuring project |
| Time to bank account | Local founder, local bank (timeline not researched) | US account for a non-resident founder plus Italian account; expect the slower of the two (assumption) | As A |
| Cost to unwind | Liquidation of one Italian company | Two wind-ups in two countries | As A before the flip, as B after |
| Fit with 5,000 EUR budget | Most likely to fit (quotes needed) | Least likely to fit (quotes needed) | Fits now; flip cost later |
| Fit with funding in four months | Risk that US angels decline or delay | Ready for US angels if formed in time | Risk of restructuring during the raise, when time and leverage are lowest |

## 6. Recommendation (pending your approval)

**Recommended, conditionally: Option B, formed parent-first, and only after two checks.**

Reasoning: your stated plan is a raise mostly from US angels in four months. If they require a US vehicle, forming the Delaware parent first and the S.r.l. beneath it avoids a later flip, and a restructuring is cheapest when the company has little value. The S.r.l. keeps a local EU counterparty for accounting firms and holds the Italian operations where they actually are.

The two checks before anything is formed:
1. **Ask the angels.** Put profile Open question 3 to at least three of the likely investors. If they will invest in an Italian S.r.l., Option A is better: cheaper, simpler, and all your work is in Italy.
2. **Get a written view from an Italian cross-border tax adviser** on the Delaware parent's Italian tax residence, your own position, and where the IP should sit. If the adviser finds the dual-residence cost unacceptable, fall back to Option A or C.

**What would change the recommendation**
- Angels accept an S.r.l., or the round shifts to Italian or EU investors (who can use the Italian deductions): choose A.
- Quotes for B exceed what you can spend before the raise: choose C, with the flip costed in advance by the tax adviser.
- You plan to relocate, or add a US-based co-founder or director: management may no longer be in Italy; re-run this memo.
- The raise slips well beyond four months: choose A or C and revisit at term-sheet stage.

## 7. Timeline (assumptions, to be replaced with adviser and registry figures)

Neither Option B nor a full Italian formation with banking should be planned inside a 14-day sprint. Filing a Delaware certificate can be quick, but a US bank account for a non-resident founder, the Italian notarial or online formation, VAT number, and bank onboarding are each likely to take longer. Plan in weeks, working back from the raise in about March 2027, and aim to have the investing entity bankable at least a month before the first investor signs.

Can proceed in parallel now, with no entity: angel vehicle check, adviser quotes, name and domain checks, developer IP assignment draft, customer contract drafts, product and design-partner work.

## 8. Approval gates

Nothing proceeds on these without your explicit approval of the specific action:
1. Choice of jurisdiction and legal form.
2. Each registry filing and each fee or adviser engagement.
3. Share numbers, par value, and capital contributed.
