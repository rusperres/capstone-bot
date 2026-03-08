# Enhance Volunteer Application and Admin Review Workflow

## Problem

Volunteer apply/review functionality exists, but it lacks stronger workflow controls such as duplicate prevention, clearer rejection handling, and richer admin operations for sustained crisis management. Current behavior is functional but not robust enough for high-volume onboarding.

## Potentially Related Files

- [apps/api/src/modules/disaster-response/volunteers/volunteers.controller.ts](../apps/api/src/modules/disaster-response/volunteers/volunteers.controller.ts) - User-facing apply/status endpoints.
- [apps/api/src/modules/disaster-response/volunteers/volunteers.service.ts](../apps/api/src/modules/disaster-response/volunteers/volunteers.service.ts) - Volunteer application creation rules.
- [apps/api/src/modules/disaster-response/admin-operations/admin-operations.controller.ts](../apps/api/src/modules/disaster-response/admin-operations/admin-operations.controller.ts) - Admin review endpoint for applications.
- [apps/api/src/modules/disaster-response/admin-operations/admin-operations.service.ts](../apps/api/src/modules/disaster-response/admin-operations/admin-operations.service.ts) - Transactional approve/reject logic and decision logging.
- [apps/admin/src/app/volunteers/components/VolunteerApprovalsPage.tsx](../apps/admin/src/app/volunteers/components/VolunteerApprovalsPage.tsx) - Existing admin review UI.
- [apps/api/prisma/schema/models/disaster-response.prisma](../apps/api/prisma/schema/models/disaster-response.prisma) - VolunteerApplication, VolunteerProfile, VolunteerDecisionLog models.

## What to Fix

1. Add backend validation to prevent duplicate active applications by the same user.
2. Extend review flow to require/store a structured rejection reason when status is REJECTED.
3. Add admin-side filtering and sorting enhancements for queue triage (date submitted, hazard experience, status).
4. Add optional bulk review actions for low-risk approvals/rejections with audit logging.
5. Add suspension/reactivation endpoint and UI action for volunteer lifecycle management.
6. Surface complete decision history in admin UI to improve accountability.
7. Add tests for duplicate apply prevention, rejection reason requirements, and lifecycle transitions.

## Acceptance Criteria

- Users cannot submit duplicate pending applications.
- Admin rejection requires a reason and stores it for audit/history.
- Admin can filter, sort, and efficiently process large application queues.
- Volunteer profile status stays in sync with final application decisions.
- Suspension/reactivation actions are available and logged.
- Tests cover apply, review, and profile status synchronization.
