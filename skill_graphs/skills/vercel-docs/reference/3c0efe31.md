##  [Teams](https://vercel.com/docs/getting-started-with-vercel#teams)[](https://vercel.com/docs/getting-started-with-vercel#teams)
Teams on Vercel let you collaborate with other members on projects and access additional resources.
###  [Creating a team](https://vercel.com/docs/getting-started-with-vercel#creating-a-team)[](https://vercel.com/docs/getting-started-with-vercel#creating-a-team)
DashboardcURLSDK
  1. Click on the team switcher at the top left of the nav bar
  2. Choose to create a new team
  3. Name your team
  4. Depending on the types of team plans that you have already created, you'll be able to select a team plan option:

![Selecting a team plan.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Fnew-team-light.png&w=1080&q=75)![Selecting a team plan.](https://vercel.com/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fteams%2Fnew-team-dark.png&w=1080&q=75)Selecting a team plan.
To create an Authorization Bearer token, see the [access token](https://vercel.com/docs/rest-api/reference/welcome#creating-an-access-token) section of the API documentation.
cURL
```
curl --request POST \
  --url https://api.vercel.com/v1/teams \
  --header "Authorization: Bearer $VERCEL_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
  "slug": "<team-slug>",
  "name": "<team-name>"
}'
```

To create an Authorization Bearer token, see the [access token](https://vercel.com/docs/rest-api/reference/welcome#creating-an-access-token) section of the API documentation.
createTeam
```
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: '<YOUR_BEARER_TOKEN_HERE>',
});

async function run() {
  const result = await vercel.teams.createTeam({
    slug: 'team-slug',
    name: 'team-name',
  });

  // Handle the result
  console.log(result);
}

run();
```

Collaborating with other members on projects is available on the [Pro](https://vercel.com/docs/plans/pro-plan) and [Enterprise](https://vercel.com/docs/plans/enterprise) plans.
Upgrade from the [Hobby](https://vercel.com/docs/plans/hobby) plan to [Pro](https://vercel.com/docs/plans/hobby#upgrading-to-pro) to add team members.
### Experience Vercel Pro for free
Unlock the full potential of Vercel Pro during your 14-day trial with $20 in credits. Benefit from 1 TB Fast Data Transfer, 10,000,000 Edge Requests, up to 200 hours of Build Execution, and access to Pro features like team collaboration and enhanced analytics.
[Start your free Pro trial](https://vercel.com/signup?next=/upgrade/docs-trial-button&plan=pro)
After [creating a new trial](https://vercel.com/docs/plans/pro-plan/trials), you'll have 14 days of Pro premium features and collaboration for free.
###  [Team membership](https://vercel.com/docs/getting-started-with-vercel#team-membership)[](https://vercel.com/docs/getting-started-with-vercel#team-membership)
You can join a Vercel team through an invitation from a [team owner](https://vercel.com/docs/rbac/access-roles#owner-role), automatic addition by a team's [identity provider](https://vercel.com/docs/saml), or by requesting access yourself. To request access, you can push a commit to a private Git repository owned by the team.
###  [Leaving a team](https://vercel.com/docs/getting-started-with-vercel#leaving-a-team)[](https://vercel.com/docs/getting-started-with-vercel#leaving-a-team)
You can't leave a team if you are the last remaining [owner](https://vercel.com/docs/rbac/access-roles#owner-role) or the last confirmed [member](https://vercel.com/docs/rbac/access-roles#member-role).
To leave a team:
  1. If there isn't another owner for your team, you must assign a different confirmed member as the team owner
  2. Go to your team's dashboard and open Settings in the sidebar
  3. Scroll to the Leave Team section and select the Leave Team button
  4. Click Confirm
  5. If you are the only remaining member, you should delete the team instead


###  [Deleting a team](https://vercel.com/docs/getting-started-with-vercel#deleting-a-team)[](https://vercel.com/docs/getting-started-with-vercel#deleting-a-team)
To delete a team:
  1. Remove all team domains
  2. Go to your team's dashboard and open Settings in the sidebar
  3. Scroll to the Delete Team section and select the Delete Team button
  4. Click Confirm


If you'd prefer to cease payment instead of deleting your team, you can [downgrade to Hobby](https://vercel.com/docs/plans/pro-plan#downgrading-to-hobby).
###  [Default team](https://vercel.com/docs/getting-started-with-vercel#default-team)[](https://vercel.com/docs/getting-started-with-vercel#default-team)
Your default team will be used when you make a request through the [API](https://vercel.com/docs/rest-api) or [CLI](https://vercel.com/docs/cli) and don’t specify a specific team. It will also be the team shown whenever you first log in to Vercel or navigate to `/dashboard`. The first Hobby or Pro team you create will automatically be nominated as the default team.
####  [How to change your default team](https://vercel.com/docs/getting-started-with-vercel#how-to-change-your-default-team)[](https://vercel.com/docs/getting-started-with-vercel#how-to-change-your-default-team)
If you delete, leave, or are removed from your default team, Vercel will automatically choose a new default team for you. However, you may want to choose a default team yourself. To do that:
  1. Navigate to [vercel.com/account/settings](https://vercel.com/account/settings)
  2. Under Default Team, select your new default team from the dropdown
  3. Press Save


###  [Find your team ID](https://vercel.com/docs/getting-started-with-vercel#find-your-team-id)[](https://vercel.com/docs/getting-started-with-vercel#find-your-team-id)
Your Team ID is a unique and unchangeable identifier that's automatically assigned when your team is created.
There are a couple of methods you can use to locate your Team ID:
  * Vercel API: Use the [Vercel API](https://vercel.com/docs/rest-api/reference/endpoints/teams/list-all-teams) to retrieve your Team ID
  * Dashboard: Find your Team ID directly from your team's Dashboard on Vercel:
    * Navigate to the following URL, replacing `your_team_name_here` with your actual team's name: `https://vercel.com/teams/your_team_name_here/settings#team-id`. If you're unable to locate your Team ID using the URL method, follow these steps:
    * Open your team's dashboard and head over to the Settings section in the sidebar
    * Choose General from the left-hand navigation
    * Scroll down to the Team ID section and your Team ID will be there ready for you to copy
