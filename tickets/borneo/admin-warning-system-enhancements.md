# Complete Warning System for Creation, Consumption, and Lifecycle

## Problem

Warning creation exists in admin and warning retrieval exists in API, but user-facing consumption is still stubbed and lifecycle operations are limited. This prevents warnings from acting as a reliable end-to-end emergency communication channel.

## Potentially Related Files

- [apps/admin/src/app/warnings/new/components/ManualWarningPage.tsx](../apps/admin/src/app/warnings/new/components/ManualWarningPage.tsx) - Existing multi-step warning compose/confirm UI.
- [apps/admin/src/app/warnings/new/components/warning-flow.utils.ts](../apps/admin/src/app/warnings/new/components/warning-flow.utils.ts) - Validation and flow helpers used by admin warning creation.
- [apps/mobile/src/components/screens/Warnings.tsx](../apps/mobile/src/components/screens/Warnings.tsx) - Currently hardcoded warnings list needing API integration.
- [apps/api/src/modules/disaster-response/warnings/warnings.controller.ts](../apps/api/src/modules/disaster-response/warnings/warnings.controller.ts) - User warning retrieval endpoints.
- [apps/api/src/modules/disaster-response/warnings/warnings.service.ts](../apps/api/src/modules/disaster-response/warnings/warnings.service.ts) - Warning query rules by user/family/location.
- [apps/api/src/modules/disaster-response/admin-operations/admin-operations.controller.ts](../apps/api/src/modules/disaster-response/admin-operations/admin-operations.controller.ts) - Admin warning creation endpoints.
- [apps/api/prisma/schema/models/disaster-response.prisma](../apps/api/prisma/schema/models/disaster-response.prisma) - WarningEvent and WarningEventLog storage.

## What to Fix

1. Wire mobile warnings screen to `warnings/me` and `warnings/family` APIs.
2. Add merged warning feed logic with deduplication and severity ordering.
3. Add warning lifecycle operations for admin (amend, cancel, archive) with event logs.
4. Display warning area metadata and guidance clearly in mobile cards.
5. Add optional acknowledgment action for users to mark warnings as seen.
6. Improve admin list/history view for sent warnings and their effective windows.
7. Add tests for warning retrieval filters and lifecycle transitions.

## Acceptance Criteria

- Mobile warnings page displays real warning data instead of placeholders.
- Users see warnings targeted to them and their family area context.
- Admin can amend/cancel warnings and updates are reflected in client views.
- Warning lifecycle actions generate logs for auditing.
- Warning feed ordering is deterministic by severity and recency.
- Tests verify warning retrieval and lifecycle mutation behavior.
