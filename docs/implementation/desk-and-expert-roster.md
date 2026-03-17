# Desk And Expert Roster

This note records the current first-wave analytical desk set and first-wave expert roster for the Axis system.

This file is implementation guidance for the current first-pass desk roster, expert roster, expert remits, desk memberships, and explanatory style.

It is subordinate to [`SPECIFICATION.md`](/Users/wjm/Code/Axis/SPECIFICATION.md).

These experts are system-level agents. They belong to the system, not to any one desk.
Analytical desks may assign them as needed.

Desk and expert assignments in this file are first-pass implementation choices, not canonical permanent ontology beyond what the spec already defines.

This note does not yet define detailed watchlists, prompts, or finalized implementation behavior inside OpenClaw.

## Analytical Desks

- `Energy Desk`
- `Materials Desk`
- `Infrastructure Desk`
- `Manufacturing Desk`
- `Logistics Desk`
- `Conflict Desk`
- `Influence Desk`
- `Macro Desk`

## First-Wave Experts

- `Oil & Gas`
- `Power`
- `Mining`
- `Metals`
- `Materials`
- `AI`
- `Chemicals`
- `Agriculture`
- `Defense`
- `Shipping`
- `Central Banks`
- `Markets`
- `Geopolitics`
- `US Politics`
- `Narratives`
- `Influence Operations`
- `Institutional Trust`
- `Conspiracy Theory`
- `Manufacturing`
- `Trade`
- `Construction`
- `Labor`
- `Trends`

## First-Pass Expert Remits

### `Oil & Gas`

Tracks hydrocarbon supply, transport, refining, LNG, inventories, and energy-security stress in the current operating system.

### `Power`

Tracks power sufficiency, generation adequacy, grid stress, interconnection pressure, and the ability of electrical systems to support growth.

### `Mining`

Tracks upstream extraction, reserve quality, project realism, depletion, jurisdictional constraints, and mine-level supply risk.

### `Metals`

Tracks metal processing, refining, inventories, pricing, visible tightness, and intermediate-stage control in metallic value chains.

### `Materials`

Tracks non-metal industrial and building materials, intermediate inputs, and physical material constraints on construction and industrial buildout.

### `AI`

Tracks AI-driven demand, capability shifts, deployment intensity, and where AI changes physical-system requirements or bottlenecks.

### `Chemicals`

Tracks industrial chemicals, fertilizers, petrochemical chains, process inputs, and chemical-system constraints on production, agriculture, and buildout.

### `Agriculture`

Tracks food and agricultural production systems, fertilizer dependence, yield risk, trade sensitivity, and agricultural vulnerability under stress.

### `Defense`

Tracks defense demand, procurement, mobilization, stockpiling, and military-industrial pressure on constrained inputs and production systems.

### `Shipping`

Tracks maritime movement, shipping lanes, freight flow, chokepoints, and seaborne transport as a constraint on supply and resilience.

### `Central Banks`

Tracks monetary policy, liquidity provision, funding conditions, reserve behavior, and central-bank actions that shape capital availability.

### `Markets`

Tracks what global markets are doing, how funds are positioned, and what catalysts markets are looking for.

Its role is to help the system understand:

- how physical-economy and geopolitical pressures are being priced
- where positioning is vulnerable or crowded
- what catalysts the market expects, fears, or is ignoring
- where market behavior confirms or contradicts desk thinking

`Markets` is not a generic financial-news expert. Its purpose is to interpret market state, positioning, and catalyst expectations as signals relevant to the physical economy.

### `Geopolitics`

Tracks state competition, alignment, coercion, sanctions pressure, regional instability, and geopolitical transmission into physical systems.

### `US Politics`

Tracks the US political process, coalition incentives, regulatory and fiscal direction, and domestic political forces shaping strategic systems.

### `Narratives`

Tracks framing, storyline formation, symbolic payloads, memetic spread, and competition among narratives shaping public interpretation.

### `Influence Operations`

Tracks deliberate persuasion, coordinated amplification, state and non-state influence tactics, and information operations aimed at shaping outcomes.

### `Institutional Trust`

Tracks legitimacy, credibility erosion, distrust cascades, and confidence in governments, firms, markets, and public institutions.

### `Conspiracy Theory`

Tracks hidden-actor narratives, cover-up logic, self-sealing belief systems, and narrative forms built around suspicion and covert control.

### `Manufacturing`

Tracks factory-side production capacity, industrial throughput, conversion of inputs into usable outputs, and bottlenecks in scalable production.

### `Trade`

Tracks tariffs, trade restrictions, cross-border commercial policy, trade-flow reordering, and trade architecture as a constraint on the physical economy.

### `Construction`

Tracks physical buildout, EPC reality, commissioning, schedule slippage, and execution constraints in getting assets actually built.

### `Labor`

