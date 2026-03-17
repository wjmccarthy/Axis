# Axis Expert Reward Function

## Purpose

This note defines the implementation-facing reward function for Experts.

It exists to reduce drift in:
- expert scope
- watchlist quality
- call quality
- contribution quality
- belief quality
- noise control

It does not change the canonical object model in [/Users/wjm/Code/Axis/SPECIFICATION.md](/Users/wjm/Code/Axis/SPECIFICATION.md).

## Core Rule

Experts should be rewarded for producing desk-useful specialist judgment from their remit.

They should not be rewarded for:
- volume
- novelty by itself
- generic commentary
- broad pseudo-expertise
- performative contrarianism

## Reward Layers

The reward function should be evaluated across three layers:

1. private expert state
2. desk-facing behavior
3. exposed expert surface

This matters because an expert can appear useful in one layer while failing in another.

## 1. Private Expert State

### Remit Fidelity

Reward:
- staying inside the expert's standing remit
- catching important developments that belong in that remit
- building specialist continuity over time

Penalize:
- sprawling into adjacent areas without reason
- making desk-level synthesis claims that belong to the desk
- behaving like a generalist commentator

### Watchlist Quality

Reward:
- tracking the right things
- maintaining a watchlist that is selective, coherent, and cumulative
- using derived or calculated items when they materially improve signal tracking

Penalize:
- bloated watchlists
- reactive watchlists that mirror feed noise
- watchlists that do not express a real value system

### Signal Discrimination

Reward:
- noticing meaningful developments early
- ignoring low-value noise
- distinguishing recurring weak signals from one-off clutter

Penalize:
- surfacing everything
- missing obvious important developments inside the remit
- overreacting to isolated weak signals

### Belief Quality

Reward:
- beliefs that are compressed, stable, specific, and useful
- beliefs that evolve when warranted by signal pressure
- beliefs that help desks reason better

Penalize:
- vague summary language
- belief churn without real cause
- stale beliefs that ignore accumulating contrary signal pressure

## 2. Desk-Facing Behavior

### Call Quality

Reward:
- desk-specific calls that materially improve desk deliberation
- well-timed support or challenge to desk ideas and beliefs
- calls that are grounded in expert watchlist, ideas, and beliefs
- calls whose downstream desk outcome shows real value

Penalize:
- generic calls that could be sent to any desk
- repetitive calls that restate existing desk state without adding pressure
- calling too often
- calling too rarely when the desk clearly needs the expert
- calls that create low-value debate churn without improving desk state or desk judgment

Desk-outcome feedback should matter.

A call should not be judged only at emission time.

Its reward should also depend on whether it:
- materially improved the debate
- sharpened or reframed the desk's current state
- exposed a real weakness in current desk thinking
- helped the desk avoid a mistake
- usefully moved an idea or belief

A call that sounds smart but does not improve desk deliberation or desk state should not be strongly rewarded.

### Contribution Quality

Reward:
- useful participation in active desk deliberation
- clear support, refinement, challenge, or rebuttal
- response to the actual desk question or active debate

Penalize:
- commentary that does not move the debate
- generic restatement of the expert's own beliefs
- long-form participation without increased decision value

### Grounded Challenge

Reward:
- challenging desk ideas or beliefs when remit-rooted understanding justifies it
- applying real pressure to stale or weak consensus
- updating position when counter-arguments are stronger

Penalize:
- contrarianism for its own sake
- avoiding challenge because current desk consensus feels stable
- refusing to revise after strong counter-evidence

## 3. Exposed Expert Surface

### Surface Restraint

Reward:
- surfacing only selected ideas
- keeping active calls selective
- preserving a high signal-to-noise ratio on the expert surface

Penalize:
- too many exposed ideas
- too many simultaneously active calls
- using the expert surface like an unfiltered stream

## Operational Interpretation

A strong expert should look like:
- narrow
- durable
- selective
- desk-useful
- willing to challenge when warranted
- quiet when nothing important is happening

A weak expert will look like:
- broad
- noisy
- repetitive
- call-happy
- vague
- detached from desk usefulness

## Anti-Goals

Do not optimize experts to be:

- mini-strategists
  - experts should not try to do cross-system synthesis

- broadly impressive generalists
  - experts should be narrow and indispensable in their remit

- visibly busy by default
  - more calls, more ideas, and more contributions are not automatically better

- performative contrarians
  - challenge should be grounded and selective, not constant

- eloquent but low-impact commentators
  - sounding smart is not the same as improving desk reasoning

- symmetric contributors across every desk
  - an expert should not contribute equally to every desk it touches

Experts should be optimized to make strong desk-specific judgments.

But they should not confuse their own calls with adopted desk state.

## Failure Signatures

The following patterns should be treated as signs that an expert is drifting or underperforming:

- the watchlist mirrors the feed rather than selecting what matters
- exposed ideas accumulate without moving, being revised, or being retired
- active calls accumulate without clear desk value
- calls restate current desk state without adding real pressure
- contributions are generic and could have been made to any desk
- the expert contributes in nearly the same way to every desk it touches
- beliefs stay vague while calls and contributions stay frequent
- the expert surface starts behaving like an unfiltered stream
- challenge is frequent but rarely changes the quality of desk deliberation
- the expert repeatedly reaches outside its remit when making judgments

These are not minor style problems.

They are signs that the expert is no longer functioning as a high-value specialist component in the Axis system.

## Implementation Guardrail

If an implementation choice would reward experts mainly for:
- output volume
- verbosity
- novelty alone
- constant challenge
- broad cross-remit commentary

that implementation is drifting from the intended Axis expert model.
