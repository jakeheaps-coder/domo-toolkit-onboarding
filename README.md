# Domo Domo Toolkit — Onboarding Site

Role-based onboarding pages for the Domo Domo Toolkit. Hosted via GitHub Pages so employees can follow setup instructions based on their assigned role.

## Access

```
https://jakeheaps-coder.github.io/domo-toolkit-onboarding/
```

## Pages

| Page | Description |
|------|-------------|
| `index.html` | Role selection landing page — users pick their role to see the right guide |
| `owner.html` | Full access: engineering + design + admin (18 capability cards) |
| `admin.html` | Full engineering + design, toolkit changes require PR review (16 cards) |
| `creative.html` | Design, media, Figma, research. Can propose improvements (10 cards) |
| `builder.html` | Design, media, Figma, research. Cannot modify the toolkit (10 cards) |
| `viewer.html` | Research only: messaging, products, competitors, brand check (4 cards) |

## Structure

All role pages share identical Steps 1-7 (from account setup through toolkit installation). Step 8 and the Tips section are customized per role based on their capabilities.

### Shared Steps (1-7)
1. Request Claude Code Access (Domo App Studio)
2. Check Email and Create Account (Anthropic)
3. Download VS Code (with admin access note)
4. Install Claude Code Extension (6 sub-steps)
5. Create GitHub Account
6. Request Toolkit Access (GitHub username form)
7. Set Up Your Toolkit (clone command)

### Role-Specific (Step 8 + Tips)
Each role gets a tailored set of capability cards and tips based on what they can do.

## Design System

- **Primary**: Domo Blue `#99CCEE`
- **CTA**: Orange `#FF9922`
- **Font**: Open Sans (300, 400, 600, 700, 800)
- **Dark text**: `#3F454D`
- **All pages**: Progress bar, smooth scroll, scroll animations, mobile responsive

## Adding a New Role

See [CREATING_NEW_ROLES.md](CREATING_NEW_ROLES.md) for the full process:
1. Define the role in `roles.json`
2. Create Claude config files
3. Create the onboarding HTML page
4. Add a card to `index.html`
5. Add users
6. Deploy

## Related Repos

- **domo-toolkit** — The toolkit itself (claude-config, scripts, templates)
- **domo-toolkit-onboarding** — This repo (onboarding pages)