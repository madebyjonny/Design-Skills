## UI work: design system rules

Before writing any UI, read `DESIGN-SYSTEM.md` and the tokens/components it points to.

1. Climb the ladder: existing pattern → existing component → composition → token-only
   styling → STOP and flag. Never skip rungs.
2. Needing an override means a missing component or a misuse. Don't override; flag it.
3. No raw colours, px values, shadows, or arbitrary utility values. Tokens only.
4. Don't add variants or sizes. Use documented defaults.
5. Interaction rules in the design system are non-negotiable (see DESIGN-SYSTEM.md).
6. Mark unavoidable gaps with `ds-gap:` comments and list them in your final message.
7. Run `python scripts/ds_lint.py <paths>` (design-rules-linter) before finishing.
8. Say what a human still needs to review. You're producing a better first draft, not a final.
