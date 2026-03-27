---
name: trading_office_planner
description: >
  Turns research council reports into actionable trade plans for equities and 
  crypto, respecting strict risk management constraints.
version: 0.1.0
status: inactive_planning
---

# Trading Office Skill

## Overview
This skill takes the final "Gold Standard" Research Report and market data to output a "Today's Plan." **It never executes trades automatically; it only plans.**

## Components
- **Market Data Ingest:** Pulls prices and positions via Alpha Vantage/CCXT.
- **Risk Agent:** Enforces `RISK_CONFIG` (Max position %, max daily loss, max drawdown).
- **Trade Planner:** Extracts candidate trades from research and applies risk filters.

## Constraints
- **P1 Priority:** Currently secondary to Research & Branding.
- **Manual Approval:** All proposed trades require the end-user's manual click/execution.
- **Solo Friendly:** Designed for personal capital management (~$1K capital).

## Operational Rules
- No options or leveraged products in Phase 1.
- Every trade must have an explicit "Rationale" linked to a Research Council conclusion.
