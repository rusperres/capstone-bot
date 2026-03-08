# Generate Bounding-Box Damage Report PDF in Admin

## Problem

Admins need to produce a regional damage report based on an interactively selected bounding box and current weather/hazard context, but there is no geospatial report aggregation or PDF generation pipeline. This prevents standardized incident documentation.

## Potentially Related Files

- [apps/admin/src/app/map/components/OperationsMapPage.tsx](../apps/admin/src/app/map/components/OperationsMapPage.tsx) - Bbox selection UI.
- [apps/api/src/modules/disaster-response/admin-operations/admin-operations.controller.ts](../apps/api/src/modules/disaster-response/admin-operations/admin-operations.controller.ts) - Report endpoint.
- [apps/api/src/modules/disaster-response/admin-operations/admin-operations.service.ts](../apps/api/src/modules/disaster-response/admin-operations/admin-operations.service.ts) - Aggregation flow.
- [apps/api/src/modules/disaster-response/risk-intelligence/risk-intelligence.service.ts](../apps/api/src/modules/disaster-response/risk-intelligence/risk-intelligence.service.ts) - Weather context.
- [apps/api/src/modules/disaster-response/shared/geo.util.ts](../apps/api/src/modules/disaster-response/shared/geo.util.ts) - Spatial helpers.
- [apps/api/prisma/schema/models/disaster-response.prisma](../apps/api/prisma/schema/models/disaster-response.prisma) - Source models.

## What to Fix

1. Add admin map interaction for selecting/storing a bounding box polygon/extent.
2. Build backend bbox aggregation query for hazards, warnings, help requests, and pin statuses.
3. Merge current weather context (flood, earthquake, typhoon-related indicators) into report payload.
4. Implement server-side PDF generation service with standardized report template.
5. Expose an admin endpoint to request/download generated PDF.
6. Add report metadata (time generated, bbox coordinates, operator, data snapshot timestamp).
7. Add tests for bbox filtering correctness and PDF generation success/failure paths.

## Acceptance Criteria

- Admin can draw/select a bounding box from map UI.
- Generated report includes hazards, warnings, and weather context for that area.
- Report is exportable as a PDF file via admin endpoint/UI.
- Report output includes bbox coordinates and generation timestamp.
- Data in report reflects the selected region only.
- Tests validate bbox data selection and PDF generation behavior.
