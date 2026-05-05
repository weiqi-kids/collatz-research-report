# Paper B — No Finite Local Potential Function Is a Strict Lyapunov Function for the Accelerated Collatz Map

Title: No Finite Local Potential Function Is a Strict Lyapunov Function for the Accelerated Collatz Map: An Impossibility Result

## Summary

A self-contained Type C (impossibility) paper proving that no function of the form V(n) = log_2(n) + g(n mod 2^k), with k a fixed integer and g : Z/2^k Z -> R any correction, can be a strict Lyapunov function for the accelerated Collatz map S(n) = (3n+1)/2^v_2(3n+1).

The proof is short and elementary: along the family n_M = 2^(ell+k) * M - 1 with ell large, the residue n_M mod 2^k is pinned at -1, the residue S^ell(n_M) mod 2^k is also pinned at -1, and the log_2 ratio grows by ell * log_2(3/2). For ell large enough (compared to the oscillation max(g) - min(g)), this growth exceeds any compensation g can offer, and at least one of the ell single steps must witness V(S(n)) >= V(n).

The paper closes a class of attempted Collatz attacks and complements Conway's 1972 universality results.

## Key Result

**Main Theorem (Theorem 3.1):** For every fixed k >= 1 and every g : Z/2^k Z -> R, there exist infinitely many odd n > 1 with V_{k,g}(S(n)) >= V_{k,g}(n).

**Corollary 3.2:** Any uniform bound on max(g) - min(g) (across all k) is incompatible with V_{k,g} being a Lyapunov function; any escape requires unbounded oscillation.

## Target Journals (ranked)

1. **Integers** (electronic journal) — natural home for elementary Collatz-adjacent impossibility results. Estimated acceptance after revision: 50–60%. (Type C results are easier to publish per the skill's guidance.)
2. **American Mathematical Monthly** — possible if reframed expositorily; the proof is short and readable. Estimated: 30–40%.
3. **Journal of Integer Sequences** — fits the integer-dynamics scope. Estimated: 35–45%.
4. **arXiv preprint (math.NT + math.DS)** — recommended first step.

## MSC 2020 Classification

- **Primary:** 11B37 (Recurrences, including Collatz-type problems)
- **Secondary:** 37B99 (Topological dynamics, none of the above), 11A63 (Radix representation)

## Submission Strategy

1. Post to **arXiv** first (math.NT + math.DS); the impossibility framing is the headline.
2. After 2-4 weeks of community feedback, submit to Integers.
3. If rejected, target J. Integer Sequences with light revision.

## Must-Cite Related Work

- Conway 1972 — universality of generalized Collatz; complementary impossibility result
- Lagarias 1985, 2010 — standard surveys
- Tao 2022 — almost-everywhere convergence (motivates why bounded-oscillation potentials might have seemed plausible)
- Kirby–Paris 1982 — Goodstein independence; canonical example of an ordinal-potential approach that *does* work where Peano-level approaches do not

## Known Limitations (address before submission)

1. **Folkloric content.** That small-k versions (k = 2, 3) fail is folklore. The novelty is the uniform statement for all k with a single proof.
2. **Result is negative.** The paper does not advance toward a proof of Collatz; it closes one avenue. This is an honest limitation, addressed in the Discussion.
3. **Several variants left open.** Adaptive precision k(n) -> infinity, trailing-1 features, ordinal potentials, and global potentials are all explicitly noted as out of scope.

## Reviewer's Most Likely Objection

"This impossibility is obvious from the trailing-1 family n = 2^k - 1; experts have known this for decades. Why is it worth publishing?"

Response strategy: Concede the qualitative folklore, but emphasize that (a) we have not located a published unified statement covering all k with all g; (b) the quantitative form (Corollary 3.2) — that bounded oscillation is insufficient regardless of the precision k — is a clean delineation that has not been recorded; (c) the paper saves future researchers from re-deriving the obstruction at small k. Offer to add an appendix tabulating which residue classes fail at k = 2, 3, 4 to make the article more concretely useful.

## File Info

- **Source:** paper.tex
- **PDF:** to be compiled by main agent (target ≥ 4 pages)
