---
name: using-grok-symphony-skills
description: >
  Routes incoming work to the correct Grok Symphony mode, skill, memory layer,
  and verification path. Use before substantial tasks, repo edits, system
  updates, manuscript builds, artifact registration, or recursive synthesis.
version: 0.1.0
status: DRAFT
owner_mode: meta-router
---

# Using Grok Symphony Skills

## Overview
This skill routes tasks into the correct mode, skill, or memory layer within Grok Symphony by using context-based decision logic. It prevents unnecessary context flooding or all-or-nothing mode activation.

## When to Use
Use this skill:
- Before initiating substantial tasks.
- During artifact registration.
- When performing recursive synthesis.

## When NOT to Use
Avoid this skill when:
- The task’s scope is localized and self-evident.
- Historical references or memory dives are not required.

## Core Routing Logic
Choose the appropriate mode based on:
- **Insight Mode:** For analysis, brainstorming, or synthesis.
- **Builder Mode:** For active file creation or structural work.
- **Registrar Mode:** For verifying artifact identity and provenance.
- **Bot 4 Review:** For anti-bloat, rationalization checks, and cleanup.

## Mode Selection
- **Insight Mode:** Exploration, understanding, or plan clarification.  
- **Builder Mode:** Implementing actionable tasks within blocks.  
- **Registrar Mode:** Historical alignment or artifact review.
- **Bot 4:** Strictly for quality assurance and contradiction checks.

## Skill Selection
Tasks can trigger:
1. Context Packing
2. Artifact Identity Verification
3. Skill Crystallization
4. Doubt Cycle Review

## Context Packing
- Consolidate related information into minimal actionable blocks.
- Prevent overloading downstream modes with unnecessary details.

## Common Rationalizations
1. "All context is important." → False. Use progressive disclosure.
2. "A skill can solve every task." → False. Context specificity matters.

## Red Flags
- Overloading memory layers unnecessarily.
- Triggering too many modes simultaneously.
- Bypassing required Bot 4 review.

## Verification Checklist
- [ ] Correct mode selected for the task.
- [ ] No unnecessary memory loading occurred.
- [ ] Outputs routed correctly to registries or archives.

## Related Skills
- Context Packing
- Doubt Cycle Review
- Skill Crystallization