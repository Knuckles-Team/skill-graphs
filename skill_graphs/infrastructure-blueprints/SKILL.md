---
name: infrastructure-blueprints
description: >-
  Library of Docker Swarm / Compose blueprints for company software.
  Deploy via portainer-mcp or container-manager-mcp with KG-native
  topology registration and Technitium DNS wiring.
tags: [infrastructure, docker, blueprints, deployment, portainer]
concept: ECO-4.14
---

# Infrastructure Blueprints

**CONCEPT:ECO-4.14 — Infrastructure Blueprint Library**

Reusable Docker Compose / Swarm stack definitions for company software.
Each blueprint includes resource requirements, DNS configuration,
and KG topology registration metadata.

## 📦 Available Blueprints

| Blueprint | Category | Memory | CPU | Description |
|-----------|----------|--------|-----|-------------|
| `erpnext` | Accounting/ERP | 2048 MB | 2.0 | Full-featured open-source ERP |
| `akaunting` | Accounting | 512 MB | 1.0 | Lightweight accounting |
| `twenty-crm` | CRM | 1024 MB | 1.0 | Modern CRM platform |
| `docassemble` | Legal | 1024 MB | 1.0 | Legal document automation |
| `plane` | Project Mgmt | 1024 MB | 1.0 | Project management (already deployed) |
| `orangehrm` | HR | 512 MB | 1.0 | HR management system |
| `docuseal` | Legal/HR | 512 MB | 0.5 | Document signing |
| `gitea` | DevOps | 512 MB | 1.0 | Git hosting |
| `uptime-kuma` | Monitoring | 256 MB | 0.5 | Uptime monitoring (already deployed) |

## 🚀 Deployment Flow

```
1. Select blueprint from catalog
2. Check host capacity (availableMemoryMB, availableCPU)
3. Deploy via portainer-mcp create_standalone_stack
4. Register DNS record via technitium-dns-mcp
5. Create CompanySoftware node in KG
6. Create DeploymentBlueprint → CompanySoftware edge
7. Create CompanySoftware → InfrastructureHost edge
```

## 📁 Blueprint File Layout

```
infrastructure-blueprints/
├── SKILL.md              # This file
└── company-software/
    ├── erpnext.yaml
    ├── akaunting.yaml
    ├── twenty-crm.yaml
    ├── docassemble.yaml
    ├── orangehrm.yaml
    └── docuseal.yaml
```

## 🔧 Blueprint YAML Format

Each blueprint follows this schema:
```yaml
name: erpnext
description: Full-featured open-source ERP system
category: accounting
version: "15.0"
requires:
  memory_mb: 2048
  cpu_cores: 2.0
  gpu: false
dns_rewrite: erp.knuckles.team
mcp_server: null  # or 'erpnext-mcp' if available
stack_file: |
  version: "3.8"
  services:
    app:
      image: frappe/erpnext:v15
      ...
```

## 🤖 Agent Usage Guide

- Use `portainer-mcp` `create_standalone_stack` to deploy
- Use `technitium-dns-mcp` `add_record` for DNS
- Use `graph-os` `graph_write` to register in KG topology
- Check host capacity before deployment via `portainer-mcp` `docker_get_system_df`
