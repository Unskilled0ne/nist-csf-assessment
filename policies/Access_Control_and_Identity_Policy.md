# Enterprise Access Control & Identity Management Policy
**Standard Mapping:** NIST CSF 2.0 (PR.AA) | ISO 27001:2022 (A.5.15, A.5.18) | EU DORA (Art. 9)  
**Document ID:** POL-SEC-004  
**Version:** 2.1 | **Classification:** Internal  

---

## 1. Purpose & Scope
This policy mandates technical and procedural controls to ensure only authorized identities (human, service, and machine) access Apex Financial Technologies computing systems, cloud tenants, databases, and customer financial data.

## 2. Principle of Least Privilege & Zero Trust
1. All access permissions must be granted on a Need-to-Know basis according to Role-Based Access Control (RBAC).
2. Production access for engineers is disabled by default; access is granted via Just-In-Time (JIT) elevation requiring dual-approval for a maximum session time of 4 hours.
3. Default-deny policies must be applied at every network and IAM perimeter.

## 3. Authentication & Credential Standards
1. **Multi-Factor Authentication (MFA):** Mandatory for 100% of corporate accounts. SMS and voice-call MFA are strictly prohibited due to SIM-swap vulnerabilities. All privileged administrators (AWS, Okta, GitHub, Google Workspace) must authenticate using FIDO2/WebAuthn hardware security keys.
2. **Password Length:** Minimum 16 characters for administrative accounts; 14 characters for standard users. Passwords must not contain predictable corporate or personal tokens.
3. **API & Machine Keys:** Long-lived access keys in AWS/GCP are prohibited. Cloud workloads must use IAM Roles with short-lived STS tokens. Any static token must automatically rotate every 90 days.

## 4. Offboarding & Revocation SLA
1. Voluntary offboarding: All digital identities, VPN credentials, and SaaS tokens must be automatically de-provisioned within 4 hours of termination.
2. Involuntary offboarding: All access revoked immediately upon notification from Human Resources.

## 5. Audit & Compliance Enforcement
Access reviews across all privileged IAM roles must be performed quarterly and signed off by the CISO. Violations will result in access suspension and formal disciplinary review.
