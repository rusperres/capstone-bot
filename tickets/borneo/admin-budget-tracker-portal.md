# Build Budget Tracker Portal for Disaster Operations

## Problem

There is no budget tracking capability in schema, API, or admin UI, yet operations require visibility into allocations and spending per incident/region. Without this portal, financial accountability and response planning are manual and error-prone.

## Potentially Related Files

- [apps/admin/src/app/page.tsx](../apps/admin/src/app/page.tsx) - Admin home card grid where budget portal entry can be added.
- [apps/admin/src/app/shell.tsx](../apps/admin/src/app/shell.tsx) - Admin navigation configuration.
- [apps/api/src/modules/disaster-response/disaster-response.module.ts](../apps/api/src/modules/disaster-response/disaster-response.module.ts) - Root module where budget module can be mounted.
- [apps/api/prisma/schema/models](../apps/api/prisma/schema/models) - Location for new budget models and relationships.
- [packages/api-client/openapi/openapi.json](../packages/api-client/openapi/openapi.json) - Contract to regenerate for admin hooks.
- [packages/api-client/scripts/sync-openapi.mjs](../packages/api-client/scripts/sync-openapi.mjs) - OpenAPI sync flow used after backend endpoint changes.

## What to Fix

1. Add Prisma models for budget entities (allocation, category, transaction, adjustment, audit log).
2. Create backend budget module with CRUD endpoints and summary/report endpoints.
3. Enforce admin-only authorization and audit logging for all budget mutations.
4. Build admin budget portal UI (list, filter, create/edit transaction, summary cards).
5. Add budget-to-region/disaster tagging to support operational reporting.
6. Regenerate API client hooks and wire React Query data flow in admin screens.
7. Add tests for financial calculations, permissions, and mutation logging.

## Acceptance Criteria

- Admin can create and manage budget allocations and transactions.
- Budget totals, spent, and remaining values compute correctly.
- Budget records can be filtered by region/disaster context.
- Non-admin users cannot access budget mutation endpoints.
- All financial changes produce audit log entries.
- Tests validate calculation correctness and access control.
