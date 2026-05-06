# Paper C — Metadata

## Title

The 65/41 Barrier: Continued-Fraction Convergents of log₂3 Bound Worst-Case Descent Ratios in the Compressed Collatz Map

## Author

Lightman Chang (Independent Researcher) — `lightman.chang@gmail.com`

## Type

Type B: Experimental mathematics paper (rigorous theorem + empirical conjecture + rigorous corollary).

## Summary (3 sentences)

For the compressed Collatz map S(n) = (3n+1)/2^v_2(3n+1), the descent ratio B_T/T = (sum of valuations)/(steps) of an orbit segment must exceed log₂3 to descend. The paper proves rigorously that the deterministic minimum of this ratio over T ∈ [1,93] is exactly 65/41 (the sixth principal convergent of log₂3, attained at T = 41 and T = 82), reports a computational study (exhaustive for odd n < 2^21, structured sample for n < 2^44) showing that the worst-case observed first-descent ratio takes values in the three-element set {65/41, 149/94, 233/147} and is at least 233/147 in every bit-bin tested at k ≥ 13, and derives as a clean rigorous corollary the cycle-element upper bound m < 2^B · 3^P / (4(2^B − 3^P)) using only the irrationality of log₂3. The paper deliberately separates rigorous content (Theorem 3.1 and Corollary 5.5) from empirical content (Conjecture 4.2, Observation 4.4) so each can be evaluated on its own terms.

## Key result(s)

1. **Theorem 3.1 (Continued-fraction barrier, rigorous):** For every integer T ∈ [1, 93], B(T)/T ≥ 65/41, with equality iff T ∈ {41, 82}. Sharp at T = 94 (where 149/94 < 65/41 first occurs).
2. **Conjecture 4.2 (Empirical descent-ratio barrier):** For every odd n of bit-length k ≥ 13, ρ_des(n) ≥ 233/147; the bit-bin worst case lies in {65/41, 149/94, 233/147, …} along upper convergents of log₂3, and at sampled scales (k ≤ 44) only the first three values are realized.
3. **Corollary 5.5 (Cycle bound, rigorous):** For any nontrivial cycle of S of period P with cumulative valuation B, m_min < 2^B · 3^P / (4(2^B − 3^P)), where 2^B − 3^P ≥ 1 by the irrationality of log₂3 (no Gelfond–Schneider needed).

## Target journals (ranked)

| Rank | Journal | Acceptance estimate | Rationale |
|------|---------|--------------------|-----------|
| 1 | **Experimental Mathematics** | 25–35% | Exact fit: rigorous theorems bookending an experimental conjecture, full reproducibility, modest scope, table-heavy. Their sweet spot. |
| 2 | **Integers (Electronic Journal of Combinatorial Number Theory)** | 30–40% | Open-access, rapid review, accepts shorter computational/CF papers in this area. Good fallback. |
| 3 | **Journal of Integer Sequences** | 35–50% | Strong fit if the paper foregrounded the OEIS denominator sequence (q_k of log₂3 convergents and the 65/41 phenomenon). May want light revision to match house style. |
| 4 | **INTEGERS (proceedings volumes)** | 30–40% | If submitted alongside conference talk. |
| 5 | **arXiv (math.NT) — preprint only** | 100% | Mandatory first step regardless of journal target; gives DOI-able link for citation in companion papers A and B. |

## MSC 2020 codes

- **Primary**: 11B37 — Recurrences (includes Collatz-type problems)
- **Secondary**:
  - 11A55 — Continued fractions
  - 11J70 — Continued fractions and generalizations (Diophantine approximation)
  - 11Y55 — Calculation of integer sequences
  - 11Y65 — Continued-fraction calculations (numerical results)

## Submission strategy

1. **Pre-submission** (week 0):
   - Post on arXiv (math.NT, cross-list math.DS) to establish priority.
   - Cite as `arXiv:2026.XXXXX` in companion papers A and B.
2. **Primary target** (week 1–2): Submit to *Experimental Mathematics*.
3. **If rejected without revision**: Resubmit to *Integers* with minimal changes.
4. **If desk-rejected for scope** (e.g., "too applied / too narrow"): Resubmit to *Journal of Integer Sequences*, refocus the abstract slightly toward the OEIS angle.
5. **Iterate**: Track referee comments; computational claims are easy to extend if asked (we can always extend to k = 50 or 60 if a referee wants more bins).

## What the user needs to fill in

- [ ] **Acknowledgements section**: not currently present. Add a brief paragraph (e.g., thanking computing resources, discussions with colleagues if any). Suggested location: just before References.
- [ ] **arXiv ID for companion papers**: the bibliography currently cites `[ChangPaperA]` and `[ChangPaperB]` as "preprint, 2026". Replace with arXiv IDs once those papers are posted.
- [ ] **Repository URL pin**: confirm `https://github.com/weiqi-kids/collatz-research-report` is the correct, public, intended URL. If a tagged release / DOI (Zenodo) is preferred, replace.
- [ ] **Funding / affiliation disclosure**: paper is currently authored as "Independent Researcher". Confirm.
- [ ] **Re-verify Experiment E3 numbers**: Table 5.3 reports specific bit-bins where 149/94 occurs (k = 19, 29, 31). These values came from the original notebook; user may want to re-run the structured-sampling code and confirm the exact bins where 149/94 appears in the worst case (verses 65/41) before journal submission. Currently described as approximate per the notebook.
- [ ] **Citation crosscheck**: `[BarinaCheckup]` is cited for the n ≤ 2^68 verification; if the user prefers a different citation (e.g., Oliveira e Silva, Roosendaal), swap.
- [ ] **Optional figure**: a plot of B(T)/T versus T showing record-breaking minima at T = 1, 3, 5, 17, 29, 41, 94 would be visually striking. Currently the paper is table-only.

## Compile

Single-shot compile expected:

```bash
cd /root/proof/collatz-research-report/paper-c
tectonic paper.tex
```

No external bibliography file (uses `thebibliography` inline). No figures.

## Length

LaTeX source: ~1290 lines. Estimated typeset length ~22–26 pages in `article` 11pt — within the typical Experimental Mathematics range (15–30 pages).

## Notes on epistemic discipline

- The title does NOT claim to solve Collatz.
- The abstract clearly distinguishes "Theorem", "Conjecture", "Corollary".
- The cycle-element bound is presented as a corollary of well-known transcendence input, not a new result; the discussion explicitly attributes it to Crandall and Eliahou.
- Conjecture 6.1 is flagged as stronger than what Theorem 4.1 implies, with a quantitative gap analysis in Remark 6.2.
- No use of "clearly", "obviously", "we solve", "revolutionary", or "structural barrier" (all forbidden by the writing guide).
