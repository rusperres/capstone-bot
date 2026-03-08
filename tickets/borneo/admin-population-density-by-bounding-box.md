# Add Population Density Analysis by Bounding Box

## Problem

Admins currently lack a way to evaluate population density inside a selected map region, limiting response planning and resource allocation. The requested capability requires geospatial queries and an analysis view tied to interactive bounding boxes.

## Potentially Related Files

- [apps/admin/src/app/map/components/OperationsMapPage.tsx](../apps/admin/src/app/map/components/OperationsMapPage.tsx) - Existing map operations page to host bbox density tools.
- [apps/api/src/modules/disaster-response/admin-operations/admin-operations.controller.ts](../apps/api/src/modules/disaster-response/admin-operations/admin-operations.controller.ts) - Admin endpoint surface to extend for density queries.
- [apps/api/src/modules/disaster-response/admin-operations/admin-operations.service.ts](../apps/api/src/modules/disaster-response/admin-operations/admin-operations.service.ts) - Candidate service for density computation orchestration.
- [apps/api/src/modules/disaster-response/risk-intelligence/risk-intelligence.service.ts](../apps/api/src/modules/disaster-response/risk-intelligence/risk-intelligence.service.ts) - Existing geospatial/weather analysis patterns to reuse.
- [apps/api/src/modules/disaster-response/shared/geo.util.ts](../apps/api/src/modules/disaster-response/shared/geo.util.ts) - Spatial helper baseline for bbox math.
- [apps/api/prisma/schema/models/disaster-response.prisma](../apps/api/prisma/schema/models/disaster-response.prisma) - `UserLocationSnapshot` and regional snapshots useful for density estimates.

## What to Fix

1. Add interactive bbox selection controls in admin map for density analysis.
2. Implement backend query to compute population count/density within selected bounds.
3. Define density data source strategy (live user snapshots, cached regional snapshots, or external demographic dataset).
4. Add API response format with totals, density metric, and confidence/source metadata.
5. Add admin visualization layer (heatmap/choropleth or summary panel) for selected bbox.
6. Add optional export/share of density analysis snapshot alongside map context.
7. Add tests for bbox inclusion logic and density calculation consistency.

## Acceptance Criteria

- Admin can select a bounding box and request density analysis.
- API returns population count and density metrics for selected area.
- UI displays density output in a clear, actionable format.
- Density response includes data source or confidence metadata.
- Results update when bbox changes.
- Tests confirm geospatial filtering and density computations.
