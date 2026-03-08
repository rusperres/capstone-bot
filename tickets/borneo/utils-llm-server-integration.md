# Implement Real LLM Server Integration for Assistant

## Problem

The assistant module currently relies on a simple provider with static behavior, which does not satisfy the requirement for a real LLM-backed server capability. This blocks richer, contextual disaster Q&A and operational guidance.

## Potentially Related Files

- [apps/api/src/modules/disaster-response/assistant/assistant.module.ts](../apps/api/src/modules/disaster-response/assistant/assistant.module.ts) - Provider wiring.
- [apps/api/src/modules/disaster-response/assistant/assistant.service.ts](../apps/api/src/modules/disaster-response/assistant/assistant.service.ts) - Inquiry orchestration.
- [apps/api/src/modules/disaster-response/assistant/assistant.controller.ts](../apps/api/src/modules/disaster-response/assistant/assistant.controller.ts) - API entrypoint.
- [apps/api/src/modules/disaster-response/assistant/simple-assistant.provider.ts](../apps/api/src/modules/disaster-response/assistant/simple-assistant.provider.ts) - Stub to replace.
- [apps/api/.env.example](../apps/api/.env.example) - LLM env vars.
- [apps/mobile/src/components/screens/LLMAssistant.tsx](../apps/mobile/src/components/screens/LLMAssistant.tsx) - Client consumer.

## What to Fix

1. Introduce an LLM provider abstraction and concrete server integration (model endpoint, timeout, retries).
2. Replace `SimpleAssistantProvider` in module wiring with the new configurable provider.
3. Add strict environment config and startup validation for LLM credentials and endpoint.
4. Add request safety controls (rate limiting, prompt guardrails, and output truncation policy).
5. Add disaster-context prompt shaping using hazard/location metadata from request payload.
6. Add observability hooks (latency, failures, provider fallback behavior).
7. Add tests for provider integration boundaries and graceful failure paths.

## Acceptance Criteria

- Assistant endpoint returns real LLM-generated responses via configured provider.
- Missing or invalid LLM config fails fast with clear startup/runtime errors.
- Assistant still returns controlled fallback responses when provider is unavailable.
- Response quality includes request context (location/hazard when provided).
- Rate limiting and safety constraints are enforced for assistant requests.
- Tests cover success, timeout, and provider-error scenarios.
