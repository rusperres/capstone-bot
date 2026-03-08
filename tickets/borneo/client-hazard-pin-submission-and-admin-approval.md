# Implement Hazard Pin Submission with Admin Approval

## Problem

The data model includes map pin status records and admin can list pin statuses, but users cannot yet submit hazard pins with text/photo evidence and admins cannot run an explicit approval workflow. This blocks a critical crowdsourced hazard reporting loop.

## Potentially Related Files

- [apps/mobile/src/components/MapComponent.tsx](../apps/mobile/src/components/MapComponent.tsx) - Mobile map where hazard pin submission entry can be triggered.
- [apps/mobile/src/components/screens/MapForecast.tsx](../apps/mobile/src/components/screens/MapForecast.tsx) - Forecast/map context for pin overlays and location UX.
- [apps/api/src/modules/disaster-response/admin-operations/admin-operations.controller.ts](../apps/api/src/modules/disaster-response/admin-operations/admin-operations.controller.ts) - Existing pin status listing endpoint under admin operations.
- [apps/api/src/modules/disaster-response/admin-operations/admin-operations.service.ts](../apps/api/src/modules/disaster-response/admin-operations/admin-operations.service.ts) - Current pin status query logic.
- [apps/admin/src/app/map/components/OperationsMapPage.tsx](../apps/admin/src/app/map/components/OperationsMapPage.tsx) - Admin map for reviewing and updating submitted pins.
- [apps/api/prisma/schema/models/disaster-response.prisma](../apps/api/prisma/schema/models/disaster-response.prisma) - `MapPinStatus` model and pin lifecycle fields.
- [packages/api-client/openapi/openapi.json](../packages/api-client/openapi/openapi.json) - API schema to expose new pin submit/review endpoints.

## What to Fix

1. Add authenticated user endpoint to submit hazard pins with title, hazard type, note, coordinates, and optional photo metadata.
2. Introduce explicit approval/rejection/publish status transitions for admin moderation.
3. Add admin review queue in map operations UI with filters by hazard type, region, and status.
4. Add storage integration plan for photo evidence and signed URL handling.
5. Show submission status back to reporting users (pending/approved/rejected/resolved).
6. Add audit trail entries for admin moderation actions.
7. Add tests for submission validation, moderation permissions, and status transitions.

## Acceptance Criteria

- Users can submit hazard pins with text details and optional photo attachment metadata.
- Submitted pins are not publicly treated as approved until admin moderation.
- Admin can approve/reject/update pin status from the admin interface.
- Reporter can view the moderation status of submitted pins.
- Moderation actions are permission-protected and audited.
- Tests verify submission, review, and lifecycle integrity.