Tracks workforce availability, skilled-labor bottlenecks, wage pressure, training capacity, and labor as a constraint on buildout and production.

### `Trends`

Tracks what topics, narratives, and developments are gaining traction fast enough to matter for editorial attention and cross-desk awareness.

## Desk Detail

### `Energy Desk`

Themes:

- `Oil, Gas, and Energy Security`
- `Energy Abundance and the Future of Power Generation`
- `Fuel security, energy-system sufficiency, and resilience under stress`
- `Power-market tightness, generation adequacy, and energy availability for industrial growth`
- `Energy as a binding constraint on infrastructure, manufacturing, and conflict transmission`

Assigned experts:

- `Oil & Gas`
- `Power`
- `AI`
- `Agriculture`
- `Markets`
- `Geopolitics`
- `US Politics`

Explanation style:

- what looks like an AI boom is really a power sufficiency story
- what looks like a geopolitical oil shock is really a system resilience and transport-security story
- what looks like an energy transition story is really a question of generation build speed and fuel backup

### `Materials Desk`

Themes:

- `Copper Supply and the Energy Buildout`
- `Rare Earths and Magnet-Supply Concentration`
- `Material sufficiency for electrification, industrial buildout, and strategic capacity`
- `Upstream extraction, downstream processing, and concentration of control over critical inputs`
- `Strategic materials as constraints on manufacturing, defense, and energy expansion`

Assigned experts:

- `Mining`
- `Metals`
- `Materials`
- `Chemicals`
- `Manufacturing`
- `Geopolitics`
- `US Politics`
- `Shipping`
- `Markets`

Explanation style:

- what looks like an industrial expansion story is really a story about constrained inputs and processing choke points
- what looks like a commodity price move is really a signal about physical tightness, inventories, and control of intermediate stages
- what looks like diversification is still dependency if refining and processing remain concentrated

### `Infrastructure Desk`

Themes:

- `AI Demand, Power Constraints, and Grid Stress`
- `Project and Capital Economics`
- `Physical buildout, delivery, and commissioning of enabling systems`
- `Grid, interconnection, transport, and other large-scale bottlenecks that limit expansion`
- `Construction, labor, trade, and project-execution constraints on physical capacity growth`

Assigned experts:

- `Power`
- `AI`
- `Materials`
- `Construction`
- `Labor`
- `Trade`
- `Markets`
- `US Politics`

Explanation style:

- what looks like strong demand is meaningless if the enabling systems cannot actually be connected and delivered
- what looks like abundant capital still fails if construction, labor, permitting, and interconnection do not clear
- what looks like inevitable growth is often delayed by the hidden timing of physical buildout

### `Manufacturing Desk`

Themes:

- `Defense Demand, Strategic Stockpiling, and the Modern Kill Chain`
- `Project and Capital Economics`
- `Industrial production capacity and the conversion of materials, energy, and equipment into usable systems`
- `Factory-side bottlenecks, industrial throughput, and constraints on scaling output`
- `Defense-industrial production pressure where it reshapes broader industrial capacity`

Assigned experts:

- `Power`
- `Mining`
- `Metals`
- `Materials`
- `Chemicals`
- `Manufacturing`
- `Defense`
- `Markets`
- `US Politics`

Explanation style:

- what looks like strategic ambition is irrelevant if industrial conversion capacity is missing
- what looks like supply security is false if factory-side throughput cannot scale
- what looks like technological progress is bottlenecked by the ability to turn materials and components into repeatable output

### `Logistics Desk`

Themes:

- `Movement, routing, and throughput of physical goods through real networks`
- `Ports, rail, trucking, warehousing, chokepoints, and logistics resilience`
- `Transport and distribution as constraints on production, buildout, and strategic supply`

Assigned experts:

- `Shipping`
- `Trade`
- `Markets`
- `Geopolitics`
- `Manufacturing`

Explanation style:

- what looks like sufficient supply on paper is irrelevant if the system cannot move goods through real networks
- what looks like a local disruption matters because routing, throughput, and storage constraints can propagate system-wide
- what looks like a trade or shipping story is often really a story about movement capacity becoming the bottleneck

### `Conflict Desk`

Themes:

- `Geopolitical Crisis, Conflict, and System Disruption`
- `Defense Demand, Strategic Stockpiling, and the Modern Kill Chain`
- `Strategic Supply Chains and Economic Statecraft`
- `Conflict transmission into energy, materials, infrastructure, and industrial systems`
- `State competition, denial, coercion, chokepoints, and disruption of critical flows`
- `Acute geopolitical shocks that force repricing of physical vulnerability and strategic control`

Assigned experts:

- `Defense`
- `Oil & Gas`
- `Agriculture`
- `Geopolitics`
- `Trade`
- `Shipping`
- `US Politics`
- `Markets`

Explanation style:

