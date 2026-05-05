# Paper A — A Three-State Finite Automaton for Carry Propagation in the Accelerated Collatz Map

Title: A Three-State Finite Automaton for Carry Propagation in the Accelerated Collatz Map: Spectral Gap and Closed-Form Shift Dynamics

## Summary

A self-contained, elementary paper providing two complementary results about the accelerated Collatz map S(n) = (3n+1)/2^v_2(3n+1):

1. A 3-state finite automaton {A,B,C} that reproduces the binary expansion of 3n+1 bit-by-bit, with transition matrix M whose characteristic polynomial factors as (lambda-1)(2lambda-1)(2lambda+1), giving spectral gap 1/2 and uniform stationary distribution.

2. An exact closed-form identity: for an odd integer n with t trailing 1-bits, the first t-1 accelerated Collatz steps act on the shifted coordinate x = n+1 as the pure scaling x -> (3/2)^(t-1) x, with no error term.

The paper is **deliberately scoped** as Type A (new theorem with proof), not as a Collatz attack. The Discussion section is explicit that the random-input model does not extend to deterministic orbits.

## Key Result

**Main Theorem (Theorem 3.1):** The 3x3 transition matrix M of the carry automaton satisfies det(lambda I - M) = (lambda - 1)(lambda - 1/2)(lambda + 1/2). Hence eigenvalues are {1, 1/2, -1/2}, the spectral gap is 1/2, and the stationary distribution is uniform on {A, B, C}.

**Supporting result (Proposition 4.1):** T^(t-1)(n) = 2 * 3^(t-1) m' - 1 = (3/2)^(t-1)(n+1) - 1 for odd n = 2^t m' - 1.

## Target Journals (ranked)

1. **Integers** (electronic journal) — best fit for elementary, self-contained Collatz-adjacent work. Estimated acceptance after revision: 40–55%.
2. **Journal of Integer Sequences** — natural home for finite-automaton constructions tied to integer dynamics. Estimated: 40–50%.
3. **Discrete Mathematics** — possible if reframed slightly toward the automata aspect. Estimated: 20–30%.
4. **arXiv preprint (math.NT + math.DS)** — recommended first step, no gatekeeping.

## MSC 2020 Classification

- **Primary:** 11B37 (Recurrences, including Collatz-type problems)
- **Secondary:** 11A63 (Radix representation; digital problems), 68Q45 (Formal languages and automata), 37B15 (Dynamical aspects of cellular automata)

## Submission Strategy

1. Post to **arXiv** first (math.NT + math.DS), tagged 11B37
2. Solicit feedback from MathOverflow ("is this 3-state automaton known?")
3. Submit to Integers; in parallel, prepare a slightly expanded version for J. Integer Sequences

## Must-Cite Related Work

- Lagarias 1985 — survey of 3x+1 problem (parity vector, shift dynamics)
- Lagarias 2010 (ed.) — collected volume; standard reference for known results
- Bernstein–Lagarias 1996 — 2-adic conjugacy
- Wirsching 1998 — dynamical systems viewpoint
- Tao 2022 — almost-everywhere result (motivates the orbit/distribution interpretation)

## Known Limitations (address before submission)

1. **Random-input model is heuristic.** The spectral gap does not extend to deterministic orbits. Discussion section is explicit on this.
2. **Folkloric content.** The closed-form formula T^j(n) = (3^j n + (3^j - 2^j))/2^j is folklore; we credit it but emphasize the shift-coordinate interpretation as the contribution.
3. **No new bound on Collatz orbits is claimed.** The contribution is structural (a clean finite-state description), not dynamical.

## Reviewer's Most Likely Objection

"The 3-state automaton is essentially a re-parameterization of the standard 4-state (prev_bit, carry) tracking that anyone who has computed 3n+1 bit-by-bit could write down. Where is the novelty?"

Response strategy: The novelty is in (a) explicitly merging the two equivalent (prev,carry) configurations into a single state B, leaving exactly 3 states; (b) computing the spectral gap of the resulting matrix and identifying it as 1/2 via the clean factorization (lambda-1)(2lambda-1)(2lambda+1); (c) coupling this with the shift-coordinate identity to produce a unified geometric picture. We are not claiming the bit-by-bit computation is new; we are claiming the 3-state quotient and its spectrum are.

## File Info

- **Source:** paper.tex
- **PDF:** to be compiled by main agent (target ≥ 5 pages)
