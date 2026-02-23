# Creating a New Role Page

## When to Create a New Role
- A new permission level is needed (between existing roles)
- A new team function needs different capabilities
- An existing role needs to be split into more granular access levels

## Steps

### 1. Define the Role
Add the role to `creative-director-toolkit/claude-config/access-control/roles.json`:
- Define capabilities (what they can/can't do)
- Define MCPs, plugins, hooks
- Define editable/read-only/blocked files
- Define available commands

### 2. Create Claude Config Files
In `creative-director-toolkit/claude-config/`:
- Create `CLAUDE.{rolename}.md` — Role-specific instructions
- Create `settings.{rolename}.json` — Role-specific MCP/plugin config

### 3. Create the Onboarding Page
In `creative-toolkit-onboarding/`:
1. Copy an existing role page (closest match) as `{rolename}.html`
2. Steps 1-7: Keep IDENTICAL (do not modify)
3. Update the navbar role label (e.g., `<span class="navbar-role">NewRole</span>`)
4. Update Step 8 capabilities grid:
   - Add/remove capability cards based on roles.json capabilities
   - Use the same card HTML structure
5. Update Tips section with role-appropriate advice
6. Update the page `<title>`

### 4. Add to Index
Add a new card to `index.html` with:
- Role name
- Description from roles.json
- Link to `{rolename}.html`

### 5. Update Users
Add users to `creative-director-toolkit/claude-config/access-control/users.json`

### 6. Deploy
Commit and push both repos:
- `creative-director-toolkit` (roles.json, CLAUDE.md, settings.json)
- `creative-toolkit-onboarding` ({rolename}.html, index.html)

---

## Role Card HTML Template (for index.html)

```html
<div class="role-card">
  <div class="role-icon">
    <!-- SVG icon here -->
  </div>
  <h3>Role Name</h3>
  <p class="role-desc">Description of what this role can do.</p>
  <a href="rolename.html" class="btn-primary">
    Get Started
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  </a>
</div>
```

## Capability Card HTML Template (for Step 8)

```html
<div class="capability-card">
  <div class="card-icon">
    <!-- SVG icon here -->
  </div>
  <h4>Capability Name</h4>
  <p>Short description of what this capability does</p>
</div>
```

For engineering cards, add the `engineering` class:
```html
<div class="capability-card engineering">
```

For admin cards, add the `admin-card` class:
```html
<div class="capability-card admin-card">
```

## Capability Card Categories

### Design
- Landing Pages — "Build complete Domo-branded responsive pages"
- Email Templates — "Create responsive HTML emails that work everywhere"
- Social Media — "Design LinkedIn, X, and Instagram assets"
- Presentations — "Build HTML slide decks with Domo branding"
- Infographics — "Create data-driven visual stories and charts"
- Banner Ads — "Design display ads in standard IAB sizes"

### Media
- AI Images (Gemini 3 Pro) — "Generate images with Google Gemini AI"
- AI Videos (Veo 3.1) — "Create short videos with Google Veo"
- Image Editing — "Remove backgrounds, change styles, retouch"
- Icons & Animations — "Create SVG icons and CSS motion design"

### Figma
- Figma to Code — "Convert Figma designs into real pages"
- Figma Inspect — "Extract specs, tokens, and assets from Figma files"

### Research
- Messaging Research — "Query Domo's messaging, value props, positioning"
- Brand Check — "Validate designs against Domo brand guidelines"
- Competitor Intel — "Research competitor strengths, weaknesses, and Domo differentiators"
- Product Info — "Deep-dive on any Domo product's features and audiences"

### Engineering
- Gemini Agent Development — "Build and test Gemini AI agents with Vertex AI ADK"
- Vertex AI Deployment — "Deploy agents to production on Vertex AI"
- Knowledge Graph API — "Develop and maintain the Neo4j messaging knowledge graph"
- Domo Custom Apps — "Build and publish Domo platform applications"
- Cloud Run Deployment — "Deploy containerized services to GCP Cloud Run"

### Admin
- User Management — "Control who has access and what role they have"
- Toolkit Sync — "Push local changes to all toolkit users"
- System Status — "Monitor toolkit health, APIs, and service uptime"

## Current Roles (ordered by access level)

| Role | Design | Media | Figma | Research | Engineering | Admin | Propose Changes |
|------|--------|-------|-------|----------|-------------|-------|-----------------|
| Owner | Yes | Yes | Yes | Yes | Yes | Yes | N/A (direct) |
| Admin | Yes | Yes | Yes | Yes | Yes | Status only | Via PR |
| Creative | Yes | Yes | Yes | Yes | No | No | Yes |
| Builder | Yes | Yes | Yes | Yes | No | No | No |
| Viewer | No | No | No | Yes | No | No | No |