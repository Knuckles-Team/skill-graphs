##  [Working with member information](https://vercel.com/docs/integrations/create-integration/marketplace-api#working-with-member-information)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#working-with-member-information)
Get details about team members who have access to an installation. Use this endpoint to retrieve member information for access control, audit logs, or displaying member details in your integration.
To retrieve information about a specific team member associated with an installation, use the [`/v1/installations/{installationId}/member/{memberId}`](https://vercel.com/docs/integrations/create-integration/marketplace-api/reference/vercel/get-member) endpoint.
###  [Member information request parameters](https://vercel.com/docs/integrations/create-integration/marketplace-api#member-information-request-parameters)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#member-information-request-parameters)
  * `installationId` - The installation ID
  * `memberId` - The member ID


###  [Member information request](https://vercel.com/docs/integrations/create-integration/marketplace-api#member-information-request)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#member-information-request)
get-member-info.ts
```
async function getMemberInfo(
  installationId: string,
  memberId: string
): Promise<MemberInfo> {
  const response = await fetch(
    `https://api.vercel.com/v1/installations/${installationId}/member/${memberId}`,
    {
      headers: {
        'Authorization': `Bearer ${token}`,
      },
    }
  );

  if (!response.ok) {
    throw new Error(`Failed to get member info: ${response.statusText}`);
  }

  return response.json();
}
```

###  [Member information response](https://vercel.com/docs/integrations/create-integration/marketplace-api#member-information-response)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#member-information-response)
get-member-info-response.json
```
{
  "id": "member_abc123",
  "name": "John Doe",
  "email": "john@example.com",
  "role": "ADMIN",
  "avatar": "https://example.com/avatar.jpg",
  "createdAt": "2025-01-15T10:00:00Z"
}
```

###  [Member roles](https://vercel.com/docs/integrations/create-integration/marketplace-api#member-roles)[](https://vercel.com/docs/integrations/create-integration/marketplace-api#member-roles)
Members can have the following roles:
  * `ADMIN` - Full access to the installation and its resources
  * `USER` - Limited access, can use resources but can't modify settings


Check the member's role to determine what actions they can perform below.
