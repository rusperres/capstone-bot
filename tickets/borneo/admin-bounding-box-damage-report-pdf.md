# Generate Bounding-Box Damage Report PDF in Admin

## Problem

Admins need to produce a regional damage report based on an interactively selected bounding box and current weather/hazard context, but there is no geospatial report aggregation or PDF generation pipeline. This prevents standardized incident documentation.

## Potentially Related Files

- [apps/admin/src/app/map/components/OperationsMapPage.tsx](../apps/admin/src/app/map/components/OperationsMapPage.tsx) - Existing map UI where interactive bounding-box selection can be added.
- [apps/api/src/modules/disaster-response/admin-operations/admin-operations.controller.ts](../apps/api/src/modules/disaster-response/admin-operations/admin-operations.controller.ts) - Existing admin operations surface to extend with report endpoint.
- [apps/api/src/modules/disaster-response/admin-operations/admin-operations.service.ts](../apps/api/src/modules/disaster-response/admin-operations/admin-operations.service.ts) - Aggregation orchestration entrypoint candidate.
- [apps/api/src/modules/disaster-response/risk-intelligence/risk-intelligence.service.ts](../apps/api/src/modules/disaster-response/risk-intelligence/risk-intelligence.service.ts) - Weather and hazard intelligence source.
- [apps/api/src/modules/disaster-response/shared/geo.util.ts](../apps/api/src/modules/disaster-response/shared/geo.util.ts) - Existing geospatial utility patterns.
- [apps/api/prisma/schema/models/disaster-response.prisma](../apps/api/prisma/schema/models/disaster-response.prisma) - Hazard/help/warning models needed for report aggregation.

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