- what looks like a political crisis matters because it reroutes energy, materials, and industrial access
- what looks like war news is really a reprioritization of flows, stockpiles, chokepoints, and production
- what looks like sanctions policy is really a struggle over who gets access to the physical economy

### `Influence Desk`

Themes:

- `Narrative manipulation and influence operations`
- `Institutional trust, distrust production, and legitimacy shocks`
- `Synthetic persuasion, memetic spread, and information warfare`
- `Psychological and narrative pressure shaping politics, markets, and physical-economy response`

Assigned experts:

- `US Politics`
- `AI`
- `Geopolitics`
- `Markets`
- `Trends`
- `Narratives`
- `Influence Operations`
- `Institutional Trust`
- `Conspiracy Theory`

Explanation style:

- what looks like spontaneous public belief is often guided by narrative construction, amplification, and trust erosion
- what looks like political sentiment can be the downstream effect of influence operations acting on existing institutional fractures
- what looks like fringe noise matters when narratives are engineered to alter consent, legitimacy, and response inside the physical economy

### `Macro Desk`

Themes:

- `Monetary Order Transition`
- `Project and Capital Economics`
- `Capital flows, liquidity, and financing conditions for the physical economy`
- `Monetary, settlement, and reserve shifts that change real-asset funding and strategic trade`
- `Macro-financial conditions as constraints or accelerants on physical buildout`

Assigned experts:

- `Central Banks`
- `Markets`
- `Trade`
- `Geopolitics`

Explanation style:

- what looks like financial easing or tightening matters because it changes what can actually be funded and built
- what looks like a reserve or settlement shift matters because it changes strategic trade and real-asset financing
- what looks like market calm can still mask structural capital starvation in the physical economy

## Expert Assignments

- `Oil & Gas`
  - `Energy Desk`
  - `Conflict Desk`

- `Power`
  - `Energy Desk`
  - `Infrastructure Desk`
  - `Manufacturing Desk`

- `Mining`
  - `Materials Desk`
  - `Manufacturing Desk`

- `Metals`
  - `Materials Desk`
  - `Manufacturing Desk`

- `Materials`
  - `Materials Desk`
  - `Infrastructure Desk`
  - `Manufacturing Desk`

- `AI`
  - `Energy Desk`
  - `Infrastructure Desk`
  - `Influence Desk`

- `Agriculture`
  - `Energy Desk`
  - `Conflict Desk`

- `Chemicals`
  - `Materials Desk`
  - `Manufacturing Desk`

- `Defense`
  - `Manufacturing Desk`
  - `Conflict Desk`

- `Shipping`
  - `Materials Desk`
  - `Logistics Desk`
  - `Conflict Desk`

- `Central Banks`
  - `Macro Desk`

- `Markets`
  - `Energy Desk`
  - `Materials Desk`
  - `Infrastructure Desk`
  - `Manufacturing Desk`
  - `Logistics Desk`
  - `Conflict Desk`
  - `Influence Desk`
  - `Macro Desk`

- `Geopolitics`
  - `Energy Desk`
  - `Materials Desk`
  - `Logistics Desk`
  - `Conflict Desk`
  - `Influence Desk`
  - `Macro Desk`

- `US Politics`
  - `Energy Desk`
  - `Materials Desk`
  - `Infrastructure Desk`
  - `Manufacturing Desk`
  - `Conflict Desk`
  - `Influence Desk`

- `Narratives`
  - `Influence Desk`

- `Influence Operations`
  - `Influence Desk`

- `Institutional Trust`
  - `Influence Desk`

- `Conspiracy Theory`
  - `Influence Desk`

- `Manufacturing`
  - `Materials Desk`
  - `Manufacturing Desk`
  - `Logistics Desk`

- `Trade`
  - `Infrastructure Desk`
  - `Logistics Desk`
  - `Conflict Desk`
  - `Macro Desk`

- `Construction`
  - `Infrastructure Desk`

- `Labor`
  - `Infrastructure Desk`

- `Trends`
  - `Editors Desk`
  - `Influence Desk`

## Notes

- This is the current first-pass roster and desk map, not a permanent final structure.
- The desk set is intended to reflect the broader physical-economy framing:
  - energy
  - materials and minerals
  - infrastructure
  - industrial systems
  - capital flows
- `Conflict Desk` and `Macro Desk` are cross-system desks that interpret pressures flowing through those physical systems.
- `Trade` and `Shipping` are assigned where flow control, routing, logistics, and disruption are persistent parts of the desk's deliberation rather than merely outside context.
- Expert remit definitions are intentionally deferred until the system is running in OpenClaw and can be shaped against real signal flow.
- `Trends` is included in the first-wave expert roster but is expected to report primarily to `Editors Desk`.
- Additional experts and desks may be added later if recurring signal volume or analytical need justifies a split.
