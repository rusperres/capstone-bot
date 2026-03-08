# Implement Account-Linked Family Addition and Management

## Problem

Basic family create/join endpoints exist, but family management is incomplete and user experience is limited to code-based joins. The project requirement is account-bound family addition with practical management controls and clearer membership workflows.

## Potentially Related Files

- [apps/mobile/src/components/screens/Family.tsx](../apps/mobile/src/components/screens/Family.tsx) - Family UI currently using placeholder member data.
- [apps/mobile/src/components/MainApp.tsx](../apps/mobile/src/components/MainApp.tsx) - Family route integration.
- [apps/api/src/modules/disaster-response/families/families.controller.ts](../apps/api/src/modules/disaster-response/families/families.controller.ts) - Existing create/join/me/map endpoints.
- [apps/api/src/modules/disaster-response/families/families.service.ts](../apps/api/src/modules/disaster-response/families/families.service.ts) - Family and membership rules.
- [apps/api/prisma/schema/models/disaster-response.prisma](../apps/api/prisma/schema/models/disaster-response.prisma) - Family and FamilyMember models.
- [apps/api/src/modules/auth/auth.controller.ts](../apps/api/src/modules/auth/auth.controller.ts) - Account/session source for authenticated family operations.

## What to Fix

1. Ensure all family create/join actions are authenticated and strictly account-bound.
2. Replace placeholder family UI with real member list, roles, and join status.
3. Add invitation workflow improvements (share invite code UX and optional invitation entity for pending invites).
4. Add endpoints and UI actions for family owner to remove members and rotate invite code.
5. Add family profile editing (name updates) with ownership checks.
6. Add tests for account ownership, membership boundaries, and invite handling.

## Acceptance Criteria

- Only authenticated users can create or join a family.
- Family screen shows real memberships tied to account identity.
- Family owner can manage membership (remove member, refresh/rotate invite mechanics).
- Family metadata updates are permission-checked and persisted.
- Unauthorized users cannot mutate family membership.
- Tests cover create/join/manage authorization paths.
