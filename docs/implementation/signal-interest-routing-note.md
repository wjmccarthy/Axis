# Signal Interest Routing Note

This note records an implementation direction for Signal Desk routing and coverage management.

It is an implementation note only.

It does not change the current specification.

## Core Idea

Signal routing should be driven not only by static expert remit, but also by published expert interests.

The intended flow is:

1. each expert publishes its current interests
2. Signal Desk consolidates those interests into a routing catalog
3. Signal Desk uses that catalog to match incoming signals to experts
4. Signal Desk evaluates repeated routing gaps
5. Signal Desk reports those gaps for human review

## Expert Interests

Experts should publish the kinds of signals they currently want to see.

This is not the same as the full expert remit.

Remit defines the expert's durable interpretive scope.
Interests define the expert's current intake appetite within that scope.

Examples:

- an expert may always own a broad remit
- but only currently want to see certain signal classes, entities, geographies, bottlenecks, or catalysts

## Signal Desk Routing Catalog

Signal Desk should maintain a consolidated routing catalog derived from:

- expert remit
- published expert interests
- current routing guidance from Strategist

This catalog should be the practical basis for deciding where signals go.

## Gap Evaluation

Signal Desk should evaluate recurring routing gaps, including:

- signals that do not match any current expert destination
- repeated signals that fit only weakly or ambiguously
- areas where important signal classes appear under-covered
- areas where watcher coverage appears misaligned with current expert demand

## Gap Reporting

When gaps recur, Signal Desk should report them to the human operator.

The resulting actions may include:

- add watchers
- reduce or narrow watcher scope
- add experts
- split experts
- change routing rules
- deliberately ignore a class of input

## Why This Matters

This approach preserves cost discipline.

It avoids collecting broad data without a clear use path while still giving the system a way to detect where its current expert/watcher structure is insufficient.
