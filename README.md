# Saturo Gojo of Business

A portable AI skill for source-grounded sales and business advice. It helps an agent diagnose offers, lead generation, sales conversations, objections, unit economics, retention, and operational constraints without inventing customer facts or promising unsupported results.

This is an independent fan-named project. It is not affiliated with or endorsed by the creators, publishers, or rights holders of *Jujutsu Kaisen*.

The included knowledge pack contains original close-reading syntheses and critiques across major sales books and Alex Hormozi material. It does **not** redistribute the copyrighted books or transcripts.

## Install

### Claude Code

Copy `saturo-gojo-of-business/` into your project's `.claude/skills/` directory:

```text
your-project/
└── .claude/
    └── skills/
        └── saturo-gojo-of-business/
```

Invoke it with:

```text
Use $saturo-gojo-of-business to help me prepare for this sales call.
```

### Codex and compatible agents

Copy `saturo-gojo-of-business/` into a configured skills directory such as `.agents/skills/` or your agent's personal skills folder, then invoke `$saturo-gojo-of-business`.

## Optional private source library

If you legally own source books or transcripts, place them under `saturo-gojo-of-business/library/` for local retrieval. That directory and common ebook formats are gitignored. Never commit or redistribute private source material.

The skill works without the private library from the included synthesis pack. Without an original source, the agent should identify a claim as synthesis-based instead of pretending it checked a verbatim passage.

## What makes it different

- Separates observed facts, assumptions, source principles, and recommendations.
- Uses honest contribution and payback economics rather than revenue theater.
- Treats activity, qualification, sales, cash, and retained profit as different outcomes.
- Preserves consent and a clean refusal path.
- Routes to the relevant source tradition instead of blending every author into generic advice.

## Validate

From the repository root:

```powershell
python saturo-gojo-of-business/scripts/verify_pack.py
```

The validation checks the portable knowledge pack and confirms that no private corpus is present.
