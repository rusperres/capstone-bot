# Add Pregnant Status and Age Group to User Profile

## Problem

The current user model lacks critical vulnerability attributes requested by stakeholders: pregnant status and age group. Without these fields, risk intelligence and operational triage cannot personalize warnings and aid prioritization.

## Potentially Related Files

- [apps/api/prisma/schema/models/auth.prisma](../apps/api/prisma/schema/models/auth.prisma) - User model where new fields must be added.
- [apps/api/prisma/schema/models/disaster-response.prisma](../apps/api/prisma/schema/models/disaster-response.prisma) - Downstream models and services that may consume vulnerability signals.
- [apps/api/src/modules/auth/auth.controller.ts](../apps/api/src/modules/auth/auth.controller.ts) - Existing user/session endpoints to extend with profile updates.
- [apps/api/src/modules/auth/auth.service.ts](../apps/api/src/modules/auth/auth.service.ts) - Candidate location for profile update logic.
- [apps/mobile/src/components/screens/Profile.tsx](../apps/mobile/src/components/screens/Profile.tsx) - Mobile profile UI where fields should be editable.
- [apps/admin/src/app/map/components/OperationsMapPage.tsx](../apps/admin/src/app/map/components/OperationsMapPage.tsx) - Admin map context that may display vulnerability-aware signals.

## What to Fix

1. Add `pregnantStatus` and `ageGroup` fields to user profile schema with a migration.
2. Define a clear `ageGroup` enum or constrained values to avoid inconsistent text input.
3. Add authenticated API endpoint to update/read these fields.
4. Add validation and privacy-safe handling for sensitive health-related data.
5. Add mobile profile form controls and session refresh behavior after updates.
6. Integrate fields into risk-intelligence response shaping where appropriate.
7. Add tests for migration integrity, validation, and profile update authorization.

## Acceptance Criteria

- User records include pregnant status and age group fields after migration.
- Authenticated users can update their own fields and read back persisted values.
- Invalid age group values are rejected by validation.
- Sensitive profile values are not writable/readable by unauthorized users.
- Mobile profile UI supports editing both fields successfully.
- Tests cover schema, validation, and ownership rules.
