# Implement Help Request System End-to-End

## Problem

The backend already has a `help-requests` module, but the mobile side is still mostly a UI shell and users cannot reliably submit, track, and update emergency help requests from the app. This creates a gap between existing API capability and real user access during emergencies.

## Potentially Related Files

- [apps/mobile/src/components/screens/HelpDashboard.tsx](../apps/mobile/src/components/screens/HelpDashboard.tsx) - Current help dashboard UI shell for requester and volunteer tabs.
- [apps/mobile/src/components/screens/MapForecast.tsx](../apps/mobile/src/components/screens/MapForecast.tsx) - Source of user location context that can prefill help request coordinates.
- [apps/mobile/src/components/MainApp.tsx](../apps/mobile/src/components/MainApp.tsx) - Route switch where help flow navigation is mounted.
- [apps/api/src/modules/disaster-response/help-requests/help-requests.controller.ts](../apps/api/src/modules/disaster-response/help-requests/help-requests.controller.ts) - Existing create/list/claim/status endpoints to wire into UI.
- [apps/api/src/modules/disaster-response/help-requests/help-requests.service.ts](../apps/api/src/modules/disaster-response/help-requests/help-requests.service.ts) - Business logic for lifecycle and assignment.
- [apps/api/src/modules/disaster-response/shared/approved-volunteer.guard.ts](../apps/api/src/modules/disaster-response/shared/approved-volunteer.guard.ts) - Volunteer-only enforcement for claims.
- [packages/api-client/openapi/openapi.json](../packages/api-client/openapi/openapi.json) - API contract source for generated client hooks.

## What to Fix

1. Build a full mobile help-request submission form (hazard type, urgency, description, location, optional family context).
2. Wire the form to existing help request endpoints via `@wira-borneo/api-client` hooks and handle loading/error/success states.
3. Implement requester timeline/status UI so users can see OPEN, CLAIMED, IN_PROGRESS, and RESOLVED updates.
4. Implement volunteer-side assignment view showing claimable requests and claimed tasks with status updates.
5. Ensure location is captured consistently (manual map pin and/or geolocation fallback).
6. Add guard-aware UX: hide claim actions for non-approved volunteers and show status guidance.
7. Add API and UI tests for request creation, claim flow, and status transitions.

## Acceptance Criteria

- Mobile users can create a help request that persists in backend storage.
- Requesters can view their own requests and current status history.
- Approved volunteers can claim open requests and move assignments through valid statuses.
- Non-approved volunteers cannot claim requests and see a clear blocking message.
- Help request location is saved with valid latitude/longitude and displayed consistently.
- Critical flows are covered by tests for create, claim, and update transitions.
